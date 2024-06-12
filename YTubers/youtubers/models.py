from django.db import models
#from ckeditor.fields import RichTextField
# Create your models here.

class Youtuber(models.Model):

    crew_choses = (
        ('solo','solo'),
        ('small','small'),
        ('larger','large')
    )

    camera_choses = (
        ('canon','canon'),
        ('nikon','nikon'),
        ('sony','sony'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('others','others'),
    )

    category_choses = (
        ('code','code'),
        ('mobile_review','mobile_review'),
        ('vlogs','vlogs'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('movie_review','movie_review'),
        ('cooking','cooking'),
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    age = models.IntegerField()
    video_url = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField()
    #description = RichTextField()
    photo = models.ImageField(upload_to='media/youtuber/%Y/%m/')
    height = models.IntegerField()
    crew = models.CharField(max_length=255,choices=crew_choses)
    camera_type = models.CharField(max_length=255,choices=camera_choses)
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255,choices=category_choses)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name