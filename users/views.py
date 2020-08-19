import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from users.models import Profile, Choices
from users.forms import SignupForm, ProfileForm, Choice1Form


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('compatability'))
    else:
        return redirect(reverse_lazy('register'))


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse_lazy('login'))
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def profileDetials(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(user)
            profile.save()
            messages.success(request, f'Profile submitted for {user}!')
            return redirect(reverse_lazy('question1'))
    else:
        form = ProfileForm()
    return render(request, 'users/profile-details.html', {'form': form})
    

def question1(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question1 =  profile.questions[0][1]

    if request.method == 'POST':
        form = Choice1Form(request.POST)
        data = request.POST['option']
        if form.is_valid():
            choice = Choices.objects.create(user=user, question=question1, option=data)
            choice.save()
            return redirect(reverse_lazy('question2'))
    else:
        form = Choice1Form({'choices':profile.choice1()})
    return render(request, 'users/questions.html', {'form': form, 'question': question1})


def question2(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question2 =  profile.questions[1][1]

    if request.method == 'POST':
        form = Choice1Form(request.POST)
        data = request.POST['option']
        if form.is_valid():
            choice = Choices.objects.create(user=user, question=question2, option=data)
            choice.save()
            return redirect(reverse_lazy('question3'))
    else:
        form = Choice1Form({'choices':profile.choice2()})
    return render(request, 'users/questions.html', {'form': form, 'question': question2})


def question3(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question3 =  profile.questions[2][1]

    if request.method == 'POST':
        form = Choice1Form(request.POST)
        data = request.POST['option']
        if form.is_valid():
            choice = Choices.objects.create(user=user, question=question3, option=data)
            choice.save()
            return redirect(reverse_lazy('compatibility'))
    else:
        form = Choice1Form({'choices':profile.choice3()})
    return render(request, 'users/questions.html', {'form': form, 'question': question3})
    



def compatibility(request):
    user = request.user
    # profile = Profile.objects.get(user=user)
    pass