from django.urls import path
from . import views

# Configure URLs
urlpatterns = [
    path('form/', views.form),
    path('form_output/', views.form_output, name='form_output')
]