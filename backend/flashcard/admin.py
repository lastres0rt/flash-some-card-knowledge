from django.contrib import admin
import nested_admin
from .models import Flashcard, Choice

class ChoiceInline(nested_admin.NestedTabularInline):
    model = Choice
    extra = 4
    max_num = 4

class FlashcardInline(nested_admin.NestedTabularInline):
    model = Flashcard
    inlines = [ChoiceInline,]
    extra = 19


class FlashcardAdmin(admin.ModelAdmin):
    list_display = ('question', 'difficulty')
    inlines = [ChoiceInline,]
    extra = 4

# Register your models here.

admin.site.register(Flashcard, FlashcardAdmin)