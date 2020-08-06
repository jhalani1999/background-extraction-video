import imutils
import numpy as np
import cv2
import time
from pip._vendor.msgpack.fallback import xrange


path = "resources/cut.mp4"


def frames_per_second(location):
    """
    Calculate FPS
    Inout: Path of the Video
    Output: return list of fps(size 2).
    """

    # video from path
    video = cv2.VideoCapture(location);

    # getting fps
    fps1 = video.get(cv2.CAP_PROP_FPS)

    # Number of frames to capture
    num_frames = 100;
    start = time.time()
    # Grab a few frames
    for i in xrange(0, num_frames):
        ret, frame = video.read()
    end = time.time()
    seconds = end - start   # Time elapsed
    fps = num_frames / seconds  # Calculate frames per second
    return [fps1, fps]


cap = cv2.VideoCapture(path)
images = []
fps = frames_per_second(path)
out = cv2.VideoWriter('output2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps[0], (720, 480))


while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=720)
    cv2.imshow('image', frame)
    dim = (720, 480)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)  # resampling using pixel area relation

    images.append(frame)
    # removing the images after every 300 image
    if len(images) == 300:
        images.pop(0)

    image = np.array(images)
    image = np.mean(image, axis=0)
    image = image.astype(np.uint8)
    out.write(image)
    cv2.imshow('background', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
