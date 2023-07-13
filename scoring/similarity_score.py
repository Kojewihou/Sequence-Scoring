# No Global Imports

from matrices import blosum62

def pairwise_similarity(sequenceA, sequenceB, limit=2):
    if len(sequenceA) != len(sequenceB):
        raise("Length not matching")
    
    seq_score=0
    for (resA, resB) in zip(sequenceA,sequenceB):
        if "-" in (resA,resB):
            continue
        else:
            try:
                res_score = blosum62[(resA,resB)]
            except:
                res_score = blosum62[(resB,resA)]
            if res_score > limit:
                seq_score+=1
    return round((seq_score/len(sequenceA))*100,2)