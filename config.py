import datetime

# Video Path
VIDEO_CONFIG = {
	"VIDEO_CAP" : "video/test.mp4",
	"IS_CAM" : False,
	"CAM_APPROX_FPS": 30,
	"HIGH_CAM": False,
	"START_TIME": datetime.datetime(2024, 8, 8, 0, 0, 0, 0)
}

# Load YOLOv3-tiny weights and config
YOLO_CONFIG = {
	"WEIGHTS_PATH" : "YOLOv4-tiny/yolov4-tiny.weights",
	"CONFIG_PATH" : "YOLOv4-tiny/yolov4-tiny.cfg"
}
# Show individuals detected
SHOW_PROCESSING_OUTPUT = True
# Show individuals detected
SHOW_DETECT = True
# Data record
DATA_RECORD = True
# Data record rate (data record per frame)
DATA_RECORD_RATE = 24
# Check for restricted entry
RE_CHECK = False
# Restricted entry time (H:M:S)
RE_START_TIME = datetime.time(0,0,0) 
RE_END_TIME = datetime.time(23,0,0)
# Check for social distance violation
SD_CHECK = False
# Show violation count
SHOW_VIOLATION_COUNT = False
# Show tracking id
SHOW_TRACKING_ID = True
# Threshold for distance violation
SOCIAL_DISTANCE = 15
# Check for abnormal crowd activity
ABNORMAL_CHECK = True
# Min number of people to check for abnormal
ABNORMAL_MIN_PEOPLE = 5
# Abnormal energy level threshold
ABNORMAL_ENERGY = 1866
# Abnormal activity ratio threhold
ABNORMAL_THRESH = 0.66
# Threshold for human detection minumun confindence
MIN_CONF = 0.1
# Threshold for Non-maxima surpression
NMS_THRESH = 0.4
# Resize frame for processing
FRAME_SIZE = 512
# Tracker max missing age before removing (seconds)
TRACK_MAX_AGE = 3