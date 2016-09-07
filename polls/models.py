from django.db import models
from tinymce.models import HTMLField

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = HTMLField(blank=False)




