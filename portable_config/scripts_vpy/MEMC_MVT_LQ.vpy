import sys
import os
# If the directory containing k7sfunc is not in sys.path, Python won't be able to find and import it.
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import vapoursynth as vs
from vapoursynth import core
import k7sfunc as k7f

clip = video_in

H_Pre = 1440
Recal = True
Block = True
Lk_Fmt = False


ret = k7f.FPS_CTRL(clip, fps_in=container_fps, fps_ret=True)
clip = k7f.FMT_CTRL(clip, h_max=H_Pre, fmt_pix=1 if Lk_Fmt else 0)
clip = k7f.MVT_LQ(clip, fps_in=container_fps, fps_out=container_fps*2, recal=Recal, block=Block)

clip.set_output()
