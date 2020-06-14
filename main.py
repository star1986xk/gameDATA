import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


class GameData(object):
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)

    #各个游戏公司在各个年龄段中的平均得分（区分性别）
    def company_age_avg_score(self):
        self.df['age'] = np.floor(self.df['age'].astype('float') / 10) * 10
        self.df['age'] = self.df['age'].astype('int')
        df = self.df.groupby(['game_company', 'age', 'sex']).mean()
        print(df['score'])

        df = df['score'].unstack().unstack()
        df.plot(kind='bar')
        plt.show()

    #各个年龄段在各个性别中参与打分的总人数
    def age_sex_count(self):
        self.df['age'] = np.floor(self.df['age'].astype('float') / 10) * 10
        self.df['age'] = self.df['age'].astype('int')
        df = self.df.groupby(['age', 'sex']).count()
        print(df['username'])

        df = df['username'].unstack()
        df.plot(kind='bar')
        plt.show()

    #各个性别玩游戏的人员的平均年龄
    def sex_avg_age(self):
        df = self.df.groupby(['sex']).mean()
        print(df['age'])

        df['age'].plot(kind='bar')
        plt.show()

    #各个游戏公司的平均得分并按照从大到小排序且选出top3
    def company_avg_score(self):
        df = self.df.groupby(['game_company']).mean()
        df = df.sort_values(['score'], ascending=False).head(3)
        print(df['score'])

        df['score'].plot()
        plt.show()

    #各个国家在各个年龄段玩游戏的分布情况
    def country_age_count(self):
        self.df['age'] = np.floor(self.df['age'].astype('float') / 10) * 10
        self.df['age'] = self.df['age'].astype('int')
        df = self.df.groupby(['country', 'age']).count()
        print(df['username'])

        df = df['username'].unstack()
        df.plot(kind='bar')
        plt.show()

if __name__ == '__main__':
    # file_path = 'game.csv'
    file_path = input('读取csv文件：')
    OBJ = GameData(file_path)
    flag = True
    while flag:
        print('''
        选择功能：
        1.各个游戏公司在各个年龄段中的平均得分（区分性别）
        2.各个年龄段在各个性别中参与打分的总人数
        3.各个性别玩游戏的人员的平均年龄
        4.各个游戏公司的平均得分并按照从大到小排序且选出top3
        5.各个国家在各个年龄段玩游戏的分布情况
        6.退出
        ''')
        option = input('请输入：')
        if option == '1':
            OBJ.company_age_avg_score()
        elif option == '2':
            OBJ.age_sex_count()
        elif option == '3':
            OBJ.sex_avg_age()
        elif option == '4':
            OBJ.company_avg_score()
        elif option == '5':
            OBJ.country_age_count()
        elif option == '6':
            flag = False

