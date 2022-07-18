from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from django.conf import settings
from django.core.mail import send_mail


send_mail('Тема', 'Тело письма', settings.EMAIL_HOST_USER, ['to@example.com'])

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
          'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


