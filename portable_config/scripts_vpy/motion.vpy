"""
Script by @maoiscat (https://github.com/maoiscat/mpv-mvtools-script)
This script is not mine, I just added the ability to use it with 24 fps videos, not current display refresh rate.
Eg. Video recorded at 24 fps and 144 hz monitor. Script adjust frame rate video from 24 fps to 60 fps.
Tips: try using multiple of x when it's come to frame. (24 x 2 = 48, 24 x 3 = 72, 24 x 4 = 96, etc.)
Still working on it, but it's usable. Maybe can work, maybe can broke itself.
Adjust "frame" variable to your prefered frame rate or display refresh rate.
"""

import vapoursynth as vs
core = vs.core
clip = video_in.resize.Bicubic(format=vs.YUV420P8)
vden = 1000
vfps = container_fps*vden
# change frame to your prefered frame rate or display refresh rate
frame = 59
dfps = frame*vden
if container_fps < frame:
    clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
    super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2)
    mvfw = core.mv.Analyse(super, blksize=32, isb=False, search=3, dct=5)
    mvbw = core.mv.Analyse(super, blksize=32, isb=True,  search=3, dct=5)
    clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=vden, mask=1)
    clip.set_output()
else:
    clip.set_output()
