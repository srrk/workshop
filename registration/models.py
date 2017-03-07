from django.db import models

class users(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    reg_date = models.DateField(auto_now_add=False)
    birthdate = models.DateField()
    group = models.CharField(max_length=50)
    slot = models.CharField(max_length=50)

    def __str__(self):
        return self.name
