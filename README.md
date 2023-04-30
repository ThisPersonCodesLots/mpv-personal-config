## INFO

- Please modify the file to your needs and not blindly copy-paste!
- Take your time and read comments!
- I tried to make it as simple as possible, using only the necessary features and for low end PCs. (_25W Max Power Usage_, AMD Ryzen 7 4800HS, nVidia GTX 1650 mobile, 2k monitor, +120hz)

## ***ISSUE***

- Using vapoursynth + shaders cause losing frames. (I'm still trying to fix it).
- TBA: HDR support! (mpv default seems to be weird sometimes. Eg. OLED TV).

## ***WIKI*** + ***Resources***

- [mpv manual](https://mpv.io/manual/master/)
- [iamscum](https://iamscum.wordpress.com/guides/videoplayback-guide/mpv-conf/)
- [mpv_lazy](https://github.com/hooke007/MPV_lazy)
- [maoiscat](https://github.com/maoiscat/mpv-mvtools-script)
- [interpolation_test](https://github.com/haasn/interpolation-samples)

### input.conf

- SWIFT+a - change subtitles font
- ESC - exit MPV and save current timeline
- CTRL+NUM - active shaders

### mpv.conf
- TBA

### Interpolation:

- For a 72 fps video, you may want to set the _buffered-frames_ parameter to a value that is at least equal to the duration of one frame (i.e., 1/72 seconds), so that there are enough buffered frames available to maintain a steady processing rate. A value of 4 may be sufficient for this purpose.

- As for the _concurrent-frames_ parameter, you can experiment with different values to see what works best for your system and the specific video you are processing. You may want to start with a value of 8 or 16 and increase it gradually to see if it improves performance.

-  _Keep in mind that increasing the number of concurrent frames may use more CPU and GPU resources, so make sure your system can handle the load without overheating or crashing._

- I recommend you to use Flowframes ( https://nmkd.itch.io/flowframes ) and take your time to use it properly.

- If you are lucky and got RTX GPU, ~24min -> 10-25 min of processing from 24 fps to 72/120 fps. And WORTH IT.

### Shaders:

- Shaders tested on +480p videos, using a 2k monitor, +120 hz.
- After some research and custom configuration of shaders, I found that the best shaders for me are
    - [Upscale+Sharpen+Thin+Dark](https://github.com/vioo-bkp/mpv-personal-config/tree/main/portable_config/shaders/safe)

- I recommend you to use the shaders that are in the folder "safe" and test them one by one, to see which one is the best for you. (I'm still testing them, so I can't tell you which one is the best for you).
- Use the shaders that are in the folder "unsafe" only if you have a good GPU and CPU. [Anime4K](https://www.reddit.com/r/animepiracy/comments/spbyhu/evaluating_the_effectiveness_of_anime4k_for/) it's a bad idea to use it.

#### Disclaimer:

- I'm not a professional, I just like to watch anime and movies with a better quality. I'm still learning about shaders and how to use them properly. If you have any suggestions, please let me know!

- [MAL link](https://myanimelist.net/profile/kuwapt)