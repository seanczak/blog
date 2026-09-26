#!/usr/bin/env bash
# Local preview using the same Jekyll version as GitHub Pages (pinned in jekyll/Gemfile).
# Usage: jekyll/serve.sh [extra jekyll serve flags], then open http://127.0.0.1:4001/blog/
set -euo pipefail
cd "$(dirname "$0")"

# Call Bundler through Ruby so no `bundle` executable needs to be on PATH.
bundle() { ruby -e 'load Gem.bin_path("bundler", "bundle")' -- "$@"; }

if [ ! -d vendor/bundle ]; then
  bundle config set --local path vendor/bundle
  bundle install
fi

exec bundle exec jekyll serve --safe --source .. --destination ../_site --host 127.0.0.1 --port 4001 "$@"
