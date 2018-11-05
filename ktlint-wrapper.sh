#!/bin/bash
set -euo pipefail

DOWNLOAD_URL="https://github.com/shyiko/ktlint/releases/download/0.29.0/ktlint"
CACHE_DIR=$(dirname "${BASH_SOURCE[0]}")

if [ ! -f "$CACHE_DIR/ktlint" ]; then
    if command -v curl > /dev/null; then
        curl -sSL -o "$CACHE_DIR/ktlint" "$DOWNLOAD_URL"
    elif command -v wget > /dev/null; then
        wget -q -O "$CACHE_DIR/ktlint" "$DOWNLOAD_URL"
    else
        >&2 echo "Please install curl or wget."
        exit 1
    fi
    chmod a+x "$CACHE_DIR/ktlint"
fi

command "$CACHE_DIR/ktlint" "$@"
