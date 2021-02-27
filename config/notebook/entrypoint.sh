#!/bin/bash

start_webserver () {
    cd /web && exec gunicorn --bind 0.0.0.0:3000 webserver:app
}

start_notebook_server () {
    cd /home/jovyan/work && exec start.sh jupyter notebook --NotebookApp.token=''
}

# Start the helper process and put it in the background
start_webserver &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start my_first_process: $status"
  exit $status
fi

# Start the main process
start_notebook_server
if [ $status -ne 0 ]; then
  echo "Failed to start my_second_process: $status"
  exit $status
fi

# Naive check runs checks once a minute to see if either of the processes exited.
# This illustrates part of the heavy lifting you need to do if you want to run
# more than one service in a container. The container exits with an error
# if it detects that either of the processes has exited.
# Otherwise it loops forever, waking up every 60 seconds

while sleep 60; do
  ps aux | grep gunicorn | grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux | grep jupyter | grep -q -v grep
  PROCESS_2_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done

