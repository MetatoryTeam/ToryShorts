import os
import shutil
import datetime
import pytz

# 복사할 파일 경로와 이름
src_file = "./output_video.mp4"
try:
    # 서울 시간으로 현재 날짜 계산
    seoul = pytz.timezone('Asia/Seoul')
    now = datetime.datetime.now(seoul)

    # 저장할 디렉토리 경로 생성
    dir_path = os.path.join("./archive", now.strftime("%Y-%m-%d"))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # 디렉토리 안의 파일 개수 확인
    file_count = len(os.listdir(dir_path))

    # 파일 이름 생성
    file_name = f"{file_count+1}.mp4"
    dst_file = os.path.join(dir_path, file_name)

    # 파일 복사
    shutil.copy(src_file, dst_file)
    print("동영상 파일 복사 완료!")
except:
    print("동영상 파일 복사 실패!")

#퀴즈 이미지 아카이브
quiz_src_file = "./quiz.png"
try:
    # 서울 시간으로 현재 날짜 계산
    seoul = pytz.timezone('Asia/Seoul')
    now = datetime.datetime.now(seoul)

    # 저장할 디렉토리 경로 생성
    quiz_dir_path = os.path.join("./quiz", now.strftime("%Y-%m-%d"))
    if not os.path.exists(quiz_dir_path):
        os.makedirs(quiz_dir_path)

    # 디렉토리 안의 파일 개수 확인
    quiz_file_count = len(os.listdir(quiz_dir_path))

    # 파일 이름 생성
    quiz_file_name = f"{quiz_file_count+1}.png"
    quiz_dst_file = os.path.join(quiz_dir_path, quiz_file_name)

    # 파일 복사
    shutil.copy(quiz_src_file, quiz_dst_file)
    print("퀴즈 이미지 파일 복사 완료!")

except:
    print("퀴즈 이미지 파일 복사 실패!")


################################생성 AI 잠정 보류 ##############################
# #생성AI로 생성한 이미지 아카이브
# quiz_src_file = "./generate/quiz.png"
# try:
#     # 서울 시간으로 현재 날짜 계산
#     seoul = pytz.timezone('Asia/Seoul')
#     now = datetime.datetime.now(seoul)

#     # 저장할 디렉토리 경로 생성
#     quiz_dir_path = os.path.join("./quiz", now.strftime("%Y-%m-%d"))
#     if not os.path.exists(quiz_dir_path):
#         os.makedirs(quiz_dir_path)

#     # 디렉토리 안의 파일 개수 확인
#     quiz_file_count = len(os.listdir(quiz_dir_path))

#     # 파일 이름 생성
#     quiz_file_name = f"{quiz_file_count+1}.png"
#     quiz_dst_file = os.path.join(quiz_dir_path, quiz_file_name)

#     # 파일 복사
#     shutil.copy(quiz_src_file, quiz_dst_file)
#     print("생성AI 이미지 파일 복사 완료!")

# except:
#     print("생성AI 이미지 파일 복사 실패!")