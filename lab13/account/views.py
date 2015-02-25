from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView
"""
class LoginView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Login Viev')
"""
class LoginView(TemplateView):

    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)

        is_auth = False
        name = None

        if self.request.user.is_authenticated():
            is_auth = True
            name = self.request.user.username

        context.update({'is_auth': is_auth, 'name': name})

        return context

#class ProfileView(TemplateView):

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/account/login/')
