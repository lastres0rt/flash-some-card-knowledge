import html
import random

from django import forms
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.views.generic import DetailView
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FlashcardSerializer, ChoiceSerializer
from .models import Flashcard, Choice

# Create your views here.

class FlashcardView(viewsets.ModelViewSet):
    serializer_class = FlashcardSerializer
    queryset = Flashcard.objects.all()

class ChoiceView(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

def hello(request):
    message = repr(Flashcard.objects.all())
    return HttpResponse('Hello Tommy' + html.escape(message))

@never_cache
def random_question(request):
    # chosen = random.choice(Flashcard.objects.all())
    # return HttpResponse(html.escape(repr(chosen.choices.all())))
    def weight(q):
        return [0, 1.0, 0.5, 0.25, 0.2, 0.1][q.difficulty]
    chosen = None
    qq = Flashcard.objects.all()
    weights = [weight(q) for q in qq]
    r = random.uniform(0,sum(weights))
    accum = 0.0
    for q, w, in zip(qq, weights):
        accum += w
        if r < accum: 
            chosen = q
            break
    response = redirect('/api/flashcards/' + str(chosen.id) + '/')
    return response
    # return chosen

# @api_view(['GET', 'POST'])
# def choice_evaluation(request):
#     if request.method == 'GET':
#         return Response()
#     elif request.method == 'POST':
#         return Response()

# class RandomFlashcardView(DetailView):
#     serializer_class = FlashcardSerializer
#     model = Flashcard

#     def get_object(self, queryset=None):
#         def weight(q):
#             return [0, 1.0, 0.5, 0.25, 0.2, 0.1][q.difficulty]
#         chosen = None
#         qq = Flashcard.objects.all()
#         weights = [weight(q) for q in qq]
#         r = random.uniform(0,sum(weights))
#         accum = 0.0
#         for q, w, in zip(qq, weights):
#             accum += w
#             if r < accum: 
#                 chosen = q
#                 break
#         return chosen

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context('form') = AnswerSubmissionForm()
    #     return context