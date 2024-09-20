import pytest
import pandas as pd
from all_functions import *

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'food': ['apple', 'banana', 'carrot'],
        'Caloric Value': [52, 89, 41],
        'Protein': [0.3, 1.1, 0.9],
        'Fat': [0.2, 0.3, 0.2]
    })

@pytest.fixture
def meal_plan():
    return {'apple': 2, 'banana': 1}

def test_get_nutritional_info(sample_data, mocker):
    mocker.patch('all_functions.pd.read_csv', return_value=sample_data)
    result = get_nutritional_info('apple')
    expected = {'Caloric Value': 52, 'Protein': 0.3, 'Fat': 0.2}
    assert result == expected

def test_filter_nutritional_info():
    categories = ['Protein', 'Fat', 'Carbs']
    sizes = [10, 20, 30]
    filtered_categories, filtered_sizes, explode = filter_nutritional_info(categories, sizes)
    assert filtered_categories == ['Protein', 'Fat', 'Carbs']
    assert filtered_sizes == [10, 20, 30]
    assert explode == [0.1, 0.0, 0.0]

def test_create_pie_chart():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    filtered_sizes = [10, 20, 30]
    filtered_categories = ['Protein', 'Fat', 'Carbs']
    explode = [0.1, 0.0, 0.0]
    pie = create_pie_chart(filtered_sizes, filtered_categories, explode, ax)
    assert pie is not None

def test_create_bar_graph():
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    filtered_categories = ['Protein', 'Fat', 'Carbs']
    filtered_sizes = [10, 20, 30]
    bar = create_bar_graph(filtered_categories, filtered_sizes, ax)
    assert bar is not None

def test_filter_food_by_nutrition(sample_data):
    result = filter_food_by_nutrition(sample_data, 'Caloric Value', 50, 100)
    expected = sample_data[sample_data['food'].isin(['apple', 'banana'])]
    pd.testing.assert_frame_equal(result, expected[['food', 'Caloric Value']])

def test_get_food_details(sample_data, meal_plan):
    food_key, quantity, total_calories = get_food_details(sample_data, 'apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 104