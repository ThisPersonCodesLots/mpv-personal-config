# mpv.conf

## ***ISSUE***
- Using vapoursynth + shaders cause losing frames. (I'm still trying to fix it)

## INFO

- Please modify the file to your needs and not blindly copy-paste!
- Take your time and read comments!
- Still updating this!
- I tried to make it as simple as possible, using only the necessary features and for low end PCs. (AMD Ryzen 7 4800HS, nVidia GTX 1650 mobile, 2k monitor, +120hz)

## ***WIKI***
- [iamscum](https://iamscum.wordpress.com/guides/videoplayback-guide/mpv-conf/)
- [mpv manual](https://mpv.io/manual/master/)

### input.conf
- SWIFT+a - change subtitles font
- ESC - exit MPV and save current timeline
- CTRL+NUM - active shaders

### mpv.conf
- TBA

### Interpolation:
- For a 72 fps video, you may want to set the _buffered-frames_ parameter to a value that is at least equal to the duration of one frame (i.e., 1/72 seconds), so that there are enough buffered frames available to maintain a steady processing rate. A value of 4 may be sufficient for this purpose.

- As for the _concurrent-frames_ parameter, you can experiment with different values to see what works best for your system and the specific video you are processing. You may want to start with a value of 8 or 16 and increase it gradually to see if it improves performance. _Keep in mind that increasing the number of concurrent frames may use more CPU and GPU resources, so make sure your system can handle the load without overheating or crashing._

- After some test cases I conclude that vapoursynth had no real motion interpolation.
Yeah, it does a small improvement but you can't tell the difference from 24 fps to 48/72/120 and so on.

- I recommend you to use Flowframes ( https://nmkd.itch.io/flowframes ) and take your time to use it properly. RIFE it's more advanced than DAIN/Vapour!

- If you are lucky and got RTX GPU, ~24min -> 10-25 min of processing from 24 fps to 72/120 fps. And WORTH IT.

### Shaders:

- TBA: HDR support! (mpv default seems to be weird sometimes).
- Shaders tested on +480p videos, using a 2k monitor, +120 hz.
- After some research and custom configuration of shaders, I found that the best shaders for me are:
    - [Upscale+Sharpen+Thin+Dark](https://github.com/vioo-bkp/mpv-personal-config/tree/main/portable_config/shaders/safe)
    - Upscale+Sharpen+Thin
- I recommend you to use the shaders that are in the folder "safe" and test them one by one, to see which one is the best for you. (I'm still testing them, so I can't tell you which one is the best for you).

#### Disclaimer: 
- I'm not a professional, I just like to watch anime and movies with a better quality. I'm still learning about shaders and how to use them properly. If you have any suggestions, please let me know!