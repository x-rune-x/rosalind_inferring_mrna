# Map amino acid by letter code to the number of codons that code for it.
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

    # Begin with 3 to take into account the 3 stop codons that will always be present in an mRNA sequence.
    total_combinations = 3

    rna_string = input_file.read().strip("\n")
    # Multiply each amino acid in the sequence by its number of codons to get the total mRNA combinations.
    for aa in rna_string:
        total_combinations = total_combinations * codon_dict[aa]
        # The problem asks to provide the answer to modulo 1000000 to avoid dealing with very large numbers.
        total_combinations = total_combinations % 1000000

    return total_combinations


practice = calc_rna("rosalind_mrna.txt", codon_count)
print(practice)
