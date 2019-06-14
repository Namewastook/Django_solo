from django.db import models


class Races(models.Model):
    dwarf = models.CharField(max_length=30),
    elf = models.CharField(max_length=30),
    halfelf = models.CharField(max_length=30),
    halforc = models.CharField(max_length=30),
    halfling = models.CharField(max_length=30),
    human = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Classes(models.Model):
    cleric = models.CharField(max_length=30),
    fighter = models.CharField(max_length=30),
    rogue = models.CharField(max_length=30),
    wizard = models.CharField(max_length=30)

    def __str__(self):
        return self.name
