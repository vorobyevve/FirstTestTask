from django.urls import path
from .views import LinkView

app_name = 'domains'

urlpatterns =[
    path('visidet_domains', LinkView.as_view()),
]