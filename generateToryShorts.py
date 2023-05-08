import os
import random
from moviepy.editor import *



# /intro 디렉토리에서 intro.mov 선택
intro_file = "./intro/Intro.mov"
intro = VideoFileClip(intro_file)

intro_dir = "./intro"
only_music_file = "only.mp3"
intro_music = AudioFileClip(os.path.join(intro_dir, only_music_file))
intro.set_audio(intro_music)

# /outro 디렉토리에서 outro.mov 선택
outro_file = "./outro/Outro.mp4"
outro = VideoFileClip(outro_file)


# /music 디렉토리에서 무작위로 음악 파일 선택
music_dir = "./music"
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
random_music_file = random.choice(music_files)

# /asset 디렉토리에서 무작위로 영상 파일 선택
asset_dir = "./asset"
video_files = [f for f in os.listdir(asset_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
random_video_file = random.choice(video_files)

# 선택한 영상 파일을 읽고,9초로 자르기
video = VideoFileClip(os.path.join(asset_dir, random_video_file))
video_duration = video.duration

if video_duration > 9:
    start_time = random.uniform(0, video_duration - 9)
    end_time = start_time + 9
    video = video.subclip(start_time, end_time)

# /image 디렉토리에서 무작위로 이미지 파일 선택
image_dir = "./image"
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random_image_file = random.choice(image_files)

#선택한 이미지 파일을 읽고, 1280*1280 정사각형으로 resize 하고, 영상 중앙에 위치하도록 조정
image = ImageClip(os.path.join(image_dir, random_image_file)).resize((1280, 1280)).set_pos((440, 401))

# 선택한 음악 파일을 읽기
music = AudioFileClip(os.path.join(music_dir, random_music_file))

# 음악과 영상, 이미지를 합치기
video_with_music_and_image = CompositeVideoClip([video, image.set_duration(video_duration)])
final_clip = concatenate_videoclips([intro, video_with_music_and_image, outro])

# 음악의 길이를 영상의 길이에 맞게 자르거나 반복
if music.duration < final_clip.duration:
    music = music.loop_to(final_clip.duration)
else:
    music = music.subclip(0, final_clip.duration)
    
final_clip = final_clip.set_audio(music)

# 합쳐진 동영상 파일을 내보내기
final_clip.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
