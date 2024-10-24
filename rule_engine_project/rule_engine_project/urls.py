"""
URL configuration for rule_engine_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rule_engine.views import index, create_rule_view, evaluate_rule_view  # Import delete_rule_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Root URL mapped to index view
    path('create_rule/', create_rule_view, name='create_rule'),
    path('evaluate_rule/', evaluate_rule_view, name='evaluate_rule'),

]


