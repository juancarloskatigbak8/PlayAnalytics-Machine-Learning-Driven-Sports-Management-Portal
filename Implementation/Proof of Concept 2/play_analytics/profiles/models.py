from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()
    avg_minutes = models.FloatField()
    avg_fg_attempts = models.FloatField()
    steals = models.FloatField()
    blocks = models.FloatField()
    fouls = models.FloatField()
    total_injuries = models.IntegerField()
    predicted_risk = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='player_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='journal_entries')
    date = models.DateField()
    title = models.CharField(max_length=200)
    note = models.TextField()