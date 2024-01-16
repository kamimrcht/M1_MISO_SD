def read_fasta(file_path):
    """
    Reads a FASTA file and returns a list of tuples with sequence IDs and sequences.

    :param file_path: Path to the FASTA file.
    :return: A list of tuples. Each tuple contains (sequence_id, sequence).
    """
    sequences = []
    with open(file_path, 'r') as file:
        sequence_id = None
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence_id is not None:
                    sequences.append((sequence_id, sequence))
                sequence_id = line.strip().lstrip('>')
                sequence = ''
            else:
                sequence += line.strip()
        if sequence_id is not None:
            sequences.append((sequence_id, sequence))
    return sequences

def extract_kmers(sequence, k):
    """
    Extracts k-mers from a given sequence.

    :param sequence: A string representing the DNA sequence.
    :param k: The k-mer size.
    :return: A list of k-mers.
    """
    kmers = []
    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        kmers.append(kmer)
    return kmers