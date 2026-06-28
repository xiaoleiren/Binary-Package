# ab 3: Rust/C FFI and Unsafe Boundaries

## 1. Setup
Build the example:

cd lab3-ffi/
rustc source/wrapper.rs -o wrapper
gcc -c source/c_lib.c -o source/c_lib.o

## 2. Source Review
Rust code (wrapper.rs):

extern "C" {
    fn c_process_buffer(ptr: *mut u8, len: usize);
}

fn process_data(data: &mut [u8]) {
    unsafe {
        c_process_buffer(data.as_mut_ptr(), data.len());
    }
}

fn main() {
    let mut data = vec![1, 2, 3, 4, 5];
    process_data(&mut data);
}

C code (c_lib.c):

void c_process_buffer(unsigned char *buf, size_t len) {
    // Assumes len <= 5
    for (size_t i = 0; i < len; i++) {
        buf[i] = buf[i] + 1;
    }
}

Question 1: What is the unsafe boundary in this code?

Question 2: What assumption does the C function make?

## 3. Binary Inspection
Open the compiled binary in Ghidra. Locate the call from Rust to C.

Question 3: How are arguments passed? (Registers? Stack?)

Question 4: Which contract violation could occur?

## 4. Mitigation
Propose at least two ways to make this FFI boundary safer.

## 5. Reflection
Why does Rust's source-level safety not guarantee safety across FFI?

extern "C" {
fn c_process_buffer(ptr: *mut u8, len: usize);
}

fn process_data(data: &mut [u8]) {
unsafe {
c_process_buffer(data.as_mut_ptr(), data.len());
}
}

fn main() {
let mut data = vec![1, 2, 3, 4, 5];
println!("Before: {:?}", data);
process_data(&mut data);
println!("After: {:?}", data);
}

#include <stdio.h>

void c_process_buffer(unsigned char *buf, size_t len) {
printf("C: processing %zu bytes\n", len);
for (size_t i = 0; i < len; i++) {
buf[i] = buf[i] + 1;
}
}