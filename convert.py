import cv2
import sys

def FrameCapture(path):
    """
    Converts a video into frames. Saves into current directory.
    """

    vidCap = cv2.VideoCapture(path)
    count = 0

    length = int(vidCap.get(cv2.CAP_PROP_FRAME_COUNT))
    numDigits = len(str(length)) + 1
    success, image = vidCap.read()

    while success:
        frameString = "frame" + str(count).zfill(numDigits) + ".jpg"
        cv2.imwrite(frameString, image)
        success, image = vidCap.read()
        count += 1

    if count == 0:
        print("Conversion failed!")
    else:
        print("Conversion successful!")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        FrameCapture(sys.argv[1])
