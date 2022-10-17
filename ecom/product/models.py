

from django.db import models
from base.models import basemodel
from django.utils.text import slugify



class Category(basemodel):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True , null=True ,blank=True)
    category_image= models.ImageField(upload_to="categories")

    

    def save(self , *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category , self).save(*args , **kwargs)

    def __str__(self) -> str:
        return self.category_name

class ColorVariant(basemodel):
    color_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.color_name

class SizeVariant(basemodel):
    size_name=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.size_name




class Product(basemodel):
    product_name=models.CharField(max_length=100)
    slug= models.SlugField(unique=True , null=True , blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE ,related_name='Products' , null=True , blank=True)
    price = models.IntegerField()
    product_discription= models.TextField()
    color_varient= models.ManyToManyField(ColorVariant , blank=True  )
    size_variant=models.ManyToManyField(SizeVariant , blank=True )



    def save(self ,*args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product , self).save(*args , *kwargs)

    def __str__(self) -> str:
        return self.product_name





class ProductImage(basemodel):
    product= models.ForeignKey(Product , on_delete=models.CASCADE , related_name='Product_image')
    image = models.ImageField(upload_to='Product')
    