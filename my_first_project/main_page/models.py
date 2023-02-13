from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

# add def __str__ to name category name visible for admin managemnt tools 
    def __str__(self) -> str:
        return f'{self.title}'

class Meta: # settings for selecting data
    ordering = ('position',)
    # ordering = ('position-',) # add <-> minus to sort in reverse



class Dish(models.Model):
    title = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingridients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    # category connection with category, define connection type (1<>1, 1<>many, many<>many) 
    is_special = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'

class Meta:
    ordering = ('category', 'posistion')