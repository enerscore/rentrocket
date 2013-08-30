from django.db import models
import re

#feed info moved to source.models.FeedInfo

def to_tag(item):
    """
    take any string and convert it to an acceptable tag

    tags should not contain spaces or special characters
    numbers, lowercase letters only
    underscores can be used, but they will be converted to spaces in some cases
    """
    #item = self.name.lower()
    item = item.lower()
    #get rid of trailing and leading blank spaces:
    item = item.strip()
    item = re.sub(' ', '_', item)
    item = re.sub("/", '_', item)
    item = re.sub("\\\\'", '', item)
    item = re.sub("\\'", '', item)
    item = re.sub("'", '', item)

    #todo:
    # filter any non alphanumeric characters

    return item


class City(models.Model):
    """
    Details to define a specific City
    """
    #Name of the municipality providing this feed.
    #For example 'San Francisco' or 'Multnomah County'
    #municipality_name = models.CharField(max_length=20)

    name = models.CharField(max_length=200)

    #URL of the publishing municipality's website
    url = models.CharField(max_length=100, blank=True)

    #this is what we'll use to look up a city:
    tag = models.CharField(max_length=200, unique=True, default=to_tag(str(name)))

    #in case we want to represent other types of municipalities, not just cities
    type = models.CharField(max_length=50)

    added = models.DateTimeField('date published', auto_now_add=True)
    updated = models.DateTimeField('date updated', auto_now=True)
