# No Global Imports

from matrices import blosum62

def pairwise_identity(sequenceA, sequenceB):
    score = 0
    for (resA, resB) in zip(sequenceA, sequenceB):
        if resA == resB:
            score+=1
    return round((score/len(sequenceA))*100,2)