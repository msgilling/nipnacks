from django.db import models

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=500)
    pot = models.ForeignKey("pots.Pot", on_delete=models.CASCADE)
  

    def __str__(self):
        return f'{self.text}'