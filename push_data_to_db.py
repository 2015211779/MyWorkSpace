# coding=utf-8
# python_version:python3
import mysql.connector

jenkinsbuilddata = {'jenkinsbuilddata': {'Data': [[
    u'4041',
    u'SUCCESS',
    u'Started by upstream project "master/master-pipeline-merge" build number 3,054',
    '2020-02-02 21:41:37',
    u'https://cloudci.zte.com.cn/wireline-zenic-vdc/view/test-data-collect/job/master/job/test/job/master-test-worker/4041/',
    1145,
    '2020-02-07 11:22:31',
    u'master/master-pipeline-merge',
    u'master-pipeline-merge-3054-part1',
    86,
    0,
    86,
    u'4041',
    u'SUCCESS',
    76,
    u'SUCCESS',
    886,
    u'SUCCESS',
    121
]]},
    'Columns': [
        "build_num_api",
        "build_result",
        "trigger_reason",
        "build_time",
        "build_url",
        "build_duration",
        "grabdata_time",
        "version_num",
        "test_part_name",
        "test_total_count",
        "test_fail_count",
        "test_pass_count",
        "build_num_wfapi",
        "alloctopo_result",
        "alloctopo_duration",
        "deploy_result",
        "deploy_duration",
        "test_result",
        "test_duration"
    ]}


def push_data_to_db(table_name, db_name):
    columns = jenkinsbuilddata["Columns"]
    columns = tuple(columns)
    columns = str(columns).replace('\'', '')
    print(columns)
    rows = jenkinsbuilddata["jenkinsbuilddata"]["Data"]

    conn = mysql.connector.connect(host='127.0.0.1', port=3306, user='root',
                                   password='201211', database=db_name, charset='utf8')
    cursor = conn.cursor()

    for row in rows:
        row = tuple(row)
        # print(row)
        sql_insert_sentence = "insert into " + str(table_name) + columns + " values" + str(row)
        # print("sql_insert_sentence:", sql_insert_sentence)
        try:
            cursor.execute(sql_insert_sentence)
        except mysql.connector.errors.IntegrityError:
            print("Duplicate insert the following row:\n" + str(row))

    conn.commit()

    cursor.execute("select * from " + str(table_name))
    values = cursor.fetchall()
    for value in values:
        print(value)

    cursor.close()


if __name__ == '__main__':
    push_data_to_db("jenkinsbuilddata", "test")
