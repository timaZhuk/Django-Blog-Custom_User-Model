from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug

#-------Create your models here----------.
class Post(models.Model):
    # stored in DB
    ACTIVE = 'active'
    DRAFT = 'draft'
# we can see in Admin interface
    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    #field in Db for status
    status = models.CharField(max_length = 10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to = 'uploads/',blank=True, null=True)
 
    class Meta:
        ordering=('-created_at',)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

#-----Model for comments----------------
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = ('Comments')

    def __str__(self):
        return self.name
