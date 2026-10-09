#!/usr/bin/env bash
set -euo pipefail
test -n "${1:-}"
echo "Bonjour $1"
echo "OK"
