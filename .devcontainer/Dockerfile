FROM mcr.microsoft.com/devcontainers/base:bookworm

# Use Debian's Python so the interpreter and Tkinter come from the same build.
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
       python3 python3-tk x11-utils \
    && rm -rf /var/lib/apt/lists/*
