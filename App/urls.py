
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('createprofile/',views.create_profile,name="signup"),
    path('login/',views.Login,name="Login"),
    path('logout/',views.Logout,name="logout"),
    path('profile/',views.profile,name="profile"),
    path('profile/<int:id>/',views.profile,name="profile"),
    path('search/',views.search,name="search"),
    path('follow/<int:id>/<str:username>/',views.follow,name="follow"),
    path('uploadpost/',views.upload_post,name="upload_post"),
    path("like/<int:id>/",views.like_post,name="like"),
    path("upload_reel",views.upload_reel,name="upload_reel"),
    path('reels/',views.reels,name="reels"),
    path("likereel/<int:id>/",views.like_reel,name="likereel"),
    path("uploadstory/",views.upload_story,name="upload_story"),
    
]
