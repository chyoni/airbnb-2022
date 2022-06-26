# 2022 Airbnb

- python, django

- #01 Init

  - brew install pipenv (pipenv 설치)
  - pipenv --three (python3 환경을 가진 가상환경 생성)
  - pipenv shell (가상환경 안으로 진입)
  - pipenv install django (가상환경 안에서 장고 설치)

  - pipenv install requests (이게 이제 pipfile에서 설치된 패키지들의 리스트를 보고 다른PC에서 필요한 패키지들을 내려받는 명령어)

- #02 Config setting

  - django-admin startproject config (config 파일생성)
  - 이렇게 config 폴더를 생성하면 그 config 폴더안에 또다른 config 폴더가 생기는데 그 폴더와 manage.py를 root로 옮겨주고 상위 config 폴더는 지워준다.

- #03 Linter (flake8)

  - pipenv install flake8 --dev (가상환경 내 dev 환경에서 flake8을 install)
  - pipenv install black --dev --pre (formatter)
  - 그리고 이거는 python 규칙같은건데 모든 py로 끝나는 파일을 특정 폴더에 집어넣고 그 파일을 사용하려면 \_\_init\_\_.py 파일이 그 폴더에 들어있어야 한다. 이게 이 폴더의 py 파일을 다른데서도 사용하겠다는 일종의 규칙이다.

- #04 Run server

  - python manage.py runserver (server를 실행)
  - python manage.py makemigrations (프로젝트 내 models 확인하고 변경사항을 migration 파일로 생성)
  - python manage.py migrate (장고와 database(db.sqlite3)를 migrate)
  - python manage.py createsuperuser (admin 계정 생성 (localhost:8080/admin 에서 사용하는 계정))

- #05 Create application

  - django-admin startapp "Application name" (model을 만든다고 생각하면 되는데 그 모델안에 api, url 등등이 다 들어있어서 그걸 application이라고 명함, 그리고 이 application name은 복수형이어야 함)

- #06 User Model

- #07 User Model 2

- #08 Admin Panel

- #09 Abstract Model and Core Model

- #10 Django country list

  - pipenv install django-countries

- #11 Room Model and ForeignKey()

- #12 Room Items

- #13 Verbose Set Photo Model

- #14 Reviews Model

- #15 Reservation Model

- #16 List Model

- #17 Conversation and Message Model

- #18 Admin site

  - https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.ModelAdmin.search_fields

- #19 Admin site 2

- #20 Admin site 3 (count object's specific attributes)

- #21 QuerySet, vars, dir, set, objects

  - QuerySet은 list를 나타내고 장고에서 어떤 리스트들을 반환할 때 사용된다.
  - dir()는 어떤 객체의 가지고 있는 변수와 메소드를 보여준다.
  - vars()는 어떤 객체의 attributes를 dictionary 형태로 보여준다.
  - set은 foreign key에 대한 데이터를 보여준다 (장고에서 만들어주는 기능)
  - objects 는 클래스의 object (객체)를 전부 가져와서 원하는걸 찾을 수 있다. (ex: User.objects.all())

- #22 Related name for set

  - set으로 foreign key를 가져오는데 그 set의 이름을 바꿔주는 게 related_name이다.

- #23 Admin site and photo counts func

- #24 Average Function

- #25 Reservation status by check InOut

- #26 Conversation, List Admin and Model

- #27 MEDIA_ROOT on Django

  - https://docs.djangoproject.com/en/4.0/ref/settings/#media-root

- #28 MEDIA_URL and urlpatterns

- #29 Photo Admin

- #30 Inline Admin

- #31 Save method Override

  - https://docs.djangoproject.com/en/4.0/topics/db/models/#overriding-model-methods

- #32 Django-seeds and custom commands

  - Create my custom commands practice

- #33 Amenities created for command

- #34 Using django_seed for fake user create

  - pipenv install django_seed
  - https://github.com/Brobin/django-seed

- #35 Using django_seed and faker for fake room create

- #36 Photo seed

- #37 Amenity, Facility, HouseRule seed

- #38 Review seed

- #39 Lists seed

- #40 Reservations seed

- #41 Views, Urls interaction

- #42 urls patterns fix

- #43 Django templates settings

- #44 Base HTML

- #45 Templates syntex (Divide and Conquer)

- #46 Handle URL QueryString

- #47 Django Templates filter

  - https://docs.djangoproject.com/en/4.0/ref/templates/language/#filters

- #48 Vanilla Pagination with python

- #49 Django Paginator

  - https://docs.djangoproject.com/en/4.0/ref/paginator/#paginator

- #50 Handle Exception for Paginator.page()

- #51 Classed Base View

  - https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-display/#listview
  - https://ccbv.co.uk/

- #52 Django URLs arguments
