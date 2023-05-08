import os
import random
from moviepy.editor import *


# Load intro video and audio
intro_dir = "./intro"
intro_file = os.path.join(intro_dir, "Intro.mov")
intro = VideoFileClip(intro_file)

only_music_file = "only.mp3"
intro_music_file = os.path.join(intro_dir, only_music_file)
intro_music = AudioFileClip(intro_music_file)
intro = intro.set_audio(intro_music)


# Load outro video
outro_dir = "./outro"
outro_file = os.path.join(outro_dir, "Outro.mp4")
outro = VideoFileClip(outro_file)


# Load random video file and trim to 9 seconds
asset_dir = "./asset"
video_files = [f for f in os.listdir(asset_dir) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
random_video_file = random.choice(video_files)

video_file = os.path.join(asset_dir, random_video_file)
video = VideoFileClip(video_file)

if video.duration > 9:
    start_time = random.uniform(0, video.duration - 9)
    end_time = start_time + 9
    video = video.subclip(start_time, end_time)

# Load random image file and resize to 1280x1280
name_dir = "./"
name_image_file = "name.png"

name_file = os.path.join(name_dir, name_image_file)
image_name = ImageClip(name_file).set_pos((0, 2909))


# Load random image file and resize to 1280x1280
image_dir = "./image"
image_files = [f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
random_image_file = random.choice(image_files)

image_file = os.path.join(image_dir, random_image_file)
image = ImageClip(os.path.join(image_dir, random_image_file)).resize((1000, 1000)).set_pos((580, 302))


# Load random music file
music_dir = "./music"
music_files = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
random_music_file = random.choice(music_files)

music_file = os.path.join(music_dir, random_music_file)
music = AudioFileClip(music_file)


# Combine video, image and music
video_with_image = CompositeVideoClip([video, image.set_duration(video.duration), image_name.set_duration(video.duration)])
final_clip = concatenate_videoclips([intro, video_with_image, outro])

if music.duration < final_clip.duration:
    music = music.loop_to_duration(final_clip.duration)
else:
    music = music.subclip(0, final_clip.duration)

final_clip = final_clip.set_audio(music)


# Export final video
final_clip.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
