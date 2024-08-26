from email.mime import image
from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField

# abc.com/category/beyaz-esya = beyaz-esya bir slugdır.
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
        
    #kategori isimlerinin blog işlemi gibi yapılması için
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True, unique=True,db_index=True,editable=False) #editable=false olursa bu özellik editlenemez
    categories = models.ManyToManyField(Category, blank=True)
    #kategoriye ait blog yazıları silinmesin istyorsak  on_delete=models.SET_NULL dersek sadece kategori silinir.Blog yazılarımızın bir kategorisi olmaz. ancak bunun için null=True olması gerekir
    
    #admin panelindeki blogların isimlendirilmesi blog1 değil python yazması için başlık isimlendirme
    def __str__(self): 
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

