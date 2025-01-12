from datetime import datetime

# 현재 시각을 'YYYY-MM-DD HH:MM:SS' 형식으로 가져오기
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 추가할 내용 생성
log_entry = f'실행 시각: {current_time}\n\n'

# README.md 파일에 실행 시각 추가
with open('README.md', 'a', encoding='utf-8') as file:
  file.write(log_entry)