#!/bin/bash
cd /app
VENV=/app/venv
LOGDIR="$HOME/.local/share/steamprotipsai"
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/log.txt"

$VENV/bin/python /app/src/steamprotipsai/main.py >> "$LOGFILE" 2>&1
