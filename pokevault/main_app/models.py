from django.db import models
from django.urls import reverse

class Card(models.Model):
    name = models.CharField(max_length=100)
    set_name = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return f"A card named {self.name} from the {self.set_name} set."
    
    def get_absolute_url(self):
        return reverse('card-detail', kwargs={'pk': self.id})

CONDITIONS = (
    ('M', 'Mint'),
    ('NM', 'Near Mint'),
    ('EX', 'Excellent'),
    ('G', 'Good'),
    ('P', 'Poor'),
)

class Condition(models.Model):
    date = models.DateField("Date Logged")
    grade = models.CharField(
        verbose_name="Condition:",
        max_length=2,
        choices=CONDITIONS,
        default=CONDITIONS[0][0]
    )
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='conditions')

    def __str__(self):
        return f"{self.get_grade_display()} on {self.date}"