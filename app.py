import cv2
from imutils import paths
import imutils
import numpy

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

imglist=sorted(list(paths.list_images("subjects")))

for imgpath in imglist:
	for w in range(500, 1001, 100):
		image=cv2.imread(imgpath)
		img=imutils.resize(image, width=w)
		gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

		faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=2)

		imgCropped = []
		for x, y, w, h in faces:
			imgCropped.append(img[y:y+h, x:x+w])
			imgCropped[-1] = imutils.resize(imgCropped[-1], width = 500)

		if (faces != ()):
			print("SAVING " + imgpath[9:-4] + "-Size" + str(w) + ".jpg" + "...")

		if (len(faces) != 0):
			for img in imgCropped:
				cv2.imwrite("./cropped/" + imgpath[9:-4] + "-Size" + str(w) + ".jpg", img)

		prevFaces = faces

cv2.destroyAllWindows()
