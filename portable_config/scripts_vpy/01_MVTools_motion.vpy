"""
Script by @maoiscat (https://github.com/maoiscat/mpv-mvtools-script)
Inspiration from @ahjolinna (https://github.com/ahjolinna/mpv-conf)
fork by @ ()
"""

# vapoursynth is installed in the portable_config folder so link it
import vapoursynth as vs

# Precautionary measures
max_width = 1920
max_height = 1080
max_fps = 60
# use BlockFPS instead of FlowFPS for better performance
max_flow_width = 1280
max_flow_height = 720

core = vs.core
# Set the desired output frame rate (eg. 48fps)
output_fps = 59

if not (video_in.width > max_width or video_in.height > max_height or video_in.fps > max_fps):
    # Resize the video to a smaller size for better performance
    # clip = video_in.resize.Bilinear(format=vs.YUV420P8)
    clip = video_in.resize.Bicubic(format=vs.YUV420P8)

    # Assume the input video frame rate and convert it to a high frame rate
    vden = 1000
    vfps = int(container_fps * vden)
    clip = core.std.AssumeFPS(video_in, fpsnum=vfps, fpsden=vden)

    # Perform motion estimation using the MVTools2 plugin
    # 'pel' can be changed to 4 for better accuracy or 1 for better speed (values allowed: 1 2 4)
    super = core.mv.Super(clip, pel=4, sharp=0, rfilter=2)

    # Forward motion vector
    mvfw = core.mv.Analyse(super, blksize=64, isb=False, search=4, dct=5)
    # Backward motion vector
    mvbw = core.mv.Analyse(super, blksize=64, isb=True, search=4, dct=5)

    dfps = int(output_fps * vden)
    use_block = clip.width > max_flow_width or clip.height > max_flow_height

    if use_block:
        # Use BlockFPS for better performance
        clip = core.mv.BlockFPS(clip, super, mvbw, mvfw, num=dfps, den=vden)
    else:
        # Use FlowFPS for better quality
        clip = core.mv.FlowFPS(clip, super, mvbw, mvfw, num=dfps, den=vden, mask=2)

# Set the output clip
clip.set_output()