"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include #imported include
from rest_framework import routers
from flashcard import views

router = routers.DefaultRouter()
router.register(r'flashcards', views.FlashcardView, 'flashcard')
# router.register(r'flashcards/random', views.RandomFlashcardView, 'flashcard/random')
router.register(r'choices', views.ChoiceView, 'choice')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    path('api/', include(router.urls)),
    # path('api/flashcards/random', views.RandomFlashcardView.as_view()),
    path('hello', views.hello),
    path('random_question', views.random_question)
]
