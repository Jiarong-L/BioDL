
import gzip


raw_file_source = 'SILVA_132_SSURef_Nr99_tax_silva.fasta.gz'
file_source = 'SILVA.fa'



first_line = True
with gzip.open(raw_file_source, 'rb') as fr, open(file_source, 'w') as fw:
    for line in fr:
        line = line.decode()
        if '>' in line:
            if first_line:
                first_line = False
            else:
                fw.write('\n')
            fw.write(line)
        else:
            fw.write(line.strip())






# len_dict = {
#     'Archaea': [],
#     'Bacteria': [],
#     'Eukaryota': []
# }
# with open(file_source,'r') as fr:
#     while True:
#         lineH = fr.readline()
#         lineS = fr.readline()
#         if not lineS:
#             break
#         len_dict[lineH.strip().split(';')[0].split(' ')[-1]].append(len(lineS.strip()))

# print(min(len_dict['Archaea']), max(len_dict['Archaea']))        ## 900 3106
# print(min(len_dict['Bacteria']), max(len_dict['Bacteria']))      ## 1200 4000
# print(min(len_dict['Eukaryota']), max(len_dict['Eukaryota']))    ## 900 3930



def extract_seq(file_source, key_word, max_num = 15000, max_len = 3200, min_len = 1200):
    file_target = '{}.fa'.format(key_word)
    with open(file_source,'r') as fr, open(file_target, 'w') as fw:
        while True:
            lineH = fr.readline()
            lineS = fr.readline()
            if (not lineS) or (max_num <= 0) :
                break
            if key_word in lineH.split(';')[0]:
                if len(lineS) <= max_len and len(lineS) >= min_len:
                    max_num -= 1
                    fw.write(lineH)
                    fw.write(lineS)


extract_seq(file_source, 'Archaea', max_num = 10000, max_len = 3100, min_len = 1200)
extract_seq(file_source, 'Bacteria', max_num = 10000, max_len = 3100, min_len = 1200)


