import random

def generate_random_sequence(sequence_length = 10):
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"
    lookup_table = {i: aa for i, aa in enumerate(amino_acids)}
    seq = ''.join([lookup_table[random.randint(0, len(amino_acids) - 1)] for i in range(sequence_length)])
    return seq