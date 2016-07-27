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


def gc_percent(dna):
    return ((dna.count('G') + dna.count('C')) / len(dna)) * 100


def max_gc_percent(fasta_file):
    records = parse_fasta(fasta_file)
    content_records = []

    for _ in records:
        content_records.append(
            (_[0], gc_percent(_[1]))
        )

    return sorted(content_records, key=lambda x:x[1], reverse=True)[0]


if __name__ == '__main__':
    max_gc = max_gc_percent(sys.argv[1])
    print(max_gc[0])
    print(max_gc[1])
