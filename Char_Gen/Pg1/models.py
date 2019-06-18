from django.db import models


class Character(models.Model):
    race = models.CharField(max_length=50)
    classes = models.CharField(max_length=50)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    def __str__(self):
        return f"{self.race}, {self.classes}, Str:{self.strength}, Dex:{self.dexterity}, Con:{self.constitution}, Int:{self.intelligence}, Wis:{self.wisdom}, Cha:{self.charisma}"
