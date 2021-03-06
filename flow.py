import numpy as np 
import matplotlib.pyplot as plt 
import cv2

import StreamData as sd

x_pix = 320
y_pix = 240

x_ang = np.radians(54.4)
y_ang = np.radians(37.8)

def getHeight():
	return 3

def track():
	# params for ShiTomasi corner detection
	feature_params = dict( maxCorners = 100,
	                       qualityLevel = 0.3,
	                       minDistance = 7,
	                       blockSize = 7 )

	velocities = {}

	cv2.namedWindow('frame')
	pipe = sd.StreamData('v1.mov')
	pipe.getVideo()

	ret, prev_frame = pipe.getFrame()
	prev_points = cv2.goodFeaturesToTrack(prev_frame, mask = None, **feature_params)
	prev_time = pipe.getTime()

	first_vel = np.zeros(prev_points.shape)
	velocities[prev_time / 1000.0] = first_vel

	i = 0
	while ret is True:

		h = getHeight()

		xdist = (h * np.tan(x_ang / 2.0))
		ydist = (h * np.tan(y_ang / 2.0)) 
		
		pix2mx = x_pix / xdist
		pix2my = y_pix / ydist

		# get new frame
		ret, curr_frame = pipe.getFrame()
		
		# calculate optical flow between two frames; get new points
		new_points, status, error = cv2.calcOpticalFlowPyrLK(prev_frame, curr_frame, prev_points)

		good_new = new_points[status==1]
		good_old = prev_points[status==1]

		curr_time = pipe.getTime()

		# compute velocity components
		assert good_new.shape == good_old.shape



		vel = []
		for x in range(len(good_new)):
			xcomp = ((good_new[x][1] - good_old[x][1]) / x_pix) / ((curr_time - prev_time) / 1000.0) 
			ycomp = ((good_new[x][0] - good_old[x][0]) / y_pix) / ((curr_time - prev_time) / 1000.0)
			vel.append([xcomp, ycomp])

		velocities[curr_time / 1000.0] = vel
		
		# iterate next frames
		prev_frame = curr_frame
		new_points = prev_points
		prev_time = curr_time

		if i == 300:
			ret = False
		i += 1
	print velocities
	pipe.close()



def main():
	track()

	

if __name__ == '__main__':
 	main() 