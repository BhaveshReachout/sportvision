from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/', views.home, name='index'),
    path('', RedirectView.as_view(url='index')),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup_view, name='register'),
    path('profile/', views.profile_final_view, name='profile_final'),
    path('profile/edit/', views.profile_final_edit_view, name='profile_edit_final'),
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about_view, name='about'),

    path('post/create/', views.PostCreateView.as_view(success_url='/community/post')),
    path('post/delete/<int:pk>',
         views.PostDeleteView.as_view(success_url='/community/post')),
    path('post/', views.PostListView.as_view()),
    path('activity/', views.AllPostListView.as_view()),

    path('group/', views.group_view, name='group'),
    path('group/details/', views.groupdetails_view, name='group_details'),
    path('group/create/', views.GroupCreateView.as_view(success_url='/community/group')),

    path('member/', views.ProfileListView.as_view()),
    path('member/<int:pk>', views.ProfileDetailView.as_view()),

    path('profile/follow/<int:pk>', views.follow_view, name="follow_view"),
    path('profile/unfollow/<int:pk>', views.unfollow_view, name="unfollow_view"),

    path('profile/like/<int:pk>', views.like_view, name="follow_view"),
    path('profile/unlike/<int:pk>', views.unlike_view, name="unfollow_view"),
]
