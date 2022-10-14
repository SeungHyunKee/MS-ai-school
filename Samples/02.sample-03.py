from gtts import gTTS                   # gTTS 전부말고, gtts부분만 가져온다는 뜻
from playsound import playsound         # mp3를 재생할때 사용하는 패키지
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))  # 
text = "안녕하세요 마이크로스프트 에이아이 스쿨에 오신것을 환영합니다."
tts = gTTS(text= text, lang ='ko')      # gtts패키지 설치하는방법 : 터미널에 pip install gtts 입력해서 설치

current_file_path = os.getcwd() + "./hi.mp3"
tts.save(current_file_path)

playsound(current_file_path)            # playsound패키지 설치하는방법 : 터미널에 pip install playsound 입력해서 설치




# 처음 만들었던 코드(위에는 에러발생해서 변경한 코드)
# from gtts import gTTS                   # gTTS 전부말고, gtts부분만 가져온다는 뜻
# from playsound import playsound         # mp3를 재생할때 사용하는 패키지

# text = "안녕하세요 마이크로스프트 에이아이 스쿨에 오신것을 환영합니다."

# tts = gTTS(text= text, lang ='ko')      # gtts패키지 설치하는방법 : 터미널에 pip install gtts 입력해서 설치
# tts.save('hi.mp3')

# playsound('hi.mp3')                     # playsound패키지 설치하는방법 : 터미널에 pip install playsound 입력해서 설치