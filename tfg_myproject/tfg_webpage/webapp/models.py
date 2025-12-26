from django.db import models


class Storygraph_Book(models.Model):
    title = models.CharField(max_length=300)
    authors = models.JSONField(max_length=300)
    pages = models.IntegerField()
    first_published_year = models.IntegerField()
    average_rating = models.FloatField()
    description = models.TextField(default='')

    def __str__(self):
        return f"{self.title} by {self.authors}"


class Storygraph_Tag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_type = models.CharField(max_length=100)  # e.g., genre, mood, theme

    def __str__(self):
        return f"{self.tag_name} ({self.tag_type})"


class Tagged_Book(models.Model):
    book = models.ForeignKey(Storygraph_Book, on_delete=models.CASCADE)
    tag = models.ForeignKey(Storygraph_Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} tagged with {self.tag.tag_name}"
