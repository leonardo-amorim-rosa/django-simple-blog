from __future__ import unicode_literals

from django.db import models

class Post(models.Model):

	title = models.CharField(max_length=100, null=False)
	text = models.TextField(null=False)

	def __str__(self):
		return self.title