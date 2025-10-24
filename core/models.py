from django.db import models




class Ruc(models.Model):
    document = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    code  =  models.CharField(max_length=20)
    key = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.code} - {self.name}'
    
    
    
class ChargeRuc(models.Model):
    name_arc = models.CharField(max_length=255)
    date_charge = models.DateTimeField(auto_now_add=True)
    record = models.PositiveIntegerField()
    
    def __str__(self):
        return f'{self.name_arc} - {self.date_charge.strftime("%Y-%m-%d %H:%M:%S")}'    