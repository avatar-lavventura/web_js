#!/bin/bash

PORT=8001
pid=$(sudo lsof -n -i :$PORT | grep LISTEN| awk '{print $2}');
if [ -n "$pid" ]; then
  sudo kill -9 $pid
fi

python -m SimpleHTTPServer $PORT
