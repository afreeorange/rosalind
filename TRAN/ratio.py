import sys


def parse_fasta(filename):
    title = ''
    dna = []
    records = []

    fasta = open(filename)

    while True:
        line = fasta.readline().rstrip()
        if not line:
            # Add the last record before quitting
            records.append((title, ''.join(dna)))
            break
        if line[0] == '>':
            if title:
                records.append((title, ''.join(dna)))
            title = line[1:]
            dna = []
        else:
            dna.append(line)

    return records


def get_tt_ratio(dna1, dna2):
    transitions = {'A': 'G', 'G': 'A', 'C': 'T', 'T': 'C'}
    mutations = [
        0 if transitions[n1] != n2 or transitions[n2] != n1
        else 1
        for n1, n2
        in zip(dna1, dna2)
        if n1 != n2
    ]
    return mutations.count(1) / mutations.count(0)


if __name__ == '__main__':
    records = parse_fasta(sys.argv[1])
    dna1 = records[0][1]
    dna2 = records[1][1]

    print(get_tt_ratio(dna1, dna2))
