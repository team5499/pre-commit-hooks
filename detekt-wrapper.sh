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
    command tar -zxf "RC9.2.tar.gz" 
    command rm RC9.2.tar.gz
    command cd "detekt-RC9.2"
    command ./gradlew build shadowJar
    command cd ..
fi

command java -jar "$CACHE_DIR/detekt-RC9.2/detekt-cli/build/libs/detekt-cli-1.0.0.RC9.2-all.jar" --debug -i "$@"
