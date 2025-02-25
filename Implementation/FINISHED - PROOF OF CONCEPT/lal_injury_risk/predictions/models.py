from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    avg_minutes = models.FloatField()
    avg_field_goals = models.FloatField()
    injuries_last_3_years = models.IntegerField(default=0)
    total_injuries = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculate_risk(self):
        """Calculate injury risk based on injuries, age, and workload."""
        risk_score = 0

        # Increase risk based on past injuries
        if self.injuries_last_3_years >= 11:
            risk_score += 3
        elif 4 <= self.injuries_last_3_years <= 10:
            risk_score += 2
        else:
            risk_score += 1

        # Increase risk for older players
        if self.age >= 35:
            risk_score += 2
        elif 30 <= self.age < 35:
            risk_score += 1

        # Increase risk for high workload
        if self.avg_minutes >= 35:
            risk_score += 2
        elif 30 <= self.avg_minutes < 35:
            risk_score += 1

        # Increase risk if shooting a lot
        if self.avg_field_goals >= 200:
            risk_score += 2

        # Determine final risk category
        if risk_score >= 6:
            return "High"
        elif risk_score >= 4:
            return "Medium"
        else:
            return "Low"

    @property
    def predicted_risk(self):
        return self.calculate_risk()

    def __str__(self):
        return f"{self.name} - {self.predicted_risk} (Injury Risk)"
