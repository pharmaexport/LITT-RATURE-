# LITT-RATURE-

Studio éditorial automatisé pour la collection **Regards au Levant**.

## Objectif

Produire régulièrement des concepts de romans graphiques LGBTQ+ en français, situés dans des contextes naturistes traités de manière artistique, contemplative et non sexualisée.

## Principes éditoriaux

- Tous les personnages sont clairement adultes.
- Chaque histoire comprend un protagoniste d’environ cinquante ans et un autre adulte sensiblement plus jeune.
- Les personnages doivent être nettement différenciés par l’âge, le visage, la silhouette, la posture et le tempérament.
- Les textes sont courts, naturels et très lisibles.
- Chaque tome adopte une direction artistique originale, sans imiter précisément un artiste vivant ou une œuvre existante.
- La couverture porte la signature graphique constante **J.-H. Hogan**.
- Le livrable final visé est un PDF optimisé pour tablette.

## Structure

- `briefs/` : briefs éditoriaux générés automatiquement.
- `scripts/` : scripts de génération et d’assemblage.
- `output/` : PDF et éléments finaux.
- `.github/workflows/` : automatisation GitHub Actions.

## Limite actuelle

Le workflow fourni génère automatiquement un brief éditorial horaire. Pour générer des images et assembler un PDF sans intervention, il faut ajouter un service d’images accessible par API ainsi qu’un mécanisme d’authentification Google Drive. Ces éléments doivent être configurés dans les secrets GitHub du dépôt.
