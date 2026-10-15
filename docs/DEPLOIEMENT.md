# Déployer sans installer de logiciel ni encoder sur votre ordinateur

## GitHub, depuis le navigateur

1. Utiliser un compte GitHub existant et un **dépôt public** nommé `HISTORIA`. Ne pas activer de runner payant, service IA ou budget de dépassement. La connexion à un compte peut faire l’objet de contrôles GitHub ; aucune méthode ne garantit l’accès gratuit si le service bloque le compte.
2. Placer **le contenu** du dossier HISTORIA à la racine du dépôt, dont `.github/workflows/`. L’archive seule n’est pas exécutée par GitHub. Le transfert de fichiers et l’affichage web utilisent votre appareil ; le rendu reste dans le cloud.
3. Settings → Pages → Source : **GitHub Actions**. Un administrateur du dépôt doit parfois activer cette option. Dans Actions, activer les workflows si GitHub le demande.
4. Actions → **Deploy HISTORIA PWA** → Run workflow. Le lien de déploiement apparaît dans le lancement. Pour un dépôt de projet, il sera normalement `https://Lehan0301.github.io/HISTORIA/`, à confirmer avec le résultat du déploiement.
5. Actions → **Render HISTORIA (cloud)** → sélectionner `both`, d’abord `smoke=true` pour deux extraits de 8 secondes, puis `smoke=false` pour les épisodes complets. Chaque lancement doit être demandé explicitement ; aucune boucle ni planification installée.
6. Ouvrir le lancement terminé et télécharger son artifact dans les **24 heures**. Il contient les MP4 FR/EN, WAV de narration, SRT, miniatures JPEG, descriptions, frises minutées, images de chaque scène, sources, métadonnées Commons et rapport de décodage. Les WAV proviennent de la piste AAC du film final, donc ne sont pas des masters audio sans perte de génération.
7. Écouter les deux voix, contrôler les chiffres, regarder les schémas, vérifier les temps des sous-titres. Les noms propres peuvent nécessiter une adaptation phonétique. Lire les limites dans DROITS.md. La qualité eSpeak est intelligible mais mécanique ; ce premier rendu doit être traité comme un pilote à évaluer.
8. Après validation, publier manuellement dans YouTube Studio. Choisir la langue de chaque vidéo, ajouter SRT, miniature et description correspondants. Ajouter aux playlists FR/EN. Vérifier les paramètres d’audience et les demandes de déclaration de contenu synthétique selon la vidéo et la politique courante. Aucun accès YouTube ni téléversement automatique n’est configuré.

## Utiliser l’atelier PWA

Ouvrir l’URL HTTPS, puis « Installer l’application » si le navigateur le propose, ou « Ajouter à l’écran d’accueil » sur iOS. Les icônes PNG sont préparées sur GitHub ; elles ne sont pas pré-calculées localement. Installer et vérifier le mode hors ligne après le premier chargement réussi. Les pages et scripts sont mis en cache ; l’état GitHub nécessite Internet.

Le bouton FR/EN change l’introduction et la langue du script ; les commandes d’administration restent en français. La PWA n’est donc pas une traduction complète de toute l’interface. Les scripts sont éditables et enregistrés localement si le navigateur l’autorise. Exporter `episode.json`, puis remplacer le fichier **à la racine** du dépôt via l’éditeur web GitHub avant de relancer le rendu. L’interface n’envoie aucun token et ne déclenche pas directement Actions : « Ouvrir les rendus » ouvre le workflow authentifié dans GitHub. État du dernier lancement lu via API publique, sans simulation de progression.

Après modification du script, relancer Pages pour mettre à jour le dossier affiché. Conserver ou exporter son brouillon avant d’utiliser « Restaurer ». Le service worker utilise le réseau en priorité et le cache en secours.

## Ajouter un épisode

Ce kit produit le pilote Pompéi, pas un générateur universel. Pour un nouvel épisode : créer une branche dans GitHub ; remplacer texte, sources, médias et visuels ; refaire la validation de droits et des faits ; adapter `render.py` si de nouveaux types de plans sont requis ; lancer les tests puis le rendu. Ne pas supprimer les sources pour faire passer un script non vérifié.

## Dépannage

- `Media hash changed` ou `Media license changed` : comparer la fiche Commons au registre ; ne pas contourner le contrôle par une recherche automatique non vérifiée.
- HTTP 429/503 : quota ou indisponibilité temporaire, réessayer plus tard. Le rendu s’arrête après quatre tentatives réseau ; il n’invente pas un fichier de remplacement.
- Workflow non visible : `.github/workflows/*.yml` doit être sur la branche par défaut.
- Pages 404 : vérifier Source = GitHub Actions et le lancement de déploiement.
- Job sauté : dépôt privé ; la garde 0 CHF bloque volontairement cette configuration.
- Stockage plein : télécharger et supprimer les anciens artifacts depuis GitHub. Pas d’ajout de carte ni de dépassement payant requis.
- Dépassement de 45 min ou archive >240 Mio : raccourcir le pilote ou réduire l’encodage, pas de runner plus coûteux.

L’administration et le transfert manuel restent possibles sur téléphone/tablette, mais l’upload des fichiers source initiaux est plus simple une fois le dépôt fourni par l’agent.
