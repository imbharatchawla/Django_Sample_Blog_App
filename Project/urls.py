"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
    path('admin/', admin.site.urls),
    # if kept blank in '', it will look for '' in blog urls and redirect
    # if written 'blog/', it will look for anything after / in blog in urls and load the match view
    # for exmaple if localhost:8000/blog/ is hit, path('blog/', include(blogapp.urls')) will load '' since there is nothing after blog and will load '' from blog.views
    # and if localhost:8000/about is hit, path('blog/', include(blogapp.urls')) will load 'about/' from blog.views

    path('', include('blogapp.urls')),

]
