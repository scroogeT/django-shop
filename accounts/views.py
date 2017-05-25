from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from accounts.forms import SignUpForm


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:signup-success')
    template_name = 'accounts/signup.jinja'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def signup_success(request):
    return render(request, 'accounts/signup_success.jinja')


class SignInView(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('shop:book_list')
    template_name = 'accounts/signin.jinja'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)

        return HttpResponseRedirect(reverse_lazy('shop:book_list'))
