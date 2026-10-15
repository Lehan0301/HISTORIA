# Voix de la version 2 — vérification du 15 octobre 2026

Synthèse Piper 1.8.0 sur CPU GitHub Actions uniquement, sans API payante, jeton ou calcul audio local.

- FR : fr_FR-tom-medium, Tom Darboux / Tjiho. Fiche : https://huggingface.co/rhasspy/piper-voices/blob/main/fr/fr_FR/tom/medium/MODEL_CARD ; licence AGPLv3. Modèle et sources correspondantes : https://git.bksp.space/Tjiho/French-tts-model-piper . Modèle utilisé sans modification, non redistribué dans les livrables. Aucune interface publique de synthèse hébergée.
- EN : en_US-ljspeech-high. Fiche : https://huggingface.co/rhasspy/piper-voices/blob/main/en/en_US/ljspeech/high/MODEL_CARD ; entraîné depuis zéro sur LJ Speech, données déclarées domaine public aux États-Unis. Linda Johnson / Keith Ito : https://keithito.com/LJ-Speech-Dataset/ . La portée du domaine public peut varier selon le pays.
- Piper : GPL-3.0-or-later, https://github.com/OHF-Voice/piper1-gpl . L'installation se fait depuis PyPI ; le logiciel et les modèles gardent leurs licences propres, distinctes de la licence Apache du projet.

Révision des modèles figée dans scripts/speech.py. Chaque rendu conserve les fiches et empreintes SHA256 des fichiers réellement téléchargés. Les empreintes sont des preuves de provenance, pas une validation indépendante du contenu.

Siwis et UPMC n'ont pas été sélectionnés : leurs fiches mentionnent un ajustement de Lessac, dont les données renvoient à une licence de recherche. Cela ne constitue pas une conclusion juridique sur tous les modèles dérivés.

Les sous-titres sont produits à partir de passages de 76 caractères maximum, synthétisés séparément. Leurs bornes sont mesurées sur les échantillons PCM, avec une pause de 120 ms entre passages. Pas d'alignement mot à mot. Les pauses et prononciations restent à apprécier à l'écoute. Aucun enregistrement d'une personne n'est présenté comme sa participation au documentaire.
