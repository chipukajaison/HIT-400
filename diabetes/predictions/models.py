from django.db import models


class Patient(models.Model):
    pregnancies = models.DecimalField(max_digits=400, decimal_places=4)
    glucose  = models.DecimalField(max_digits=400, decimal_places=4)
    blood_pressure  = models.DecimalField(max_digits=400, decimal_places=4)
    skin_thickness = models.DecimalField(max_digits=400, decimal_places=4)
    insulin = models.DecimalField(max_digits=400, decimal_places=4)
    BMI  = models.DecimalField(max_digits=400, decimal_places=4)
    diabetes_pedigree_function = models.DecimalField(max_digits=400, decimal_places=4)
    age = models.DecimalField(max_digits=400, decimal_places=4)
    result = models.TextField(max_length=200, null=True, default=None)

    def get_absolute_url(self):
        return f'/prediction/new-record'

    def __str__(self):
        return f'{self.result}'
