import ctypes as ct
from JSL import *
import numpy as np
from matplotlib import pyplot as plt
import bpy
import time


if __name__ == "__main__":
	numDevices = JslConnectDevices()
	handle = ct.c_int()
	JslGetConnectedDeviceHandles(ct.byref(handle), numDevices)

	while True:
		bpy.data.objects["Empty"].location.x = JslGetAccelX(handle)
		bpy.data.objects["Empty"].location.y = JslGetAccelY(handle)
		bpy.data.objects["Empty"].location.z = JslGetAccelZ(handle)
		
		time.sleep(0.125)
		