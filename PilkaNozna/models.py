'''
Kamil Jarmoc, Jan Kucharski

'''
from django.db import models

# Create your models here.
class Liga(models.Model):
    id_ligi = models.AutoField(primary_key = True)
    nazwa_ligi = models.TextField()
    class Meta:
        verbose_name_plural = "Liga"

    def __str__(self):
        return self.nazwa_ligi

class Pozycja(models.Model):
    id_pozycji = models.AutoField(primary_key=True)
    nazwa_pozycji = models.TextField()
    class Meta:
        verbose_name_plural = "Pozycja"

    def __str__(self):
        return self.nazwa_pozycji

class Klub(models.Model):
    id_klubu = models.AutoField(primary_key = True)
    id_ligi = models.ForeignKey(Liga, on_delete = models.CASCADE)
    nazwa_klubu = models.TextField()

    class Meta:
        verbose_name_plural = "Klub"

    def __str__(self):
        return self.nazwa_klubu

class Pilkarz(models.Model):
    id_pilkarza = models.AutoField(primary_key = True)
    imie = models.TextField()
    nazwisko = models.TextField()
    data_urodzenia = models.DateField()
    id_klubu = models.ForeignKey(Klub, on_delete = models.CASCADE)
    id_pozycji = models.ForeignKey(Pozycja, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "Piłkarz"

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Mecz(models.Model):
    id_meczu = models.AutoField(primary_key = True)
    id_klubu1 = models.ForeignKey(Klub, on_delete = models.CASCADE, related_name="Klub_1")
    id_klubu2 = models.ForeignKey(Klub, on_delete = models.CASCADE, related_name="Klub_2")
    kolejka = models.IntegerField()
    data_meczu = models.DateField()

    class Meta:
        verbose_name_plural = "Mecz"

    def __str__(self):
        return self.id_meczu

class Statystyki_gracza(models.Model):
    id_statystyki = models.AutoField(primary_key = True, default = 0)
    id_pilkarza = models.ForeignKey(Pilkarz, on_delete = models.CASCADE)
    id_meczu = models.ForeignKey(Mecz, on_delete = models.CASCADE)
    gole = models.IntegerField(default = 0)
    asysty = models.IntegerField(default = 0)
    faule = models.IntegerField(default = 0)
    zolta = models.IntegerField(default = 0)
    czerwona = models.IntegerField(default = 0)

    class Meta:
        verbose_name_plural = "Statystyki"

    def __str__(self):
        return "{} {}".format(self.id_pilkarza, self.gole)
