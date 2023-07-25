#!/bin/bash

# Navigate to the target/release directory.
cd target/a

# Remove the deps and build directories.
rm -rf deps
rm -rf build

# Remove all .fingerprint directories.
find . -type d -name '.fingerprint' -exec rm -rf {} +

# Remove all .cargo-check files.
find . -type f -name '*.cargo-check' -exec rm -f {} +

echo "Cleanup completed."