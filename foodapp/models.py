from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    
    class Meta():
         ordering=('name',)
         verbose_name='category'
         verbose_name_plural="categories"
    def __str__(self) :
         return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
    
    #def get_url(self):
     #    return reverse('prod_cat',args=[self.slug])

     

class product(models.Model):
     name=models.CharField(max_length=250,unique=True)
     slug=models.SlugField(max_length=250,unique=True)
     img=models.ImageField(upload_to='product')
     desc=models.TextField()
     stock=models.IntegerField()
     available=models.BinaryField()
     price=models.IntegerField()
     category=models.ForeignKey(categ,on_delete=models.CASCADE)
    
     

     def __str__(self):
          return '{}'.format(self.name)
     def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])
     
     def you(self):
        return reverse('items',args=[self.name])
     
     
     
class cartlist(models.Model):
   cartid=models.CharField(max_length=250,unique=True)
   date_added=models.DateTimeField(auto_now_add=True)

   def __str__(self):
          return '{}'.format(self.cartid)
   
class items(models.Model):
     prdt=models.ForeignKey(product,on_delete=models.CASCADE)
     cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
     quantity=models.IntegerField()  

     def __str__(self) :
          return '{}'.format(self.prdt)
     
     def totaltotal(self):

      return self.prdt.price*self.quantity
      
     

   

