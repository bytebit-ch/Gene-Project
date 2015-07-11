import sqlite3 as lite
import sys

genome_text_file = sys.argv[1]
name = sys.argv[2]
database = sys.argv[3]


connection = lite.connect(database)
try:
	cursor = connection.cursor()
	gene_file = open(genome_text_file, 'r+')
	cursor.execute("DELETE FROM genome_table where person=?", (name,))

	line_num = 0

	gene_list = []

	for line in gene_file: 
		if len(line) == 0 or line[0] == "#":
			continue

		a = line.strip('\n').split('\t')
		gene_list.append(a)



	for lists in gene_list:
		if len(lists) < 4:
			continue
		
		cursor.execute(
			"INSERT into genome_table(person, rsid, chromosome, position, genotype) values(?, ?, ?, ?, ?)", 
			(name, lists[0], lists[1], int(lists[2]),lists[3]))
finally:
	connection.commit()
	connection.close()
