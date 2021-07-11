from django.db import models

# Create your models here.

class Tracking_item(models.Model):
    username = models.TextField()
    tracking_item_id = models.CharField(max_length=8)
    tracking_item_name = models.TextField()
    data_type = models.IntegerField()

    def __str__(self):
        return '{}_{}_{}_{}'.format(self.username, self.tracking_item_id, self.tracking_item_name, self.data_type)

class Tracker(models.Model):
    username = models.TextField()
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=2)
    day = models.CharField(max_length=2)
    tracking_item_id = models.CharField(max_length=8)
    tracking_value = models.TextField()
    tracking_items = models.ForeignKey(Tracking_item, on_delete=models.CASCADE)

    def __str__(self):
        return '{}_{}_{}_{}_{}_{}_{}'.format(self.username, self.year, self.month, self.day, self.tracking_item_id, self.tracking_value, self.tracking_items)
