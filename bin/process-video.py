import moviepy.editor as mpy
from moviepy.video.tools.cuts import FramesMatches
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import datetime
import argparse
from subprocess import call
import img2stl

# clean up


# eg. python bin/process-video.py media/fish.mp4
parser = argparse.ArgumentParser(description='Extract seamless loops from a video')
parser.add_argument('file', metavar='N', type=str, help='vido file')
args = parser.parse_args()
clip = mpy.VideoFileClip(args.file).resize(width=200)
matches = FramesMatches.from_clip(clip, 40, 3) # loose matching
# find the best matching pair of frames > 1.5s away
best = matches.filter(lambda x: x.time_span > 1.5).best()

# create clip of loop
start_time = datetime.timedelta(0, best.t1)
end_time = datetime.timedelta(0, best.t2)
duration =  end_time - end_time

call("ffmpeg -i {} -vcodec copy -acodec copy -ss {} -to {} tmp/clip.mp4".format(args.file, start_time, end_time), shell=True)

ffmpeg_extract_subclip(args.file, best.t1, best.t2, targetname="tmp/clip.mp4")

# convert to B&W & extract frames
call("ffmpeg -i tmp/clip.mp4 -vf hue=s=0 -c:a copy tmp/bw.mp4 && ffmpeg -i tmp/bw.mp4 -vf fps=5 -vsync 0 tmp/out%d.png && convert tmp/out*.png -evaluate-sequence mean tmp/averageresult.png", shell=True)

img2stl.run("tmp/averageresult.png", "media/blended-model.stl", (5, 5))

