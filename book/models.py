from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Source(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField('date published', null=True)
    page = models.IntegerField(default=0, null=True)
    reference = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.title)


class Article(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True)
    author = models.ForeignKey(Author)
    source = models.ForeignKey(Source)
    file_path = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.title)
