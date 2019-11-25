import cv2
import sys
import os

#원본-2.jpg 파일경로 가져오기
path = sys.argv[1]
src = cv2.imread(path , cv2.IMREAD_COLOR)

#원본 파일경로 가져오기
origin_path = path[:-6] + ".jpg"
cv2.imwrite(origin_path, src)

#원본-1.jpg 삭제
path2 = path[:-6] + "-1.jpg"
os.remove(path2)

#원본-2.jpg 삭제
os.remove(path)


