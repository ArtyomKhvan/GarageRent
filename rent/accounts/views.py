from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View, CreateView, DetailView, UpdateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model, update_session_auth_hash

from accounts.forms import RegistrationForm, UserChangeForm, ProfileChangeForm, PasswordChangeForm
from accounts.models import Profile


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_path = request.POST.get("next")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_path:
                return HttpResponseRedirect(next_path)

            return redirect(settings.LOGIN_REDIRECT_URL)
        return render(request, "registration/login.html", {"has_error": True})


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)


class RegisterView(CreateView):
    model = User
    template_name = "registration/register.html"
    form_class = RegistrationForm

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
        login(self.request, user)
        return redirect("webapp:index")


class UserDetailView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        articles = self.object.article_set.order_by("-created_at")
        paginator = Paginator(articles, self.paginate_related_by,
                              orphans=self.paginate_related_orphans)
        page_num = self.request.GET.get("page", 1)
        page = paginator.get_page(page_num)
        kwargs["page_obj"] = page
        kwargs["articles"] = page.object_list
        kwargs["is_paginated"] = page.has_other_pages()
        return super().get_context_data(**kwargs)


class ChangeProfileAccessMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object() or \
               self.request.user.is_superuser or self.request.user.groups.filter(name="admins")


class UserChangeView(ChangeProfileAccessMixin, UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = "user_change.html"
    context_object_name = "user_obj"

    def get_profile_form(self):
        form_kwargs = {"instance": self.object.profile}
        if self.request.method == "POST":
            form_kwargs["data"] = self.request.POST
            form_kwargs["files"] = self.request.FILES
        return ProfileChangeForm(**form_kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        user_form = self.get_form()
        profile_form = self.get_profile_form()
        if user_form.is_valid() and profile_form.is_valid():
            return self.form_valid(user_form, profile_form)
        else:
            return self.form_invalid(user_form, profile_form)

    def form_valid(self, user_form, profile_form):
        result = super().form_valid(user_form)
        profile_form.save()
        return result

    def form_invalid(self, user_form, profile_form):
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = self.get_profile_form()
            kwargs["user_form"] = self.get_form()
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.object.pk})


class ChangePasswordView(ChangeProfileAccessMixin, UpdateView):
    model = get_user_model()
    form_class = PasswordChangeForm
    template_name = "change_password.html"
    context_object_name = "user_obj"

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.instance)
        return redirect("accounts:profile", pk=self.get_object().pk)