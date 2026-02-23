from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    set_name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"A card named {self.name} from the {self.set_name} set."