# Projet Théorie des Graphes
Recherche de chemin de valeur minimale par l’algorithme de Floyd-Warshall

## IMPORTANT
**Lisez bien l’intégralité de ce document avant de commencer à travailler. Cela vous évitera de
mauvaises surprises.**

L’algorithme de Floyd-Warshall permet de calculer les chemins de valeurs minimales de tout sommet à tout autre
sommet dans un graphe orienté et valué.
Cet algorithme est basé sur celui de Warshall dédié au calcul de la fermeture transitive d’un graphe. Le calcul de
cette fermeture transitive est adapté afin de conserver, parmi tous les chemins reliant 2 sommets, un de ceux ayant
la valeur la plus faible.

**L’algorithme de Floyd-Warshall n’est abordé ni en cours, ni en travaux dirigés. Ce projet intègre donc un petit
travail de recherche de votre part.**

## CONDITIONS GENERALES
Le projet est à réaliser par équipes. Votre enseignant de TD vous indiquera combien votre groupe TD doit constituer
d’équipes.
Vous devrez utiliser l’un des langages de programmation suivants : C, C++, Java ou Python.
Une soutenance de projet est prévue mi-novembre. Vous devrez préalablement avoir envoyé à votre enseignant le
résultat de votre travail. Des graphes de tests, à partir desquels votre programme sera testé, vous seront
communiqués quelques temps avant la soutenance. Lors de l’élaboration du programme, vous n’avez pas besoin de
ces graphes de test : il doit marcher sur n’importe quel graphe

## TRAVAIL A REALISER
*Illustration :*

![illustration de l'algorithme](../master/img/illustration.PNG?raw=true)

*Boucle principale :*

Votre programme doit pouvoir exécuter les traitements demandés sur une suite de graphes, au choix de
l’utilisateur. Lors de la soutenance, il ne doit pas être nécessaire de relancer votre programme pour le tester
avec plusieurs graphes.

*Traitement d’un graphe :*

Dans un premier temps, l’utilisateur indique le graphe à analyser. Les graphes seront identifiés par des
numéros.

Le graphe est ensuite chargé en mémoire à partir de sa description contenue dans un fichier au format
« texte ». Voir annexe.
Le graphe « lu » est stocké dans des structures de données. A partir de ce stade, votre programme ne doit en
aucun cas accéder une seconde fois au fichier : seule la représentation en mémoire est utilisée.

La représentation en mémoire du graphe sous la forme de chaînes de caractères reprenant les lignes
du fichier texte ne sera pas efficace pour un programme opérationnel devant traiter des graphes
volumineux. Cela est vrai quelle que soit sa mise en œuvre précise, utilisant des tableaux, des
vecteurs, des ensembles, …

**Le choix d’une structure de donnée plus efficace fera partie de votre évaluation.**

Le graphe est ensuite affiché à l’écran sous forme matricielle : une matrice d’adjacence plus une matrice de
valeurs, ou les deux combinées.
Faites très attention à la lisibilité de cet affichage, notamment l’alignement des colonnes et l’identification
des sommets (titres des lignes et colonnes).

L’algorithme de Floyd-Warshall est exécuté. Les valeurs intermédiaires des données de l’algorithme
(matrices habituellement nommées ‘L’ et ‘P’) sont affichées.

A la lecture du résultat de l’algorithme, votre programme indique si le graphe contient au moins un circuit
absorbant.

Si aucun circuit absorbant n’est présent, le dernier traitement consiste à afficher les chemins de valeurs
minimales. Vous pouvez les afficher tous, ou prévoir une boucle d’interface avec l’utilisateur :
```
    Chemin ?
    Si oui alors
        Sommet de départ ?
        Sommet d’arrivée ?
        Affichage du chemin
        Recommencer
    Si non alors arrêter
```

## GRAPHES A PRENDRE EN COMPTE

Votre programme doit pouvoir traiter correctement n’importe quel graphe qui répond aux critères ci-dessous :
- Graphe orienté
- Graphe valué – Valeurs numériques entières quelconques (valeurs négatives admises, valeur ‘0’ admise)
- Sommets représentés par des nombre entiers, de ‘0’ à ‘nombre de sommets moins 1’
- Au plus un arc d’un sommet x vers un sommet y.

Votre programme ne doit imposer aucune limite pour le nombre de sommets, ni pour les valeurs des arcs, ni pour le
nombre d’arcs.

## DEROULEMENT DU PROJET
**Constitution des équipes**
Nombre d’équipes par groupe TD/TP : 12
Le nombre d’étudiants par équipe sera calculé en fonction du nombre d’étudiants dans chaque
groupe TD/TP. Votre enseignant vous l’indiquera par voie d’annonce sur Moodle dans les jours qui
suivent.

Constitution des équipes : à remettre à votre enseignant au plus tard à la date qu’il vous indiquera.
Aucun changement ne sera possible après cette date. A défaut d’une constitution des équipes
fournie par les délégués de chaque groupe TD, les enseignants pourront décider eux-mêmes de la
constitution des équipes, sans possibilité de modification.

Problèmes éventuels : S’il y a problème au niveau d’une équipe (un élève qui ne participe pas au travail des
autres, un élève malade, etc…), vous êtes tenus d’en informer votre enseignant immédiatement.

**Aucune modification d’équipe sans l’aval direct de l’enseignant ne sera acceptée.**
