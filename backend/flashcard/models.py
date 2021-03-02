from django.db import models
# from model_utils.managers import InheritanceManager

# Create your models here.

class Quiz(models.Model):
    """what"""

class Session(models.Model):
    """what"""

class Flashcard(models.Model):
    question = models.TextField()
    # answer = models.CharField(max_length=120)
    # correct = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=1)
    # objects = InheritanceManager()

    def __str__(self):
        return self.question

class Choice(models.Model):
    flashcard = models.ForeignKey("Flashcard", on_delete=models.CASCADE, related_name="choices")
    choice_text = models.CharField("Choice", max_length=120)
    position = models.IntegerField("position")
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text

    class Meta:
        # TODO: some way to verify every Flashcard has at least one choice that is a correct answer
        unique_together = [
            ("flashcard", "choice_text"),
            ("flashcard", "position")
        ]
        ordering = ("position",)