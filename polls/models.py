import datetime

from django.db import models
from django.utils import timezone 


# Create your models here.
#update charfield size of question and choice text
class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published') # date published - name of model field

    def __str__(self): # normal method
        return self.question_text

    def was_published_recently(self): # custom method
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # delete objects that reference choices model
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text