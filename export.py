import csv
import cx_Oracle

username = 'katyak'
password = '96katyak96'
databaseName = 'localhost/xe'

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()

insurance_tables = ['human', 'country', 'human_insurance', 'human_trip', 'insurance_agency']

for table in serials_tables:
    with open (table + '.csv', 'w', newline="") as file:
        cursor.execute("SELECT * FROM " + table)
        database = cursor.fetchall()

        csv_writer=csv.writer(file, delimiter = ',')

        for row in database:
            csv_writer.writerow(row)

cursor.close()
connection.close()