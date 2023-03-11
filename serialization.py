import json
import pandas as pd

def load_csv(path):
    data = pd.read_csv(path)
    return data


def transform_data(data):
    accepted_varieties = ['White Wine', 'Red Wine']
    min_rating = 90
    max_rating = 92

    for row in range(len(data)):
        wrong_variety = data['variety'][row] not in accepted_varieties
        wrong_rating = data['rating'][row] < min_rating or data['rating'][row] > max_rating
        if wrong_variety or wrong_rating:
            data = data.drop(row)
    
    return data


def serialize_json(path):
    with open(path, encoding="utf8") as f:
        data = json.load(f)
        return data


data = load_csv('sample_data/wine-ratings-small.csv')
data = transform_data(data)
print(data)