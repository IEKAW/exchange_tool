# coding: utf8

from django.db import connection


def calculate_date(from_date, to_date):
    '''
    テーブルの一覧を取得する
    '''
    sql = """
        SELECT
            *
        FROM
            polls_kessai
        WHERE
            contract_date <= %s
        ORDER BY
            contract_date
    """
    cursor = connection.cursor()
    params = (from_date)
    cursor.execute(sql, params=params)
    for row in cursor.fetchall():
        yield row
