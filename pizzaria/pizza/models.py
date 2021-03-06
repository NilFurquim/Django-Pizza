from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    ingridients = models.TextField()
    picture = models.ImageField(blank=True, null=True)

    def __unicode__(self):
	   return 'Pizza de {}'.format(self.name)

    def __repr__(self):
        return unicode(self)