#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nom : backup.py
Auteur : Valentin
Date : 26/11/2026

Description :
    Ce script permet de sauvegarder un dossier vers un répertoire
    de destination en ajoutant un horodatage.

Fonctionnalités :
    - Copie d'un dossier spécifié.
    - Création d'une sauvegarde horodatée.
    - Gestion des erreurs.
    - Journalisation des opérations.
    - Notification de sauvegarde (simulation email).
"""

# Importation des bibliothèques
import os
import shutil
import logging
import argparse

from datetime import datetime
from pathlib import Path



def create_backup(source_dir, backup_dir):
    """
    Effectue une sauvegarde horodatée d'un dossier.

    Args:
        source_dir : dossier à sauvegarder.
        backup_dir : répertoire de destination.

    Returns:
        Le chemin de la sauvegarde créée.
    """

    # Vérification du dossier source
    if not source_dir.exists():
        raise FileNotFoundError("Le dossier source n'existe pas.")

    if not source_dir.is_dir():
        raise NotADirectoryError("La source n'est pas un dossier.")

    # Création du répertoire de sauvegarde
    backup_dir.mkdir(parents=True, exist_ok=True)

    # Génération de l'horodatage
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Création du nom de la sauvegarde
    backup_path = backup_dir / f"{source_dir.name}_{timestamp}"
    
    logging.info(f"Début de la sauvegarde : {source_dir}")

    # Copie du dossier
    shutil.copytree(source_dir, backup_path)
    
    logging.info(f"Sauvegarde réussie : {backup_path}")

    return backup_path



def setup_logging():
    """
    Configure le système de journalisation du script.
    Les événements sont enregistrés dans logs/backup.log.
    """

    # Détermination du chemin du fichier de log
    project_dir = Path(__file__).resolve().parent.parent
    log_dir = project_dir / "logs"

    # Création du dossier logs s'il n'existe pas
    log_dir.mkdir(parents=True, exist_ok=True)

    log_file = log_dir / "backup.log"

    # Configuration de la journalisation
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
    

def send_notification(backup_path, recipient):
    """
    Simule l'envoi d'une notification par email après une sauvegarde.
    """
    subject = "Sauvegarde terminée avec succès"
    message = f"La sauvegarde a été créée ici : {backup_path}"

    print("\n--- Notification email ---")
    print(f"Destinataire : {recipient}")
    print(f"Objet : {subject}")
    print(f"Message : {message}")
    print("--------------------------\n")

    logging.info("Notification email simulée envoyée à %s", recipient)    
    
    
    


def main():
    """
    Programme principal du script de sauvegarde.
    Récupère les paramètres et lance la sauvegarde.
    """

    # Création des arguments du programme
    parser = argparse.ArgumentParser(
        description="Outil de sauvegarde automatique de dossiers."
    )

    parser.add_argument(
        "source",
        type=Path,
        help="Chemin du dossier à sauvegarder."
    )

    parser.add_argument(
        "destination",
        type=Path,
        help="Chemin du répertoire de sauvegarde."
    )
    
    parser.add_argument(
    "--email",
    default="administrateur@example.com",
    help="Adresse email du destinataire de la notification."
    )
    
    

    # Récupération des arguments
    args = parser.parse_args()

    # Configuration des logs
    setup_logging()

    try:
        # Lancement de la sauvegarde
        backup_path = create_backup(args.source, args.destination)

        print(f"[SUCCES] Sauvegarde créée : {backup_path}")
        send_notification(backup_path, args.email)

    except (OSError, shutil.Error) as error:
        logging.exception("Échec de la sauvegarde.")
        print(f"[ERREUR] La sauvegarde a échoué : {error}")
        return 1

    return 0


# Point d'entrée du programme
if __name__ == "__main__":
    exit(main())
