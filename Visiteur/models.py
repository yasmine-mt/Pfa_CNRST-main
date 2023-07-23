from django.db import models
from auditlog.models import AuditlogHistoryField


class Visiteur(models.Model):
    TYPE_CHOICES = (
        ('Universitaire', 'Universitaire'),
        ('Administratif', 'Administratif'),
        ('Commercial', 'Commercial')
    )

    CIN = models.CharField(max_length=200, unique=True, null=True)
    Type = models.CharField(max_length=200, null=True, choices=TYPE_CHOICES)
    Prenom_v = models.CharField(max_length=200, null=True)
    Nom_V = models.CharField(max_length=200, null=True)
    history = AuditlogHistoryField()  # Champ pour stocker l'historique des modifications
    def __str__(self):
        return self.Nom_V
