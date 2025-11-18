import debogue_moi
import pytest
#Référence Jeu_Bingo travail d'equipe avec Wilona

def test_ajouter_apres_dernier():
    #Arrange
    nom = "Amélie"
    temps = 45
    #Act
    confirmation = ajouter_apres_dernier(calendrier, nom, temps)
    #Assert
    assert "Rendez-vous confirmer à" in confirmation

def test_ajouter_apres_dernier_duree_minimal(calendrier):
    #Arrange
    nom = "Hakim"
    temps = "15"
    #Act
    confirmation = ajouter_apres_dernier(calendrier,nom,temps)
    #Assert
    assert "Rendez-vous confimer à " in confirmation

