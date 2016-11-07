import pymysql


class DBConnect:

    def execute_select_query(query):
        # this method connects to DB and execute select query then it returns the query result
        conn = pymysql.connect(host='10.1.22.67', port=3306, user='Selenium', passwd='python', db='peel')
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchone()
        return result