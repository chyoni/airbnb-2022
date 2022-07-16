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

- #53 get_absolute_url() method for admin panel to viewsite

- #54 Room Detail Page

- #55 Search views 1

- #56 Search views 2

- #57 Search views 3

- #58 Search filtering

- #59 Search filtering 2

- #60 Search views done

- #61 Login views 1

- #62 Login views 2

  - clean method

- #63 Login views 3

  - clean method implements

- #64 Login, Logout views 4

- #65 Signup views 1

- #66 Signup views 2

- #67 django-dotenv, Send email for verification 1

  ```bash
  pipenv install django-dotenv
  ```

- #68 Send email for verification 1

- #69 Send email for verification 2

- #70 Send email for verification DONE

- #71 Github login 1

  - https://docs.github.com/en/developers/apps/building-oauth-apps

- #72 Github login 2

  - requests라는 라이브러리는 axios같은 rest api를 때릴 수 있는 라이브러리

  ```bash
  pipenv install requests
  ```

- #73 Github login 3

- #74 Github login DONE

- #75 Kakao login 1

  - https://developers.kakao.com

- #76 Kakao login 2

- #77 Kakao login DONE

- #78 Kakao login really DONE

- #79 TailwindCSS Setup

  - ##1

  ```bash
  npm init
  npm install gulp gulp-postcss gulp-sass gulp-csso node-sass sass
  npm install tailwindcss -D
  npm install autoprefixer -D
  npx tailwind init
  ```

  - ##2
  - create gulpfile.js
  - gulpfile.js setup
  - create assets folder > scss folder > styles.scss

- #80 TailwindCSS Setup 2

  - set static folder path on settings.py
  - use static/css/styles.css for html file

- #81 Design 1

  - ### tailwindCSS가 3.0 이상 버전으로 올라오면서 tailwind.config.js 파일에 content에 어떤 파일이 tailwind css를 사용할것이냐를 지정해줘야 한다.
  - ### tailwind css 이거를 지금 gulp로 가져왔는데 postcss 방식으로 가져와보자. 현재는 지금 새로운 properties 추가될때마다 "gulp" script를 실행해야해서 너무 귀찮다.
  - em = 가장 가까운 요소의 font-size
  - rem = root의 font-size

- #82 Design 2

- #83 Design 3

  - pass variable template to template

- #84 Design 4

- #85 Design 5

  - room card done

- #86 Design 6

  - search icon absolute position

- #87 Design 7

  - font family

- #88 Design 8

  - login, signup screen

- #89 Design 9

  - login screen error message

- #90 Design 10

  - signup screen error message

- #91 Design 11

  - message pop (https://docs.djangoproject.com/en/4.0/ref/contrib/messages/#message-tags)

- #92 Design 12

  - message fade in out

- #93 UserProfileView

  - Class based view
  - function based로 하려니, 2개를 만들어야함 왜냐하면 내 프로필을 선택하는거랑 특정 유저를 클릭했을 때 그 유저를 가져오는 부분에서
    장고가 기존에 context에 담은 유저를 가져와서 문제가 있음

- #94 Design 13

  - User profile position

- #95 Design 14

  - User profile 2

- #96 Design 15

  - User profile 3

- #97 Design 16

  - Edit screen

- #98 Design 17

  - Edit screen

- #99 Design 18

  - Edit screen

- #100 Design 19

- #101 User update views

- #102 Design 20

  - User avatar input

- #103 User avatar update done

- #104 Password change done

- #105 Set permission to each screen

- #106 Login required decorator

- #107 Room detail 1

- #108 Room detail 2

- #109 Room detail 3

- #110 Room detail 4

- #111 Room detail 5
