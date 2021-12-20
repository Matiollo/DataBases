import psycopg2
import matplotlib.pyplot as plt

connect = psycopg2.connect(user="postgres", password="Omezoh38", host="localhost", port="5432", database="course_work")
cursor = connect.cursor()

cursor.execute("explain analyze select height from participants where height>80")
connect.commit()
res = cursor.fetchall()

results = []
cursor.execute('set enable_seqscan to on;')
connect.commit()
for j in range(100):
    cursor.execute("explain analyze select height from participants where height>80")
    connect.commit()
    res = cursor.fetchall()
    for i in res:
        if i[0].find('Execution') > -1:
            result = None
            for k in i[0].split():
                try:
                    result = float(k)
                    break
                except:
                    continue
            results.append(result)
cursor.execute('create index idxheight on participants(height)')
connect.commit()
print(results)

cursor.execute('set enable_seqscan to off;')
connect.commit()

results2 = []
for j in range(100):
    cursor.execute("explain analyze select height from participants where height>80")
    connect.commit()
    res = cursor.fetchall()
    for i in res:
        if i[0].find('Execution') > -1:
            result = None
            for k in i[0].split():
                try:
                    result = float(k)
                    break
                except:
                    continue
            results2.append(result)
print(results2)

plt.plot(results)
plt.plot(results2)
plt.show()
cursor.close()
connect.close()
