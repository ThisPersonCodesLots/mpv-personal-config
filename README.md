## INFO

- Please modify the file to your needs and not blindly copy-paste!
- Take your time and read comments!
- I tried to make it as simple as possible, using only the necessary features and for medium/low end PCs. (_20W Max Power
  Usage_, AMD Ryzen 7 4800HS, nVidia GTX 1650 mobile, 2k monitor, +120hz)
- Make sure you have Vapoursynth and MVtools installed as portable files and/or they are in *path system*.

## ***Resources***

- [mpv manual](https://mpv.io/manual/master/)
- [iamscum](https://iamscum.wordpress.com/guides/videoplayback-guide/mpv-conf/)
- [mpv_lazy](https://github.com/hooke007/MPV_lazy)
- [maoiscat](https://github.com/maoiscat/mpv-mvtools-script)
- [interpolation_test](https://github.com/haasn/interpolation-samples)
- [Soap Opera Effect](https://www.reddit.com/r/mpv/comments/oke3aa/guide_how_to_get_motion_interpolation_soap_opera/)

### input.conf

- SWIFT+s - change subtitles font
- ESC - exit MPV and save current timeline
- CTRL+number - active shaders
- CTRL+M - motion interpolation on/off

### mpv.conf

- Vapoursynth as toggle option. (Can cause losing frames when toggle on/off, just skip 1-2 seconds to reset the buffer)

### Info about mvtools parameters

While choosing the values, the primary thing to consider is the hardware capabilities of your machine, as well as the
demands of the video processing task you're performing. Higher values can result in increased utilization of system
resources (CPU, GPU, and memory). So, you need to test and make sure your system can handle the load.

1. buffered-frames: Specifies the number of frames to be buffered before being processed. This value is not required to
   be a multiple of 4. You can choose any positive integer that suits your needs and hardware. Remember that a larger
   buffer size might increase memory usage but potentially allows for smoother playback.
   For buffered-frames, the default value is typically around 4-8. This should be more than enough for most use cases.
   Increasing this value might help if you're experiencing stuttering or slower frame rates, but it will also consume
   more RAM. If you're not having any playback issues, leaving it at the default is generally recommended.

2. concurrent-frames: This parameter sets the concurrency, or the number of frames being processed at the same time.
   Again, the value is not required to be a multiple of 4, but it should ideally not exceed the number of logical
   processors (cores) available on your computer, or it may not bring much extra performance and can even slow things
   down due to overheads of task switching.
   For concurrent-frames, a good starting point could be equal to the number of logical processors your CPU has. In my
   case with Ryzen 7 4800HS, that would be 16 (8 cores x 2 threads per core). This setting allows the maximum
   exploitation of your CPU's multi-threading capabilities.

3. blksize: This is the size of the block the motion estimation algorithm will consider. Smaller blocks will require less
  computation, hence improve overall performance. However, using smaller blocks might reduce the accuracy of motion
  estimation as detailed motion patterns may be ignored.

4. search: This parameter controls the motion estimation algorithm's search distance around the block. A larger search
  radius could potentially enhance motion estimation accuracy as it takes into account a wider area for prediction. But,
  it considerably increases the amount of computation, reducing execution speed.

### Shaders:

- Shaders tested on +480p videos, using a 2k monitor, +120 hz.
- After some research and custom configuration of shaders, I found that the best shaders for me are
    - [Upscale+Sharpen+Thin+Dark](https://github.com/vioo-bkp/mpv-personal-config/tree/main/portable_config/shaders/safe)

- I recommend you to use the shaders that are in the folder "safe" and test them one by one, to see which one is the
  best for you.

- Use the shaders that are in the folder "unsafe" only if you have a good GPU and
  CPU. [Anime4K](https://www.reddit.com/r/animepiracy/comments/spbyhu/evaluating_the_effectiveness_of_anime4k_for/) it's
  a bad idea to use it.

#### Disclaimer:

- I'm not a professional, I just like to watch anime and movies with a better quality. I'm still learning about shaders
  and how to use them properly. If you have any suggestions, please let me know!
