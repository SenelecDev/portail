from django.contrib import admin
from .models import Client, Facture, Coupure

@admin.register(Client)

class ClientAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('nom_complet', 'numero_compteur', 'telephone', 'type_abonnement', 'actif')
    # Filtres dans la barre latérale
    list_filter = ('type_abonnement', 'actif', 'date_inscription')
    # Champs pour la recherche
    search_fields = ('nom_complet', 'numero_compteur', 'telephone', 'email')
    # Champs modifiables directement dans la liste
    list_editable = ('actif',)

    # Organisation par date
    date_hierarchy = 'date_inscription'

@admin.register(Facture)

class FactureAdmin(admin.ModelAdmin):
    list_display = ('numero_facture', 'client', 'periode', 'montant', 'statut', 'date_echeance')
    list_filter = ('statut', 'date_emission', 'date_echeance')
    search_fields = ('numero_facture', 'client__nom_complet')
    list_editable = ('statut',)
    date_hierarchy = 'date_emission'
    
    # Organisation des champs dans le formulaire
    fieldsets = (
        ('Informations Client', {
        'fields': ('client',)
        }),
        
        ('Détails Facture', {
        'fields': ('numero_facture', 'periode', 'montant')
        }),
        
        ('Dates', {
        'fields': ('date_emission', 'date_echeance', 'date_paiement')
        }),
        
        ('Statut', {
        'fields': ('statut',)
        }),
    )

@admin.register(Coupure)

class CoupureAdmin(admin.ModelAdmin):
    list_display = ('zone', 'date_coupure', 'duree_estimee', 'type_coupure', 'terminee')
    list_filter = ('type_coupure', 'terminee', 'date_coupure')
    search_fields = ('zone', 'raison')
    list_editable = ('terminee',)
    date_hierarchy = 'date_coupure'