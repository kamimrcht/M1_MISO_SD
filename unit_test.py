import unittest
from io import StringIO
import sys
from extract_kmer import read_fasta, extract_kmers 
from extract_count import get_count_header
from get_kmer_counts_from_bcalm import print_kmer_counts

class TestKmerExtraction(unittest.TestCase):

    def test_read_fasta(self):
        expected = [('seq1', 'ATCGA'), ('seq2', 'GGCTA')]
        result = read_fasta('test/sample.fasta')
        self.assertEqual(result, expected)

    def test_extract_kmers(self):
        sequence = 'ATCGA'
        k = 3
        expected = ['ATC', 'TCG', 'CGA']
        result = extract_kmers(sequence, k)
        self.assertEqual(result, expected)

    def test_extract_kmers_empty_sequence(self):
        sequence = ''
        k = 3
        expected = []
        result = extract_kmers(sequence, k)
        self.assertEqual(result, expected)

    def test_extract_kmers_k_greater_than_sequence_length(self):
        sequence = 'ATCG'
        k = 5
        expected = []
        result = extract_kmers(sequence, k)
        self.assertEqual(result, expected)

class TestKmerCountExtraction(unittest.TestCase):

    def test_count_header_1(self):
        expected = 1.0
        result = get_count_header(">0 LN:i:23 KC:i:3 km:f:1.0    L:-:241269:+")
        self.assertEqual(result, expected)
    
    def test_count_broken_header(self):
        expected = None
        result = get_count_header(">0 LN:i:23 KC:i:\n")
        self.assertEqual(result, expected)

class TestPrintKmerCounts(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture the print statements
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_print_kmer_counts(self):
        k_size = 21
        fasta_file = 'test/sample_2.fasta'
        expected_output = "CCTTGCCTGGCGCTATTTTTA 1.0\nCTTGCCTGGCGCTATTTTTAC 1.0\nTTGCCTGGCGCTATTTTTACA 1.0\nAAAAAAAAAGCGTCTGGCAAA 6.0\nAAAAAAAAAAAAAAGCGTCCC 1.0\nAAAAAAAAAAAAAGCGTCCCA 1.0\nAAAAAAAAAAAAGCGTCCCAG 1.0\nAAAAAAAAAAAGCGTCCCAGG 1.0\nAAAAAAAAAAGCGTCCCAGGA 1.0\nAAAAAAAAAGCGTCCCAGGAG 1.0"

        # Call the function
        print_kmer_counts(k_size, fasta_file)

        # Get the actual output and compare with expected
        self.capturedOutput.seek(0)  # Go to the start of the captured output
        actual_output = self.capturedOutput.read().strip()
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()