from django.db import models

# Create your models here.
class Feedback_new(models.Model):
    name_m = models.CharField(max_length=32)
    text_m = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)

    def _str_(self):
        return (f'{self.name_m} + {self.text_m}')

class Author(models.Model):
    name = models.CharField(max_length=32)
    email =  models.CharField(max_length=50)
    webpage = models.CharField(max_length=50)

    def __str__(self):
        return f'Author{self.name}'


class Subject(models.Model):
    name_subject =  models.CharField(max_length=32)
    name_bot = models.CharField(max_length=32)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    author = models.ForeignKey(Author, null=True, on_delete=models.PROTECT)
                               #    on_delete=models.CASCADE)
                               #    default='unknown'
    # def __str__(sels):
    #     return f'Bot{self.name_subject}'

