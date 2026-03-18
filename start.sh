#!/bin/bash
set -e
echo "Starting AI-Driven Personalized Learning Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9100 --workers 1
