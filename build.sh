#!/usr/bin/env bash
set -e
gcc -shared -fPIC c_module.c -o libc_module.so
echo "Gerado: libc_module.so"
