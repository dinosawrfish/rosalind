def count_nuc(s):

    counter = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }

    for nuc in s:
        counter[nuc] += 1

    return f'{counter["A"]} {counter["C"]} {counter["G"]} {counter["T"]}'


if __name__ == "__main__":

    dna_string = ""

    with open('../data/dna_data.txt', 'r') as file:
        dna_string = file.readline().strip()

    ans = count_nuc(dna_string)

    print(ans)