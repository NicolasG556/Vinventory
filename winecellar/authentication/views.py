import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm
from wines.forms import PhotoForm
from authentication.models import User

from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request,
                  'authentication/signup.html',
                  context={'form': form})


@login_required
def update_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    print(f"User ID from URL parameter: {user_id}")
    print(f"User fetched from database: {user.username}")

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_picture_form = PhotoForm(request.POST, request.FILES, instance=user.profile_pic)
        if any([user_form.is_valid(), profile_picture_form.is_valid()]):
            profile_pic = profile_picture_form.save()
            user_profile = user_form.save(commit=False)
            user_profile.profile_pic = profile_pic
            user_profile.save()
            messages.success(request, 'Your profile is updated successfully')
            # rediriger vers la page détaillée de l'évenement que nous venons de mettre à jour
            return redirect('update-user', user_id=user_id)

    user_form = UpdateUserForm(instance=user)  # on pré-rempli le formulaire avec un évenement existant
    # Create a separate photo_form instance for the photo associated with the event
    if user.profile_pic:
        profile_picture_form = PhotoForm(instance=user.profile_pic)
    else:
        profile_picture_form = PhotoForm()

    return render(request,
                  'authentication/update_user.html',
                  {'user_form': user_form,
                   'profile_picture_form': profile_picture_form,
                   'user': user})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request,
                  'authentication/user_list.html',
                  {'users': users})
