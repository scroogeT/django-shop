from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render
from accounts.forms import SignUpForm
from django.urls import reverse_lazy


class SignUpView(FormView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:signup-success')
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/signup_success')

    args = {}
    args.update(csrf(request))
    args['form'] = SignUpForm()
    return render(request, 'accounts/signup.html', args)


def signup_success(request):
    return render(request, 'accounts/signup_success.html')


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }

    return JsonResponse(data)
