# mpv.conf

## Interpolation:
- For a 72 fps video, you may want to set the _buffered-frames_ parameter to a value that is at least equal to the duration of one frame (i.e., 1/72 seconds), so that there are enough buffered frames available to maintain a steady processing rate. A value of 4 may be sufficient for this purpose.

- As for the _concurrent-frames_ parameter, you can experiment with different values to see what works best for your system and the specific video you are processing. You may want to start with a value of 8 or 16 and increase it gradually to see if it improves performance. Keep in mind that increasing the number of concurrent frames may use more CPU and GPU resources, so make sure your system can handle the load without overheating or crashing.

- After some test cases I conclude that vapoursynth had no real motion interpolation.
Yeah, it does a small improvement but you can't tell the difference from 24 fps to 48/72/120 and so on.
- I recommend you to use Flowframes [1] and taking your time to use it properly. RISE it's more advanced than DAIN/Vapour!
- If you are lucky and got RTX GPU, ~24min -> 10-25 min of processing from 24 fps to 48 fps. And WORTH IT.
[1] https://nmkd.itch.io/flowframes