import ctypes as ct

# load library
JSL_prefix = "D:/usr/local/packages/JSL"
jsl_lib = ct.CDLL(JSL_prefix + "/x64/JoyShockLibrary.dll")

# JSL structures - python implementations

class JOY_SHOCK_STATE(ct.Structure):
	_fields_ = [("buttons", ct.c_int),
				("lTrigger", ct.c_float),
				("rTrigger", ct.c_float),
				("stickLX", ct.c_float),
				("stickLY", ct.c_float),
				("stickRX", ct.c_float),
				("stickRY", ct.c_float)]

class IMU_STATE(ct.Structure):
	_fields_ = [("accelX", ct.c_float),
				("accelY", ct.c_float),
				("accelZ", ct.c_float),
				("gyroX", ct.c_float),
				("gyroY", ct.c_float),
				("gyroZ", ct.c_float)]

class MOTION_STATE(ct.Structure):
	_fields_ = [("quatW", ct.c_float),
				("quatX", ct.c_float),
				("quatY", ct.c_float),
				("quatZ", ct.c_float),
				("accelX", ct.c_float),
				("accelY", ct.c_float),
				("accelZ", ct.c_float),
				("gravX", ct.c_float),
				("gravY", ct.c_float),
				("gravZ", ct.c_float)]

class TOUCH_STATE(ct.Structure):
	_fields_ = [("t0Id", ct.c_int),
				("t1Id", ct.c_int),
				("t0Down", ct.c_bool),
				("t1Down", ct.c_bool),
				("t0X", ct.c_float),
				("t0Y", ct.c_float),
				("t1X", ct.c_float),
				("t1Y", ct.c_float)]

# JSL mask constants
JSOFFSET_UP = 0
JSOFFSET_DOWN = 1
JSOFFSET_LEFT = 2
JSOFFSET_RIGHT = 3
JSOFFSET_PLUS = 4
JSOFFSET_OPTIONS = 4
JSOFFSET_MINUS = 5
JSOFFSET_SHARE = 5
JSOFFSET_LCLICK = 6
JSOFFSET_RCLICK = 7
JSOFFSET_L = 8
JSOFFSET_R = 9
JSOFFSET_ZL = 10
JSOFFSET_ZR = 11
JSOFFSET_S = 12
JSOFFSET_E = 13
JSOFFSET_W = 14
JSOFFSET_N = 15
JSOFFSET_HOME = 16
JSOFFSET_PS = 16
JSOFFSET_CAPTURE = 17
JSOFFSET_TOUCHPAD_CLICK = 17
JSOFFSET_MIC = 18
JSOFFSET_SL = 18
JSOFFSET_SR = 19

DS5_PLAYER_1 = 4
DS5_PLAYER_2 = 10
DS5_PLAYER_3 = 21
DS5_PLAYER_4 = 27
DS5_PLAYER_5 = 31

JSMASK_UP = int("0x00001",16)
JSMASK_DOWN = int("0x00002",16)
JSMASK_LEFT = int("0x00004",16)
JSMASK_RIGHT = int("0x00008",16)
JSMASK_PLUS = int("0x00010",16)
JSMASK_OPTIONS = int("0x00010",16)
JSMASK_MINUS = int("0x00020",16)
JSMASK_SHARE = int("0x00020",16)
JSMASK_LCLICK = int("0x00040",16)
JSMASK_RCLICK = int("0x00080",16)
JSMASK_L = int("0x00100",16)
JSMASK_R = int("0x00200",16)
JSMASK_ZL = int("0x00400",16)
JSMASK_ZR = int("0x00800",16)
JSMASK_S = int("0x01000",16)
JSMASK_E = int("0x02000",16)
JSMASK_W = int("0x04000",16)
JSMASK_N = int("0x08000",16)
JSMASK_HOME = int("0x10000",16)
JSMASK_PS = int("0x10000",16)
JSMASK_CAPTURE = int("0x20000",16)
JSMASK_TOUCHPAD_CLICK = int("0x20000",16)
JSMASK_MIC = int("0x40000",16)
JSMASK_SL = int("0x40000",16)
JSMASK_SR = int("0x80000",16)

# JSL functions

# int JslConnectDevices();
JslConnectDevices = jsl_lib.JslConnectDevices
JslConnectDevices.argtypes = []
JslConnectDevices.restype = ct.c_int

# int JslGetConnectedDeviceHandles(int* deviceHandleArray, int size);
JslGetConnectedDeviceHandles = jsl_lib.JslGetConnectedDeviceHandles
JslGetConnectedDeviceHandles.argtypes = [ct.POINTER(ct.c_int), ct.c_int]
JslGetConnectedDeviceHandles.restype = ct.c_int

# void JslDisconnectAndDisposeAll();
JslDisconnectAndDisposeAll = jsl_lib.JslDisconnectAndDisposeAll
JslDisconnectAndDisposeAll.argtypes = []
JslDisconnectAndDisposeAll.restype = None

# JOY_SHOCK_STATE JslGetSimpleState(int deviceId);
JslGetSimpleState = jsl_lib.JslGetSimpleState
JslGetSimpleState.argtypes = [ct.c_int]
JslGetSimpleState.restype = JOY_SHOCK_STATE

# IMU_STATE JslGetIMUState(int deviceId);
JslGetIMUState = jsl_lib.JslGetIMUState
JslGetIMUState.argtypes = [ct.c_int]
JslGetIMUState.restype = IMU_STATE

# MOTION_STATE JslGetMotionState(int deviceId);
JslGetMotionState = jsl_lib.JslGetMotionState
JslGetMotionState.argtypes = [ct.c_int]
JslGetMotionState.restype = MOTION_STATE

# TOUCH_STATE JslGetTouchState(int deviceId);
JslGetTouchState = jsl_lib.JslGetTouchState
JslGetTouchState.argtypes = [ct.c_int]
JslGetTouchState.restype = TOUCH_STATE

# int JslGetButtons(int deviceId);
JslGetButtons = jsl_lib.JslGetButtons
JslGetButtons.argtypes = [ct.c_int]
JslGetButtons.restype = ct.c_int

# float JslGetLeftX(int deviceId);
JslGetLeftX = jsl_lib.JslGetLeftX
JslGetLeftX.argtypes = [ct.c_int]
JslGetLeftX.restype = ct.c_float

# float JslGetLeftY(int deviceId);
JslGetLeftY = jsl_lib.JslGetLeftY
JslGetLeftY.argtypes = [ct.c_int]
JslGetLeftY.restype = ct.c_float

# float JslGetRightX(int deviceId);
JslGetRightX = jsl_lib.JslGetRightX
JslGetRightX.argtypes = [ct.c_int]
JslGetRightX.restype = ct.c_float

# float JslGetRightY(int deviceId);
JslGetRightY = jsl_lib.JslGetRightY
JslGetRightY.argtypes = [ct.c_int]
JslGetRightY.restype = ct.c_float

# float JslGetLeftTrigger(int deviceId);
JslGetLeftTrigger = jsl_lib.JslGetLeftTrigger
JslGetLeftTrigger.argtypes = [ct.c_int]
JslGetLeftTrigger.restype = ct.c_float

# float JslGetRightTrigger(int deviceId);
JslGetRightTrigger = jsl_lib.JslGetRightTrigger
JslGetRightTrigger.argtypes = [ct.c_int]
JslGetRightTrigger.restype = ct.c_float

# float JslGetGyroX(int deviceId);
JslGetGyroX = jsl_lib.JslGetGyroX
JslGetGyroX.argtypes = [ct.c_int]
JslGetGyroX.restype = ct.c_float

# float JslGetGyroY(int deviceId);
JslGetGyroY = jsl_lib.JslGetGyroY
JslGetGyroY.argtypes = [ct.c_int]
JslGetGyroY.restype = ct.c_float

# float JslGetGyroZ(int deviceId);
JslGetGyroZ = jsl_lib.JslGetGyroZ
JslGetGyroZ.argtypes = [ct.c_int]
JslGetGyroZ.restype = ct.c_float

# float JslGetAccelX(int deviceId);
JslGetAccelX = jsl_lib.JslGetAccelX
JslGetAccelX.argtypes = [ct.c_int]
JslGetAccelX.restype = ct.c_float

# float JslGetAccelY(int deviceId);
JslGetAccelY = jsl_lib.JslGetAccelY
JslGetAccelY.argtypes = [ct.c_int]
JslGetAccelY.restype = ct.c_float

# float JslGetAccelZ(int deviceId);
JslGetAccelZ = jsl_lib.JslGetAccelZ
JslGetAccelZ.argtypes = [ct.c_int]
JslGetAccelZ.restype = ct.c_float

# int JslGetTouchId(int deviceId, bool secondTouch = false);
JslGetTouchId = jsl_lib.JslGetTouchId
JslGetTouchId.argtypes = [ct.c_int, ct.c_bool]
JslGetTouchId.restype = ct.c_int

# bool JslGetTouchDown(int deviceId, bool secondTouch = false);
JslGetTouchDown = jsl_lib.JslGetTouchDown
JslGetTouchDown.argtypes = [ct.c_int, ct.c_bool]
JslGetTouchDown.restype = ct.c_bool

# float JslGetTouchX(int deviceId, bool secondTouch = false);
JslGetTouchX = jsl_lib.JslGetTouchX
JslGetTouchX.argtypes = [ct.c_int, ct.c_bool]
JslGetTouchX.restype = ct.c_float

# float JslGetTouchY(int deviceId, bool secondTouch = false);
JslGetTouchY = jsl_lib.JslGetTouchY
JslGetTouchY.argtypes = [ct.c_int, ct.c_bool]
JslGetTouchY.restype = ct.c_float

# float JslGetStickStep(int deviceId);
JslGetStickStep = jsl_lib.JslGetStickStep
JslGetStickStep.argtypes = [ct.c_int]
JslGetStickStep.restype = ct.c_float

# float JslGetTriggerStep(int deviceId);
JslGetTriggerStep = jsl_lib.JslGetTriggerStep
JslGetTriggerStep.argtypes = [ct.c_int]
JslGetTriggerStep.restype = ct.c_float

# float JslGetPollRate(int deviceId);
JslGetPollRate = jsl_lib.JslGetPollRate
JslGetPollRate.argtypes = [ct.c_int]
JslGetPollRate.restype = ct.c_float

# void JslResetContinuousCalibration(int deviceId);
JslResetContinuousCalibration = jsl_lib.JslResetContinuousCalibration
JslResetContinuousCalibration.argtypes = [ct.c_int]
JslResetContinuousCalibration.restype = None

# void JslStartContinuousCalibration(int deviceId);
JslStartContinuousCalibration = jsl_lib.JslStartContinuousCalibration
JslStartContinuousCalibration.argtypes = [ct.c_int]
JslStartContinuousCalibration.restype = None

# void JslPauseContinuousCalibration(int deviceId);
JslPauseContinuousCalibration = jsl_lib.JslPauseContinuousCalibration
JslPauseContinuousCalibration.argtypes = [ct.c_int]
JslPauseContinuousCalibration.restype = None

# void JslGetCalibrationOffset(int deviceId, float& xOffset, float& yOffset, float& zOffset);
JslGetCalibrationOffset = jsl_lib.JslGetCalibrationOffset
# JslGetCalibrationOffset.argtypes = [ct.c_int, ct.byref(ct.c_float), ct.byref(ct.c_float), ct.byref(ct.c_float)]
JslGetCalibrationOffset.restype = None

# void JslSetCalibrationOffset(int deviceId, float xOffset, float yOffset, float zOffset);
JslSetCalibrationOffset = jsl_lib.JslSetCalibrationOffset
JslSetCalibrationOffset.argtypes = [ct.c_int, ct.c_float, ct.c_float, ct.c_float]
JslSetCalibrationOffset.restype = None

# void JslSetCallback(void(*callback)(int, JOY_SHOCK_STATE, JOY_SHOCK_STATE, IMU_STATE, IMU_STATE, float));
JslSetCallback = jsl_lib.JslSetCallback
# JslSetCallback.argtypes = []
JslSetCallback.restype = None

# void JslSetTouchCallback(void(*callback)(int, TOUCH_STATE, TOUCH_STATE, float));
JslSetTouchCallback = jsl_lib.JslSetTouchCallback
# JslSetTouchCallback.argtypes = []
JslSetTouchCallback.restype = None

# int JslGetControllerType(int deviceId);
JslGetControllerType = jsl_lib.JslGetControllerType
JslGetControllerType.argtypes = [ct.c_int]
JslGetControllerType.restype = ct.c_int

# int JslGetControllerSplitType(int deviceId);
JslGetControllerSplitType = jsl_lib.JslGetControllerSplitType
JslGetControllerSplitType.argtypes = [ct.c_int]
JslGetControllerSplitType.restype = ct.c_int

# int JslGetControllerColour(int deviceId);
JslGetControllerColour = jsl_lib.JslGetControllerColour
JslGetControllerColour.argtypes = [ct.c_int]
JslGetControllerColour.restype = ct.c_int

# void JslSetLightColour(int deviceId, int colour);
JslSetLightColour = jsl_lib.JslSetLightColour
JslSetLightColour.argtypes = [ct.c_int, ct.c_int]
JslSetLightColour.restype = None

# void JslSetRumble(int deviceId, int smallRumble, int bigRumble);
JslSetRumble = jsl_lib.JslSetRumble
JslSetRumble.argtypes = [ct.c_int, ct.c_int, ct.c_int]
JslSetRumble.restype = None

# void JslSetPlayerNumber(int deviceId, int number);
JslSetPlayerNumber = jsl_lib.JslSetPlayerNumber
JslSetPlayerNumber.argtypes = [ct.c_int, ct.c_int]
JslSetPlayerNumber.restype = None
