#!/bin/sh

echo "Started Engine"

rasa run -m bot/models -p 5005 --enable-api --cors “”rasa run -m models --enable-api --cors “” &

python3 app.py