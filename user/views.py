from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views import View
# Create your views here.
def index(request):
    return render(request,'user/home.html')
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
    return redirect('/')
