# HISTORIA — pilote Pompéi et atelier web

Projet bilingue FR/EN, sans Higgsfield, conçu pour un rendu cloud sans service payant. **Les scripts et le code sont préparés ; un fichier source n’est pas une vidéo produite.** L’état réel des essais est décrit dans `docs/VALIDATION.md`.

- `episode.json` : voix off intégrales FR et EN, 8 scènes et liens aux sources.
- `sources.json`, `media.json` : références et registre du média CC0.
- `docs/CONCEPT.md`, `RECHERCHE.md`, `STORYBOARD.md`, `DROITS.md` : dossier éditorial.
- `site/` : interface responsive, éditeur bilingue, export, lecture de statut GitHub et PWA.
- `scripts/render.py` : synthèse vocale libre, dessins, FFmpeg, MP4, WAV, SRT, miniature et description par langue. Exécution cloud seulement.
- `.github/workflows/render.yml` : contrôles et rendu à la demande, archive 24 h.
- `.github/workflows/pages.yml` : préparation et déploiement de la PWA, à la demande.
- `docs/DEPLOIEMENT.md`, `QUOTAS.md` : lancement depuis navigateur et limites du budget.

Le fichier JSON racine est l’unique référence du montage. Le workflow Pages copie les données dans `site/` et génère ses icônes PNG. Les scripts lisibles Markdown et les fichiers finaux sont préparés dans le cloud ; ils ne sont pas rendus sur le PC.

Première action de mise en service : fournir ce contenu à un dépôt public, configurer Pages sur GitHub Actions, puis lancer un test court. Aucun compte créé ni publication YouTube réalisée par le kit.
