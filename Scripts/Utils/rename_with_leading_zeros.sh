#!/bin/bash
for file in "${1:-.}"/page_*.png; do
    base=$(basename "$file" .png | sed 's/page_//')
    if [[ "$base" =~ ^[0-9]+$ ]]; then
        new_base=$(printf "page_%02d" "$base")
        mv "$file" "${1:-.}/$new_base.png"
    fi
done
