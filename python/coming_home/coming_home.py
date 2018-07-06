import os
import multiprocessing as mp
import subprocess
import time

# URL = r"https://www.firstonetv.net/Live/United-Kingdom/BBC-One--4"
# URL = r"https://vs-hls-uk-live.akamaized.net/pool_902/live/bbc_one_hd/bbc_one_hd.isml/bbc_one_hd-pa4=128000-video=2812032.m3u8"
URL = r"http://a.files.bbci.co.uk/media/live/manifesto/audio_video/simulcast/hls/uk/hls_tablet/ak/bbc_one_london.m3u8"
# URL = r"http://vs-hls-uk-live.akamaized.net/pool_902/live/bbc_one_london/bbc_one_london.isml/bbc_one_london-pa2%3d48000-video%3d156000.norewind.m3u8"

# See https://gist.github.com/random-robbie/e56919b5603ecc87af885391e7331657

class DownloadTask:
  def __init__(self):
    self.counter = 0
  
  def make_task(self, q, q2, q3):
    self.counter += 1
    c = self.counter
    def fn(c, q, q2, q3):
      fname = "{:04d}.mp4".format(c)
      fnamePart = fname.replace(".mp4", ".mp4.part")
      if os.path.exists(fnamePart):
        os.unlink(fnamePart)
      #proc = subprocess.Popen('python -m youtube_dl "{}" -o "{}"'.format(URL, fname))
      #                        # stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      # T = "00:15:00"
      T = "00:00:20"
      cmd = 'ffmpeg -y -i "{}" -t {} -f mp4 -acodec copy -vcodec copy "{}"'.format(URL, T, fnamePart)
      q3.put(cmd)
      # subprocess.check_output(cmd, shell=True)
      os.system(cmd)
      q.put( {"counter":c, "fnamePart": fnamePart, "fname": fname } )
      q2.put( 0 )
    return lambda : fn(c, q, q2, q3)

def convert(q, q3):
  while True:
    stuff = q.get()
    cmd = 'ffmpeg -y -i "{}" -acodec aac -b:a 48k -vcodec libx264 -crf 28 "{}"' \
        .format(stuff["fnamePart"], stuff["fname"])
    q3.put(cmd)
    os.system(cmd)
    os.unlink(stuff["fnamePart"])

def download(d, q, q2, q3):
  while True:
    q2.get()
    task = d.make_task(q, q2, q3)
    task()

def log(q3):
  with open('log.txt', 'w') as f:
    while True:
      line = q3.get()
      f.write(line)
      f.flush()
  
if __name__ == '__main__':
  q = mp.Queue()
  q2 = mp.Queue()
  q3 = mp.Queue()
  d = DownloadTask()

  t1 = mp.Process( target=convert, args=(q, q3, ) )
  t2 = mp.Process( target=download, args=(d, q, q2, q3, ) )
  t3 = mp.Process( target=log, args=(q3, ) )
  
  t1.start()
  t2.start()
  t3.start()

  q2.put( 0 )

  t1.join()
  t2.join()
  t3.join()
