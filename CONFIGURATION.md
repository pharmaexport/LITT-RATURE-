# Configuration requise

Le pipeline est installé mais deux secrets GitHub doivent être ajoutés avant l’envoi vers Google Drive.

## Secrets GitHub

Dans **Settings → Secrets and variables → Actions → New repository secret** :

1. `GOOGLE_DRIVE_FOLDER_ID`
   - Valeur : `18JCSxcoZXjO3vRyIhqtDNnCXaBK5-saF`

2. `GOOGLE_SERVICE_ACCOUNT_JSON`
   - Valeur : contenu JSON complet d’un compte de service Google Cloud autorisé à écrire dans le dossier Drive.

Le dossier Drive doit être partagé avec l’adresse e-mail du compte de service en rôle **Éditeur**.

## Génération d’images

Le workflow n’invente pas une API d’images. Il assemble automatiquement toutes les images placées dans `output/pages/`, classées par nom de fichier. Une future étape de génération doit produire :

- `00_couverture.png`
- `01_page.png`
- `02_page.png`
- etc.

Sans images, le workflow génère seulement le brief et s’arrête proprement avant le PDF.

## Exécution

Le workflow `Production PDF horaire` fonctionne :

- automatiquement chaque heure ;
- manuellement depuis l’onglet **Actions** avec **Run workflow**.
