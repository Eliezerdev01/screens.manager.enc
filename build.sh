#!/usr/bin/env bash
# Exit on error
set -o errexit

# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Install Playwright browser binaries (Chromium)
playwright install chromium

# 3. Install system dependencies for Chromium 
# (This is required for Render's Linux environment)
playwright install-deps chromium