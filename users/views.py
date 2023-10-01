import random
import string

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserForm, UserRegisterForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailing:messages')


class LogoutView(BaseLogoutView):
    success_url = reverse_lazy('mailing:messages')


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = "users/register.html"

    def form_valid(self, form):
        new_user = form.save()
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        new_user.email_verification_token = token
        new_user.save()

        # current_site = get_current_site(self.request)
        # mail_subject = 'Подтвердите ваш аккаунт'
        # message = (
        #     f'Для завершения регистрации перейдите по ссылке:\n'
        #     f'http://{current_site.domain}{reverse("users:verify_email", kwargs={"uid": new_user.pk, "token": token})}'
        # )
        # send_mail(subject=mail_subject, message=message, from_email=settings.EMAIL_HOST_USER,
        #           recipient_list=[new_user.email])

        return super().form_valid(form)


class VerifyEmailView(View):
    def get(self, request, uid, token):
        try:
            user = User.objects.get(pk=uid, email_verification_token=token)
            user.is_active = True
            user.save()
            return render(request, 'users/registration_success.html')
        except User.DoesNotExist:
            return render(request, 'users/registration_failed.html')


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('mailing:messages')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user
