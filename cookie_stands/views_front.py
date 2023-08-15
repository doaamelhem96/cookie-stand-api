from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import CookieStand


class CookieStandListView(LoginRequiredMixin, ListView):
    template_name = "cookie_stands/cookie_stand_list.html"
    model = CookieStand
    context_object_name = "cookie_stands"


class CookieStandDetailView(LoginRequiredMixin, DetailView):
    template_name = "cookie_stands/cookie_stand_detail.html"
    model = CookieStand
    def get_success_url(self):
        return reverse_lazy("cookie_stand_list", args=[self.object.pk])


class CookieStandUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "cookie_stands/cookie_stand_update.html"
    model = CookieStand
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("cookie_stand_detail", args=[self.object.pk])





class CookieStandCreateView(LoginRequiredMixin, CreateView):
    template_name = "cookie_stands/cookie_stand_create.html"
    model = CookieStand
    fields = "__all__" # "__all__" for all of them
    def get_success_url(self):
        return reverse_lazy("cookie_stand_detail", args=[self.object.pk])


class CookieStandDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "cookie_stands/cookie_stand_delete.html"
    model = CookieStand
    success_url = reverse_lazy("cookie_stand_list")
