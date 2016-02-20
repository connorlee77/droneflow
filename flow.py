import numpy as np 
import matplotlib.pyplot as plt 
import cv2

import StreamData as sd


def main():
	cv2.namedWindow('frame')

	pipe = sd.StreamData('v1.mov')
	pipe.getVideo()
	frame = pipe.getFrame()

	sd.printMatrix(frame)	

	cv2.imshow('frame', frame)
	cv2.waitKey()
	pipe.close()

if __name__ == '__main__':
 	main() 