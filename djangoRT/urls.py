"""djangoRT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from firstPage import views

# urlpatterns = [
#     path('', views.index, name = 'Home'),
#     path('notify/', views.notify, name = 'Notify'),
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path


from firstPage.views import home  # Importing basic home view
# Importing Notifications View
from firstPage.views import notification_test_page
from firstPage.views import add_person  # Importing person API

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("notifications-test/", notification_test_page, name="notifications-test"),
    path("add_person_notify/", add_person, name="add_person")
]
