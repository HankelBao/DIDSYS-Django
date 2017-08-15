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
    url(r'^one', views.one),

    # Ajax
    url(r'^ajax/get-scorerboard', views.scorerboard),
    url(r'^ajax/score-submit', views.scorerboard_submit),
    url(r'^ajax/more_on_scoreboard', views.more_on_scoreboard),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Angular Test
    url(r'^angular', views.angular)
]
