# Soal 2
# Ujian_Balik_Elemen_List

def balikPosisi(data):
   ListData = len(data)
   data_list = []
   for i in range(ListData):
     data_list.append(data[ListData - i - 1])
   return data_list

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))