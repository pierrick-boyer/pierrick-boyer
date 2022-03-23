""" Simple function to change user password using basic Django forms. This example does not include the front-end. """

from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


@login_required
def change_password(request):

    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user, request.POST)

        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password was successfully updated', extra_tags='success')
            return redirect('profile')

    else:
        password_form = PasswordChangeForm(request.user)

    return render(request, 'app9/change_password.html', {'password_form': password_form})