void c_process_buffer(unsigned char *buf, size_t len) {
    // Assumes len <= 5
    for (size_t i = 0; i < len; i++) {
        buf[i] = buf[i] + 1;
    }
}