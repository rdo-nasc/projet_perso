# Analyse des Worlds 2019 de League Of Legends

Pour mon projet de fin de formation j'ai choisi d'analyser le Championnat du Monde de League Of Legends édition 2019. Cette compétition a pris place en Europe en passant par Berlin, Madrid, sa finale se déroulant à Paris dans l'enceinte de L'Accor Hotel Arena. 

J'ai voulu un jeu de données dans un domaine où j'ai des connaissances assez larges pour donner un sens concret aux résultats obtenus. Cela me permet par la même occasion de traiter un sujet atypique, pour ceux qui ne connaissent pas ou peu le monde du jeu video compétitif. 

L'analyse des données de ce genre de compétitions permet de dégager les tendances générales des stratégies employées, montrer l'évolution de celles-ci au cours du tournoi et nous donne même une idée des points de vue des équipes sur ces statégies. Ces analyses sont utilisées dans les ligues régionales pour determiner quelles stratégies mettre en place contre les adversaires de la semaine. Je note également que cela est également valable dans les sports traditionnels.

De plus ce type d'études élargies à tous les joueurs du jeu, permet à l'éditeur de mettre en place plusieurs directions allant de l'équilibrage futur du jeu aux stratégies économiques mises en place (Un champion trop fort verra sûrement ces caractéristiques baissées,Un champion très joué est plus susceptible d'être mis en avant pour la vente des objets de personalisations payants).

Voici donc un sommaire de l'analyse.

## Analyse globale de la compétition
### Statistiques globales
    - Longueur de partie moyenne, partie la plus longue, partie la plus courte.
    - Gold diff (10 min, 15 min, fin de la partie).
    - Creep score (10 min , 15 min) / poste, CS diff / poste.
    - Xp diff / poste .
    - Stats (KDA, Dmg share, Gold share, Golds/minutes, Wards share) / poste.
### Champions
    - Les champions les plus Picks/Bans.
    - Les champions avec le plus haut/bas winrate.
### Side
    - Winrate.
    - Longueur de la partie.
    - Gold diff (10 min, 15min, fin de la partie).
    - Nombre d'objectifs neutres.
### Objectifs
    - Dragons : nombre/game, temps de prise du premier dragon,% de chaque élément, winrate par combinaison d'éléments.
    - Héraut de la faille : nombre par game, temps de prise de l'Héraut, winrate des équipes ayant pris le Héraut.
    - Baron Nashor : nombre par game, temps de prise du premier Nashor, winrate en fonction du nombre de Nashors pris et du temps de prise du premier Nashor.
    - Dragon Ancestral : nombre par game, winrate en fonction du nombre de Dragon Ancestraux pris.
    - Winrate (par nombre de tourelles prises, par nombre de premières tourelles, par temps de premières tourelles.

### Conclusion
De par ces statistiques on pourra définir quels champions il valait mieux bannir, quelle type de composition d'équipe a été la meilleure durant ce tournoi, quel coté de la carte était-il judicieux de choisir et enfin quels sont les objectifs qu'il fallait prioriser lors d'une partie.

**Source dataset: Télechargé sur https://oracleselixir.com/match-data/** 