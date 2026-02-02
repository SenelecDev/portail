from django.shortcuts import render, get_object_or_404
from .models import Client, Coupure, Facture

# Vue pour la page d'accueil
def accueil(request):
    return render(request, "accueil.html")

# Vue pour la page des services
def services(request):
    
# Liste des services SENELEC
    data = [
        {"nom": "Raccordement Électrique", "icon": "🔌"},
        {"nom": "Dépannage 24/7", "icon": "🔧"},
        {"nom": "Compteurs Intelligents", "icon": "📊"},
    ]
    return render(request, "services.html", {"services": data})

# Vue pour la page contact
def contact(request):
    
    # Informations de contact SENELEC
    info = {
    "tel": "800 00 93 93",
    "urgence": "800 00 41 41"
    }
    return render(request, "contact.html", {"info": info})

#Vue pour la page zones
def zones(request):
    zones_list = [
           {"nom": "Dakar", "population": "3.8M"},
           {"nom": "Thiès", "population": "2M"},
           {"nom": "Saint-Louis", "population": "1.2M"},
       ]
    return render(request, "zones.html", {"zones": zones_list})

def liste_clients(request):
    # Récupérer tous les clients actifs
    clients = Client.objects.filter(actif=True)

    context = {
    'clients': clients,
    'total': clients.count(),
    }
    return render(request, "liste_clients.html", context)

def detail_client(request, client_id):
    
    # Récupérer le client ou erreur 404
    client = get_object_or_404(Client, id=client_id)
    # Récupérer toutes les factures du client
    factures = client.factures.all()
    context = {
    'client': client,
    'factures': factures,
    }
    return render(request, "detail_client.html", context)

def liste_coupures(request):
    # Coupures à venir (non terminées)
    coupures_futures = Coupure.objects.filter(terminee=False)
    context = {
    'coupures': coupures_futures,
    }
    return render(request, "liste_coupures.html", context)