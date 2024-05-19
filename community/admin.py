from django.contrib import admin
from .models import Profile, Contact, Category, Post, Like, CommunityRule, Community, Comments, Follow
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class UserProfile(ModelAdmin):
    list_display = ['name', 'gender', 'age']
    search_fields = ['name', 'gender', 'age']
    list_filter = ['age']


admin.site.register(Profile, UserProfile)

admin.site.register(Contact)


class CategoryAdmin(ModelAdmin):
    list_display = ['C_name', 'C_disc']
    search_fields = ['C_name']


admin.site.register(Category, CategoryAdmin)


class UserPost(ModelAdmin):
    list_display = ['upload_by', 'subject', 'pic']
    search_fields = ['upload_by', 'subject']
    list_filter = ['subject']


admin.site.register(Post, UserPost)


class UserLike(ModelAdmin):
    list_display = ['like_post', 'like_by']
    search_fields = ['like_by']


admin.site.register(Like, UserLike)


class UserComments(ModelAdmin):
    list_display = ['post', 'comment_by', 'msg']
    search_fields = ['comment_by', 'msg']
    list_filter = ['flag']


admin.site.register(Comments, UserComments)


class UserFollow(ModelAdmin):
    list_display = ['profile', 'followed_by']
    search_fields = ['profile', 'followed_by']


admin.site.register(Follow, UserFollow)


class UserCommunity(ModelAdmin):
    list_display = ['c_admin', 'c_name', 'visiblity']
    search_fields = ['c_admin', 'c_name']
    list_filter = ['visiblity', 'cr_date']


admin.site.register(Community, UserCommunity)


class UserCommunityRule(ModelAdmin):
    list_display = ['c_name', 'title']
    search_fields = ['c_name', 'title', 'desc']
    list_filter = ['cr_date']


admin.site.register(CommunityRule, UserCommunityRule)
