# Budget strict : 0 CHF

Vérification documentaire : 15 octobre 2026. Les offres et conditions peuvent changer ; les URLs officielles font foi lors du lancement.

| Élément | Choix et limites |
|---|---|
| Calcul | GitHub Actions, dépôt public, runner standard Ubuntu uniquement : minutes gratuites pour les dépôts publics ; pas de promesse de capacité illimitée. Job hébergé limité à 6 heures côté service ; notre workflow s’arrête à 45 minutes. |
| Stockage | GitHub Free : 500 Mo d’artifacts partagés avec Packages ; le temps gratuit des dépôts publics ne supprime pas ce quota. Une archive est plafonnée ici à 240 Mio avant upload, conservée 1 jour. Un second rendu peut dépasser le stockage partagé : vérifier/supprimer l’ancien avant de relancer. |
| Dépôt privé | Allocation Free généralement 2000 minutes/mois et même stockage ; désactivé par ce kit pour éviter toute ambiguïté de facturation. |
| PWA | GitHub Pages, site publié max 1 Go ; bande passante souple 100 Go/mois ; limite souple de 10 constructions/heure (exception workflow personnalisé). Ne pas y stocker les films. |
| État public | API GitHub anonyme : 60 requêtes/heure/IP, partagées avec d’autres usages. Lecture seulement au clic ; erreur explicite si limite atteinte. |
| Médias | Commons : disponibilité et limitations réseau sans SLA ; cache limité au dossier du lancement ; contrôle d’empreinte avant usage. Aucune archive externe n’est garantie disponible. |
| Voix | eSpeak NG dans le runner : pas de crédit IA ni quota de caractères ; voix mécanique, limitée par le temps du runner. |
| IA | Aucun service externe IA appelé. Ni crédit de bienvenue, ni carte, ni contournement de quota, ni service de voix dont les conditions gratuites seraient incertaines. |
| YouTube | Téléversement manuel, sans API configurée. Contraintes du compte, vérifications et politiques propres à YouTube. Monétisation non garantie. |

Le premier rendu complet des deux langues a pris **2 min 16 s** sur le runner standard, installation et téléversement inclus. C’est une mesure de ce pilote, pas une garantie pour un épisode plus long ni pour une autre charge du service. L’archive finale pèse environ **134 Mo** (les WAV occupent l’essentiel du volume). Le timeout peut nécessiter une seule langue par lancement. Aucun calcul vidéo, TTS ou miniature n’est demandé au PC utilisateur. Le navigateur utilise nécessairement un peu de calcul pour afficher/éditer la page ; l’objectif réalisable est zéro calcul de production audiovisuelle sur le PC, pas zéro instruction exécutée par l’appareil.

Ne pas activer de budget de dépassement. Garder les dépenses Actions/stockage bloquées à zéro selon les contrôles de facturation du compte ; les outils fournis n’ont pas accès à ces paramètres. L’absence de dépassement autorisé peut bloquer un rendu, ce qui est préférable à une facture. Les workflows ne sont pas une garantie contractuelle du prix d’un service tiers.

Références :
- https://docs.github.com/en/billing/concepts/product-billing/github-actions
- https://docs.github.com/en/actions/reference/limits
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api
- https://support.google.com/youtube/answer/1311392

YouTube demande un apport original et authentique ; des vidéos répétitives ou produites en masse peuvent ne pas être monétisables. Les sources libres et une voix synthétique ne garantissent ni acceptation ni revenus. Le dossier original et la validation éditoriale restent essentiels.
