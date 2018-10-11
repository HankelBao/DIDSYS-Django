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
    url(r'^scoreboard/get_by_date$', views.scoreboard_get_by_date),
    url(r'^scorerank/get_by_type$', views.scorerank_get_by_type),
    url(r'^scoremoments/query$', views.scoremoments_query),
    url(r'^scorer/signin$', views.scorer_login),
    url(r'^scorer/signout$', views.scorer_session_del),
    url(r'^scorer/get_session$', views.scorer_get_session),
    url(r'^scorer/get_scores$', views.scorer_get_scores),
    url(r'^scorer/submit_score$', views.scorer_submit_score),
    url(r'^scorer/update_totals$', views.scorer_update_totals),

    url(r'^scorers/get_names$', views.scorers_get_names),
    url(r'^classes/get_names$', views.classes_get_names),
    url(r'^subjects/get_names$', views.subjects_get_names),

    url(r'^admin/', admin.site.urls),
]
