from django.db import models
from Laboratoire.models import Laboratoire
from auditlog.models import AuditlogHistoryField
class Equipement(models.Model):
    ETAT_CHOICES = (
        ('Installé', 'Installé'),
        ('en panne', 'En panne'),
        ('Fonctionnel', 'Fonctionnel')
    )
    Reference = models.CharField(max_length=200, unique=True, null=True)
    Etat = models.CharField(max_length=200, null=True, choices=ETAT_CHOICES)
    Date_Acquisition = models.DateField(auto_now_add=True)
    Marque = models.CharField(max_length=200, null=True)
    Laboratoire = models.ForeignKey(Laboratoire, on_delete=models.CASCADE)
    history = AuditlogHistoryField()  # Champ pour stocker l'historique des modifications
  
    def __str__(self):
        return self.Reference
