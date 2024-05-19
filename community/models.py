from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="single", choices=(
        ("single", "single"), ("married", "married"), ("widow", "widow")))
    gender = models.CharField(max_length=20, default="male", choices=(
        ("Male", "Male"), ("Female", "Female")))
    address = models.TextField(null=True, blank=True)
    your_facebook = models.CharField(max_length=100)
    your_bio = models.TextField(null=True, blank=True)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return "%s" % self.user

    class Meta:
        db_table = 'profile'

    def set_data(self, n, sta, gen, form_pic, y_fb, y_bio, a='default'):
        self.name = n
        self.status = sta
        self.gender = gen
        temp = self.picture
        self.picture = form_pic
        if self.picture == None:
            self.picture = temp
        self.your_facebook = y_fb
        self.your_bio = y_bio
        self.address = a
        self.save()
        return 'done'


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=10)
    msg = models.TextField(max_length=500)

    def __str__(self):
        return "%s" % self.user

    class Meta:
        db_table = 'contact'

    def set_data(self, f_name1, l_name1, email1, mobile1, msg1):
        self.f_name = f_name1
        self.l_name = l_name1
        self.email = email1
        self.mobile = mobile1
        self.msg = msg1
        self.save()
        return 'done'


class Category(models.Model):
    C_name = models.CharField(max_length=35)
    C_disc = models.CharField(max_length=200)

    def __str__(self):
        return "%s" % self.C_name


class Post(models.Model):
    upload_by = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=CASCADE)
    pic = models.ImageField(null=True, blank=True)
    subject = models.CharField(max_length=25)
    msg = models.TextField(max_length=500)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.subject

    class Meta:
        db_table = 'Post'

    def set_data(self, pic1, subject1, msg1, cr_date1):
        self.pic = pic1
        self.subject = subject1
        self.msg = msg1
        self.cr_date = cr_date1
        self.save()
        return 'done'


class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    comment_by = models.ForeignKey(Profile, on_delete=CASCADE)
    msg = models.TextField(max_length=500)
    pic = models.ImageField(null=True, blank=True)
    flag = models.CharField(max_length=20, null=True, blank=True, choices=(
        ("racist", "racist"), ("abbusing", "abbusing")))
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.msg

    class Meta:
        db_table = 'Comment'

    def set_data(self, pic1, subject1, msg1, cr_date1):
        self.pic = pic1
        self.subject = subject1
        self.msg = msg1
        self.cr_date = cr_date1
        self.save()
        return 'done'


class Like(models.Model):
    like_post = models.ForeignKey(Post, on_delete=CASCADE)
    like_by = models.ForeignKey(Profile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.like_by

    class Meta:
        db_table = 'Like'


class Follow(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=CASCADE, related_name='profile')
    followed_by = models.ForeignKey(
        Profile, on_delete=CASCADE, related_name='followed_by')

    def __str__(self):
        return "%s" % self.followed_by

    class Meta:
        db_table = 'Follow'


class Community(models.Model):
    c_admin = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=CASCADE)
    c_name = models.CharField(primary_key=True, max_length=60)
    visiblity = models.CharField(max_length=20, choices=(
        ("private", "private"), ("public", "public")))
    pic = models.ImageField(null=True, blank=True)
    desc = models.CharField(max_length=20)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.c_name

    class Meta:
        db_table = 'Community'

    def set_data(self, pic1, subject1, msg1, cr_date1):
        self.pic = pic1
        self.subject = subject1
        self.msg = msg1
        self.cr_date = cr_date1
        self.save()
        return 'done'


class CommunityRule(models.Model):
    c_name = models.ForeignKey(Community, on_delete=CASCADE)
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=500)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.c_name

    class Meta:
        db_table = 'CommunityRule'

    def set_data(self, pic1, subject1, msg1, cr_date1):
        self.pic = pic1
        self.subject = subject1
        self.msg = msg1
        self.cr_date = cr_date1
        self.save()
        return 'done'
