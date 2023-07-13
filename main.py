import random

from scoring import pairwise_similarity, pairwise_identity, pairwise_score
from utils import generate_random_sequence




if __name__ == "__main__":

    sequence_1 = generate_random_sequence(600)
    sequence_2 = generate_random_sequence(600)

    print(pairwise_similarity(sequence_1, sequence_2,0))


