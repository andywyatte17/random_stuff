# (py-)win-clip

Python code for experimenting with bitmap-type data on the Windows (and other?) system clipboards.

## clipboard_win_read.py

Use this to extract bitmap clipboard data from various Windows programs, for example:

  - Run Gimp
  - Load an image.
  - Select All.
  - Copy.
  - Run clipboard_win_read.py - these will dump base64 data of the clipboard contents.

    py clipboard_win_read.py PNG
    py clipboard_win_read.py CF_DIBV5

The data here can be put into `clipboard_win_example_data.py` as an `Install_....DIBV5()` or
`Install_....PNG()` function to build up a set of test data.

## clipbard_win.py

Use this to either parse CF_DIBV5 data in the clipboard, either from an example or from the
current clipboard:

Read example data '0':

    py clipboard_win.py 0

Read from the clipboard (ie after Gimp > Load > Select > Copy sequence):

    py clipboard_win.py CF_DIBV5
