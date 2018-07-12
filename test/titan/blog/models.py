from django.db import models


class Title(models.Model):
	name = models.CharField(max_length=10, default='woca')

	def __str__(self):
		return self.name


class Author(models.Model):
	name = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return f'{self.id}'


class Tag(models.Model):
	name = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Blog(models.Model):
	title = models.OneToOneField(Title, related_name='blog', on_delete=models.CASCADE)
	author = models.ForeignKey(Author, related_name='blogs', on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag, related_name='blogs')
	content = models.TextField()

	def __str__(self):
		return self.content
