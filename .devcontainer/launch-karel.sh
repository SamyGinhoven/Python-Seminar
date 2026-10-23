#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

# The desktop feature starts X on display :1. Wait until its window server
# accepts connections before opening Karel's Tkinter window.
export DISPLAY=:1
for _ in {1..30}; do
    if xdpyinfo -display "$DISPLAY" >/dev/null 2>&1; then
        break
    fi
    sleep 1
done

if ! xdpyinfo -display "$DISPLAY" >/dev/null 2>&1; then
    echo "Karel desktop did not start; use the Run Karel task after reconnecting." >&2
    exit 1
fi

if ! pgrep -f '[p]ython3 01-karel-world/run_world.py' >/dev/null; then
    nohup /usr/bin/python3 01-karel-world/run_world.py \
        >/tmp/python-seminar-karel.log 2>&1 </dev/null &
fi
