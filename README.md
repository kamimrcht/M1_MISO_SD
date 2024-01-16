# M1 MISO : structures de données

## TP 1 : listes

### Matériel Initial

Vous avez accès à ces 3 fichiers :
- `extract_kmer.py`
- `extract_count.py`
- `get_kmer_count_from_bcalm.py`


et à ces fichiers à compléter :
- `main.py`
- `kmer_count_in_final_datastructure.py`

ainsi qu'à ces tests unitaires:
- `unit_test.py`

A un dossier contenant des données pour les tests :

`test`

A un dossier contenant des données d'entrée :

`input`

Commencez par **cloner le répertoire pour récupérer le code et le reste du contenu**.
`
git clone xxxxxxx
cd M1_MISO_SD
`

### Evaluation
Pour évaluer je vais :

0. récupérer une **archive** de ce répertoire (contenant ce fichier, le code, les inputs et fichiers pour les tests), construite de cette manière :
`tar cvzf M1_MISO_SD.tar.gz M1_MISO_SD` 
1. **lancer les tests** `python3 unit_test.py` (vous devrez en rajouter). S'ils passent tous, je passe à l'étape suivante.
2. lancer le programme principal `python3 main.py 21`, qui devrait me générer une **image** `runtime_plot.png` quand vous aurez fini la partie 3.
3. lire vos réponses aux questions (à écrire directement dans ce document)
4. lire la **documentation** des fonctions que vous aurez ajoutées
5. lire les fonctions/le code ajouté(es) s'il y a de la documentation

Les points 1,2 et 4 sont les plus importants.

### Contexte

Les séquences présentes dans input ont été produites par séquençage RNA-seq d'un transcriptome humain.
Dans le cas de la RNA-seq, on est tout particulièrement intéressés par les occurrences des séquences, qui sont reliées aux niveau d'expression des gènes.
On veut réaliser un programme qui extrait les k-mers d'un fichier FASTA de input et leur associe leur comptage dans ce fichier FASTA dans une structure de données.

### Partie 1 - comprendre le TP

Dans notre cas d'utilisation, les fichiers FASTA utilisés en entrée sont déjà formattés de telle manière qu'on connait le comptage des k-mers pour une séquence donnée. Par exemple : 

`
>0 LN:i:23 KC:i:3 km:f:6.0    L:-:241269:+ 
CCTTGCCTGGCGCTATTTTTACA
`

Indique dans le champ `km:f:` que pour tous les k-mers en dessous, le comptage est de `6.0` (le reste des champs ne nous intéresse pas).
Pour des k-mers de taille 21, cela veut dire que `CCTTGCCTGGCGCTATTTTTA`, `CTTGCCTGGCGCTATTTTTAC`, `TTGCCTGGCGCTATTTTTACA` ont pour comptage `6.0`.

On veut donc parser le fichier FASTA en entrée pour en extraire les k-mers et le comptage associé. Cela est réalisé en lançant main.py.
Plus exactement 
`python3 main.py -k 21 -f input/sample_2.fasta > result_sample_2.txt`
va écrire une liste de k-mers et leurs comptages associés dans le fichier `result_sample_2.txt`.

**Question 0:** Décrire brièvement ce que font `extract_kmer.py`, `extract_count.py` et `get_kmer_count_from_bcalm.py` dans le cadre de ce TP.

**Question 1 :** Essayer la commande ci-dessus. Décrire le format de `result_sample_2.txt`.

**Question 2 :** Quel est le comptage du k-mer `AAAAAAAAAGCGTCTGGCAAA` pour ce jeu de données ?

**Question 3 :** Lancer les tests unitaires. Dans `class TestKmerCountExtraction(unittest.TestCase)`, ajouter une fonction et sa documentation, qui teste l'extraction d'un comptage de valeur 6 depuis un header.

Une fois qu'on a parsé le fichier FASTA et récupéré les k-mers, on veut les insérer dans différentes structures de données pour tester et comparer leurs efficacités.

### Partie 2 - Comparer des listes pour insérer les k-mers et leurs comptages
On va maintenant travailler dans le fichier à compléter `kmer_count_in_final_datastructure.py`.

**Question 4 :** Ecrire la fonction `get_kmers_and_counts()` qui extrait les k-mers et leurs comptages d'un fichier comme `result_sample_2.txt`. 

**Question 5:** Ecrire la fonction `put_kmers_counts_in_unsorted_list()` qui prend la sortie de `get_kmers_and_counts()`  et écrit les k-mers et leurs comptages aux mêmes indices dans deux listes.                      
Par exemple si le contenu de `result_sample_2.txt` est:
`
TTGCCTGGCGCTATTTTTACA 1.0
AAAAAAAAAGCGTCTGGCAAA 6.0
`
on doit avoir deux listes
`
[TTGCCTGGCGCTATTTTTACA, AAAAAAAAAGCGTCTGGCAAA]
[1.0, 6.0]
`

**Question 6:** Ecrire la fonction `put_kmers_counts_in_sorted_list()` qui prend la sortie de `get_kmers_and_counts()` et écrit les k-mers et leurs comptages comme des paires dans une liste triée de listes (tri par le premier élément des paires, le k-mer).
Par exemple si le contenu de `result_sample_2.txt` est:
`
CAAAAAACAGCGTCTGGCAAA 1.0
TTGCCTGGCGCTATTTTTACA 3.0
AAAAAAAAAGCGTCTGGCAAA 6.0
`
on doit avoir la liste
`
[[AAAAAAAAAGCGTCTGGCAAA, 6.0], [CAAAAAACAGCGTCTGGCAAA, 1.0], [TTGCCTGGCGCTATTTTTACA, 3.0] ]
`

**Question 7 :** Quelle fonction entre `put_kmers_counts_in_unsorted_list()` et `put_kmers_counts_in_sorted_list()` doit être la plus rapide pour l'insertion de nouvel élément ? Pour la recherche d'élément ? Pourquoi ?


**Question 8 :** 

Dans les tests unitaires, créer une classe `class TestKmerLists(unittest.TestCase)` et réaliser les tests suivants avec leur documentation : 
    - `test_get_kmers(self)` qui teste la fonction `get_kmers_and_counts()`
    - `test_sorted(self)` qui teste `put_kmers_counts_in_sorted_list()`
    - `test_unsorted(self)` qui teste `put_kmers_counts_in_unsorted_list()`

### Partie 3 - Restitution graphique des résultats

**Question 9 :** A partir de `input/sample_10000.fasta`, créer des petits jeux de données `input/sample_X.fasta`, pour `X` valant 100, 200, 500, 1000, 2000. Produire un fichier `result_sample_X.txt` pour chaque et le stocker dans `input`.

**Question 10:** Dé-commenter le code en TODO dans `main.py`. Il vous permet de générer un fichier `runtimes.txt` qui teste le temps de calcul pour insérer les k-mers et leurs comptes dans les listes triée et non triée.

**Question 11**: Visionnez le résultat avec la commande suivante à mettre dans votre terminal : 

`
gnuplot -e "set terminal png; set output 'runtime_plot.png'; set title 'Runtime Comparison'; set xlabel 'Dataset Size'; set ylabel 'Runtime (seconds)'; set grid; set key left top; plot 'runtimes.txt' using 1:2 title 'Unsorted List' with lines, 'runtimes.txt' using 1:3 title 'Sorted List' with lines, 'runtimes.txt' using 1:4 title 'Dict' with lines; set terminal wxt; set output;"
`

**Question 12**: Vous attendiez-vous à ce résultat ? Est-ce en accord avec votre réponse à la question 7?

**Question 13**: Modifiez le benchmark en utilisant la fonction `put_kmers_counts_in_sorted_bisect` à la place de la fonction `put_kmers_counts_in_sorted`. Il s'agit aussi d'une insertion dans une liste triée. Regénerez la figure, que se passe-t-il cette fois ? Comment interpréter cela ?

