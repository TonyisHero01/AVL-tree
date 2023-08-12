Stručné zadání:

AVL-strom je datová struktura neboli soubor dat. Strom udržuje hodnoty seřazené. AVL-strom je binární vyhledávací strom a rozdíl výšek dvou podstromů u všech vrcholů je nejvýš 1, neboli je to vyvážený strom. AVL-strom má výšku logaritmickou vzhledem k počtu vrcholů, proto mají funkce logaritmické časy.  Aby byl strom vyvážený, jeho vrcholy, které porušují vyváženost, potřebují rotovat. 

`  `Funkce AVL-stromu obsahuje: přidání a smazaní hodnoty, hledání minima, hledání maxima, hledání následníka a zjištění daného hodnoty ve stromě. 

`  `Vstupní data jsou navzájem porovnatelná neboli úplně uspořádaná. Například: ve stromě můžou být čísla nebo řetězce, ale ne obojí současně. A každá hodnota může být maximálně jednou. 


Algoritmus funkce:

Třída vrcholu:

`  `Pokud se chceme podívat, jak vypadá strom neboli chceme se podívat, či je či dítě, tak spustíme funkce simple\_repr pro jednoduchou reprezentaci stromu.

`  `Hlavní funkce vrcholů je rotace: rotace doleva, rotace doprava, rotace doleva-doprava a rotace doprava-doleva. Když bude rozdíl podstromu menší než 0, tak je levý podstrom těžší, když bude rozdíl podstromu větší než 0, tak je pravý podstrom těžší a když se rovná 0, tak mají stejnou výšku. Rozdíl výšek leží v celočíselné množině {-2;2}. Když je rozdíl výšek daného vrcholu -2 a rozdíl výšek levého dítěte je -1 nebo 0, otáčí se doprava. Když je rozdíl výšek daného vrcholu -2 a rozdíl výšek levého dítěte je 1, otáčí se doleva-doprava. Když je rozdíl výšek daného vrcholu 2 a rozdíl výšek pravého dítěte je 0 nebo 1, otáčí se doleva. Když je rozdíl výšek daného vrcholu 2 a rozdíl výšek pravého dítěte je -1, otáčí se doprava-doleva. 

Příklad rotace doprava:

`                    `A`                            `B

`                   `/` `\\`                         `/` `\\

`                  `/`   `\\`                       `/`   `\\

`                 `/`     `\\`                     `/`     `\\

`                `B`       `e`      `==>`      `c`       `A

`               `/` `\\`                                  `/` `\\

`              `/`   `\\`                                `/`   `\\

`             `c`     `d`                             `d`     `e








Příklad rotace doleva:

`                `B`                           `A

`               `/` `\\`                         `/` `\\

`              `/`   `\\`                       `/`   `\\

`             `/`     `\\`                     `/`     `\\

`            `c`       `A`       `==>`      `B`       `e

`                    `/` `\\`                 `/` `\\

`                   `/`   `\\`               `/`   `\\

`                  `d`     `e`             `c`    `d

Příklad rotace doleva-doprava:

![](Aspose.Words.90ccf2ab-e2a3-4a53-9e59-ef152e772bde.001.png)

Příklad rotace doprava-doleva:

![](Aspose.Words.90ccf2ab-e2a3-4a53-9e59-ef152e772bde.002.png)

`  `Funkce update\_height updatuje výšku daného vrcholu. Algoritmus je tak, že k větší výšce z levého a pravého podstromu přičteme 1.

`  `Funkce compute\_balance\_factor vrací rozdíl výšek levého a pravého podstromu.

Třída stromu:

`  `Pro funkce insert (přidání vrcholu) najde nejdřív správné místo pomocí funkce \_find, potom přidává a vyváží každý vrchol na cestě od kořene do rodiče přidaného vrcholu. 

`  `Pro funkce remove (odstranění vrcholu) najde daný vrchol, potom smaže a vyváží každý vrchol na cestě od kořene do rodiče smazaného vrcholu pomocí pomocnou funkci \_balance. 

`  `Algoritmus funkce clear uloží None do kořene a počítadlo se vynuluje. 

`  `Funkce extend uloží všechny vrcholy z daného iteratoru do stromu. 

`  `Funkce \_\_iter\_\_ iteruje všechny vrcholy a vrací v inorderové pořadí. 

`  `Funkce hledání minima vrací rovnou další hodnotu iterovatelného objektu (první hodnota iterovatelného objektu je None, což znamená, že vrací první hodnotu v inorder stromu).

`  `Funkce hledání maxima je potřeba obrátit celý iterator, potom vrací první hodnotu iteratoru.

`  `Funkce hledání následníka najde nejdřív daný vrchol, potom najdeme nejlevější vrchol jeho pravého dítěte.

`  `Algoritmus funkce contains pracuje pomocí funkce \_find. Když 2 prvek posledního prvku vracené hodnoty není None, tak to znamená, že jsme tu hodnotu našli. 

Funkce \_\_len\_\_ vrací počet prvku ve stromě.

Funkce \_\_repr\_\_ vrací reprezentace stromu.


Reprezentace vstupních a výstupných dat:

\>>> node = Node(2) 	#založení vrcholu

\>>> node			

Node(2)				#reprezentace vrcholu

\>>> node.lchild = Node(1)	#přidání levého dítě

\>>> Node.simple\_repr(node)

((None, 1, None), 2, None)	#jednoduchá reprezentace vrcholu

\>>> node.rchild = Node(3)

\>>> Node.simple\_repr(node)

((None, 1, None), 2, (None, 3, None))

\>>> tree = AVLTree()	#založení prázdného stromu

\>>>tree.insert(2)		#přidání vrchol

\>>>tree

AVLTree([2])			#reprezentace stromu

\>>>tree.insert(3)

\>>>tree

AVLTree([2, 3])

\>>>tree.remove(3)	#smazaní vrchol

\>>>tree

AVLTree([2])

\>>> tree

AVLTree([2, 3, 4, 5, 6])

\>>>len(tree)

5

\>>> tree.find\_min()	#hledání minima

2

\>>> tree.find\_max()	#hledání maxima

6

\>>> tree.find\_next(4) 	#hledání následníka

5

\>>> tree.\_\_contains\_\_(3) #obsahování daného vrcholu

True

\>>> Node.simple\_repr(tree.root)		#jednoduchá reprezentace vztahy vrcholů

((None, 2, None), 3, ((None, 4, None), 5, (None, 6, None)))

Zdroje:

<https://en.wikipedia.org/wiki/AVL_tree>

Průvodce labyrintem algoritmů – Martin Mareš, Tomáš Valla



