from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from account.forms import UserForm, UserProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, FormView

class RegisterView(FormView):
    template_name = 'account_register.html'
    form_class, second_form_class = UserForm, UserProfileForm

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)

        if 'user_form' not in context:
            context.update({'user_form': self.form_class(prefix='user')})
        if 'profile_form' not in context:
            context.update({'profile_form': self.second_form_class(prefix='profile')})

        return context

    def post(self, request, *args, **kwargs):

        user_form = UserForm(data=request.POST, prefix='user')
        profile_form = UserProfileForm(data=request.POST, prefix='profile')

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.userprofile = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'profile-userprofile_picture' in request.FILES:
                profile.userprofile_picture = request.FILES['profile-userprofile_picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            return HttpResponseRedirect('/order/')
        else:
            return HttpResponse('%s %s' % (user_form, profile_form))


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

    def post(self, request, *args, **kwargs):

        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/order/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

#class ProfileView(TemplateView):

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/account/login/')
