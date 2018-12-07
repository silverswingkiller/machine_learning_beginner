'''
注意事项,csv文件名称不能出现中文,并且需要utf-8编码
转换方法,用记事本打开,另存为选项里有编码选择

'''

import os
import pandas as pd
#获取当前目录
dirpath=os.getcwd()
#获取当前文件夹内文件
filelist=os.listdir(dirpath)
#需要合并的列名
selected_columns=['日期']

out_xls=pd.DataFrame(columns=selected_columns)
for each in filelist:
    if os.path.isfile(each):
        if os.path.splitext(each)[1]=='.csv':
            tmp_xls=pd.read_csv(each)[selected_columns]
            out_xls=pd.concat((out_xls,tmp_xls))
        elif os.path.splitext(each)[1] in ['.xls','.xlsx']:
            tmp_xls=pd.read_excel(each)[selected_columns]
            out_xls=pd.concat((out_xls,tmp_xls))
#输出文件名
out_xls.to_excel('result.xls')