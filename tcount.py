import cv2 
import numpy as np

def change(back, orientation, R, G, B):
	disp = back
	disp[:,:,0] = R
	disp[:,:,1] = G
	disp[:,:,2] = B
	for i in range(194,196):
		for j in range(192,208):
			disp[i][j] = [0,0,0]
	for i in range(195,208):
		for j in range(199,201):
			disp[i][j] = [0,0,0]
	return np.rot90(disp, orientation - 1)

cv2.namedWindow("Tcount", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Tcount", 500,500)

back = np.zeros((400,400,3))

TS = 100
n = np.random.choice([11, 12, 13, 14, 21, 22, 23, 24, 31, 32, 33, 34, 41, 42, 43, 44], TS, replace=True)
flag = False
cv2.imshow("Tcount", back)
or_count = 0

while chr(cv2.waitKey()) != 's':
	continue
print("Starting....")

for i in range(TS):
	R = ((n[i]%10 == 1)+1) / 2 * np.random.rand()
	G = ((n[i]%10 == 2)+1) / 2 * np.random.rand()
	B = ((n[i]%10 == 3)+1) / 2 * np.random.rand()
	R = np.clip(R, 0.1, 1)
	G = np.clip(G, 0.1, 1)
	B = np.clip(B, 0.1, 1)
	orientation = np.floor(n[i]/10)
	slide = change(back, orientation, R, G, B)
	cv2.imshow("Tcount", slide)
	cv2.waitKey(400)
	or_count = or_count + (orientation == 1) * 1

score = int(chr(cv2.waitKey()))  * 10 
score = score + int(chr(cv2.waitKey()))
score = np.abs(score - or_count) / or_count * 100
score = 100 - score
cv2.destroyAllWindows()
print("***   Answer is  : " + str(or_count) + "   ***")
print("***   Your score : " + str(score) + "   ***")