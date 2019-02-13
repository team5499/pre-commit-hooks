#!/bin/bash
set -euo pipefail

DOWNLOAD_URL="https://github.com/arturbosch/detekt/releases/download/RC10/detekt-cli-1.0.0-RC10-all.jar"
CACHE_DIR=$(dirname "${BASH_SOURCE[0]}")

if [ ! -e "$CACHE_DIR/detekt.jar" ]; then
    if command -v curl > /dev/null; then
        curl -sSL -o "$CACHE_DIR/detekt.jar" "$DOWNLOAD_URL"
    elif command -v wget > /dev/null; then
        wget -q -O "$CACHE_DIR/detekt.jar" "$DOWNLOAD_URL"
    else
        >&2 echo "Please install curl or wget."
        exit 1
    fi
fi

INPUT_FILES=""
EXTRA_ARGS=("")
for arg in "$@"; do
    if [ -f "$arg" ]; then
        INPUT_FILES="$INPUT_FILES,$arg"
    else
        EXTRA_ARGS+=("$arg")
    fi
done

INPUT_FILES="$(echo "$INPUT_FILES" | cut -c 2-)"

java -jar "$CACHE_DIR/detekt.jar" ${EXTRA_ARGS[@]} -i "$INPUT_FILES"
