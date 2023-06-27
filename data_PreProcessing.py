############배경 동영상에 대해서 Resize 후 Crop하는 코드
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.fx.all import resize, crop
import os

# 저장할 디렉토리를 지정합니다.
output_directory = './crop/'

# '/crop' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# '/asset' 디렉토리에 있는 모든 파일을 순회합니다.
for filename in os.listdir('./asset'):
    if filename.endswith(".mov"):
        # 동영상 파일을 로드합니다.
        clip = VideoFileClip(os.path.join('./asset', filename))

        # 동영상을 7865x3840 크기로 변경합니다.
        resized_clip = resize(clip, newsize=(7865, 3840))

        # 정중앙 기준으로 좌우로 1080을 잘라내서 2160x3840 크기로 만듭니다.
        cropped_clip = crop(resized_clip, width=2160, height=3840, x_center=resized_clip.w/2, y_center=resized_clip.h/2)

        # 새로운 크기로 변경된 동영상을 '/crop' 디렉토리에 저장합니다.
        cropped_clip.write_videofile(os.path.join(output_directory, f'resized_{filename}'), codec='libx264')
