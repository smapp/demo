from django.db import models

class Person(models.Model):
	"""Contact and vital details."""
	fname = models.CharField(max_length=30)
	lname = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)

class Resume(models.Model):
	"""Resume for the topic indicated in name."""
	name = models.CharField(max_length=30)
	person = models.ForeignKey(Person, related_name='resume_set')

class EntrySection(models.Model):
	"""Major heading section, for ex. 'Employment'"""
	resume = models.ForeignKey(Resume, related_name='section_set')
	title = models.CharField(max_length=30)
	mode = models.IntegerField()

class Entry(models.Model):
	"""One item contained within the section."""
	section = models.ForeignKey(EntrySection, related_name='entry_set')
	format_type = models.IntegerField()
	title = models.CharField(max_length=30)
	byline = models.CharField(max_length=30)
	description = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
