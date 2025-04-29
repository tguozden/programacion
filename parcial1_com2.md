Primer parcial comisión 2:

Decimos que, en una lista de enteros, una escalera sucesión
de elementos en la diferencia entre elementos sucesivos
es la misma:

delta = lista[n+1] - lista[n]

Por ejemplo en 
lista = [4 3 -1 0 2 4 6 7]
a partir de lista[3] (=0) los siguientes 3 números van de dos en dos




Escriba un programa que dado una lista de números enteros retorne los
índices de comienzo y final de la escalera más larga. Por ejemplo:
`[2,5,3,-1,3,5,7,9,1,2,4,3,5,9] —> [3,7]`




para ello, resuelva los siguientes problemas como funciones:


1. Escriba una función que dada una lista de números enteros (supongamos lista1), y un índice
de esa lista ( supongamos n), retorne el largo de la escalera que comienza en el índice n.
Por ejemplo: [2,5,3,-1,3,5,7,9,1,2,4,3,5,9] - 5 —> 3


2. Escriba una función que dada una lista de números enteros (lista1), cree una
nueva lista (lista2) de la misma longitud que lista1 que contenga en cada posición el
largo de la escalera que comienza en esa posición en lista1. Por ejemplo:
[2,5,3,-1,3,5,7,9,1,2,4,3,5,9] —> [2,1,1,5,4,3,2,1,3,2,1,3,2,1]


3. Usando A. y B. resuelva el problema planteado originalmente
