from django import forms
from .models import Reclamation, Client


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['client', 'sujet', 'description','piece_jointe']
        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'
            }),
            'sujet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Facture incorrecte',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Décrivez votre réclamation en détail...',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'
            }),
                'piece_jointe': forms.FileInput(attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 5px;'
            }),

        }
        labels = {
            'client': 'Sélectionnez votre compte client',
            'sujet': 'Sujet de la réclamation',
            'description': 'Description détaillée',
            'piece_jointe': 'Pièce jointe (optionnel)',
        }
