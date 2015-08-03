from django.db import models

# Create your models here.
class DepressionScore(models.Model):
	"""docstring for DepressionScore"""
	depression_score_week1 = models.IntegerField(default=0)
	depression_score_week2 = models.IntegerField(default=0)
	depression_score_week3 = models.IntegerField(default=0)
	depression_score_week4 = models.IntegerField(default=0)
	depression_score_week5 = models.IntegerField(default=0)
	depression_score_week6 = models.IntegerField(default=0)
	depression_score_week7 = models.IntegerField(default=0)
	depression_score_week8 = models.IntegerField(default=0)
	#should return the user name
	def __str__(self):
		return 'user'