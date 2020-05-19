# Comento - Job Camp

- 경욱님 Django 연동하였으니 웹 제작부터 시작해보세요!
- 파이썬에 이거부터 설치하고 시작하세요!
- pip install django
- pip install djangorestframework
- 웹 실행 방법
  - job_camp > backend 위치에서 vscode 터미널 창에 python manage.py runserver
- views / models / urls 등을 수정할 시
  - job_camp > backend 위치에서 python manage.py makemigrations 를 한 뒤,python manage.py migrate
- System check identified no issues (0 silenced).
  May 18, 2020 - 21:31:02
  Django version 3.0.5, using settings 'backend.settings'
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  - 터미널창에 이와 같은 결과가 나오면  http://127.0.0.1:8000/api/index << 접속
  - job_camp > backend > api > templates > frontend > index.html 
  - 이 html 페이지 꾸미기
  - 로그인 페이지부터 만들기 시작
- 로그인 페이지를 따로 두고 싶다면 urls.py 수정!
- 4주차 과제는 계속 해서 이어서 해보시면 좋을 것입니다!!