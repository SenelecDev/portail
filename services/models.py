from django.db import models

class Client(models.Model):
    
    # Informations personnelles
    nom_complet = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(blank=True) # Optionnel
    adresse = models.TextField()
    
    # Informations du compteur
    numero_compteur = models.CharField(max_length=20, unique=True)
    type_abonnement = models.CharField(
        max_length=20,
        choices=[
        ('RESIDENTIEL', 'Résidentiel'),
        ('COMMERCIAL', 'Commercial'),
        ('INDUSTRIEL', 'Industriel'),
        ],
        default='RESIDENTIEL'
    )
    
    # Métadonnées
    date_inscription = models.DateTimeField(auto_now_add=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['nom_complet'] # Tri par nom
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def __str__(self):
        return f"{self.nom_complet} - {self.numero_compteur}"

class Facture(models.Model):
    
    # Relation avec Client
    client = models.ForeignKey(
    Client,
    on_delete=models.CASCADE,
    related_name='factures'
    )
    
    # Informations de facturation
    numero_facture = models.CharField(max_length=20, unique=True)

    periode = models.CharField(max_length=20) # Ex: "Janvier 2025"
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Statut de paiement
    statut = models.CharField(
    max_length=20,
    choices=[
        ('IMPAYEE', 'Impayée'),
        ('PAYEE', 'Payée'),
        ('PARTIELLE', 'Paiement partiel'),
        ],
        default='IMPAYEE'
    )
    
    # Dates
    date_emission = models.DateField()
    date_echeance = models.DateField()
    date_paiement = models.DateField(blank=True, null=True)
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_emission'] # Plus récentes en premier
        verbose_name = "Facture"
        verbose_name_plural = "Factures"
    
    def __str__(self):
        return f"Facture {self.numero_facture} - {self.client.nom_complet}"

class Coupure(models.Model):
    # Zone concernée
    zone = models.CharField(max_length=100)
    # Date et heure
    date_coupure = models.DateTimeField()
    duree_estimee = models.IntegerField(help_text="Durée en minutes")
    # Raison
    raison = models.TextField()
    type_coupure = models.CharField(
    max_length=20,
    choices=[
    ('MAINTENANCE', 'Maintenance programmée'),
    ('PANNE', 'Panne technique'),
    ('TRAVAUX', 'Travaux'),
    ]
    )
    # Statut
    terminee = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_coupure']
        verbose_name = "Coupure"
        verbose_name_plural = "Coupures"
        
    def __str__(self):
        return f"Coupure {self.zone} - {self.date_coupure.strftime('%d/%m/%Y')}"
    

class Reclamation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='reclamations')
    sujet = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
    max_length=20,
    choices=[

    ('OUVERTE', 'Ouverte'),
    ('EN_COURS', 'En cours de traitement'),
    ('RESOLUE', 'Résolue'),
    ],
    default='OUVERTE'
    )
    
    # Nouveau champ pour l'upload
    piece_jointe = models.FileField(upload_to='reclamations/', blank=True, null=True)


    class Meta:
        ordering = ['-date_creation']
    def __str__(self):
        return f"{self.sujet} - {self.client.nom_complet}"