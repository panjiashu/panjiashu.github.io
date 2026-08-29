#!/bin/bash

set -e

CONFIG_FILE=_config.yml
export BUNDLE_PATH="${BUNDLE_PATH:-/home/vscode/.bundle}"
JEKYLL_ARGS=(
  serve
  --watch
  --port=8080
  --host=0.0.0.0
  --livereload
  --verbose
  --trace
  --force_polling
  --config _config.yml,_config_dev.yml
)

if ! bundle check; then
  bundle install
fi

bundle exec jekyll "${JEKYLL_ARGS[@]}" &

while true; do
  inotifywait -q -e modify,move,create,delete "$CONFIG_FILE"

  if [ $? -eq 0 ]; then
    echo "Change detected to $CONFIG_FILE, restarting Jekyll"

    jekyll_pid=$(pgrep -f jekyll)
    kill -KILL "$jekyll_pid"

    bundle exec jekyll "${JEKYLL_ARGS[@]}" &
  fi
done
