from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserChangeForm, ProfileForm

@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_update')
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    
    return render(request, 'users/profile_update.html', context)
