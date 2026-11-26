#!/bin/bash

# Monitoring - Espace de Stockage

log="/var/log/alerte_disque.log"

# Déclaration d'un seuil en pourcentage
seuilmax_disque=80

# Affiche l'espace du disque principal
df -h /

# Vérification du seuil
verif_seuil=$(df --output=pcent / | tail -1 | tr -dc '0-9')

if [ "$verif_seuil" -ge "$seuilmax_disque" ]; then

	alerte_disque="$(date '+%Y-%m-%d %H:%M:%S') - Alerte CRITIQUE : Disque à ${verif_seuil}% (seuil max : ${seuilmax_disque}%)"
else
	alerte_disque="$(date '+%Y-%m-%d %H:%M:%S') - OK : Disque à ${verif_seuil}% (seuil max : ${seuilmax_disque}%)"

# Affichage de l'alerte dans le fichier log
	echo "$alerte_disque" | sudo tee -a "$log"
fi

