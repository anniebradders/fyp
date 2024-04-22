from django.urls import path
from fyp import views
from .views import prediction_view
from .views import evaluation

urlpatterns = [
    path("", prediction_view, name='fyp'),
    path('evaluation/', evaluation , name='evaluation'),
]