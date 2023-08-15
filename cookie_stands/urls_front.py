from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path("c/", CookieStandListView.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="cookie_stand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookie_stand_create"),
    path("cookie_stands/<int:pk>/update/",CookieStandUpdateView.as_view(), name='cookie_stand_update'),
    path("cookie_stands/<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookie_stand_delete"),
]
