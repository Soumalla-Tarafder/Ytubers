from django.db import models

class hiretuber(models.Model):
    
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=255)
    user_id = models.IntegerField(blank=True)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    phone = models.IntegerField()
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
