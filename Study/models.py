from django.db import models
from index.models import Level
# Create your models here.

class Textbook(models.Model):
    name = models.CharField(max_length=50)
    image = models.FileField()

    def __str__(self):
        return self.name
    
    
class SemesterCategory(models.Model):
    semester = models.CharField(max_length=70)
    def __str__(self):
        return self.semester


class StudyCourse(models.Model):         
      name = models.CharField(max_length=225)
      level = models.ForeignKey(Level, on_delete=models.CASCADE)
      description = models.TextField(default='')
    #   image = models.FileField()
      def __str__(self):
          return self.name


class Study(models.Model):
    course = models.ForeignKey(StudyCourse, on_delete=models.CASCADE)
    semester = models.ForeignKey(SemesterCategory, on_delete=models.CASCADE, related_name='semest')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    course_material = models.URLField(null=True, blank=True)
    past_Question = models.URLField(null=True, blank=True)
    video_refence = models.URLField(null=True, blank=True)
    Useful_link  = models.URLField(null=True, blank=True)
    General_assessment = models.URLField(null=True, blank=True)
    Topic_assessment = models.URLField(null=True, blank=True)
    Other_material = models.URLField(null=True, blank=True)
    Old_material = models.URLField(null=True, blank=True) 


    def __str__(self):
        return self.Old_material     
    
    
      
class Tutor(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    topic = models.CharField(max_length=200, help_text="Topic you want to be tutor on")
    course = models.CharField(max_length=200, help_text="Course")
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tutor Me"

    def __str__(self):
        return self.name + "-" +  self.topic      