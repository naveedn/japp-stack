#!/bin/bash
exec gunicorn --bind 0.0.0.0:3000 webserver:app