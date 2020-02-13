from django.urls import path
from . import views

app_name= 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>',views.detail,name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
    path('about/',views.about,name = 'about'),
    path('contact/',views.contact,name = 'contact'),
    path('idea/',views.idea,name = 'idea'),
    path('search/',views.search,name = 'search'),
]