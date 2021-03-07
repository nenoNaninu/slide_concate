import numpy as np
import cv2
import sys
import glob
import os

if __name__ == '__main__':
    dir = sys.argv[1]
    save_name = sys.argv[2]

    dir = os.path.join(dir, "[1-9].png")
    print(dir)
    imgs_path = glob.glob(dir)
    print(imgs_path)

    img_list = []
    for path in imgs_path:
        img = cv2.imread(path)
        img_list.append(img)

    height, width, _ = img_list[0].shape

    buffer = np.zeros((3 * height, 3 * width, 3), dtype=img_list[0].dtype)

    for i in range(3):
        for j in range(3):
            img = img_list[i * 3 + j]
            img[0:height, 0] = 0
            img[0, 0:width] = 0
            
            img[0:height, (width - 1)] = 0
            img[(height - 1), 0:width] = 0

            buffer[i * height:(i + 1) * height, j * width: (j + 1) * width, :] = img

    cv2.imwrite("big.png", buffer)
