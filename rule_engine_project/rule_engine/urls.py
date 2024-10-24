from django.urls import path
from . import views

urlpatterns = [
    path('create_rule/', views.create_rule_view, name='create_rule'),
    path('get_rules/', views.get_rules, name='get_rules'),
    path('evaluate_rule/', views.evaluate_rule_view, name='evaluate_rule'),
]
