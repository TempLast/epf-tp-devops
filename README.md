# <img width="512" height="512" alt="devops_logo_1" src="https://github.com/user-attachments/assets/0a4adb20-8e01-4942-a88a-f3a6a2c767ac" /> TP - Bilan DevOps

Mise en place de script d'automatisation pour la sauvegarde, monitoring et la rotation des logs.

## Script BASH - Monitoring Disque
monitoring_disque.sh permet d'afficher l'espace disque, alerte si un seuil critique est atteint (80%), un log (alerte_disque.log) est aussi créé.

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


