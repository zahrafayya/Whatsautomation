import pywhatkit as pw
from sys import stdin

text = "man, tolong join grup wa sch nlc ya :D"

number = []
name = []

print("Input number:")
for line in stdin:
    end_statement = "end\n"
    if(line == end_statement): break
    else:
        number.append(line.rstrip())

print("Input name:")
for line in stdin:
    end_statement = "end\n"
    if(line == end_statement): break
    else: name.append(line.rstrip())

if(len(number) == len(name)):
    i = 0
    for x in number:
        text = 'Halo, ' + name[i] + '!\n\nTerima kasih telah membeli tiket Schematics NST 2022. Open gate untuk Schematics NST akan dilaksanakan pada hari *Sabtu, 22 Oktober 2022 jam 09.00* sehingga dimohon untuk hadir tepat waktu.\n\nTidak akan ada penukaran tiket fisik sehingga mohon menunjukkan tiket digital/QR Code yang terdapat pada laman pembayaran di schematics.its.ac.id. Seluruh informasi mengenai acara Schematics NST dapat diakses melalui sosial media Schematics.\n\nInstagram Schematics: @schematics.its\n\nSalam,\nKesekretariatan Schematics'
        pw.sendwhatmsg_instantly(number[i], text, 10, True, 5)
        print(number[i])
        # print(text)
        i += 1
