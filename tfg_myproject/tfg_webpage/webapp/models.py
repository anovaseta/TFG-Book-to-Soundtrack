from django.db import models


class Storygraph_Book(models.Model):
    storygraph_id = models.CharField(max_length=300, default='')
    title = models.CharField(max_length=300)
    authors = models.JSONField(max_length=500)
    isbn_uid = models.CharField(max_length=300, default='')
    pages = models.IntegerField()
    first_published_year = models.IntegerField()
    description = models.TextField(default='')
    cover_source = models.URLField(default='')
    number_of_reviews = models.CharField(max_length=300, default='')
    tag_percentages = models.JSONField(max_length=3000, default=dict)
    pace_percentages = models.JSONField(max_length=3000, default=dict)
    tag_weights = models.JSONField(max_length=3000, default=dict)

    def __str__(self):
        return f"{self.title} by {self.authors}"


class Storygraph_Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    # MOOD,GENRE,PACE,OTHER
    tag_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tag_name} ({self.tag_type})"


class Tagged_Book(models.Model):
    book = models.ForeignKey(Storygraph_Book, on_delete=models.CASCADE)
    tag = models.ForeignKey(Storygraph_Tag, on_delete=models.CASCADE)
    weight = models.FloatField(default=-1)

    def __str__(self):
        return f"{self.book.title} tagged with {self.tag.tag_name}"
    

class Synonym(models.Model):
    synonym = models.CharField(max_length=100)

    # SELF,THESAURUS
    source = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.synonym} ({self.source})"
    

class Synonym_Relation(models.Model):
    tag = models.ForeignKey(Storygraph_Tag, on_delete=models.CASCADE)
    synonym = models.ForeignKey(Synonym, on_delete=models.CASCADE)
    affinity = models.CharField(max_length=50, default='') # [weak, strong, strongest]

    def __str__(self):
        return f"{self.synonym.synonym} ({self.synonym.source}) is a synonym of {self.tag.tag_name} with affinity {self.affinity}"
    

class LastFM_Entity(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100) 
    tag = models.CharField(max_length=100, default='') 
    def __str__(self):
        return f"{self.name} ({self.type})"
    
class Entity_Tag_Relation(models.Model):
    entity = models.ForeignKey(LastFM_Entity, on_delete=models.CASCADE)
    tag = models.ForeignKey(Synonym, on_delete=models.CASCADE)
    source = models.CharField(max_length=100, default='') # TRACK, FROM_ARTISTS, FROM_ALBUMS

    def __str__(self):
        return f"{self.entity.name} is related to {self.tag.synonym}"