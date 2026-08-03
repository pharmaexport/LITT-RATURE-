from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

STYLES = [
    "aquarelle méditerranéenne lumineuse",
    "encre noire expressionniste avec lavis",
    "ligne claire contemporaine et cinématographique",
    "pastel sec aux contrastes doux",
    "réalisme pictural aux ombres chaudes",
    "gravure moderne à palette limitée",
]

LOCATIONS = [
    "Île du Levant",
    "Cap d’Agde",
    "Euronat",
    "Montalivet",
    "Charco del Palo",
    "Vera Playa",
]


def main() -> None:
    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y-%m-%d_%H-%M")
    idx = int(now.timestamp() // 3600)
    style = STYLES[idx % len(STYLES)]
    location = LOCATIONS[idx % len(LOCATIONS)]

    content = f"""# Brief horaire — {stamp} UTC

## Cible
Adultes francophones intéressés par les romances LGBTQ+ sensibles, les récits contemplatifs et les lieux naturistes.

## Personnages
- Protagoniste A : homme de 50 à 57 ans, visage marqué, présence calme, posture assurée.
- Protagoniste B : adulte de 27 à 35 ans, silhouette et tempérament nettement différents.
- Relation équilibrée, consentie, non explicite.

## Lieu
{location}.

## Direction artistique
{style}.

## Contraintes
- Naturisme présenté comme cadre de vie, sans sexualisation.
- Aucun acte sexuel ni posture suggestive.
- Narration par les regards, silences, micro-expressions, lumière et paysage.
- Dialogues courts, entièrement en français, très lisibles.
- Couverture signée « J.-H. Hogan ».
- Livrable final visé : PDF avec couverture et pagination.

## Trame proposée
1. Une rencontre visuelle lente dans un espace ouvert sur le paysage.
2. Une séparation brève qui crée l’attente.
3. Une rencontre fortuite le lendemain.
4. Un échange simple qui révèle la différence d’âge et de tempérament sans déséquilibre.
5. Une fin ouverte donnant envie de lire le tome suivant.
"""

    out_dir = Path("briefs")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"brief_{stamp}.md").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
