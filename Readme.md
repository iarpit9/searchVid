# **Searching for a snippet inside a Video** 

---

**Searching for a snippet inside a Video**

This is a simple tool to search for a video snippet inside a parent (or not) video.
---


### 1. Functioning:

To generate a snippet of a larger video ffmpeg_extract_subclip can be used as follows:

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("Input", t_start, t_end, targetname="OutputPath")

However, without setting keyframes correctly, ffmpeg tends to give inacccurate results with certain frames at the start and at the end turning
out to be black/empty. It is strongly advisable to check the trimmed output to make sure that this has not happened to your result, before using the 
tool. 

It may be preferable to use a simple video editing tool to trim a test video.

Latest version of the following libraries have been used while testing the script:

1 - OpenCV.
2 - Numpy.

The script searchvid.py requires two parameters at run time-

1 - The path of the video in which the search has to be performed.
2 - The path of the video which has to be searched for.

For the sake of testing a short video clip and a snippet starting at 5 s and ending at 10 s , has been placed inside the 'testVids' folder. 

Example:

python searchvid.py testVid.mp4 snip2.mp4

On running the script the paths entered for the two videos are displayed for verification. The script displays an output like so if the snippet 
is found:

The snippet video was found from -  5 s ( 5372 ms) to  10  s ( 10043 ms)

If not found, the following message is displayed:

The snippet video was not found.

If for some reason the script is unable to read the video from the given path a message saying "Invalid Input" is displayed.

### 2. Approach

The approach used is based on the intuition that two images having the same resolution will have effectively the same values. Hence subtracting the two 
should leave us with a zero matrix.

However, this still leaves a problem where two frames can have a repeated image frame at two different intervals. To tackle this we test the 
complete snippet frame-by-frame from the point of first match in the main video, making sure that each frame in the search video cancels each frame in the 
main video thus confirming that the sequence that we have detected is the correct one. On reaching the end of the snippet we break the loop and return to main.main
If, the sequence breaks at anypoint we reset the video capture for the main video to the point just after the first detection and repeat the process.If

The advantage of this approach is that only if all the frames in the subset match all the frames in the superset, will a positive detection be made.

### 3. Improvements

There might remain certain edge cases where the video is repetitive to the last frame. In such cases the result might not match the original 
trim start and end points as both would be the same.
