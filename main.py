import ctypes as ct
from JSL import *
import numpy as np
from matplotlib import pyplot as plt

ACCELEROMETER_DATA = []
recording = True


@ct.WINFUNCTYPE(None, ct.c_int, JOY_SHOCK_STATE, JOY_SHOCK_STATE, IMU_STATE, IMU_STATE, ct.c_float)
def CB_RecordAccelerometer(device_id, jss, prev_jss, imus, prev_imus, elapsed_time):
	global recording
	global ACCELEROMETER_DATA

	v = np.array([imus.accelX, imus.accelY, imus.accelZ])
	ACCELEROMETER_DATA.append(v)

	if (jss.buttons & JSMASK_N and not prev_jss.buttons & JSMASK_N):
		recording = False


if __name__ == "__main__":
	# initialize controller
	numDevices = JslConnectDevices()
	# handles = [None]*numDevices
	handles = ct.c_int * numDevices
	JslGetConnectedDeviceHandles(handles, numDevices)

	while True:
		# record until north button is pushed
		recording = True
		ACCELEROMETER_DATA = []
		JslSetCallback(CB_RecordAccelerometer)
		print("Now recording...")
		while recording:
			continue
		print("Finished recording. Displaying data...\n")
		JslSetCallback(None)

		# process data
		MAGNITUDES = [np.linalg.norm(i) for i in ACCELEROMETER_DATA]
		X_VALS = [i[0] for i in ACCELEROMETER_DATA]
		Y_VALS = [i[1] for i in ACCELEROMETER_DATA]
		Z_VALS = [i[2] for i in ACCELEROMETER_DATA]
		
		# plot the magnitudes of acceleration
		fig = plt.figure()
		
		ax1 = fig.add_subplot(2,2,1)
		plt.plot(MAGNITUDES)
		plt.text(0.5, 1.08, "MAGNITUDES", horizontalalignment='center', fontsize=10, transform=ax1.transAxes)
		
		ax = fig.add_subplot(2,2,2,sharex=ax1, sharey=ax1)
		plt.plot(X_VALS)
		plt.text(0.5, 1.08, "X_VALS", horizontalalignment='center', fontsize=10, transform=ax.transAxes)
		
		ax = fig.add_subplot(2,2,3,sharex=ax1, sharey=ax1)
		plt.plot(Y_VALS)
		plt.text(0.5, 1.08, "Y_VALS", horizontalalignment='center', fontsize=10, transform=ax.transAxes)
		
		ax = fig.add_subplot(2,2,4,sharex=ax1, sharey=ax1)
		plt.plot(Z_VALS)
		plt.text(0.5, 1.08, "Z_VALS", horizontalalignment='center', fontsize=10, transform=ax.transAxes)
		
		plt.tight_layout()
		plt.show()