import re
import csv
from pprint import pprint
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
new_phonebook = []
new_list = []
for contact in contacts_list[1:]:
  contact_list = []
  fio = " ".join(contact)
  tel = re.compile(r"(\+7|8)\s*\(*(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d+)")
  result_tel = tel.sub(r"+7(\2)\3-\4-\5", contact[5])
  dob = re.compile(r"\s*\(*доб. (\d+)\)*")
  result_dob = dob.sub(r" доб.\1", result_tel)
  fio1 = fio.split(" ")
  fio_ = fio1[:3]
  contact_list = [fio_[0], fio_[1], fio_[2], contact[3], contact[4], result_dob, contact[6]]
  if fio_[:2] not in new_list:
    new_list.append(fio_[:2])
    new_phonebook.append(contact_list)
  for new_con in new_phonebook:
    if fio_[0] and fio_[1] in new_con:
      for j in range(len(new_con)):
        if new_con[j] == '':
          new_con[j] = contact[j]
new_phonebook.insert(0, contacts_list[0])
# pprint(new_phonebook)
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_phonebook)
