from django.db import models


class Character(models.Model):
    race = models.CharField(max_length=50)
    classes = models.CharField(max_length=50)
    strength = models.CharField(max_length=50)
    dexterity = models.CharField(max_length=50)
    constitution = models.CharField(max_length=50)
    intelligence = models.CharField(max_length=50)
    wisdom = models.CharField(max_length=50)
    charisma = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.race}, {self.classes}, Str:{self.strength}, Dex:{self.dexterity}, Con:{self.constitution}, Int:{self.intelligence}, Wis:{self.wisdom}, Cha:{self.charisma}"
