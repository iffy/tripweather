#!/bin/sh

/Users/matt/.virtualenvs/tripweather/bin/python multiforecast.py
git add -A
git commit -a -m "Commit $(date)"
git push origin master
