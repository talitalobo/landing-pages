# coding: utf-8

import sys
import csv
import re

# open input file
redemet = open(sys.argv[1], 'r')
final_file = sys.argv[2]

data = []
datamax = 0
datamaxcond = 0


# tirar COR das mensagens (2013) - ok
# a visibilidade tambem pode vir assim: 7000 3000NW (N, S, E, O, NE, SE, NW, SW)
# o vento (KT) pode ter um complemento que tem V ou G (pode aparecer ou não) 

# decoding line information
def decode_line(line):
	global datamax
	global datamaxcond

	print("# ----------- Começando decodificacao: ")

	line = re.sub('(\d{2})(\d{2})(?= Q)', '\\1/\\2', line)
	line = re.sub('(Q\d{0,3}) ', '\\1', line)

	line = line.replace("=", "").strip()
	line = line.replace("COR", "")
	lista = line.split(' ')

	timestamp = ''
	airport = lista[2]
	timezone = lista[3]
	dir_int = ''
	visibility = lista[5]
	weather = ''
	cloud_group = ''
	t_td = [10]
	pressure = ''
	rerarets = 'NULL'
	tre_obs = ''
	
	listc = []
	listcond = []

	for word in lista:
		if len(word) == 10:
			timestamp = word
		elif "KT" in word:
			dir_int = word
		elif len(word) == 2 or len(word) == 3:
			listcond.append(word)
		elif "SCT" in word or "FEW" in word or "BKN" in word or "OVC" in word:
			listc.append(word)
		elif "/" in word:
			t_td = word
		elif "Q" in word:
			pressure = word
		elif "RERA" in word or "RETS":
			rera = word
	
	if datamax < len(listc):
		datamax = len(listc) 
	if datamaxcond < len(listcond):
		datamaxcond = len(listcond)

	tre_obs = [timestamp, airport, timezone, dir_int, visibility, listcond, listc, t_td, pressure, rerarets]
	data.append(tre_obs)



# iterating on redmet file
for observation in redemet:
	if "Mensagem METAR" not in observation:
		decode_line(observation)

for element in data:
	while len(element[6]) < datamax:
		element[6].append("na")
	element[6] = ','.join(element[6])
	while len(element[5]) < datamaxcond:
		element[5].append("na")
	element[5] = ','.join(element[5])


with open(final_file, 'w') as csvfile:
	fieldnames = ['Timestamp', 'Airport', 'Timezone', 'DirInten', 'Visibility'] + ['Weather%d' % x for x in range(datamaxcond)] + ['CG%d'% y for y in range(datamax)] + ['TTD', 'Pressure', 'ReraRets']
	
	csvfile.write(','.join(fieldnames) + "\n")

	for element in data:
		print(element)
		csvfile.write(','.join(element) + "\n")


print("# ----------- Arquivo finalizado ")

