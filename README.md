# 2022 Airbnb

- python, django

- #01 Init

  - brew install pipenv (pipenv 설치)
  - pipenv --three (python3 환경을 가진 가상환경 생성)
  - pipenv shell (가상환경 안으로 진입)
  - pipenv install django (가상환경 안에서 장고 설치)

- #02 Config setting

  - django-admin startproject config (config 파일생성)
  - 이렇게 config 폴더를 생성하면 그 config 폴더안에 또다른 config 폴더가 생기는데 그 폴더와 manage.py를 root로 옮겨주고 상위 config 폴더는 지워준다.
