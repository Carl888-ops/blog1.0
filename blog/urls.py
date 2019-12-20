from django.urls import path
from . import views

urlpatterns=[
    path(r'',views.blog_title),
    path('<int:article_id>/',views.blog_article)
]