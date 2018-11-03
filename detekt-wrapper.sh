#!/bin/bash
set -euo pipefail

DOWNLOAD_URL="https://github.com/arturbosch/detekt/archive/RC9.2.tar.gz"
CACHE_DIR=$(dirname "${BASH_SOURCE[0]}")

if [ ! -f "$CACHE_DIR/detekt-RC9.2/detekt-cli/build/libs/detekt-cli-1.0.0.RC9.2-all.jar" ]; then
    if command -v curl > /dev/null; then
        curl -sSL -o "$CACHE_DIR/RC9.2.tar.gz" "$DOWNLOAD_URL"
    elif command -v wget > /dev/null; then
        wget -q -O "$CACHE_DIR/RC9.2.tar.gz" "$DOWNLOAD_URL"
    else
        >&2 echo "Please install curl or wget."
        exit 1
    fi
    tar -zxf "$CACHE_DIR/RC9.2.tar.gz" -C "$CACHE_DIR"
    rm "$CACHE_DIR/RC9.2.tar.gz"
    command "$CACHE_DIR/detekt-RC9.2/gradlew" -q -p "$CACHE_DIR/detekt-RC9.2" shadowJar > /dev/null 2>&1
fi

java -jar "$CACHE_DIR/detekt-RC9.2/detekt-cli/build/libs/detekt-cli-1.0.0.RC9.2-all.jar" -i "$@"
