from pprint import pprint
import re
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

pattern = r'(8|\+7).*(495)(\D*)(\d{3})(\D*)(\d{2})(\D*)(\d{2})(\s?)\(?(\w*\.?)\s?(\d*)\)?'
repl = r'+7(\2)\4-\6-\8\9\10\11'
con_list = []

for el in contacts_list:

  s = ','.join(el)
  res = re.sub(pattern, repl, s)
  con_list.append(res.split(','))


with open('test.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerows(con_list)

pattern1 = r'(^\w+)\s?\,?(\w+)\,?\s?(\w+)?(\W+)'
repl1 = r'\1,\2,\3,'
final_data = []
with open("test.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

    for el in contacts_list:
        s = ','.join(el)
        res = re.sub(pattern1, repl1, s)
        l = res.split(',')
        final_data.append(l)
b = {}
for el in final_data:
    q = (el[0], el[1])
    if q in b:
        for data in (el[2:]):

            if data in b[q]:
                pass
            else:
                if len(data) > 20 and '@' not in data:
                    if b[q][2] == '':
                        b[q][2] = data
                    else:
                        b[q].insert(2,data)
                else:
                    if b[q][-1] == '':
                        b[q][-1] = data
                    else:
                        b[q].append(data)
    else:
        b[q] = el[2:]
w = []
for el in b:
    e = []
    e.extend(el)
    e.extend(b[el])
    w.append(e)

with open("phonebook.csv", "w", newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(w)


