#!/bin/sh

echo "Started Engine"

rasa run -m rasa_engine/models -p 5055 --enable-api &

python3 app.py