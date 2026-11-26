# TP - Bilan DevOps

<img width="625" height="320" alt="devops_logo" src="https://github.com/user-attachments/assets/122f5b7a-bbcf-4eb4-8b18-4516d642aad0" />

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


