from django.urls import path
from . import views

urlpatterns = [
    path('',views.create_class.as_view()),
    path('<int:pk>/',views.classinfo.as_view()),
    path('<int:pk>/content/',views.class_content.as_view()),
    # path('<int:pk>/member/',views.class_members.as_view()),
    path('join/',views.join_class.as_view()),
    path('<int:pk>/content/<int:pkc>/',views.content_ud.as_view()),
]
