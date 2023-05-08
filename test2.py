from moviepy.editor import *

# 음악 파일 불러오기
audio1 = AudioFileClip("audio1.mp3")
audio2 = AudioFileClip("audio1.mp3")

# 음악을 합치고 중복 재생하기
audio_mix = CompositeAudioClip([audio1, audio2])
audio_mix = audio_mix.volumex(2.0) # 볼륨 두 배로 증폭

# 합쳐진 음악 파일 내보내기
audio_mix.write_audiofile("output.mp3")