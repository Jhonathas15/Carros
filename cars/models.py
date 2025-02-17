from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'

class Car(models.Model):

    id = models.AutoField(primary_key=True)
    # Modelo
    model = models.CharField(max_length=200)
    # Marca
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    # Ano_fabricação
    factory_year = models.IntegerField(blank=True, null=True) 
    # Modelo_ano
    model_year = models.IntegerField(blank=True, null=True)
    # Placa
    plate = models.CharField(max_length=10, blank=True, null=True)
    # Valor
    value = models.FloatField(blank=True, null=True)
    # Imgs
    photo = models.ImageField(upload_to='cars/', blank=False, null=False)

    bio = models.TextField(blank=True, null=True)
    def __str__(self) -> str:
        return f'{self.model}'


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'