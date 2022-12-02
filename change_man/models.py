from django.conf import settings
from django.db import models
from django.utils import timezone


class Entry(models.Model):

    date_of_change = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    NETWORK = '01'
    PRINTING = '02'
    DHCP = '03'
    GOOGLE_ADMIN = '04'
    CATEGORY_CHOICES = [
        (NETWORK, 'Network'),
        (PRINTING, 'Printing'),
        (DHCP, 'Dhcp'),
        (GOOGLE_ADMIN, 'Google Admin'),
    ]

    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=NETWORK,
    )

    def is_upperclass(self):
        return self.category in {self.NETWORK, self.PRINTING}
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title