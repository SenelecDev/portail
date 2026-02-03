from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
    path("zones/", views.zones, name="zones"),
    path("clients/", views.liste_clients, name="liste_clients"),
    path("clients/<int:client_id>/", views.detail_client, name="detail_client"),
    path("coupures/", views.liste_coupures, name="coupures"),
    
    # Formulaire de réclamation
    path("reclamation/", views.soumettre_reclamation, name="soumettre_reclamation"),
    path("reclamation/confirmation/", views.confirmation_reclamation, name="confirmation_reclamation"),

]