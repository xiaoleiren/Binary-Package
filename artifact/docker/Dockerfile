FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    openjdk-17-jdk \
    gdb \
    objdump \
    gcc \
    g++ \
    rustc \
    cargo \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Ghidra 11.0.3
RUN wget -q https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/ghidra_11.0.3_PUBLIC_20240425.zip \
    && unzip -q ghidra_11.0.3_PUBLIC_20240425.zip -d /opt/ \
    && rm ghidra_11.0.3_PUBLIC_20240425.zip

# Set environment variables
ENV GHIDRA_INSTALL_DIR=/opt/ghidra_11.0.3_PUBLIC
ENV PATH="${GHIDRA_INSTALL_DIR}/support:${PATH}"

# Copy lab materials
WORKDIR /workspace
COPY labs/ ./labs/
COPY scripts/ ./scripts/

# Install Python dependencies
RUN pip3 install --no-cache-dir pandas numpy

# Default command
CMD ["/bin/bash"]