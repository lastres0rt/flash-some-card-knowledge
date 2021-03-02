from rest_framework import serializers
from .models import Flashcard, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'choice_text')

class FlashcardSerializer(serializers.ModelSerializer):
    # choices = serializers.StringRelatedField(many=True)
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Flashcard
        fields = ('id', 'question', 'choices')

# class ChoiceSerializer(serializers.RelatedField):
#     def to_representation(self, value):
