"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    # includeは、そのポイントまでに一致した URL の部分を切り落とし、次の処理のために残りの文字列をインクルードされた URLconf へ渡す。
    # つまり、ここでドメイン以下のページURLを設定でき、各ディレクトリで管理できる。http://localhost:8000/polls/ みたいにアクセスできる。
    # Django アプリケーションは「プラガブル (pluggable)」。アプリケーションは特定の Django インストールに結び付いていないので、アプリケーションを複数のプロジェクトで使ったり、単体で配布したりできる。
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
