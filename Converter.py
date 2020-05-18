import csv

openFile = open('resource\postalcodes.csv', 'r', encoding="utf-8-sig")
csvFile = csv.reader(openFile, delimiter = ';', quotechar = '\'')

header = next(csvFile)

headers = map((lambda x: x), header)
insert = 'insert into postalcode (' + ", ".join(headers) + ") values "

sqlFile = open('resource\insertStatements.txt', 'w', encoding='utf-8-sig')

for row in csvFile:
    values = map((lambda x: '\''+x+'\''), row)
    msg = insert +"("+ ", ".join(values) +");"
    print (msg)
    sqlFile.write(msg + "\n")
openFile.close()
sqlFile.close()
