#!/bin/bash

# cleanup.sh
echo "Cleaning up build artifacts..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info
echo "Cleanup complete!"

python -m build
