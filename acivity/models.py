from django.db import models


# Create your models here.
class RecentActivity(models.Model):
    picture = models.ImageField(upload_to='article/',verbose_name='picture')
    title = models.CharField(verbose_name='title', max_length=100, unique=True)
    date = models.DateTimeField(verbose_name='Day of publication')

    def __str__(self):
        return f'{self.picture}, {self.title}, {self.date}'