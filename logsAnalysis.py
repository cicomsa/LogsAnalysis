#!/usr/bin/env python
import psycopg2


def execute_query(query):
    try:
        connection = psycopg2.connect("dbname=news")
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        return result
    except psycopg2.Error as e:
        print('Connection error')
        print((e.pgerror))
        print((e.diag.message_detail))


def print_result(result):
    for i in range(len(result)):
        return (('%s. "%s" - %s views' %
                 (str(i + 1), result[i][0], str(result[i][1]))))


def print_last_result(result):
    date = result[0][0].strftime('%B %d, %Y')
    percent = str(result[0][1]) + '%'
    return (date + ' - ' + percent)


query_1 = """
    SELECT * \
    FROM viewed_articles \
    LIMIT 3 \
"""

query_2 = """
    SELECT name, sum(viewed_articles.views) AS views \
    FROM article_authors, viewed_articles \
    WHERE article_authors.title = viewed_articles.title \
    GROUP BY name \
    ORDER BY views desc \
"""

query_3 = """
    SELECT date, percent \
    FROM failed_logs \
    GROUP BY date, \
    percent HAVING percent > 1 \
    ORDER BY percent \
"""

result_1 = execute_query(query_1)
result_2 = execute_query(query_2)
result_3 = execute_query(query_3)

print('What are the most popular three  articles of all times?')
print(print_result(result_1))
print('--------------')
print('Who are the most popular three  article authors of all times?')
print(print_result(result_2))
print('--------------')
print('On which days did more than 1% of requests lead to errors?')
print((print_last_result(result_3)))
