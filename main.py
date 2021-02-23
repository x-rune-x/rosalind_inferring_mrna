codon_count = {
    "F": 2,
    "L": 6,
    "S": 6,
    "Y": 2,
    "C": 2,
    "W": 1,
    "P": 4,
    "H": 2,
    "Q": 2,
    "R": 6,
    "I": 3,
    "M": 1,
    "T": 4,
    "N": 2,
    "K": 2,
    "V": 4,
    "A": 4,
    "D": 2,
    "E": 2,
    "G": 4
}


def calc_rna(input_text, codon_dict):
    input_file = open(input_text, "r")

    total_combinations = 3

    rna_string = input_file.read().strip("\n")
    for aa in rna_string:
        total_combinations = total_combinations * codon_dict[aa]
        total_combinations = total_combinations % 1000000

    # total_combinations = total_combinations % 1000000
    return total_combinations


practice = calc_rna("rosalind_mrna.txt", codon_count)
print(practice)
