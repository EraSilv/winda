from django.urls import path
from . import views

app_name = 'articleblog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('test/', views.test, name='test'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),

]
