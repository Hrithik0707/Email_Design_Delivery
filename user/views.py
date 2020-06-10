from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Contacts,Grps
from django.views.generic.edit import CreateView 
from .forms import CreateGroupForm
# Create your views here.
def index(request):
    return render(request,'user/homepage.html')
def signup(request):
    if request.method =="POST":
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email Exists')
                return redirect('signup')
            user = User.objects.create_user(username = user_name,email= email, password = password1)
            user.save()
            messages.info(request,'User Created Successfully.')
            return redirect('signin')
        else:
            messages.info(request,'Wrong Password')
            return redirect('signup')
    else:
        return render(request,'user/index.html')


def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None

class LoginView(View):
    template_name = 'user/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)

        if user is not None:
            if user.is_active:
                auth.login(request, user)

                return redirect('index')
            else:
                messages.info(request,'User not active')
        else:
            messages.info(request,'Invalid Credentials')

        return render(request, self.template_name)

def logout(request):
    auth.logout(request)
    return redirect('index')

def contact(request):
    contacts = Contacts.objects.filter(user = request.user)
    return render(request,'user/contact.html',{'contacts':contacts})

def group(request):
    groups = Grps.objects.filter(user = request.user)
    return render(request,'user/groups.html',{'groups':groups})

def createcontact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        if Contacts.objects.filter(email = email).exists():
                messages.info(request,'This contact is already added.')
                return redirect('createcontact')
        else:
            contact = Contacts.objects.create(user = request.user, name = name,email= email, phone = phone , city = city)
            contact.save()
            messages.info(request,'Contact Added Successfully.')
            return redirect('allcontacts')
    else:
        return render(request,'user/createcon.html')

def creategroup(request):
    if request.method =="POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            grps = form.save(commit=False)
            grps.user = request.user
            grps.save()
            messages.info(request,'Group added successfully')
            return redirect('allgroups')
    else:
        form = CreateGroupForm()
    return render(request,'user/grps_form.html',{'form': form})


def send_mail_to_mul(request):
    if request.method == 'POST':
        sub = request.POST['subject']
        msg = request.POST['message']
        frm_mail = request.POST['from_mail']
        rec_str = request.POST['recipient_list']

        rec_list = rec_str.split(",")
        rec_list = [i.strip() for i in rec_list]
        print(rec_list)

        send_mail(
            subject=sub,
            message=msg,
            from_email=frm_mail,
            recipient_list=rec_list,
            fail_silently=False,
        )
        messages.info(request,'Email Send successfully')
        return redirect('sendemail')
    else:
        return render(request, 'user/sendemail.html') 



