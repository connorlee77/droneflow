import numpy as np 
import matplotlib.pyplot as plt 
import cv2

FILE_DIR = 'data/'

class StreamData:

	def __init__(self, video):
		self.directory = FILE_DIR + video

	def getVideo(self):
		self.cap = cv2.VideoCapture(self.directory)

		if self.cap.isOpened() is not True:
			self.cap.open()
	
	def getFrame(self):
		ret, frame = self.cap.read()

		if ret is False:
			self.cap.release()
			return ret

		return ret, cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	def close(self):
		if self.cap.isOpened():
			self.cap.release()
			return True

		return False

	def getTime(self):
		return self.cap.get(cv2.cv.CV_CAP_PROP_POS_MSEC)

def printMatrix(mat):

	for row in mat:
		s = ''
		for col in row:
			s += ' ' + str(col)
		print s 

