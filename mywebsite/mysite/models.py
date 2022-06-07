from django.db import models

# Create your models here.


class Venture(models.Model):
    v_id = models.BigIntegerField(primary_key=True)
    v_address = models.CharField(max_length=20)
    v_growth = models.CharField(max_length=20)
    v_employ = models.CharField(max_length=20)
    v_sep = models.CharField(max_length=20)
    v_predict = models.BigIntegerField()
    v_doctor = models.BigIntegerField()
    v_master = models.BigIntegerField()
    v_bachelor = models.BigIntegerField()
    v_college = models.BigIntegerField()
    v_high = models.BigIntegerField()
    v_region = models.CharField(max_length=50)
    v_field = models.CharField(max_length=50)

    def __str__(self):
        return self.name
