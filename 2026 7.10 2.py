import pandas as pd
import numpy as np
try:
    df = pd.read_csv('train.csv')
except:
    data = {
        'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Survived': [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
        'Pclass': [3, 1, 3, 1, 3, 3, 1, 3, 2, 3],
        'Name': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'female', 'male', 'female', 'male'],
        'Age': [22, 38, 26, 35, 35, None, 54, None, 2, 27],
        'SibSp': [1, 1, 0, 1, 0, 0, 0, 3, 4, 1],
        'Parch': [0, 0, 0, 0, 0, 0, 2, 1, 1, 0],
        'Fare': [7.25, 71.28, 7.93, 53.10, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07],
        'Embarked': ['S', 'C', 'S', 'S', 'S', 'Q', 'S', 'S', 'S', None]
    }
    df = pd.DataFrame(data)
print("缺失值统计：")
print(df.isnull().sum())
df1 = df.drop('Cabin', axis=1, errors='ignore')
df1['Age'] = df1['Age'].fillna(df1['Age'].median())
df1['Embarked'] = df1['Embarked'].fillna(df1['Embarked'].mode()[0])
print("\n处理后缺失值统计：")
print(df1.isnull().sum())
print(f"\n原始行数：{len(df1)}")
df1 = df1.drop_duplicates(subset=['Name'], keep='first')
print(f"去重后行数：{len(df1)}")
df1['Sex'] = df1['Sex'].map({'male': 0, 'female': 1})
df1['Embarked'] = df1['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
print("\n最终数据类型：")
print(df1.dtypes)
print("\n任务一完成")