import psycopg2

connection = psycopg2.connect("dbname=news")
cursor = connection.cursor()


def execute_query(query):
    cursor.execute(query)
    return cursor.fetchall()


def print_result(result):
    for i in range(len(result)):
        print(str(i + 1) + '. ' + '"' + result[i][0] + '"' +
              ' - ' + str(result[i][1]) + ' views')


def print_last_result(result):
    date = result[0][0].strftime('%B %d, %Y')
    percent = str(result[0][1]) + '%'
    return (date + ' - ' + percent)


query_1 = 'select articles.title, count(*) as num from articles, log where log.status like \'%200%\' and log.path ~ articles.slug group by articles.title order by num desc limit 3'

query_2 = 'select authors.name, count(*) as num from authors, articles, log where log.status like \'%200%\' and authors.id = articles.author and log.path ~ articles.slug group by authors.name order by num desc limit 4'

query_3 = 'select failedlogs.date, round(100.0*countfailedlogs/countalllogs,2) as percent from existinglogs, failedlogs where existinglogs.date = failedlogs.date and countfailedlogs*100 / countalllogs > 1'

result_1 = execute_query(query_1)
result_2 = execute_query(query_2)
result_3 = execute_query(query_3)

print('What are the most popular three  articles of all times?')
print_result(result_1)
print('--------------')
print('Who are the most popular three  article authors of all times?')
print_result(result_2)
print('--------------')
print('On which days did more than 1% of requests lead to errors?')
print(print_last_result(result_3))

connection.close()
