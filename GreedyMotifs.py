import math
k=int(3)
t=int(5)
DNA= "GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"


GREEDYMOTIFSEARCH(Dna, k, t)
        BestMotifs = motif matrix formed by first k-mers in each string
                      from Dna
        for each k-mer Motif in the first string from Dna
            Motif1 ← Motif
            for i = 2 to t
                form Profile from motifs Motif1, …, Motifi - 1
                Motifi ← Profile-most probable k-mer in the i-th string
                          in Dna
            Motifs ← (Motif1, …, Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs ← Motifs
        return BestMotifs