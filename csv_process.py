import os
import pandas as pd

dataset = 'Davis'
data = pd.read_csv('data/' + dataset + '/' + dataset + '.csv')

data = data.sample(frac=1, random_state=42).reset_index(drop=True)

train_data = data.iloc[:800]
test_data = data.iloc[800:1000].reset_index(drop=True)
print(train_data, test_data)

os.makedirs('data/' + dataset + '/DTA/fold/1', exist_ok=True)

train_data.to_csv('data/' + dataset + '/DTA/fold/1/' + dataset + '_train.csv')
test_data.to_csv('data/' + dataset + '/DTA/fold/1/' + dataset + '_test.csv')