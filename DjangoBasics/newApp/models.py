from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES =[
        ("BL", "Black"),
        ("GR", "Green"),
        ("OO", "Oolong"),
        ("WH", "White"),
        ("HE", "Herbal"),
        ("CH", "Chai"),
    ]
    name = models.CharField(max_length=100),
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default="CH")