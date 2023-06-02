from django.urls import path, include
from .views import Home, Review
app_name = 'peerapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('accounts/', include('allauth.urls')),
    path('review/', Review.as_view(), name="Review"),
]