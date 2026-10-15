# État de validation

État préparatoire au 15 octobre 2026 ; sera actualisé après un éventuel lancement cloud.

## Réalisé

- Lecture de la conversation de référence : pas de fichiers récupérables joints ; le projet est préparé à partir de la demande actuelle.
- Consultation des sources institutionnelles du Parc de Pompéi et de l’INGV, et des pages officielles GitHub sur la gratuité et les limites.
- Lecture de la fiche CC0 du média choisi, auteur, date, révision et empreinte relevés. Le fichier image sera récupéré et revérifié dans le cloud, il n’est pas prétendu téléchargé ou contrôlé visuellement ici.
- Relecture du dossier, des 8 scènes FR/EN, des liens scène → source et du code de rendu.
- Interface écrite avec champs étiquetés, grille adaptative, état de chargement/erreur, stockage de brouillon tolérant aux restrictions, aucun token dans le navigateur.
- Compte GitHub accessible via connecteur ; création de dépôt indisponible dans ce connecteur. Navigation vers GitHub/new : session navigateur non connectée, connexion utilisateur indispensable.

## Préparé mais pas encore exécuté

- Tests de cohérence JSON et sources, syntaxe Python et JavaScript, présence des ressources PWA, garde de runner et timeout.
- Synthèse eSpeak FR/EN, récupération média avec empreinte et contrôle de licence, création images/miniatures, encodage FFmpeg, inspection ffprobe, décodage complet et borne d’archive.
- Déploiement HTTPS Pages, installation PWA, test réel mobile et hors ligne.

Le code et sa relecture ne prouvent pas qu’un montage est terminé. Aucun MP4, WAV, JPEG final ou résultat de test cloud n’est revendiqué tant que le workflow ne fournit pas un lancement réussi et son rapport.

## Limites connues

- Voix mécanique, pas d’évaluation d’écoute sans WAV produit.
- SRT proportionnels, pas d’alignement phonétique.
- Un seul média photographique, plusieurs schémas : variété limitée, esthétique de documentaire explicatif sobre plutôt que reconstitution cinématographique.
- Interface partiellement bilingue : scripts et introduction FR/EN, administration FR.
- Aucun appel d’IA gratuite non vérifiée ; pas de publication ni d’identification de compte YouTube.
- Coût des services tiers soumis aux conditions du compte ; impossibilité de certifier ses budgets sans accès à ses réglages.
