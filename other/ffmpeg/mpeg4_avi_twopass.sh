#!/bin/sh
ffmpeg -y -i $1 -c:v mpeg4 -vtag xvid -b:v 600k -pass 1 -an -f avi /dev/null
ffmpeg -i $1 -c:v mpeg4 -vtag xvid -b:v 600k -pass 2 -c:a libmp3lame -b:a 112k $2
