from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
               path('',views.index,name='index'),
               path('addnew/',views.addnew,name='addnew'),
               path('insert/',views.insert),
               path('view/',views.view,name='view'),
               path('edit/<int:id>/', views.edit, name='edit'),
               path('delete/<int:id>/', views.delete, name='delete'),
              
              
              
]