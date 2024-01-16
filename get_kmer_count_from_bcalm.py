from extract_count import *
from extract_kmer import *


def print_kmer_counts(k_size, fasta_file):
    """
    Prints all k-mers and their counts from a fasta file.
    :param k_size: the kmer size
    :param fasta_file: the fasta file
    """
    # Read sequences from FASTA file
    fasta_sequences = read_fasta(fasta_file)

    # Extract k-mers from each sequence
    kmers = list()
    counts = list()
    for seq_id, sequence in fasta_sequences:
        kmers.append(extract_kmers(sequence, k_size)) # a list of lists of kmers. Each list is the kmers from one line of the BCALM file
        counts.append(get_count_header(seq_id)) # a list of counts. Each count corresponds to one line of the fasta file.

    for k, c in zip(kmers, counts):
        for kmer in k:
            print(kmer, c) #QUESTION : comprendre le code et me dire combien de fois est vu le kmer xxxx  //bonus: le confirmer avec grep/awk/sed
            #QUESTION : le fichier est un peu gros, en créer un plus petit pour les tests à partir du fichier de départ
            #Question : récupérer le resultat avec une ligne du type python3 main.py -k 21 -f test/sample_2.fasta > result.txt
            #QUestion : pourquoi y a t'il un seul kmer à 6 et 9 à 1.0 alors que le fasta sample_2.fasta ne contient que 3 lignes

            #Dans un nouveau fichier .py écrire une fonction qui lit le fichier result.txt et extrait les kmers et les comptages
            # une fonction et met les k-mers d'une part dans une liste, les comptes d'autre part dans une autre
            #2e fonction qui met les résults dans une liste de tuples

            #recherche d'un k-mer
            # recherche séquentielle, tri, recherche dichotomique
            # ajout

            #possiblement plot du temps en faisant augmenter le nombre de datasets