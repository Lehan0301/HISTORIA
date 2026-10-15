# État de validation

État au 15 octobre 2026 ; résultats cloud effectivement observés ci-dessous.

## Résultats exécutés

- Dépôt public créé : https://github.com/Lehan0301/HISTORIA ; code initial déposé au commit `d37677d3cd53ca2915f79720483b34024d52b608`.
- Vérification des fichiers JSON : 5 fichiers valides, 8 scènes dans chaque langue et toutes les références présentes ; 715 mots FR, 632 mots EN.
- Test cloud FR/EN réussi : https://github.com/Lehan0301/HISTORIA/actions/runs/38704976291 ; durée du lancement 39 s. Cinq tests Python réussis, syntaxe JS acceptée, deux MP4 de 8 s produits, inspection et décodage FFmpeg réussis, archive 17,4 Mo.
- La récupération Commons, le contrôle CC0 et la comparaison SHA-1 ont réussi dans ce test ; aucun remplacement automatique de média.
- Déploiement Pages réussi en 48 s : https://github.com/Lehan0301/HISTORIA/actions/runs/38705040798 . Site : https://lehan0301.github.io/HISTORIA/ .
- Vérification navigateur : chargement des 8 scènes, bascule FR/EN, configuration du dépôt et lecture de l’état réel d’Actions. Contrôle visuel à largeur 390 px et sur écran de bureau : navigation et introduction lisibles, sans débordement visible.
- Premier rendu complet réussi : https://github.com/Lehan0301/HISTORIA/actions/runs/38705120796 . FR 267,36 s ; EN 286,48 s ; inspection et décodage complets réussis. Archive 133 884 635 octets ; SHA-256 `0ec181c43d2e3dfc28f40f55693b42ebb2acf9403a1cf2d2c8c509801cc64b42` vérifiée après téléchargement.
- Inspection des images et des miniatures : légendes et sources lisibles ; amélioration décidée pour conserver les sauts de ligne du carton final et distinguer par la couleur le corps de la cavité. Nouveau rendu requis pour ces retouches.
- Export du JSON testé dans le navigateur : téléchargement obtenu. L’export n’envoie pas les modifications au dépôt automatiquement.

## Réalisé

- Lecture de la conversation de référence : pas de fichiers récupérables joints ; le projet est préparé à partir de la demande actuelle.
- Consultation des sources institutionnelles du Parc de Pompéi et de l’INGV, et des pages officielles GitHub sur la gratuité et les limites.
- Lecture de la fiche CC0 du média choisi, auteur, date, révision et empreinte relevés. Le fichier image sera récupéré et revérifié dans le cloud, il n’est pas prétendu téléchargé ou contrôlé visuellement ici.
- Relecture du dossier, des 8 scènes FR/EN, des liens scène → source et du code de rendu.
- Interface écrite avec champs étiquetés, grille adaptative, état de chargement/erreur, stockage de brouillon tolérant aux restrictions, aucun token dans le navigateur.
- Compte GitHub accessible via connecteur ; création du dépôt par navigateur après connexion réalisée par l’utilisateur.

## Restant à confirmer

- Rendu des retouches de mise en page et contrôle des images concernées.
- Évaluation d’écoute des voix et ajustement fin des sous-titres.
- Installation PWA sur un appareil réel et test hors ligne. Les ressources PWA sont présentes ; une capture à largeur mobile ne prouve pas l’installation sur iOS/Android.

Le rendu complet est distinct du test court. La révision finale doit être identifiée par son propre lancement après les retouches de mise en page.

## Limites connues

- Voix mécanique, pas d’évaluation d’écoute sans WAV produit.
- SRT proportionnels, pas d’alignement phonétique.
- Un seul média photographique, plusieurs schémas : variété limitée, esthétique de documentaire explicatif sobre plutôt que reconstitution cinématographique.
- Interface partiellement bilingue : scripts et introduction FR/EN, administration FR.
- Aucun appel d’IA gratuite non vérifiée ; pas de publication ni d’identification de compte YouTube.
- Coût des services tiers soumis aux conditions du compte ; impossibilité de certifier ses budgets sans accès à ses réglages.
