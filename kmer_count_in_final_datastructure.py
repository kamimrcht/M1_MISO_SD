import argparse
import timeit
from bisect import bisect_left

def binary_search_kmers(kmers_list, target):
    """
    Perform a binary search to find the index of 'target' in a sorted list of k-mers.

    :param kmers: Sorted list of k-mers (strings).
    :param target: The k-mer to search for.
    :return: The index of 'target' in 'kmers' if found, otherwise -1.
    """
    low = 0
    high = len(kmers_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = kmers_list[mid][0]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def bisect_search(kmers_list, target):
    i = bisect_left(kmers_list, target)
    return i

def put_kmers_counts_in_sorted_list_bisect(kmers_and_counts):  
    """
    stores kmers and counts in lists of pairs, in a single sorted list, optimized
    :param A list of two lists - [k-mers, corresponding counts].
    :return: a list of [kmer,count], where each k-mer appears a single time
    """
    kmer_data_structure = []
    count_data_structure = []
    for kmer, count in kmers_and_counts:
        value = bisect_search(kmer_data_structure, kmer)
        if value < len(kmer_data_structure) and kmer_data_structure[value] == kmer: #kmer is already present
            count_data_structure[value] += count
        else:
            kmer_data_structure.insert(value,kmer)
            count_data_structure.insert(value,count)
    return (kmer_data_structure, count_data_structure)


def get_kmers_and_counts(k_size, result_file):
    """
    Extracts k-mers and their counts from a RESULT file
    and their counts accordingly.

    :param k_size: The k-mer size.
    :param result_file: a text file result from print_kmer_counts() function
    :return: A list of two lists - [k-mers, corresponding counts].
    """
    pass #a remplir

def put_kmers_counts_in_unsorted_list(kmers_and_counts):                               
    """
    stores kmers and counts in the same order in two unsorted lists
    :param A list of two lists - [k-mers, corresponding counts].
    :return: a tuple of two lists of kmers and counts, where each k-mer appears and single time
    """
    pass #a remplir

def put_kmers_counts_in_sorted_list(kmers_and_counts):  
    """
    stores kmers and counts in lists of pairs, in a single sorted list
    :param A list of two lists - [k-mers, corresponding counts].
    :return: a list of [kmer,count], where each k-mer appears a single time
    """
    pass #a remplir




def put_kmers_in_dict(kmers_and_counts):
    """
    stores kmers and counts as key/value pairs in a dict
    :param A list of two lists - [k-mers, corresponding counts].
    :return: a dict of {kmer,count}
    """
    pass #attendre le cours table de hachage



def put_kmers_in_dict_several_datasets(several_kmers_and_counts):
    pass