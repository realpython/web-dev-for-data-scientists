#!/bin/bash

gunicorn app:app -D 
python scheduler.py
