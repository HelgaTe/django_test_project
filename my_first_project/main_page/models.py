from django.db import models
import uuid 
import os

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

    def __iter__(self):
        for item in self.dishes.all():
            yield item


class Dish(models.Model):
    def get_file_name(self, file_name): #set correct file name - to be sure that server will accept and return data correctly
        extention = file_name.strip().split('.')[-1] #get extantion from upload file (.jpeg, etc)
        new_file_name =f'{uuid.uuid4()}.{extention}' #generate new name for the current file
        return os.path.join('dishes/dishes/%Y_%m_%d/',new_file_name)

    title = models.CharField(max_length=50, unique=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    ingridients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='dishes/%Y_%m_%d',blank=True) #save images to folder named "dishes" -> subfolder "upload date"
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes') 
    # category connection with category, define connection type (1<>1, 1<>many, many<>many) 
    is_special = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'

class Meta:
    ordering = ('category', 'posistion') 