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
def info():
    return {'Caloric Value': 100, 'Protein': 10, 'Fat': 5}

@pytest.fixture
def meal_plan():
    return {'apple': 2, 'banana': 1}

@pytest.fixture
def test_csv(sample_data, tmpdir):
    file_path = tmpdir.join('Food_Nutrition_Dataset.csv')
    sample_data.to_csv(file_path, index=False)
    return file_path

def test_load_data_valid():
    df = load_data('Food_Nutrition_Dataset.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_load_data_invalid():
    with pytest.raises(FileNotFoundError) as exc_info:
        load_data('non_existent_file.csv')
    assert exc_info.type is FileNotFoundError

def test_search_food_by_name_valid():
    assert search_food_by_name('apple') == True
    assert search_food_by_name('banana') == True

def test_search_food_by_name_invalid():
    assert search_food_by_name('pudding') == False
    assert search_food_by_name('12') == False

def test_get_nutritional_info_valid():
    information = get_nutritional_info("cream cheese")
    assert information["Caloric Value"] == 51
    assert information["Protein"] == 0.9

def test_get_nutritional_info_invalid():
    information = get_nutritional_info("pudding")
    assert information == {}

def test_filter_nutritional_info_valid(info):
    filtered_categories, filtered_sizes, explode = filter_nutritional_info(info)
    assert len(filtered_categories) > 0
    assert len(filtered_sizes) > 0
    assert "Caloric Value" in filtered_categories

def test_filter_nutritional_info_invalid():
    filtered_categories, filtered_sizes, explode = filter_nutritional_info({})
    assert len(filtered_categories) == 0
    assert len(filtered_sizes) == 0
    assert len(explode) == 0

def test_create_pie_chart_valid():
    fig, ax = plt.subplots()
    wedges, texts, autotexts = create_pie_chart([10, 20, 30], ["A", "B", "C"], [0, 0.1, 0], ax)
    assert len(wedges) == 3

def test_create_pie_chart_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        create_pie_chart([], [], [], ax)

def test_create_bar_graph_valid():
    fig, ax = plt.subplots()
    create_bar_graph(["A", "B", "C"], [10, 20, 30], ax)
    assert len(ax.patches) == 3

def test_create_bar_graph_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        create_bar_graph([], [], ax)

def test_filter_food_by_range_valid(sample_data):
    filtered = filter_food_by_range(sample_data, "Fat", 0.1, 0.3)
    assert len(filtered) == 3
    assert "apple" in filtered["food"].values
    assert "banana" in filtered["food"].values
    assert "carrot" in filtered["food"].values

def test_filter_food_by_range_invalid(sample_data):
    with pytest.raises(KeyError):
        filter_food_by_range(sample_data, "pudding", 50, 90)

def test_get_food_details(sample_data, meal_plan):
    food_key, quantity, total_calories = get_food_details(sample_data, 'apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 104