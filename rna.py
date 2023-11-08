def to_rna(dna_strand):
    """Вычисляет результат транскрипции РНК
    :param dna_strand: строка ДНК из символов ACGT
    :return: строка РНК из символов UGCA
    """
    nucleotide_map = {"A": "U", "C": "G", "G": "C", "T": "A"}
    rna_strand = ""
    for i in dna_strand:
        rna_strand += nucleotide_map.get(i, "")
    return rna_strand
