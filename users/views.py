import random

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from users.models import Profile, Choices
from users.forms import SignupForm, ProfileForm, Choice1Form, ProfileUpdateForm


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('profile'))
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
    if not Profile.objects.filter(user=user):
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
    else:
        return redirect(reverse_lazy('question1'))
    

def question1(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question1 =  profile.questions[0][1]
    if not Choices.objects.filter(user=user, question=question1):
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
    else:
        return redirect(reverse_lazy('question2'))



def question2(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question2 =  profile.questions[1][1]

    if not Choices.objects.filter(user=user, question=question2):
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
    else:
        return redirect(reverse_lazy('question3'))


def question3(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    question3 =  profile.questions[2][1]

    if not Choices.objects.filter(user=user, question=question3):
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
    else:
        return redirect(reverse_lazy('compatibility'))
    



def compatibility(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    question1 = profile.questions[0][1]
    question2 = profile.questions[1][1]
    question3 = profile.questions[2][1]

    choice1 = Choices.objects.get(user=user, question=question1).option
    choice2 = Choices.objects.get(user=user, question=question2).option  
    choice3 = Choices.objects.get(user=user, question=question3).option

    other1 = Choices.objects.filter(question=question1).exclude(user=user)
    other2 = Choices.objects.filter(question=question2).exclude(user=user)
    other3 = Choices.objects.filter(question=question3).exclude(user=user)

    matches = []

    for obj1 in other1:
        if (obj1.user not in matches) and (obj1.option == choice1):
            matches.append(obj1.user)

    for obj2 in other2:
        if (obj2.user not in matches) and ( obj2.option == choice2):
            matches.append(obj2.user)

    for obj3 in other3:
        if (obj3.user not in matches) and (obj3.option == choice3):
            matches.append(obj3.user)
    
    compatibility = []
    for match in matches:
        pr = Profile.objects.get(user=match)
        compatibility.append((pr, round(Profile.compatibility(profile, pr),2), Profile.common_answers(profile, pr)))
    
    compatibility = sorted(compatibility, key=lambda x: x[1], reverse=True)[:5]

    context = {}
    context['matches'] = compatibility
    context['current'] = profile

    return render(request, 'users/compatibility.html', context)



def editProfile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.save()

            return redirect(reverse_lazy('compatibility'))
    else:
        form = ProfileUpdateForm(instance=Profile.objects.get(user=request.user))
    
    return render(request, 'users/editprofile.html', {'form':form})