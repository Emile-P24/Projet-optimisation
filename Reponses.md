# Projet-optimisation

## Partie 1

1)
L'expression (2) correspond aux bénéfices de la boulangerie : on soustraît les entrées d'argent par les dépenses. En particulier, on utilise min{q,d} pour obtenir la quantité vendue de chaque produit (qu'on multiplie par le prix de vente pour obtenir le revenu). En effet, q étant la quantité fabriquée et d la demande, la quantité réellement vendue correspond au minimum des deux : impossible de vendre plus que ce qu'on a produit, ni plus que ce que les clients voudront acheter.

2)
Ce dernier terme n'est cependant pas différentiable, ce qui rend inutilisable la majorité des algorithmes d'optimisation que nous avons étudiées en cours.

3)
Soit $i \in \llbracket 1,p \rrbracket$ Supposons que $q_i>d_i$ On a :
$$
h_i(q,d) = \frac{q_ie^{-\alpha q_i} + d_ie^{-\alpha d_i}}{e^{-\alpha q_i} + e^{-\alpha d_i}}
$$
$$
h_i(q,d) = \frac{q_ie^{\alpha (d_i - q_i)} + d_i}{e^{\alpha (d_i - q_i)} + 1}
$$
Or, $d_i - q_i < 0$, donc pour $\alpha \longrightarrow +\infty$ :
$$
h_i(q,d) \longrightarrow d_i
$$
le raisonnement pour $q_i$ est symétrique.

On a donc finalement :
$$
h(q,d)\underset{\alpha\to+\infty}{\longrightarrow}min(q,d)
$$

L'intérêt de s'intéresser à ce problème plutôt qu'au précédent est que la fonction h est différentiable. Nous pourrons donc utiliser des algorithmes d'optimisations qui ne s'appliquent qu'à des fonctions différentiables.

4)
On veut maximiser $v^T h(q,d) - c^T r$, c'est-à-dire minimiser $-v^T h(q,d) + c^T r$.

La contrainte qui s'applique à la production est qu'on ne peut produire sans matières premières, ce qui se réécrit $r >= Aq$

Ainsi :
* $f(z) = f(q,d) = c^T r - v^T h(q,d)$ est la fonction que nous souhaitons minimiser
* Il y a deux variables de décision : $q$ et $d$.
* f est minimisée sous la contrainte $r >= Aq$

## Partie 2

5)
Pour résoudre ce problème, on peut utiliser un algorithme d'optimisation sous contraintes. Si par exemple la fonction est convexe, il y a existence d'un point [A COMPLETER, J'AI PAS LE NOM SOUS LA MAIN on peut utiliser l'algorithme de [A COMPLETER J'AI PAS LE NOM SOUS LA MAIN]. 

6)
Les résultats résultats obtenus montrent que les maxima sont atteints pour r = Aq et q=d, ce qui semble cohérent : inutile d'acheter plus que ce dont on a besoin pour produire, et inutile de produire plus que ce que les gens achèteront ; réciproquement, produire moins que la demande serait sous-optimal : il reste un profit à aller chercher (le coût marginal de production et le prix de vente étant constants, s'il est profitable de vendre à 10 personnes, il est aussi profitable de vendre à 20).

7)
On cherche désormais à maximiser le profit espéré de notre problème, c'est à dire la fonction :
$$
PE = \sum_{k} P(d^k)\pi^k
$$
on va donc minimiser $f(z) = -PE(z)$ où $z=q,r$