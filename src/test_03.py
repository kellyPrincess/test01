# coding=utf-8

import pandas as pd
import json
import pymysql
import traceback

key1 = ['city', 'source', 'datatype', 'receiveTime', 'data']
key2 = ['PLAN_ID', 'crawlAt', 'housingDataType', 'keyRoute', 'oppositeId', 'oppositeurl'
    , '中介人', '中介人链接', '中介机构', '中介门店', '主体朝向', '二手房套数', '供暖方式', '前缀'
    , '单价', '城市', '容积率', '小区名称', '小区链接', '建成年代', '建筑面积', '开发商', '总价'
    , '总户数', '户型', '房源标签', '房源标题', '房源编号', '抓取时间', '月供', '来源', '楼层'
    , '源描述', '源链接', '片区名称', '物业公司', '物业管理费', '物业类型', '看房时间', '租房套数'
    , '类型', '纬度', '经度', '经纪人id', '绿化率', '联系电话', '行政区名称', '首付']


def parse_json(d):
    l = []
    for k in key1:
        if k != 'data':
            l.append(d[k])
        else:
            for k2 in key2:
                l.append(d[k][k2])
    return l




if __name__ == '__main__':

    # df = pd.DataFrame([['a', 'b'], ['c', 'd']],index=['row 1', 'row 2'],columns=['col 1', 'col 2'])
    # print(df)
    # df.to_json("df_table.json",orient='table')
    # print()
    # df = pd.read_json('df.json', orient='split')
    # print(df)

    con = pymysql.connect(host="127.0.0.1", user='root', password='root', database='test', charset='utf8')
    cursor = con.cursor()
    sql = '''insert into raw_data VALUES ({0})'''.format(("%s,"*52)[:-1])

    line = ''
    flag = 0
    try:
        with open("test.json","r", encoding='utf-8') as f:
            for line in f:
                flag += 1
                pp = parse_json(json.loads(line))
                cursor.execute(sql, pp)
                if 500 == flag:
                    con.commit()
    except Exception as e:
        traceback.print_exc()
        print(line)
    finally:
        con.commit()
        cursor.close()
        con.close()
        print("ok!!!")
