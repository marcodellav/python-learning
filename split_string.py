import re

with open("list.txt") as f:

    for line in f:
        if line in ['\n', '\r\n']:
            break

        DATA = line
        DATA2 = re.split(' ', DATA, maxsplit=2)
        DATA3 = str(DATA2[2])
        DATA2_1 = str(DATA2[0])
        DATA2_2 = str(DATA2[1])
        DATA4 = re.split('[\s\s|\[\s|\s\]]', DATA3, maxsplit=8)
        print(DATA4)
        DATA5 = str('[  ' + (DATA4[3]) + ' ' + (DATA4[4]) + '   ' + (DATA4[7]) + ']')
        DATA9 = ((DATA4)[8])
        DATA10 = re.split(' ', DATA9, maxsplit=5)
        DATA11 = str(DATA10[1] + ' ' + DATA10[2] + ' ' + DATA10[3] + ' ' + (DATA10[4]))
        DATA12 = str(DATA10[5])
        print((DATA2_1) + ', ' + (DATA2_2) + ', ' + (DATA5) + ', ' + (DATA11) + ', ' + (DATA12))

        with open("test.csv", "a") as myfile:
            myfile.write((DATA2_1) + ', ' + (DATA2_2) + ', ' + (DATA5) + ', ' + (DATA11) + ', ' + (DATA12))
