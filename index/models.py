from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.


# class  CustomUser(AbstractUser):
#     username = models.CharField(_('username'), max_length=20, unique=True)
#     number = models.CharField(_('number'), max_length=11, blank=True)
#     description = models.TextField(_('description'))
#     # profile = models.FileField(_('profile'))
    

#     USERNAME_FIELD = 'address'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username 




class Category(models.Model):
    name = models.CharField(max_length=225)


    def __str__(self):
        return self.name



class POST(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.FileField()
    Title = models.CharField(max_length=225)
    Authors = models.CharField(max_length=225)
    body = models.TextField()
    Description = models.TextField()
    Date_post = models.DateTimeField()
    tage = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.Title 

    def get_absolute_url(self):
        return reverse('index:blog_details', kwargs={'pk': self.pk})    

class Level(models.Model):
      level = models.CharField(max_length=10, unique=True)
      article = models.CharField(max_length=50)
      article2 = models.CharField(max_length=50)
      article3 = models.CharField(max_length=50)

      def __str__(self):
          return self.level


class Course(models.Model):         
      name = models.CharField(max_length=225)
      level = models.ForeignKey(Level, on_delete=models.CASCADE)
      image = models.FileField()

      def __str__(self):
          return self.name


class  UploadFiles(models.Model):
    # category_choices = (
    #     ('pdf', 'pdf'),
    #     ('video', 'video'),
    #     ('image', 'image'),
    # )
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=100)
    video = models.TextField(null=True, blank=True)
    pdf = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    #category = models.CharField(max_length=10, choices=category_choices)

    def __str__(self):
        return self.name    



class ExamCountdown(models.Model):
    Title = models.CharField(max_length=225)
    when = models.DateTimeField()

    def __str__(self):
        return self.Title

        

    

class Information(models.Model):
    information_title = models.CharField(max_length=225)
    information_description = models.TextField()
    information_body = models.TextField()


    def __str__(self):
        return self.information_title



class Categoryshop(models.Model):
    name = models.CharField(max_length=100)
    ordring = models.IntegerField(default=0)


    def __str__(self):
        return self.name        



class ShopIteam(models.Model):
    category = models.ForeignKey(Categoryshop,  related_name='shops', on_delete=models.CASCADE)
    title =  models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=50)
    price = models.FloatField()
    discount_price = models.CharField(null=True, blank=True, max_length=50)
    phone_number = models.CharField(max_length=225)
    Active = models.BooleanField(default=True)
    image = models.FileField()
    picture = models.FileField(null=True , blank=True)
    picture2 = models.FileField(null=True , blank=True) 
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title   


class Exco(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    image = models.FileField()


    def __str__(self):
        return self.name



class accommodationcategory(models.Model):
    name = models.CharField(max_length=50)



class Accommodation(models.Model):
    category = models.ForeignKey(accommodationcategory, related_name='accomo', on_delete=models.CASCADE , blank=True,  null=True)
    Hostel =  models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=225)
    price = models.FloatField()
    discount_price = models.CharField(null=True, blank=True, max_length=50)
    phone_number = models.CharField(max_length=225)
    Active = models.BooleanField(default=True)
    image = models.FileField()
    picture = models.FileField(null=True , blank=True)
    picture2 = models.FileField(null=True , blank=True) 
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Hostel





