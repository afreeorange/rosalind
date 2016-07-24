import math
import re
import sys

from requests import HTTPError
import requests

UNIPROT_ENDPOINT = 'http://www.uniprot.org/uniprot/{}.fasta'
N_GLYCOSYLATION_MOTIF_PATTERN = r'N[^P][S|T][^P]'


def __get_primary_stucture(protein):
    """Connects to UniProt to retrieve protein structure in FASTA
    format. Throws an exception if protein's not found for whatever
    reason.
    """
    r = requests.get(UNIPROT_ENDPOINT.format(protein))

    if r.status_code == 200:
        return ''.join(r.text.split('\n')[1:])
    else:
        raise HTTPError(
            'Could not get', UNIPROT_ENDPOINT.format(protein)
        )


def __tiles(string, length):
    """For a given string 'MLGVLVLGALALAGLGFPAPAEP' will yield:
    (0, MLGV)
    (1, LGVL)
    (2, GVLV)
    (3, VLVL)
    (4, LVLG)
    ...
    """
    for i in range(length * math.floor(len(string) / length)):
        yield (i, string[i:i + length])


def get_motif_locations(protein, pattern):
    """Search protein structure for the given motif and returns
    a list of integers that indicate locations.

    :param protein: String, name of protein. Can be in lower case.
    :param pattern: A regex object that will be used to search protein.
    """
    primary_structure = __get_primary_stucture(protein.upper())
    locations = []

    for tile in __tiles(primary_structure, 4):
        match = re.match(pattern, tile[1])

        if match:
            locations.append(tile[0] + 1)

    return locations


if __name__ == '__main__':
    with(open(sys.argv[1])) as f:
        for line in f:
            protein = line.rstrip()
            locations = get_motif_locations(
                protein,
                N_GLYCOSYLATION_MOTIF_PATTERN
            )

            if locations:
                print(protein)
                print(' '.join(
                    [
                        str(_)
                        for _
                        in locations
                    ]
                ))
