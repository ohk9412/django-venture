from django.urls import path
from mysite import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("post/", views.post, name="post"),
    path("contact/", views.contact, name="contact"),
    path("db/", views.database, name="db"),  # 데이터베이스 삽입을 위한 url(1회용)

]
