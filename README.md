# TP - Bilan DevOps

Mise en place de script d'automatisation pour la sauvegarde, monitoring et la rotation des logs avec différents languages.

## Script BASH - Monitoring Disque
**monitoring_disque.sh** permet d'afficher l'espace disque, alerte si un seuil critique est atteint (80%), un log (alerte_disque.log) est aussi créé.

### Exemple d'éxécution

```bash
chmod +x monitoring_disque.sh
./monitoring_disque.sh
```

### Exemple de sortie attendu

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G  6.1G  950G   1% /
*2026-11-26 09:14:40 - OK : Disque à 1% (seuil max : 80%)
```
### Vérification des logs

```bash
cat /var/log/alerte_disque.log
```

## Script PYTHON - Backup
**backup.py** permet de sauvegarder un dossier spécifié vers un répertoire de sauvegarde, gestion des erreurs, et envoi d'un email.





## Script BASH - Gestion Log
**log_rotate.sh** permet de trier les logs d'un dossier donné, supprime les logs vieux de plus de X jours ou au-delà d'une certaine taille.
