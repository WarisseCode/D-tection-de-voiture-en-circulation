# Détection-de-voiture-en-circulation

## Description
Système de reconnaissance automatique de plaques d'immatriculation (ANPR) utilisant YOLOv10 et PaddleOCR.

## Fonctionnalités
- Détection de véhicules en temps réel
- Reconnaissance de plaques d'immatriculation
- Sauvegarde des données en JSON et base de données SQLite
- Interface de traitement vidéo

## Installation
```bash
pip install ultralytics paddleocr opencv-python numpy sqlite3
```

## Utilisation
1. Placez vos vidéos dans le dossier `Resources/`
2. Exécutez `python anpr.py` pour le traitement en temps réel
3. Exécutez `python sqldatabase.py` pour initialiser la base de données

## Structure du projet
- `anpr.py` - Script principal de détection
- `sqldatabase.py` - Configuration de la base de données
- `ANPR_YOLOv10.ipynb` - Notebook Jupyter pour l'entraînement
- `weights/` - Modèles pré-entraînés
- `Resources/` - Vidéos et images de test
