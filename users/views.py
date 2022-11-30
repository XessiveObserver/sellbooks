from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm,\
    UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages

# Login


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return messages.success(request, 'Authenticated '
                                            'successfully')
                else:
                    return messages.error(request, 'Disabled user')
            else:
                return messages.info(request, 'Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


# Dashboard view
@login_required
def dashboard(request):
    # messages.success(request, 'Successfully logged in')
    return render(request, 'users/dashboard.html')

# Registration view


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                          'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'users/register.html',
                  {'user_form': user_form})


# Create the user profile
@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '
                             'successfully')
        else:
            messages.error(request, 'Error updating your profile')

    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'users/edit.html', {'user_form': user_form,
                                               'profile_form': profile_form})
