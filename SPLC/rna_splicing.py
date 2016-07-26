import sys

# http://rosalind.info/glossary/dna-codon-table/
t = """
TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G
""".split()
dna_codon_table = dict(zip(t[0::2], t[1::2]))
dna_codon_table['TAA'] = ''
dna_codon_table['TAG'] = ''
dna_codon_table['TGA'] = ''


def remove_introns(dna, list_of_introns):
    for intron in list_of_introns:
        dna = dna.replace(intron, '')

    return dna


def translate_dna(dna):
    protein_string = ''

    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]
        protein_string += dna_codon_table[codon]

    return protein_string


if __name__ == '__main__':
    inputs = [_.rstrip() for _ in open(sys.argv[1]).readlines()][1::2]
    dna, introns = inputs[0], inputs[1:]

    print(
        translate_dna(
            remove_introns(dna, introns)
        )
    )
