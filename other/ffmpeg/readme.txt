This gives an example of using ffmpeg to encode to a file, piping
some output (from python) that are the frames into the ffmpeg program.
The frames are in rgb24 format.

To show this in action, issue the command:

# python frame_source.py | ffmpeg -r 1 -f rawvideo -pix_fmt rgb24 -s 160x120 -i - -threads 0 -preset fast -y -crf 21 -pix_fmt yuv420p output.mp4

This will create a mp4 file of 1 fps, with frames of varying color bands.
Each top band is reddish, middle-band is greenish and bottom-band is bluish.
