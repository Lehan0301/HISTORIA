# Architecture de production

```mermaid
flowchart LR
    A[Atelier PWA sur GitHub Pages] -->|Export JSON, puis édition web| B[Dépôt public HISTORIA]
    B -->|Lancement manuel authentifié| C[GitHub Actions Ubuntu standard]
    D[Commons : média CC0 fixé par empreinte] --> C
    C --> E[eSpeak NG : voix FR et EN]
    C --> F[Schémas et miniatures originaux]
    E --> G[FFmpeg : deux films 720p]
    F --> G
    G --> H[Contrôles de durée et décodage]
    H --> I[Archive temporaire 24 h]
    I --> J[Visionnage et écoute]
    J --> K[YouTube Studio : publication manuelle]
```

La PWA ne dispose d’aucun serveur de rendu, clé API ni accès d’écriture GitHub. L’état est lu au clic via l’API publique ; le lancement et l’édition se font dans GitHub, sous l’authentification existante. Ce choix réduit les prérequis et évite de confier un jeton d’accès au navigateur.

Le calcul audiovisuel, la création des PNG/JPEG, la synthèse vocale et les contrôles FFmpeg tournent sur le runner cloud. L’appareil sert à afficher l’atelier, transférer les textes et télécharger/regarder les résultats. Le montage reste un documentaire explicatif à schémas et images fixes, avec mouvement discret ; pas de génération vidéo cinématique.

Les sources et médias sont sélectionnés éditorialement avant le montage. Le pipeline n’effectue aucune recherche autonome non vérifiée et ne remplace pas une image indisponible par une autre aux droits inconnus. Aucun service d’IA externe n’est requis. Une voix neuronale ne pourra être ajoutée qu’après vérification de sa disponibilité gratuite et de ses conditions d’usage.

Échecs bloquants : source JSON incohérente, empreinte média modifiée, licence inattendue, texte hors cadre, erreur de synthèse ou d’encodage, résolution/durée invalide, échec du décodage, sortie >240 Mio. Le job ne téléverse les résultats que si l’ensemble de ces étapes réussit.
