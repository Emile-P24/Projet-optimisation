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

On veut également une quantité fabriquée positive, soit $q > 0$

Ainsi :
* $f(z) = f(q,d) = c^T r - v^T h(q,d)$ est la fonction que nous souhaitons minimiser
* Il y a deux variables de décision : $q$ et $r$.
* f est minimisée sous les contraintes $r >= Aq$ et $q > 0$

## Partie 2

5)
Pour résoudre ce problème, on peut utiliser un algorithme d'optimisation sous contraintes. Si par exemple la fonction est convexe, il y a existence d'un point [A COMPLETER, J'AI PAS LE NOM SOUS LA MAIN on peut utiliser l'algorithme de [A COMPLETER J'AI PAS LE NOM SOUS LA MAIN]. 

6)
Les résultats résultats obtenus montrent que les maxima sont atteints pour r = Aq et q=d, ce qui semble cohérent : inutile d'acheter plus que ce dont on a besoin pour produire, et inutile de produire plus que ce que les gens achèteront ; réciproquement, produire moins que la demande serait sous-optimal : il reste un profit à aller chercher (le coût marginal de production et le prix de vente étant constants, s'il est profitable de vendre à 10 personnes, il est aussi profitable de vendre à 20).

7)
On cherche désormais à maximiser le profit espéré de notre problème, c'est à dire la fonction :
$$
PE(q,r) = \sum_{k} P(d^k,q,r)\pi^k
$$
où $P(d^k,q,r) = v^Th(q,r,d^k) - c^Tr$

On va donc minimiser $f(z) = -PE(z)$ où $z=q,r$


## Partie 3

8) **(a)**
La fonction que l'on souhaite minimiser est :
$$
f(q,r)= - \sum_{k}\pi^kP(d^k,q,r)
$$
où $P(d^k,q,r) = v^Tmin(q,d^k) - c^Tr$

Cette minimisation se fait sous les contraintes :
* (1) : "$r \ge Aq$"
* $q \ge 0$

**(b)**

Soit $(r^*,q^*)$ le point d'optimalité de f. Supposons par absurde que $r^*>Aq^*$.
$$
f(q*,r*) = - \sum_{k}\pi^k (v^Tmin(q^*,d^k) - c^Tr^*)
$$
Or $- c^Tr^* < -c^TAq^*$ car $c>0$
Donc :
$$
f(q^*,r^*) > - \sum_{k}\pi^k (v^Tmin(q^*,d^k) - c^TAq^*) = f(q^*,Aq^*)
$$
ce qui contredit l'optimalité de $(q^*,r^*)$ car $r^* \ne Aq^*$

On a donc $r^* <= Aq^*$ ainsi que l'égalité réciproque (contrainte), ce qui donne donc $r^*=Aq^*$

**(c)**

On a montré que $\underset{q,r}{\text{min}}(f)$ était nécessairement atteint dans l'ensemble $\{(r,q) | r=Aq\}$
En fixant r=Aq, on élimine r du problème d'optimisation.

Il s'agit donc de minimiser :
$$
f(q) = - \sum_{k}\pi^kP(d^k,q)
$$
où $P(d^k,q) = v^Tmin(q,d^k) - c^TAq$

Il reste, à vrai dire, la contrainte $q \ge 0$, mais on sait que l'optimisation se produira pour une valeur de q positive, on peut donc la laisser de côté.

9)

**(a)**

On veut montrer que :
$$
\underset{q}{\text{max}} v^T\text{min}(q,d^k) = \underset{\underset{u^k \le q, u^k \le d^k}{q,u^k}}{max} v^Tu^k
$$
, et que ces maxima sont atteints en de mêmes valeurs de q.

* Intéressons-nous au membre de gauche. Supposons que $q \ge d^k$. Il vient : $v^T\text{min}(q,d^k) = v^Td^k$

Supposons que $q<d^k$. On a alors $v^T\text{min}(q,d^k) = v^T q$, ce qui est strictement inférieur à $v^Td^k$.

Le membre de gauche vaut donc $v^Td^k$ et est réalisé pour $q \ge d^k$

* Intéressons-nous au membre de droite. Suppons par absurde qu'à l'optimum, $q<d^k$. Il vient :
$$
v^Tu^k \ge v^Tq < v^Td^k
$$
Or, pour $q \ge d^k$ et $u^k=d^k$, on a $v^Tu^k = v^Td^k, ce qui contredit l'optimalité supposée. A l'optimum, donc : $q \ge d^k$
Par le même raisonnement et en respectant la contrainte $u^k \le d^k$, on a nécessairement u^k = d^k à l'optimum.

Le membre de droite vaut donc $v^Td^k$ et est réalisé pour $q \ge d^k$ (et u^k = d^k).

* Ainsi, les deux problèmes de maximisation sont équivalents.


**(b)**

La fonction que l'on souhaite minimiser est :
$$
f(q)= - \sum_{k}\pi^kP(q,d^k,u^k)
$$
où $P(q,d^k,u^k) = v^Tu^k - c^TAq$

Cette minimisation se fait sous les contraintes :
* $q \ge 0$
* $\forall k, u^k \le d^k$
* $\forall k, u^k \le q$

L'intérêt de cette reformulation est que l'on optimise désormais une fonction différentiable. On a remplacé la disjonction de cas faite par la fonction par un ajout de contraintes.

**(c)**

On trouve des valeurs comparables avec les précédentes.

10)
