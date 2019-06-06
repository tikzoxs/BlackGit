import cv2 
import numpy as np
import time

cv2.namedWindow("stroop", cv2.WINDOW_NORMAL)
cv2.resizeWindow("stroop", 500,1000)

start = int(round(time.time() * 1000))
iterations = 3
T = 16
TS = T * iterations
n1 = np.random.choice([11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44], T, replace=False)
n2 = np.random.choice([11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44], T, replace=False)
n3 = np.random.choice([11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44], T, replace=False)
n4 = np.random.choice([11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44], T, replace=False)
if(iterations == 1):
	n = n1
if(iterations == 2):
	n = np.concatenate((n1,n2))
if(iterations == 3):
	n = np.concatenate((n1,n2,n3))
if(iterations == 4):
	n = np.concatenate((n1,n2,n3,n4))
flag = False
TT = 0
img = cv2.imread("point" + ".png")
cv2.imshow("stroop", img)

while chr(cv2.waitKey()) != 's':
	continue

for i in range(TS):
	start = int(round(time.time() * 1000))
	while int(round(time.time() * 1000)) < start + 1000:
		continue
	img = cv2.imread(str(n[i]) + ".png")
	cv2.imshow("stroop", img)
	t1 = int(round(time.time() * 1000))
	k = chr(cv2.waitKey())
	t2 = int(round(time.time() * 1000))
	if n[i]%10 == 1 and k == 'r':
		flag = True
	elif n[i]%10 == 2 and k == 'g':
		flag = True
	elif n[i]%10 == 3 and k == 'b':
		flag = True
	elif n[i]%10 == 4 and k == 'y':
		flag = True
	else:
		flag = False
	TT = TT * (2 - flag) + ((n[i]%10 - np.floor(n[i]/10) != 0) * -1 * 0.3 + 1) * (t2 - t1)

score = 100000 / TT * iterations
cv2.destroyAllWindows()
print("***   Your score : " + str(score) + "   ***")