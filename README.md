# 엄마와 함께 AI 동굴 탐사

엄마와 아이가 함께 동굴을 탐사하며 Python,코딩,AI를 직접 경험해보는 프로젝트입니다.

## 준비물
-Windows 컴퓨터
-Python
-VS Code

## 프로젝트 받기
GitHub에서 프로젝트 페이지에서 Code 버튼을 누릅니다.
Download ZIP을 선택해 파일을 내려 받습니다.
다운로드한 ZIP 파일 압축을 풀고 mom-ai-agent 폴더를 엽니다.

## 실행 순서
1. cave.py
2. cave_two_paths.py
3. cave_water_path.py
4. app.py

## 실행 방법
VS Code에서 Terminal을 열고 아래 명령어를 순서대로 실행합니다.
python cave.py
python cave_two_paths.py
python cave_water_path.py

## AI 연결 준비
app.py를 실행하려면 OpenAI API 연결이 필요합니다.
### 필요한 패키지 설치 
Terminal에서 아래 명령어를 실행합니다.
pip install pillow openai Python-dotenv

### API 키 설정
프로젝트 폴더에 .env 파일을 만들고 아래 형식으로 입력합니다.
OPENAI_API_KEY=자신의_API_키

※ 실제 API 키는 다른 사람에게 보여주거나 GitHib에 올리지 마세요.

### API 요금 주의
OpenAI API 사용에는 별도의 요금이 발생할 수 있습니다.
결제 설정 시 자동 충전(Auto-reload)이 켜져있으면 반드시 확인하세요.
계속 자동 결제되는 것을 원하지 않으면 Auto-reload를 꺼주세요.

### AI 실행
API 키 설정이 끝나면 Terminal에서 아래 명령어를 실행합니다.
python app.py






