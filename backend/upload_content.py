#!/usr/bin/env python3
"""
Script pour ajouter du contenu (projets, formations, médias) à la plateforme
Agroécologie & Permaculture
"""

import os
import sys
import requests
import json
from datetime import datetime, timedelta

API_URL = "http://localhost:5000/api"
ADMIN_EMAIL = "admin@agriculture.com"
ADMIN_PASSWORD = "admin123"

class ContentUploader:
    def __init__(self):
        self.token = None
        self.login()

    def login(self):
        """Se connecter en tant qu'admin"""
        response = requests.post(
            f"{API_URL}/auth/login",
            json={"email": ADMIN_EMAIL, "password": ADMIN_PASSWORD}
        )
        if response.status_code == 200:
            self.token = response.json()['access_token']
            print("✅ Connexion réussie!")
        else:
            print("❌ Erreur de connexion:", response.json())
            sys.exit(1)

    def get_headers(self):
        """Headers avec token JWT"""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def create_project(self, data):
        """Créer un projet/réalisation"""
        response = requests.post(
            f"{API_URL}/projects",
            json=data,
            headers=self.get_headers()
        )
        if response.status_code == 201:
            project = response.json()
            print(f"✅ Projet créé: {project['title']} (ID: {project['id']})")
            return project
        else:
            print(f"❌ Erreur création projet: {response.json()}")
            return None

    def create_training(self, data):
        """Créer une formation"""
        response = requests.post(
            f"{API_URL}/trainings",
            json=data,
            headers=self.get_headers()
        )
        if response.status_code == 201:
            training = response.json()
            print(f"✅ Formation créée: {training['title']} (ID: {training['id']})")
            return training
        else:
            print(f"❌ Erreur création formation: {response.json()}")
            return None

    def create_visit(self, data):
        """Créer une visite"""
        response = requests.post(
            f"{API_URL}/visits",
            json=data,
            headers=self.get_headers()
        )
        if response.status_code == 201:
            visit = response.json()
            print(f"✅ Visite créée: {visit['title']} (ID: {visit['id']})")
            return visit
        else:
            print(f"❌ Erreur création visite: {response.json()}")
            return None

    def upload_media(self, file_path, title=None, description=None):
        """Upload un fichier média"""
        if not os.path.exists(file_path):
            print(f"❌ Fichier non trouvé: {file_path}")
            return None

        files = {'file': open(file_path, 'rb')}
        data = {}
        if title:
            data['title'] = title
        if description:
            data['description'] = description

        headers = {"Authorization": f"Bearer {self.token}"}

        response = requests.post(
            f"{API_URL}/media/upload",
            files=files,
            data=data,
            headers=headers
        )

        if response.status_code == 201:
            media = response.json()
            print(f"✅ Média uploadé: {media['filename']} (ID: {media['id']})")
            return media
        else:
            print(f"❌ Erreur upload média: {response.json()}")
            return None


def create_sample_content():
    """Créer du contenu d'exemple"""
    uploader = ContentUploader()

    print("\n" + "="*60)
    print("📝 CRÉATION DE PROJETS D'EXEMPLE")
    print("="*60 + "\n")

    # Projet 1: Jardin Agroécologique
    project1 = uploader.create_project({
        "title": "Jardin Agroécologique de Ziguinchor",
        "slug": "jardin-agroecologique-ziguinchor",
        "description": """Ce projet pilote vise à démontrer la viabilité de l'agriculture urbaine
        en permaculture dans la région de Ziguinchor. Utilisant des techniques innovantes comme
        les buttes lasagnes, le keyhole garden et le compostage, ce jardin de 500m² produit
        des légumes biologiques tout en régénérant le sol.

        **Techniques utilisées:**
        - Buttes lasagnes en permaculture
        - Keyhole garden pour optimiser l'espace
        - Système de compostage intégré
        - Paillage permanent
        - Association de cultures

        **Résultats:**
        - Production de 200kg de légumes/mois
        - Amélioration de la fertilité du sol
        - Création de 3 emplois locaux
        - Formation de 50 personnes""",
        "short_description": "Jardin urbain en permaculture de 500m² produisant des légumes biologiques",
        "location": "Ziguinchor, Sénégal",
        "start_date": "2024-01-15",
        "end_date": "2024-06-30",
        "status": "completed",
        "featured": True,
        "surface_area": 500,
        "techniques_used": ["Buttes lasagnes", "Keyhole garden", "Compostage", "Paillage", "Associations de cultures"],
        "published": True
    })

    # Projet 2: Forêt Comestible
    project2 = uploader.create_project({
        "title": "Forêt Comestible Communautaire",
        "slug": "foret-comestible-communautaire",
        "description": """Création d'une forêt comestible sur 2 hectares, inspirée du modèle
        des food forests. Ce projet combine arbres fruitiers, plantes vivaces, légumes et
        plantes médicinales dans un système résilient et productif.

        **Objectifs:**
        - Sécurité alimentaire communautaire
        - Restauration écologique
        - Éducation environnementale
        - Génération de revenus durables

        **Espèces plantées:**
        - 140 arbres fruitiers (manguiers, anacardiers, agrumes)
        - 250 plantes vivaces
        - Plantes médicinales locales
        - Cultures maraîchères en sous-étage""",
        "short_description": "Forêt comestible de 2 hectares combinant production alimentaire et restauration écologique",
        "location": "Bignona, Casamance",
        "start_date": "2024-03-01",
        "status": "in_progress",
        "featured": True,
        "surface_area": 20000,
        "techniques_used": ["Guildes", "Succession écologique", "Agroforesterie", "Mulching"],
        "published": True
    })

    # Projet 3: Maraîchage Bio
    project3 = uploader.create_project({
        "title": "Maraîchage Biologique Intensif",
        "slug": "maraichage-bio-intensif",
        "description": """Exploitation maraîchère de 1 hectare utilisant les principes du
        maraîchage bio-intensif. Production diversifiée de légumes biologiques pour le marché
        local avec des techniques respectueuses de l'environnement.

        **Pratiques mises en œuvre:**
        - Planches permanentes surélevées
        - Rotation des cultures
        - Engrais verts
        - Préparations naturelles (purins, décoctions)
        - Gestion intégrée des ravageurs

        **Production annuelle:**
        - 15 tonnes de légumes variés
        - 50 variétés cultivées
        - 100% sans pesticides chimiques""",
        "short_description": "Maraîchage bio-intensif de 1 hectare avec production diversifiée",
        "location": "Kolda, Sénégal",
        "start_date": "2023-09-01",
        "status": "completed",
        "featured": False,
        "surface_area": 10000,
        "techniques_used": ["Bio-intensif", "Planches permanentes", "Engrais verts", "Rotation"],
        "published": True
    })

    print("\n" + "="*60)
    print("🎓 CRÉATION DE FORMATIONS D'EXEMPLE")
    print("="*60 + "\n")

    # Formation 1: Initiation Permaculture
    training1 = uploader.create_training({
        "title": "Initiation à la Permaculture",
        "slug": "initiation-permaculture",
        "description": """Formation d'introduction aux principes et techniques de la permaculture.
        Apprenez à concevoir des systèmes agricoles durables et résilients.

        **Au programme:**
        - Éthique et principes de la permaculture
        - Observation et lecture du paysage
        - Design de systèmes permaculturels
        - Gestion de l'eau
        - Sol vivant et compostage
        - Pratiques au jardin

        **Méthodes pédagogiques:**
        - Cours théoriques interactifs
        - Ateliers pratiques
        - Études de cas
        - Exercices de design
        - Visite de sites""",
        "short_description": "Découvrez les fondamentaux de la permaculture en 3 jours",
        "level": "beginner",
        "duration": 3,
        "max_participants": 20,
        "price": 75000,
        "prerequisites": "Aucun prérequis nécessaire",
        "objectives": [
            "Comprendre l'éthique et les principes de la permaculture",
            "Savoir observer et analyser un site",
            "Concevoir un jardin en permaculture simple",
            "Maîtriser les techniques de base du jardinage écologique"
        ],
        "program": {
            "Jour 1": ["Introduction à la permaculture", "Éthique et principes", "Observation du site"],
            "Jour 2": ["Design permaculturel", "Gestion de l'eau", "Sol vivant"],
            "Jour 3": ["Techniques de culture", "Atelier pratique", "Projet personnel"]
        },
        "certification": False,
        "active": True
    })

    # Formation 2: Agroforesterie
    training2 = uploader.create_training({
        "title": "Agroforesterie et Systèmes Alimentaires Résilients",
        "slug": "agroforesterie-systemes-resilients",
        "description": """Formation approfondie sur les systèmes agroforestiers et la création
        de forêts comestibles adaptées au climat sahélien.

        **Contenu:**
        - Principes de l'agroforesterie
        - Design de food forests
        - Sélection d'espèces adaptées
        - Guildes végétales
        - Gestion à long terme
        - Économie des systèmes agroforestiers

        **Cas pratiques:**
        - Visite de forêts comestibles
        - Exercices de design
        - Plantation collective
        - Planification de projet""",
        "short_description": "Maîtrisez la conception de systèmes agroforestiers productifs",
        "level": "intermediate",
        "duration": 5,
        "max_participants": 15,
        "price": 125000,
        "prerequisites": "Notions de base en agriculture ou permaculture recommandées",
        "objectives": [
            "Concevoir des systèmes agroforestiers adaptés",
            "Sélectionner les bonnes espèces",
            "Créer des guildes productives",
            "Gérer un système agroforestier dans le temps"
        ],
        "program": {
            "Jour 1-2": ["Fondamentaux agroforesterie", "Écologie forestière", "Design"],
            "Jour 3-4": ["Sélection espèces", "Guildes", "Pratique terrain"],
            "Jour 5": ["Gestion long terme", "Économie", "Projets participants"]
        },
        "certification": True,
        "active": True
    })

    print("\n" + "="*60)
    print("🚶 CRÉATION DE VISITES D'EXEMPLE")
    print("="*60 + "\n")

    # Visite 1: Jardin Démo
    visit1 = uploader.create_visit({
        "type": "guided_tour",
        "title": "Visite du Jardin Démonstratif",
        "description": """Découvrez notre jardin démonstratif en permaculture où nous expérimentons
        diverses techniques adaptées au climat local. Une visite guidée interactive pour voir
        la permaculture en action!

        **Vous découvrirez:**
        - Buttes de culture permanentes
        - Système de keyhole garden
        - Zone de compostage
        - Verger en guildes
        - Spirale aromatique
        - Système de récupération d'eau

        **Inclus:** Guide expert, livret pédagogique, dégustation de produits du jardin""",
        "duration": 2,
        "max_participants": 15,
        "price_per_person": 5000,
        "includes": ["Guide expert", "Livret pédagogique", "Dégustation"],
        "meeting_point": "Jardin de Ziguinchor, Quartier Tilène",
        "active": True
    })

    # Visite 2: Ferme Agroécologique
    visit2 = uploader.create_visit({
        "type": "farm_visit",
        "title": "Visite Immersive en Ferme Agroécologique",
        "description": """Passez une demi-journée dans une ferme agroécologique fonctionnelle.
        Participez aux activités quotidiennes et découvrez les pratiques agricoles durables.

        **Programme:**
        - Accueil et présentation de la ferme
        - Tour guidé des cultures
        - Participation aux travaux (récolte, plantation, entretien)
        - Atelier transformation de produits
        - Repas fermier bio
        - Échanges avec les agriculteurs

        **Parfait pour:** Familles, groupes scolaires, futurs agriculteurs""",
        "duration": 4,
        "max_participants": 20,
        "price_per_person": 15000,
        "includes": ["Transport depuis Ziguinchor", "Repas bio", "Activités", "Kit pédagogique"],
        "meeting_point": "Parking de la Gare Routière de Ziguinchor",
        "active": True
    })

    print("\n" + "="*60)
    print("✅ CONTENU D'EXEMPLE CRÉÉ AVEC SUCCÈS!")
    print("="*60)
    print("\nVous pouvez maintenant:")
    print("- Voir les projets: http://localhost:3000/realisations")
    print("- Voir les formations: http://localhost:3000/formations")
    print("- Contacter pour visites: http://localhost:3000/contact")


def interactive_mode():
    """Mode interactif pour ajouter du contenu"""
    uploader = ContentUploader()

    while True:
        print("\n" + "="*60)
        print("🎨 GESTION DU CONTENU - Menu Principal")
        print("="*60)
        print("\n1. Créer un projet/réalisation")
        print("2. Créer une formation")
        print("3. Créer une visite")
        print("4. Charger le contenu d'exemple")
        print("5. Quitter")

        choice = input("\nVotre choix (1-5): ").strip()

        if choice == "1":
            create_project_interactive(uploader)
        elif choice == "2":
            create_training_interactive(uploader)
        elif choice == "3":
            create_visit_interactive(uploader)
        elif choice == "4":
            create_sample_content()
        elif choice == "5":
            print("\n👋 Au revoir!")
            break
        else:
            print("❌ Choix invalide!")


def create_project_interactive(uploader):
    """Créer un projet en mode interactif"""
    print("\n📝 CRÉATION D'UN NOUVEAU PROJET\n")

    title = input("Titre du projet: ").strip()
    slug = input("Slug (URL-friendly): ").strip() or title.lower().replace(' ', '-')
    description = input("Description complète: ").strip()
    short_description = input("Description courte: ").strip()
    location = input("Localisation: ").strip()
    start_date = input("Date de début (YYYY-MM-DD): ").strip()

    data = {
        "title": title,
        "slug": slug,
        "description": description,
        "short_description": short_description,
        "location": location,
        "start_date": start_date,
        "status": "in_progress",
        "featured": False,
        "published": True
    }

    uploader.create_project(data)


def create_training_interactive(uploader):
    """Créer une formation en mode interactif"""
    print("\n🎓 CRÉATION D'UNE NOUVELLE FORMATION\n")

    title = input("Titre de la formation: ").strip()
    slug = input("Slug: ").strip() or title.lower().replace(' ', '-')
    description = input("Description: ").strip()
    short_description = input("Description courte: ").strip()
    duration = int(input("Durée (en jours): ").strip())
    price = int(input("Prix (FCFA): ").strip())

    data = {
        "title": title,
        "slug": slug,
        "description": description,
        "short_description": short_description,
        "level": "beginner",
        "duration": duration,
        "max_participants": 20,
        "price": price,
        "certification": False,
        "active": True
    }

    uploader.create_training(data)


def create_visit_interactive(uploader):
    """Créer une visite en mode interactif"""
    print("\n🚶 CRÉATION D'UNE NOUVELLE VISITE\n")

    title = input("Titre de la visite: ").strip()
    description = input("Description: ").strip()
    duration = int(input("Durée (en heures): ").strip())
    price = int(input("Prix par personne (FCFA): ").strip())
    meeting_point = input("Point de rencontre: ").strip()

    data = {
        "type": "guided_tour",
        "title": title,
        "description": description,
        "duration": duration,
        "max_participants": 15,
        "price_per_person": price,
        "meeting_point": meeting_point,
        "active": True
    }

    uploader.create_visit(data)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--sample":
        # Charger le contenu d'exemple
        create_sample_content()
    else:
        # Mode interactif
        interactive_mode()
