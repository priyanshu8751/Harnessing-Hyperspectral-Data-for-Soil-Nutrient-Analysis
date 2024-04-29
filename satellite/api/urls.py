# myapi/urls.py
from django.urls import path
from .views import get_model_predictions

urlpatterns = [
    path('get-model-predictions/', get_model_predictions, name='get_model_predictions'),
]
