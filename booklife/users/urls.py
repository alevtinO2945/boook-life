from django.urls import path
from .views import profile, RegisterView, profile_by_slug

urlpatterns = [

    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('profile/<int:user_id>', profile_by_slug, name='users-profile-by-slug'),
]