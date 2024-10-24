from django.db import models

# Create your models here.
from django.db import models

class Rule(models.Model):
    rule_string = models.TextField()  # Store the rule as text
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the rule was created

    def __str__(self):
        return self.rule_string
