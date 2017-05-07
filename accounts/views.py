from django.views.generic.edit import FormView
from django.shortcuts import render
from accounts.forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:signup-success')
    template_name = 'accounts/signup.jinja'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


def signup_success(request):
    return render(request, 'accounts/signup_success.jinja')
