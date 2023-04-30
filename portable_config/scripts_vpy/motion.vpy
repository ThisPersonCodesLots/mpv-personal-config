"""
Script by @maoiscat (https://github.com/maoiscat/mpv-mvtools-script)
Tips: try using multiple of x when it's come to frame. (24 x 2 = 48, 24 x 3 = 72, 24 x 4 = 96, etc.)
Adjust "frame" variable to your prefered frame rate or display refresh rate.
"""

import vapoursynth as vs

core = vs.core

# Resize the input video to YUV420P8 format using bicubic interpolation
clip = video_in.resize.Bicubic(format=vs.YUV420P8)

# Set the desired output frame rate
output_fps = 48

# Assume the input video frame rate and convert it to a high frame rate
vden = 1000
vfps = int(container_fps * vden)
clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)

# Perform motion estimation using the MVTools2 plugin
super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2)
# Modify the search parameter to change the motion estimation accuracy. I suggest to use 4 for 1080p and 8 for 4K.
mvfw = core.mv.Analyse(super, blksize=32, isb=False, search=3, dct=5)
mvbw = core.mv.Analyse(super, blksize=32, isb=True, search=3, dct=5)

# Convert the video to the desired output frame rate using motion-compensated frame interpolation
dfps = int(output_fps * vden)
clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=vden, mask=1)

# Set the output clip
clip.set_output()
