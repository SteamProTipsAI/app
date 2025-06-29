#!/bin/bash
cd /app
LOGDIR="$HOME/.local/share/steamprotipsai"
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/log.txt"

PYTHONPATH=/app/src python3 /app/src/steamprotipsai/main.py >> "$LOGFILE" 2>&1
