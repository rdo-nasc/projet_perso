# Analyse des résultats préliminaires
## Hypothèses
1. **Longueur des Parties et le Baron Nashor.**

    On constate que la longueur des parties moyenne (gamlength) de 33 minutes et donc varie entre 27 et 38 minutes (écart-type de 6 minutes), au vu du temps de prise de premier baron (fbarontime) median de 25 minutes et de la moyenne du nombre de baron pris par parties de 1,23 pour les équipes gagnantes, 0.19 pour les équipes perdantes (teambaronkills).
    
    On en déduit que les parties se finissent généralement peu après l'apparition du deuxième baron, car le temps de réaparition du baron est de 6 minutes. On trouve ainsi 31 minutes pour l'apparition du deuxième baron ce qui est proche du temps moyen de fin de partie. Cependant un seul baron est pris par les équipes gagnantes et les équipes perdantes n'en prennent pas en moyenne. 
    
    **Hypothèse** : Le baron est un objectif à haut risque, il est donc plus judicieux de forcer un combat, dès la réaparition du baron en menaçant l'équipe adverse de la prise de l'objectif. À ce moment de la partie les temps de réappartition des joueurs après une mort sont élevés, il serait facile d'avancer dans la base adverse à 5 contre 3 ou 2 et de finir la partie.

2. **Les Adcs.**

    Le poste à qui on donne le plus de resources est le poste d'adc à 27% de gold share, suivi par mid et top à 24%. Mais la répartition des dégats (dmg share) est de 25% à égalité pour les trois postes. Cela implique que les adcs ne transitionnent pas efficacement leur ressources en dégats.

    En étudiant le pickrate des adcs, on trouve que seuls trois champions ont plus de 10% de pickrate (Xayah, Kai'sa, Ezreal), se sont tout les trois des champions dit "safe" i.e ils ont des capacités leur d'échapper a leur assaillants. Mais en contre-partie ils mettent plus longtemps à atteindre leur pics de puissance.

    **Hypothèse** : Deux solutions sont disponibles, on pourrait mettre moins de ressources sur les adcs et plus sur les tops et mids afin d'avoir une meilleure efficacité des golds engrangés. Ou, choisir des champions moins "safes" en adc et de les protéger, notamment avec des support plus adaptés.

3.  **Les Bans**

    Les 10 champions les plus bannis sont : 
    |Champions   |Banrate|Winrate (Poste)|
    |------------|---|---|
    |Pantheon    |99%|100% (Middle)|
    |Qiyana      |72%|73% (Jungle)|
    |Syndra      |55%|52% (Middle)|
    |Renekton    |51%|54% (Top)|
    |Akali       |45%|52% (Middle)|
    |Xayah       |38%|62% (ADC)|
    |LeBlanc     |37%|52% (Middle|
    |Kayle       |36%|45% (Top/Middle)|
    |Elise       |29%|50% (Jungle)|
    |Gragas      |29%|50% (Jungle)|

    **Hypothèse** : le winrate de ces champions montre qu'ils ne méritent pas tous ce traitement. Trouvons lequels peuvent être changés.

    Le cas Panthéon est délicat car il n'a été joué qu'une seule partie, a gagné et a été bannis dans toutes les autres parties de la compétition. On a donc pas assez de contexte pour évaluer sa force, mais on considérera dans la suite que le fait qu'il ai été banni aussi souvent ne soit pas anodin et Panthéon fera parti de nos bans potentiels.

    Qiyana a été jouée 11 fois en jungle pour 73% de victoire et 10 fois au mid pour 40% de victoire. Manisfestement son winrate en jungle suffit a justifer son banrate.

    Syndra a été jouée 8 fois en adc pour 25% de victoire et 21 fois en mid pour 52% de winrate, Akali a été jouée 24 fois mid pour 54% de winrate et 11 fois top pour 36% de winrate et Leblanc a été jouée 21 fois mid pour 52% de winrate .Or Ryze à 7 parties jouées en top pour 71% winrate et 29 en mid pour 59% de victoire. En tant que double menace en position à dégats Ryze a été beaucoup plus dangereux que tous les autres champions lors du tournoi. On cherchera surement a bannir Ryze dans notre cas.

    Renekton a été joué 5 fois en mid pour 40% de winrate et 28 fois top pour 54% de winrate, il est de loin le champion joué en top avec le plus de présence et n'est que deuxième au pickrate derrière Gangplank. Ce dernier a lui été joué exclusivement top, 38 fois, et a un winrate similaire a Renekton de 54%. Certains champions comme Vladimir, Ornn ou Gnar on plus de winrate mais un prerate beaucoup moins élevé. On mettra donc au même niveau de priorité Renekton et Gangplank dans la phase de ban. 
    
    Xayah est de loin l'adc le plus présent du tournoi avec un prerate de 85% , de plus elle affiche 62% de winrate ,top 3 à son poste, Elle mérite son ban.

    Kayle à déçu durant cette compétition avec 22 pick séparés equitablement entre le top et le mid et seulement 45% de victoire pour chaque poste. Son taux de ban semble être éxagéré comparé aux résultats obtenus avec elle. On voudra donc remplacer ce ban par un autre, cependant déja beaucoup de ban sont focalisés sur la midlane et la toplane.
    Les champions de support ont été moins visés par les bannissements, de notre top 10 seul Gragas a été pick en support mais comparant mais son pickrate est largement supérieur en jungle (34% contre 8%). Nautilus et Rakan, 52% et 55% de winrate respectivement avec 61% et 59% de prerate.
    Il est possible que bannir ces champions ai un impact significatif.

    Renevons en à Gragas, son winrate en jungle est de 68% avec 62% de présence il fait parti des champions forts de la compétition. Il reste donc dans la liste des champions a bannir. Le dernier champion de notre top 10 est Elise, 55% de présence et 50% de victoire, ce qui reste dans notre champs de recherche. On y ajoute cependant Lee Sin, qui lui a 59% de présence et 53% de victoire.

    On rappelle que les bans ont surtout vocation a être ciblés contre des équipes spécifiques et que la priorité a donner aux champions est aussi déterminée par ce qu'a joué par les adversaires. Nous étudions un cas général que nous avons élargi à une liste de 10 champions et la décision des 5 à bannir avant la partie sera faite en fonction de l'équipe adverse.

4. **Les Picks**

    L'équipe type d'après le pickrate serait composée ainsi:
    |Poste|Champion|Pickrate|
    |-----|--------|--------|
    |Top|Gangplank|32%|
    |Jungle|Lee Sin|48%|
    |Middle|Ryze|24%|
    |Adc|Kai'Sa|60%|
    |Support|Nautilus|40%|

    Les seconds choix seraient:
    |Poste|Champion|Pickrate|
    |-----|--------|--------|
    |Top|Renekton|24%|
    |Jungle|Gragas|34%|
    |Middle|Akali|20%|
    |Adc|Xayah|47%|
    |Support|Rakan|40%|

    On estime qu'en moyenne un mélange de ces deux équipes est présente dans les parties. Le but est de trouver des champions moins joués mais qui on eu plus de succès à hauteur de un ou deux par poste.

    **Hypothèse** :
    - **_Top_** Un Champion saute aux yeux en regardant la table des winrate top. Ornn a été pris dans 7% des parties et affiche un important 75% de winrate et que 5% de banrate. Il semble que son impact est passé inaperçu lors de la compétition.
    - **_Jungle_** Taliyah et Olaf qui sont a 67% et 60% de winrate respectivement et seulement 3% et 17% de banrate .
    - **_Middle_** Cassiopeia est notre candidat pour ce poste avec 57% de winrateet un banrate de 4%.
    - **_Adc_** Nous avons deux cas particuliers avec nos adcs, Varus est un des champions moins "safe" évoqué précédemment dans la partie "Les Adcs", mais son winrate est de 67% et son banrate est de 1%. De même Yasuo est un champion pouvant être joué a deux postes, il a un winrate de 67% en adc et 60% en mid et un ban rate de 15%.
    - **_Support_** Pour soutenir notre adc on pensera à Tahm Kench et son 71% de winrate et seulement 3% de banrate. Il fait partie des champions très protecteurs dont Varus aura besoin pour briller. Mention honorable à Morgana qui arbore un winrate de 62% et un banrate de 15%.

5. **Les Sides**

    Que ce soit coté rouge ou bleu, il ne semble pas y avoir de différence notables sur la prise d'objectifs neutres. Malgrès cela le winrate est en faveur du Blueside (52%).

    **Hypothèse** : Le seul facteur qui reste et qui soit différent pour chaque side est la phase de pick et ban, car le coté bleu a le premier pick et le coté rouge a le dernier pick. Il semblerais que l'impact du premier pick soit plus important lors de cette compétition.
    Cette hypothèse ne pourra pas être verifiée car le dataset ne contient pas d'information sur l'ordre des picks par partie.

6. **Les Objectifs**

    On a déjà évoqué le Baron Nashor mais le autres objectifs ne sont pas en reste. Les équipes ayant pris 3 dragons ont 84 % de victoire contre seulement 47% pour les équipes ayant eu 2 dragons. Le Heraut de la faille par contre ne semble pas avoir autant d'incidence sur la victoire avec 59% de winrate. Pour finir les équipes ayant pris la première tourelle ont 70% de winrate qui monte jusqu'à 81% pour les premières équipes a trois tourelles, on montre également qu'à partir de 8 tourelles prises le winrate est supérieur ou égal à 88%.

    **Hypothèse** : Le Héraut de la faille est l'objectif qui est le moins représenté dans les équipes gagnantes. Les dragons et les tourelles assurent un taux de victoire élevé dès qu'on les accumule. On priorisera donc les dragons et les tourelles dès le début de la partie avant que le deuxième Baron Nashor apparaisse.