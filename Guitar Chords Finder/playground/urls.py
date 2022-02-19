from django.urls import path
from . import views

# Configure URLs
urlpatterns = [
    path('howdy/', views.howdy)
]
