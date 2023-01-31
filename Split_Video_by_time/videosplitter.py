"""
    This script will split the video into two files when valid time periods are
    given.
    ### usage
    ```python
    python videosplitter.py test.mp4 0 50 out1.mp4 out2.mp4
    ```
    OR
    ```python
    python videosplitter.py -h
    ```
"""

import ffmpeg
import argparse

parser = argparse.ArgumentParser(
    description="Split A media file into two chunks")
parser.add_argument('inputfile', help="Input filename")
parser.add_argument('starttime', type=float, help="Start time in seconds")
parser.add_argument('endtime', type=float, help="End time in seconds")
parser.add_argument('outputfile1', help="Output filename")
parser.add_argument('outputfile2', help="Output filename")

args = parser.parse_args()

in1 = ffmpeg.input(args.inputfile)


v1 = in1.filter('trim', start=float(args.starttime), end=(args.endtime))
v2 = in1.filter('trim', start=float(args.endtime))


out1 = ffmpeg.output(v1, args.outputfile1)
out2 = ffmpeg.output(v2, args.outputfile2)

out1.run()
out2.run()
