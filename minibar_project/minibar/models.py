from django.db import models

class Room(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return f'Room {self.number}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Sale(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f'{self.room}'
