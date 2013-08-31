LU
==

Simulation proies/prédateurs


Idées en vrac
-------------

 * langage : Caml ? C ? Python ? 
 * Serveur seulement, le client viendra plus tard 
 * Le monde est composé de listes (liste des bestioles, liste des biomes, liste des points d'eau/de nourriture, etc)
 * Zones avec différents "climats" (osef un peu des noms, chaque espèce préfère vivre dans un milieu random)
 * Différentes IA aléatoires (avec pondération d'une liste de caractères possibles pour chaque espèce)
 * Mutations aléatoires
 * Adaptation/Evolution
 * Communication au sein d'un groupe (mappage, scouting, ...)
 * Rôles de chaque individu pour une espèce de type communautaire
 * Reproduction (mating, oeufs, duplication, ...)
 * Priorité dans les actions du serveur (queue pondérée, pas de tick)
 * Représentation du monde (sphérique ? Plat avec des bords ? infini ?)
 * Actions de chaque bestiole dans une queue (pondérée ?)

Générateur de mondes
--------------------

 * Zones/biomes (chaque point a un certain pourcentage d'un climat, pas de zones délimitées)
 * Différents points de génération de biomes sont répartis sur la map de façon aléatoire, chaque point influence un certain rayon de terre autour de lui et avec une certaine force
 * Désert, Forêt, océan ...

Ressources
----------

 * deux ou trois types de ressources (nourriture, eau, matériaux (pas de détails))
 * Les bestiolles peuvent déplacer les ressources pour les donner aux autres bestiolles du même groupe


Action Queues
-------------

Il faudrait éviter le principe du "tick" qui est utilisé dans la plupart des jeux.
On peut donc se baser sur le principe des "queues".

Une queue pondérée est une liste de couples string*int, comprenant le nom de l'action et la priorité de l'action.

Les actions sont effectuées suivant leur priorité, puis dans l'ordre où elles apparaissent.
Si une action apparaît deux fois, sa priorité augmente en conséquence.


