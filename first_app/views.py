from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, WebPage, AccessRecord
from . import forms
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context_dict = {'access_records': webpages_list, 'text': 'Hello World', 'number':100}
    return render(request, 'first_app/index.html', context=context_dict);

def other(request):
    return render(request, 'first_app/other.html')

def form_name_view(request):
    form = forms.FormName

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("NAME: " + form.cleaned_data['name'])
            print("EMAIL: " + form.cleaned_data['email'])
            print("TEXT: " + form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', context={'form': form})

def relative(request):
    return render(request, "first_app/relative_template_url.html")

def register(request):
    registered = False

    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    return render(request, "first_app/registration.html", {'registered' : registered, 'user_form': user_form, 'profile_form': profile_form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print('LOGIN FAILED')
            print("Username: {} and password {}".format(username, password))
            return HttpResponse('Invalid login details suplied!')
    else:
        return render(request, 'first_app/login.html')
    
@login_required
def special(request):
    return HttpResponse("You are logged in, nice!")

@login_required   
def user_logout(request):
    logout(request)
    return redirect('index')