from django.db import models

# Create your models here.
class payofpansdue(models.Model):
    bankaccount = models.CharField(max_length=50)
    bankname = models.CharField(max_length=50)
    bank = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)

    def __str__(self):
       return self.bankname



class  pancategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class section(models.Model):
      category = models.ForeignKey(pancategory, on_delete=models.CASCADE, related_name='sected', null=True, blank=True )
      year1 = models.CharField(max_length=50, null=True, blank=True)
      year2 = models.CharField(max_length=50, null=True , blank=True)
      picture = models.FileField()
      active = models.BooleanField(null=True, blank=True)
      activity = models.CharField(max_length=225)

      def __str__(self):
          return self.year1