# HISTORIA — pilote Pompéi et atelier web

Projet bilingue FR/EN, sans Higgsfield, avec rendu exécuté dans GitHub Actions sur CPU standard gratuit. Site : https://lehan0301.github.io/HISTORIA/ . Dépôt : https://github.com/Lehan0301/HISTORIA . L’état réel des essais est décrit dans `docs/VALIDATION.md`.

- `episode.json` : voix off intégrales FR et EN, 8 scènes et liens aux sources.
- `sources.json`, `media.json` : références et registre du média CC0.
- `docs/CONCEPT.md`, `RECHERCHE.md`, `STORYBOARD.md`, `DROITS.md` : dossier éditorial.
- `site/` : interface responsive, éditeur bilingue, export, lecture de statut GitHub et PWA.
- `scripts/render.py` : synthèse vocale libre, dessins, FFmpeg, MP4, WAV, SRT, miniature et description par langue. Exécution cloud seulement.
- `.github/workflows/render.yml` : contrôles et rendu à la demande, archive 24 h.
- `.github/workflows/pages.yml` : préparation et déploiement de la PWA, à la demande.
- `docs/DEPLOIEMENT.md`, `QUOTAS.md` : lancement depuis navigateur et limites du budget.

Le fichier JSON racine est l’unique référence du montage. Le workflow Pages copie les données dans `site/` et génère ses icônes PNG. Les fichiers finaux sont rendus dans le cloud ; aucun encodage ou TTS n’est exécuté sur le PC. Les scripts sont aussi fournis en Markdown dans `docs/`.

Le dépôt et Pages ont été créés et configurés après connexion GitHub par l’utilisateur. Un test court bilingue et un rendu complet ont réussi. Pour une nouvelle version : modifier le JSON racine dans GitHub puis lancer le workflow Render. Aucun compte nouveau ni publication YouTube réalisés. Voix mécanique eSpeak ; SRT approximatifs à contrôler à l’écoute. L’archive Actions est conservée 24 heures, les livrables téléchargés dans cette conversation restent des fichiers indépendants.
