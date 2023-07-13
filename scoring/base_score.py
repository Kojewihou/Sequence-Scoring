# No Global Imports

from matrices import blosum62

def pairwise_score(sequence1, sequence2):
    score = 0
    gap_adjacent = False
    for i in range(len(min([sequence1,sequence2],key=len))):
        residueA = sequence1[i]
        residueB = sequence2[i]
        if "-" in residueB or "-" in residueA:
            if gap_adjacent == False:
                score-=11
                gap_adjacent = True
            else:
                score-=1
        else:
            gap_adjacent = False
            try:
                score += blosum62[(residueA,residueB)]
            except:
                score += blosum62[(residueB,residueA)]
    return score