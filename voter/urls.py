from django.urls import path, include
from . import views

urlpatterns = [
    # path('verify/',views.verify,name="captcha"),
    path('vote/<str:post_got>',views.vote,name="named_vote"),
    path('vote/',views.vote,name="vote"),
   
]
