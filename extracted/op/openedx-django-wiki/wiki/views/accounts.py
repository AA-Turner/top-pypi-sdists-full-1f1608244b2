"""This is nothing but the usual handling of django user accounts, so
go ahead and replace it or disable it!"""


from django.conf import settings as django_settings
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView

from wiki.models import URLPath


class Signup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "wiki/accounts/signup.html"

    def get_success_url(self, *args):
        messages.success(self.request, _('You are now sign up... and now you can sign in!'))
        return reverse("wiki:login")

class Logout(View):
    
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        messages.info(request, _("You are no longer logged in. Bye bye!"))
        return redirect("wiki:get", URLPath.root().path)

class Login(FormView):
    
    form_class = AuthenticationForm
    template_name = "wiki/accounts/login.html"
    
    def get_form_kwargs(self):
        self.request.session.set_test_cookie()
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def post(self, request, *args, **kwargs):
        self.referer = request.session.get('login_referer', '')
        return FormView.post(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        self.referer = request.headers.get('referer', '')
        request.session['login_referer'] = self.referer
        return FormView.get(self, request, *args, **kwargs)
    
    def form_valid(self, form, *args, **kwargs):
        auth_login(self.request, form.get_user())
        messages.info(self.request, _("You are now logged in! Have fun!"))
        if self.request.GET.get("next", None):
            return redirect(self.request.GET['next'])
        if django_settings.LOGIN_REDIRECT_URL:
            return redirect(django_settings.LOGIN_REDIRECT_URL)
        else:
            if not self.referer:
                return redirect('wiki:get', path='')
            return redirect(self.referer)
