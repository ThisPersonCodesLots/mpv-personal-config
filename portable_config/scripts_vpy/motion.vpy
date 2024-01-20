"""
Script by @maoiscat (https://github.com/maoiscat/mpv-mvtools-script)
fork by @ ()
"""

import vapoursynth as vs

core = vs.core
# Set the desired output frame rate (eg. 48fps)
output_fps = 48

# YUV444P8 - accurate for brightness/luma
# YUV420P8 - accurate for chroma subsampling
# clip = video_in.resize.Bilinear(format=vs.YUV420P8)
# clip = video_in.resize.Bicubic(format=vs.YUV420P8)
# clip = video_in.resize.Lanczos(format=vs.YUV444P8)
clip = video_in.resize.Lanczos(format=vs.YUV420P8)

# Assume the input video frame rate and convert it to a high frame rate
vden = 1000
vfps = int(container_fps * vden)
clip = core.std.AssumeFPS(video_in, fpsnum=vfps, fpsden=vden)

# Perform motion estimation using the MVTools2 plugin
super = core.mv.Super(clip, pel=2, sharp=0, rfilter=2)

# Modify the search parameter to change the motion estimation accuracy

# Forward motion vector
mvfw = core.mv.Analyse(super, blksize=32, isb=False, search=4, dct=5)
# Backward motion vector
mvbw = core.mv.Analyse(super, blksize=32, isb=True, search=4, dct=5)

# Convert the video to the desired output frame rate using motion-compensated frame interpolation
dfps = int(output_fps * vden)
clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=vden, mask=1)

# Set the output clip
clip.set_output()
