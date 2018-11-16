
import argparse
import numpy as np
import cv2


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search Video')
    parser.add_argument(
        'InputVideo',
        type=str,
        help='Path to full-length video'
    )
    parser.add_argument(
        'SnipVideo',
        type=str,
        help='Path to video snippet which has to be searched'
    )

args = parser.parse_args()

vid_path = args.InputVideo
snip_path = args.SnipVideo

t_start = 0
t_end = 0


def search_video(video_path, snipped_path):
    print("Full video Path is - ", video_path, " and snippet path is - ", snipped_path)
    global t_start, t_end
    v1 = cv2.VideoCapture(video_path)
    v2 = cv2.VideoCapture(snipped_path)
    total_frames = v2.get(cv2.CAP_PROP_FRAME_COUNT)
    ret, frame = v1.read()
    ret1, frame1 = v2.read()
    
    if ret1:
        while ret:
            
            if frame1 is not None and frame is not None and frame1.shape == frame.shape and not (np.subtract(frame1, frame).any()):
                frame_pos = v1.get(cv2.CAP_PROP_POS_FRAMES)
                t_start = v1.get(cv2.CAP_PROP_POS_MSEC)
                
                ret, frame = v1.read()
                ret1, frame1 = v2.read()
                while ret1:
                    if frame1.shape == frame.shape and not (np.subtract(frame1, frame).any()):
                        t_end = v1.get(cv2.CAP_PROP_POS_MSEC)
                        
                        if v2.get(cv2.CAP_PROP_POS_FRAMES)==total_frames-1:
                            return
                    else:
                        t_start = 0
                        t_end = 0
                        v1.set(cv2.CAP_PROP_POS_FRAMES, frame_pos + 1)
                        v2.release()
                        v2 = cv2.VideoCapture(snipped_path)
                        ret1, frame1 = v2.read()
                        break
                    ret, frame = v1.read()
                    ret1, frame1 = v2.read()
            ret, frame = v1.read()
    else:
        print("Invalid Input")

search_video(vid_path, snip_path)

if t_start==0 and t_end==0:
    print("The snippet video was not found")
else:
    print("The snippet video was found from - ", int(t_start/1000), "s (",int(t_start),"ms) to ",int(t_end/1000)," s (",int(t_end),"ms)")
