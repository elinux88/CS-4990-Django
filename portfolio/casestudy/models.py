from django.db import models

class CaseStudy(models.Model):
    name = models.CharField(max_length="200")
    description = models.TextField()

    def __unicode__(self):
        return self.name

class Item(models.Model):
    casestudy = models.ForeignKey(CaseStudy)
    title = models.CharField(max_length="200")
    image = models.ImageField(upload_to="items/%Y/%m/%d")
    description = models.TextField()

    def __unicode__(self):
        return self.title
