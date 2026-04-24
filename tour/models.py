from django.db import models

# Create your models here.

#user profile
class userprofile(models.Model):
    name=models.CharField(max_length=100, null=True)
    email=models.EmailField()
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    d_name=models.CharField(max_length=100)
    d_state=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='destination/')
    def __str__(self):
        return self.d_name
    
class Package(models.Model):
    destination=models.ForeignKey(Destination, on_delete=models.CASCADE)
    p_name=models.CharField(max_length=100)
    p_price=models.FloatField()
    p_details=models.TextField()
    duration=models.CharField(max_length=50)
    hotel=models.CharField(max_length=100)
    is_popular = models.BooleanField(default=False)
    def __str__(self):
        return self.p_name
    
class booking(models.Model):
    name=models.ForeignKey(userprofile, on_delete=models.CASCADE)
    package=models.ForeignKey(Package, on_delete=models.CASCADE,related_name='+')
    hotel=models.ForeignKey(Package, on_delete=models.CASCADE,related_name='+')
    checkin=models.DateField()
    checkout=models.DateField()
    def __str__(self):
        return self.name
