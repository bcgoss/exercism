"""Matches DNA nucleotides with RNA pairs """
import re

PAIRS = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
def to_rna(strand):
    match = re.search('[^GCTA]', strand)
    if match:
        return ''

    result = map(lookup, list(strand))
    return "".join(result)

def lookup(nulceotide):
    return PAIRS[nulceotide]
