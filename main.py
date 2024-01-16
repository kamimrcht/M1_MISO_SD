import argparse
from get_kmer_counts_from_bcalm import *
from kmer_count_in_final_datastructure import *

def measure_runtime(function, *args, number=10):
    """Measure the runtime of a function call."""
    return timeit.timeit(lambda: function(*args), number=number)

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="K-mer Analysis from FASTA file")
    parser.add_argument("-k", "--kmer_size", type=int, required=True, help="Size of the k-mers")
    parser.add_argument("-f", "--fasta_file", type=str, required=True, help="Path to the input FASTA file (in BCALM2 format)")

    # Parse arguments
    args = parser.parse_args()

    # Extract and process k-mers
    print_kmer_counts(args.kmer_size, args.fasta_file)

   
### TODO décommenter pour question 10
    # Datasets of different sizes
"""     sizes = [100, 200, 500, 1000, 2000]

    # File to store the results
    with open('runtimes.txt', 'w') as file:
        file.write("# DatasetSize UnsortedList SortedList Dict\n")
        for size in sizes:
            dataset = f"result_{size}.txt"

            kmers_and_counts = get_kmers_and_counts(args.kmer_size, dataset)

            # Measure runtime for unsorted list
            time_unsorted_list = measure_runtime(put_kmers_counts_in_unsorted_list, kmers_and_counts)

            # Measure runtime for sorted list
            time_sorted_list = measure_runtime(put_kmers_counts_in_sorted_list, kmers_and_counts)

            # Write the results to the file
            file.write(f"{size} {time_unsorted_list} {time_sorted_list} \n") """
### end TODO

if __name__ == "__main__":
    main()