#!/bin/bash

function fn {
  eval $(printf 'lynx -dump "https://www.google.co.uk/search?q=youtube premier league darts 2016 week %d&start=%d"' $1 $2)
}

function fn2 {
fn $1 $2 | \
  grep youtube | grep watch | \
  sed 's/.*https:\/\/www.youtube/https:\/\/www.youtube/g' | \
  sed 's/&.*//g' | \
  python -c $'import sys, urllib\nfor x in sys.stdin: print(urllib.unquote(x))' | \
  cut -c -43 - | \
  grep '^https' | \
  sort | uniq
}

function fn3 {
  (fn2 $1 0; fn2 $1 10) | sort | uniq
}

for x in $(fn3 $1)
do
  echo $x
  python -m youtube_dl --get-title $x 2>/dev/null
done


