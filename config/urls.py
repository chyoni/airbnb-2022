"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("core.urls"), namespace="core"),
    path('admin/', admin.site.urls),
]

"""
Dev 환경에서만 아래와 같은 설정을 진행할것이고,
MEDIA_URL은 settings 파일에 설정한 /media/ 가 된다. 이 말은 localhost:8080/media 를 의미하는 것
그리고 해당 URL에서 root 폴더는 MEDIA_ROOT를 보라는 의미 이게 개발환경에서 내가 업로드한 이미지를 가져오는 장고의 방식
urlpatterns는 장고가 제공하는 녀석이고 이 이름은 변경되서는 안됨 장고에게 너가 볼 url을 알려주는거라고 생각하면 된다.
"""
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
