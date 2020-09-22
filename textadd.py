#testing aggregation of data to per subject. will eventually be deleted from the repository
# test data - not part of the program.

import mysql.connector

cnx = mysql.connector.connect(user='spacecadet', password='3smashing3',
                              host='127.0.0.1',
                              database='ikon_som')
cursor = cnx.cursor()


query = "select * from (SELECT project_abstract,min(id) as pro_id \
	FROM ikon_som.projects \
    where project_abstract NOT LIKE '%Keine Zusammenfassung%' \
    GROUP BY project_abstract) as a \
    LEFT JOIN (SELECT project_id, subject_area from ikon_som.subject_area) as c \
    ON c.project_id = a.pro_id \
    LIMIT 5000;"


cursor.execute(query)
data = cursor.fetchall()

abstract_subject = {}

for paper_index in range(len(data)):
    if data[paper_index][3] in abstract_subject:
        abstract_subject[data[paper_index][3]] += ' ' + data[paper_index][0]
    else:
        abstract_subject[data[paper_index][3]] =  data[paper_index][0]
    print (paper_index)

x = 1
abstract_subject = {}
abstract_subject['a'] = 'bla'
x = "blue"
y = ['a','b']
for i in range(len(y)):
    if y[i] in abstract_subject:
        abstract_subject[y[i]] += ' ' + x 
    else:
        abstract_subject[y[i]] =  x 

#abstract_subject['a'] += ' ' + x

#abstract_subject['b'] += ' ' + x
y = 2
#for i in range(len(data)):
 #   if 



 #convert dict to list
 # for key, value in dict.iteritems():
 #   temp = [key,value]
 #   dictlist.append(temp)   

print(data)
