from pandas.io.json import json_normalize
import pandas as pd
import json
import time


if __name__ == '__main__':
    # 读入数据
    data_str = open('new 2.json').read()
    # print(data_str)
    for i in range(0, 10):
        data_list = json.loads(data_str)
        print(data_list)
    #     data = [[d['bigberg'], d['smallberg']] for d in data_list]
    #     df = pd.DataFrame(data, columns=['bigberg', 'smallberg'])
    #
    # print(df)
