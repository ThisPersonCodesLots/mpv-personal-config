"""
Script by @maoiscat (https://github.com/maoiscat/mpv-mvtools-script)
Tips: try using multiple of x when it's come to frame. (24 x 2 = 48, 24 x 3 = 72, 24 x 4 = 96, etc.)
Adjust "frame" variable to your prefered frame rate or display refresh rate.
"""
"C:\Program Files (x86)\SVP 4\plugins64\svpflow1.dll"
import vapoursynth as vs

core = vs.core

# Resize the input video to YUV420P8 format using bicubic interpolation
# This option can provide dropped frames when used with shaders! (uncheck if CPU = strong).
# clip = video_in.resize.Bicubic(format=vs.YUV420P8)

# Set the desired output frame rate
output_fps = 48

# Assume the input video frame rate and convert it to a high frame rate
vden = 1000
vfps = int(container_fps * vden)
clip = core.std.AssumeFPS(video_in, fpsnum=vfps, fpsden=vden)

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

# BlockFPS for 60fps using 24fps source (Ryzen 7 4800HS)

# import vapoursynth as vs
# core = vs.core

# clip = video_in
# vden = 1000
# vfps = int(container_fps*vden)
# dden = 1000
# dfps = int(display_fps*dden)
# clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
# super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2, hpad=8, vpad=8, levels=0)
# mvfw = core.mv.Analyse(super, blksize=32, overlap=16, isb=False, search=3, searchparam=2, pelsearch=2)
# mvbw = core.mv.Analyse(super, blksize=32, overlap=16, isb=True,  search=3, searchparam=2, pelsearch=2)
# clip = core.mv.BlockFPS(clip, super, mvbw, mvfw, num=dfps, den=dden)

# clip.set_output()

# FlowFPS for 60fps using 24fps source (Ryzen 7 4800HS)

# import vapoursynth as vs
# core = vs.core

# clip = video_in
# vden = 1000
# vfps = int(container_fps*vden)
# dden = 1000
# dfps = int(display_fps*dden)
# clip = core.std.AssumeFPS(clip, fpsnum=vfps, fpsden=vden)
# super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2, hpad=8, vpad=8, levels=0)
# mvfw = core.mv.Analyse(super, blksize=32, overlap=16, isb=False, search=3, searchparam=2, pelsearch=2)
# mvbw = core.mv.Analyse(super, blksize=32, overlap=16, isb=True,  search=3, searchparam=2, pelsearch=2)
# clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=dden, mask=0)

# clip.set_output()
