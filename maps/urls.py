"""maps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('createreport/', views.createreport, name="createreport"),
    path('checkreport/', views.checkreport, name="checkreport"),
    path('archives/', views.archives, name="archive"),
    path('stream/', views.stream, name="stream"),
    path('route/', views.route, name="route"),
    # re_path(r'^(?P<time>[\w-]+)/$',views.reportdetail, name="detail"),
    path('postlogin/', views.postlogin, name="postlogin"),
    path('postsignup/', views.postsignup, name="postsignup"),
    # path('postcreatereport/', views.post_createreport, name="postcreatereport"),
    path('', views.homepage, name="home")
]
