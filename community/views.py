from django.shortcuts import render
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Profile, Contact, Category, Post, Like, CommunityRule, Community, Comments, Follow
from .forms import ProfileForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login as login_process, logout, authenticate
from django.shortcuts import redirect, get_object_or_404
from django.template.loader import get_template
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'community/index.html')


def about_view(request):
    return render(request, 'community/about.html')


def signup_view(request):
    if (request.method == 'POST'):
        RF = RegistrationForm(request.POST)
        if (RF.is_valid()):
            RF.save(request)
            return HttpResponseRedirect(reverse('login'))
        else:
            HttpResponse("invalid Data")
            HttpResponse(RF.errors)
    else:
        RF = RegistrationForm()
    return render(request, 'signup.html', {'RF': RF})


class EmailAuthBackend:
    def authenticate(username, password, backend):
        try:
            user = User.objects.get(email=username)
            success = user.check_password(password)
            if success:
                return user
        except User.DoesNotExist:
            pass
        return None


def user_login(request):
    session_var = request.session.items()
    if request.session.has_key('uname') and request.session.has_key('password'):
        uname = request.session['uname']
        pwd = request.session['password']
        a1 = EmailAuthBackend
        user = a1.authenticate(username=uname, password=pwd,
                               backend='django.contrib.auth.backends.ModelBackend')
        login_process(
            request, user, 'django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect(reverse_lazy('index'))
    else:
        return user_login1(request)


def user_login1(request):
    uname = ''
    pwd = ''
    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        remind = request.POST.get('remember_me')
        a1 = EmailAuthBackend
        user = a1.authenticate(username=username, password=password,
                               backend='django.contrib.auth.backends.ModelBackend')
        if user:
            if (user.is_active):
                login_process(
                    request, user, 'django.contrib.auth.backends.ModelBackend')
                if remind:
                    request.session['uname'] = username
                    request.session['password'] = password
                return home(request)
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('invalid username and password')

    return render(request, 'login.html', {'uname': uname, 'pwd': pwd})


@login_required
def user_logout(request):
    data_key = request.session.items()
    uname = request.session.get('uname')
    pwd = request.session.get('password')
    logout(request)
    if uname and pwd:
        request.session['uname'] = uname
        request.session['password'] = pwd
    return render(request, 'community/index.html')


@login_required
def profile_view(request):
    p2 = None
    global form_pic
    form_pic = None
    user = request.user
    pr = Profile.objects.filter(user=user)
    if request.method == 'POST':
        if pr.count() is not 0:
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form_pic = form.cleaned_data.get('picture')
            p1 = Profile.objects.get(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            p = request.POST.get('picture')
            a = request.POST.get('age')
            if p1 is not None:
                p1.set_data(n, sta, gen, a, form_pic,
                            your_facebook, your_bio, add)
                messages.success(
                    request, 'profile update successfull', extra_tags='alert')
                return redirect('profile')
        else:
            p1 = Profile.objects.create(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            a = request.POST.get('age')
            if p1 is not None:
                if p1.set_data(n, sta, gen, a, form_pic, your_facebook, your_bio, add) == 'done':
                    pr = 1
                    return HttpResponse("profile update successfully")
                else:
                    return HttpResponse("profile is not updated")
    if Profile.objects.filter(user=user).count() is not 0:
        p2 = Profile.objects.get(user=user)
    form = ProfileForm()
    return render(request, 'community/profile.html', {'p2': p2, 'form': form})


@login_required
def profile_final_view(request):
    p2 = None
    global form_pic
    form_pic = None
    user = request.user
    pr = Profile.objects.filter(user=user)
    if request.method == 'POST':
        if pr.count() is not 0:
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form_pic = form.cleaned_data.get('picture')
            p1 = Profile.objects.get(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            p = request.POST.get('picture')
            a = request.POST.get('age')
            if p1 is not None:
                p1.set_data(n, sta, gen, a, form_pic,
                            your_facebook, your_bio, add)
                messages.success(
                    request, 'profile update successfull', extra_tags='alert')
                return redirect('profile')
        else:
            p1 = Profile.objects.create(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            a = request.POST.get('age')
            if p1 is not None:
                if p1.set_data(n, sta, gen, a, form_pic, your_facebook, your_bio, add) == 'done':
                    pr = 1
                    return HttpResponse("profile update successfully")
                else:
                    return HttpResponse("profile is not updated")
    if Profile.objects.filter(user=user).count() is not 0:
        p2 = Profile.objects.get(user=user)
    form = ProfileForm()
    return render(request, 'community/profile_final.html', {'p2': p2, 'form': form})


@login_required
def profile_final_edit_view(request):
    p2 = None
    global form_pic
    form_pic = None
    user = request.user
    pr = Profile.objects.filter(user=user)
    if request.method == 'POST':
        if pr.count() is not 0:
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form_pic = form.cleaned_data.get('picture')
            p1 = Profile.objects.get(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            a = request.POST.get('age')
            if p1 is not None:
                p1.set_data(n, sta, gen, form_pic,
                            your_facebook, your_bio, add)
                messages.success(
                    request, 'profile update successfull', extra_tags='alert')
                return redirect('profile_final')
        else:
            p1 = Profile.objects.create(user=user)
            n = request.POST.get('name')
            sta = request.POST.get('status')
            gen = request.POST.get('gender')
            add = request.POST.get('address')
            your_bio = request.POST.get('your_bio')
            your_facebook = request.POST.get('your_facebook')
            a = request.POST.get('age')
            if p1 is not None:
                if p1.set_data(n, sta, gen, form_pic, your_facebook, your_bio, add) == 'done':
                    pr = 1
                    return HttpResponse("profile update successfully")
                else:
                    return HttpResponse("profile is not updated")
    if Profile.objects.filter(user=user).count() is not 0:
        p2 = Profile.objects.get(user=user)
    form = ProfileForm()
    return render(request, 'community/profile_edit_final.html', {'p2': p2, 'form': form})


@login_required
def contact_view(request):
    obj2 = None
    global cf
    user = request.user
    cf = Contact.objects.filter(user=user)
    if request.method == 'POST':
        if cf.count() is not 0:
            obj1 = Contact.objects.get(user=user)
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            msg = request.POST.get('msg')
            if obj1 is not None:
                obj1.set_data(f_name, l_name, email, mobile, msg)
                messages.success(
                    request, 'Your contact request register successfully')
                cf = 1
                return home(request)
        else:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            msg = request.POST.get('msg')
            obj1 = Contact.objects.create(user=user)
            if obj1 is not None:
                if obj1.set_data(f_name, l_name, email, mobile, msg) == 'done':
                    cf = 1
                    return home(request)
                else:
                    return HttpResponse("contact is not updated")

    if Contact.objects.filter(user=user).count() is not 0:
        obj2 = Contact.objects.filter(user=user)
    return render(request, 'community/contact.html', {'obj2': obj2})


@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        post_like = Post.objects.filter(
            Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        for p1 in post_like:
            p1.like = False
            obj_list = Like.objects.filter(
                like_post=p1, like_by=self.request.user.profile)
            if obj_list:
                p1.like = True
        return post_like


@method_decorator(login_required, name='dispatch')
class AllPostListView(ListView):
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = ListView.get_context_data(self, **kwargs)
        followed_list1 = Follow.objects.filter(
            followed_by=self.request.user.profile)
        followed_list2 = []
        for e in followed_list1:
            followed_list2.append(e.profile)
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        posts = Post.objects.filter(Q(upload_by__in=followed_list2)).filter(
            Q(subject__icontains=si)).order_by("-id")
        context['post_list'] = posts
        return context

    template_name = "community/activity.html"


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post


@method_decorator(login_required, name='dispatch')
class ProfileListView(ListView):
    model = Profile

    def get_queryset(self):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        profile_follow = Profile.objects.filter(
            Q(name__icontains=si) | Q(gender__icontains=si))
        for p1 in profile_follow:
            p1.followed = False
            obj_list = Follow.objects.filter(
                profile=p1, followed_by=self.request.user.profile)
            if obj_list:
                p1.followed = True
        return profile_follow
    template_name = "community/members.html"


@method_decorator(login_required, name='dispatch')
class ProfileDetailView(DetailView):
    model = Profile


def follow_view(request, pk):
    user = Profile.objects.get(pk=pk)
    Follow.objects.create(profile=user, followed_by=request.user.profile)
    return HttpResponseRedirect(redirect_to="/community/member")


def unfollow_view(request, pk):
    user = Profile.objects.get(pk=pk)
    Follow.objects.filter(
        profile=user, followed_by=request.user.profile).delete()
    return HttpResponseRedirect(redirect_to="/community/member")


def like_view(request, pk):
    p1 = Post.objects.get(pk=pk)
    Like.objects.create(like_post=p1, like_by=request.user.profile)
    return HttpResponseRedirect(redirect_to="/community/post")


def unlike_view(request, pk):
    p1 = Post.objects.get(pk=pk)
    Like.objects.filter(like_post=p1, like_by=request.user.profile).delete()
    return HttpResponseRedirect(redirect_to="/community/post")


def group_view(request):
    return render(request, 'community/group.html')


def groupdetails_view(request):
    return render(request, 'community/group-detail.html')


@method_decorator(login_required, name='dispatch')
class GroupCreateView(CreateView):
    model = Community
    fields = ['c_name', 'visiblity', 'pic', 'desc']

    def form_valid(self, form):
        self.object = form.save()
        self.object.c_admin = self.request.user.profile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    template_name = "community/Group_Create.html"


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['subject', 'msg', 'pic']

    def form_valid(self, form):
        self.object = form.save()
        self.object.upload_by = self.request.user.profile
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    template_name = "community/post_final.html"
