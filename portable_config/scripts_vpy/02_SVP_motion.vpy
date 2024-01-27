import vapoursynth as vs

core = vs.core
clip = video_in

svps = core.svp1.Super(video_in, pel=2, scale=2)
svpv = core.svp1.Analyse(svps, isb=False, delta=1, overlap=4)
clip = core.svp2.SmoothFps(video_in, svps, svpv, num=output_fps, den=1, mask=2)

clip.set_output()
