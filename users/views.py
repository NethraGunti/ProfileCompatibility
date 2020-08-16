from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from users.forms import SignupForm


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('compatability'))
    else:
        return redirect(reverse_lazy('register'))


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print('00000000000000000')
        if form.is_valid():
            print('00000000000000000')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse_lazy('profile-details'))
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})


def profileDetials(request):
    return render(request, 'users/profile-details.html')


@login_required
def questions(request):
    return render(request, 'users/questions.html')


def compatibility(request):
    user = request.user
    # profile = Profile.objects.get(user=user)
    pass