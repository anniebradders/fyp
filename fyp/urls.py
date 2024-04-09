from django.urls import path
from fyp import views
from .views import prediction_view

urlpatterns = [
    path("", prediction_view, name='fyp'),
    #path("", views.fyp, name="fyp"),
]