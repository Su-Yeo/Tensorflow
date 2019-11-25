import cv2
import sys

#이미지 경로받아오기
path = sys.argv[1]
src = cv2.imread(path , cv2.IMREAD_COLOR)
copy_file = src.copy()

#이미지 줄이기
dst = cv2.resize(src, dsize=(750,664), interpolation=cv2.INTER_AREA)	

#이미지 자르기
#가로 : 550 세로 : 620
image = dst.copy()
image = dst[30:650, 100:650]


#상의 이미지 추출
#가로 : 550 세로 : 325
upper = image.copy()
upper = image[0:325, 0:600]


#하의 이미지 추출
#가로 : 550 세로 : 295
lower = image.copy()
lower = image[325:620, 0:600]

#하의 이미지를 -1.jpg로 변경
origin_path = sys.argv[1]
lower_path = origin_path[:-4] + "-1.jpg"

#해당 경로에 하의 이미지를 저장
cv2.imwrite(lower_path, lower)

#경로/원본파일.jpg → 경로/원본파일-2.jpg로 변경
origin_path = sys.argv[1]
save_path = origin_path[:-4] + "-2.jpg"

#해당 경로에 원본파일을 저장
cv2.imwrite(save_path, copy_file)

#원래있던 경로의 이미지에 상의를 덮어씌움
cv2.imwrite(path, upper)


#cv2.waitKey(0)
#cv2.destroyAllWindows()