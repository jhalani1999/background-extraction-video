import imutils
import numpy as np
import cv2
import time
from pip._vendor.msgpack.fallback import xrange


path = "resources/data/input.mp4"


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


def polygon(point, img):
    """
    Return polygon cropped image.
    :param: point and image
    :return: cropped image
    """
    mask = np.zeros(img.shape[0:2], dtype=np.uint8)
    cv2.drawContours(mask, [point], -1, (255, 255, 255), -1, cv2.LINE_AA)  # method 1 smooth region
    res = cv2.bitwise_and(img, img, mask=mask)
    rect = cv2.boundingRect(point)  # returns (x,y,w,h) of the rect
    cropped = res[rect[1]: rect[1] + rect[3], rect[0]: rect[0] + rect[2]]
    return cropped


cap = cv2.VideoCapture(path)
images = []
fps = frames_per_second(path)
out = cv2.VideoWriter('output2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps[0], (1202, 664))
points = np.array([[[0, 535], [1123, 0], [1201, 0], [1201, 150], [950, 663], [0, 663]]])

while True:
    ret, frame = cap.read()
    dim = (1202, 664)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)  # resampling using pixel area relation
    cv2.imshow('image', frame)

    cropped = polygon(points, frame)
    images.append(cropped)
    # removing the images after every 300 image
    if len(images) == 300:
        images.pop(0)
    image = np.array(images)
    image = np.mean(image, axis=0)
    image = image.astype(np.uint8)

    diff = frame.copy()
    cv2.absdiff(frame, cropped, diff)
    dst = cv2.addWeighted(image, 1, diff, 1, 0.0)

    out.write(dst)

    cv2.imshow('background', dst)
    cv2.imshow('cropped', cropped)
    cv2.imshow('difference', image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
