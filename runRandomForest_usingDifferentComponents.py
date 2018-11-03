import pandas as pd
import numpy as np
import datetime
import modelsFunc as models

train_queries_pca = r'/mnt/c/Users/shuyi/OneDrive/CS145/Data/after preprocess/train_queries_pca.csv'
validate_queries_pca = r'/mnt/c/Users/shuyi/OneDrive/CS145/Data/after preprocess/validate_queries_pca.csv'

train_data = pd.read_csv(train_queries_pca, header = None)
validate_data = pd.read_csv(validate_queries_pca, header = None)
print("Successfully load the data")

train_y = train_data[0]
validate_y = validate_data[0]

train_errors = list()
test_errors = list()

for i in range(10, 100, 10):
    selected_column = list(range(1, i))
    train_X = train_data[selected_column]
    validate_X = validate_data[selected_column]
    train_error, test_error = models.runRandomForest(train_X, train_y, validate_X, validate_y)
    train_errors.append(train_error)
    test_errors.append(test_error)

print(train_errors)
print(test_errors)