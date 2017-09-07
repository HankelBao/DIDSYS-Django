"""SFLSDID URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from DID import views as views

urlpatterns = [
    # Index
    url(r'^$', views.index),

    # Ajax
    url(r'^ajax/get-index', views.get_index),
    url(r'^ajax/get-scoreboard', views.get_scoreboard),
    url(r'^ajax/get-scoreranking', views.get_scoreranking),
    url(r'^ajax/get-scoremoments', views.get_scoremoments),

    # Ajax View
    url(r'^ajax/get-scorerboard', views.scorerboard),
    url(r'^ajax/score-submit', views.scorerboard_submit),
    url(r'^ajax/more-on-scoreboard', views.more_on_scoreboard),
    url(r'^ajax/more-on-scoreranking', views.more_on_scoreranking),

    # Admin
    url(r'^admin/', admin.site.urls),
]
