
from django.db import models
from django.core.validators import MinLengthValidator


class Flashcard(models.Model):
    word = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    translation = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    example_usage = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_reviewed = models.DateTimeField(null=True, blank=True)
    knowledge_level = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.word} - {self.translation}"
