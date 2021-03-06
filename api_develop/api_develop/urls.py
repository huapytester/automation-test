"""api_develop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from guest import views
from django.views import generic

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/', views.welcome_page, name='hello'),
    url(r'^user_action/', views.user_action, name='user_action'),
    url(r'^login/', views.LoginView.as_view(), name='login'),
    url(r'^$', generic.TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^event_manage/', views.event_manage, name='event_manage'),
    url(r'^search_name/', views.search_name, name='search_name'),

]
