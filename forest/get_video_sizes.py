import os
import glob
from tqdm import tqdm 

TOTAL_VIDEO_CHUNCK = 454
# BITRATE_LEVELS = [1,2,3,4,5,6]
BITRATE_LEVELS = [279652, 836887, 1282108, 1779588, 2568145, 3894863]
VIDEO_PATH = 'forest_'
# VIDEO_FOLDER = 'video'

# assume videos are in ../video_servers/video[1, 2, 3, 4, 5]
# the quality at video5 is the lowest and video1 is the highest


for bitrate,folder in enumerate(BITRATE_LEVELS):
	print('bitrate:',bitrate,'folder:',folder)
	print('filename:','video_size_' + str(bitrate))
	with open('video_size_' + str(bitrate), 'w') as f:
		for chunk_num in tqdm(range(1, TOTAL_VIDEO_CHUNCK+1)):
			# video_chunk_path = VIDEO_PATH + \
			# 				   VIDEO_FOLDER + \
			# 				   str(BITRATE_LEVELS - bitrate) + \
			# 				   '/' + \
			# 				   str(chunk_num) + \
			# 				   '.m4s'
			video_chunk_path = glob.glob(
				VIDEO_PATH + str(folder) + 'bps/*1s'+str(chunk_num)+'.m4s'
				)[0]
			chunk_size = os.path.getsize(video_chunk_path)
			f.write(str(chunk_size) + '\n')
