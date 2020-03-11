# Analyse des résultats préliminaires
## Hypothèses
1. **Longueur des Parties et le Baron Nashor.**

    On constate que la longueur des parties moyenne (gamlength)de 33 minutes et donc varie entre 27 et 38 minutes (écart-type de 6 minutes), au vu du temps de prise de premier baron (fbarontime) median de 25 minutes et de la moyenne du nombre de baron pris par parties de 1,23 pour les équipes gagnantes, 0.19 pour les équipes perdantes (teambaronkills).
    
    On en déduit que les parties se finissent généralement peu après l'apparition du deuxième baron, car le temps de réaparition du baron est de 6 minutes. On trouve ainsi 31 minutes pour l'apparition du deuxième baron ce qui est proche du temps moyen de fin de partie. Cependant un seul baron est pris par les équipes gagnantes et les équipes perdantes n'en prennent pas en moyenne. 
    
    Hypothèse : Le baron est un objectif à haut risque, il est donc plus judicieux de forcer un combat, dès la réaparition du baron en menaçant l'équipe adverse de la prise de l'objectif. À ce moment de la partie les temps de réappartition des joueurs après une mort sont élevés, il serait facile d'avancer dans la base adverse à 5 contre 3 ou 2 et de finir la partie.

2. **Les Adcs.**

    Le poste à qui on donne le plus de resources est le poste d'adc à 27% de gold share, suivi par mid et top à 24%. Mais la répartition des dégats (dmg share) est de 25% à égalité pour les trois postes. Cela implique que les adcs ne transitionnent pas efficacement leur ressources en dégats.

    En étudiant le pickrate des adcs, on trouve que seuls trois champions ont plus de 10% de pickrate (Xayah, Kai'sa, Ezreal), se sont tout les trois des champions dit "safe" i.e ils ont des capacités leur d'échapper a leur assaillants. Mais en contre-partie ils mettent plus longtemps à atteindre leur pics de puissance.

    Hypothèse : Deux solutions sont disponibles, on pourrait mettre moins de ressources sur les adcs et plus sur les tops et mids afin d'avoir une meilleure efficacité des golds engrangés. Ou, choisir des champions moins "safes" en adc et de les protéger, notamment avec des support plus adaptés.

3.  **Les Bans**

    Les 10 champions les plus bannis sont : 
    |Champions   |Banrate|
    |------------|---|
    |Pantheon    |99%|
    |Qiyana      |72%|
    |Syndra      |55%|
    |Renekton    |51%|
    |Akali       |45%|
    |Xayah       |38%|
    |LeBlanc     |37%|
    |Kayle       |36%|
    |Elise       |29%|
    |Gragas      |29%|

    Hypothèse : le winrate de ces champions montre qu'ils ne méritent pas tous ce traitement. Trouvons lequels peuvent être changés.

    Le cas Panthéon est délicat car il n'a été joué qu'une seule partie, a gagné et a été bannis dans toutes les autres parties de la compétition. On a donc pas assez de contexte pour évaluer sa force, mais on considérera dans la suite que le fait qu'il ai été banni aussi souvent ne soit pas anodin et Panthéon fera parti de nos bans potentiels.

    Qiyana a été jouée 11 fois en jungle pour 73% de victoire et 10 fois au mid pour 40% de victoire. Manisfestement son winrate en jungle suffit a justifer son banrate.

    Syndra a été jouée 8 fois en adc pour 25% de victoire et 21 fois en mid pour 52% de winrate, or Ryze à 7 parties jouées en top pour 71% winrate et 29 en mid pour 59% de victoire. En tant que double menace en position à dégats Ryze a été beaucoup plus dangereux que Syndra lors du tournoi.
    
     