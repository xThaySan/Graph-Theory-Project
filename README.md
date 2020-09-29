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
