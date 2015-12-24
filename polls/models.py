import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	# Each question model has a question and a publication date
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = "Published recently?"  # text that will show up in admin page when method field is shown

class Choice(models.Model):
	# Each choie model has two fields: the text of the choice and a vote tally. Each choice model is also associated with a question.
	question = models.ForeignKey(Question)  # ForeignKey has a many-to-one relationship: each question can have multiple choices
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text