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