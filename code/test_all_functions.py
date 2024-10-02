import pytest
import matplotlib.pyplot as plt
from all_functions import DataTable, load_data, search_food_by_name, get_nutritional_info, filter_nutritional_info, create_pie_chart, create_bar_graph, filter_food_by_nutrient_range, filter_food_by_nutrient_level, get_food_details, generate_meal_plan, generate_total_calories, remove_food_from_meal_plan
import pandas as pd

EVEN_ROW_COLOUR = '#CCE6FF'

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'food': ['apple', 'banana', 'carrot'],
        'Caloric Value': [52, 89, 41],
        'Protein': [0.3, 1.1, 0.9],
        'Fat': [0.1, 0.3, 0.2]
    })

@pytest.fixture
def data_table(sample_data):
    return DataTable(sample_data)

@pytest.fixture
def meal_plan():
    return {'apple': 2, 'banana': 1}

@pytest.fixture
def cream_cheese_info():
    return {
    'Caloric Value': 51,
    'Fat': 5,
    'Saturated Fats': 2.9,
    'Monounsaturated Fats': 1.3,
    'Polyunsaturated Fats': 0.2,
    'Carbohydrates': 0.8,
    'Sugars': 0.5,
    'Protein': 0.9,
    'Dietary Fiber': 0,
    'Cholesterol': 14.6,
    'Sodium': 0.016,
    'Water': 7.6,
    'Vitamin A': 0.2,
    'Vitamin B1': 0.033,
    'Vitamin B11': 0.064,
    'Vitamin B12': 0.092,
    'Vitamin B2': 0.097,
    'Vitamin B3': 0.084,
    'Vitamin B5': 0.052,
    'Vitamin B6': 0.096,
    'Vitamin C': 0.004,
    'Vitamin D': 0,
    'Vitamin E': 0,
    'Vitamin K': 0.1,
    'Calcium': 0.008,
    'Copper': 14.1,
    'Iron': 0.082,
    'Magnesium': 0.027,
    'Manganese': 1.3,
    'Phosphorus': 0.091,
    'Potassium': 15.5,
    'Selenium': 19.1,
    'Zinc': 0.039,
    'Nutrition Density': 7.07
}

def test_load_data_valid():
    df = load_data('Food_Nutrition_Dataset.csv')
    assert not df.empty

def test_load_data_invalid():
    with pytest.raises(FileNotFoundError) as exc_info:
        load_data('non_existent_file.csv')
    assert exc_info.type is FileNotFoundError

def test_search_food_by_name_valid():
    assert search_food_by_name('apple') == True
    assert search_food_by_name('banana') == True
    assert search_food_by_name('pudding') == False

def test_search_food_by_name_invalid():
    with pytest.raises(ValueError) as exc_info:
        search_food_by_name(12)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        search_food_by_name(' ')
    assert exc_info.type is ValueError

def test_get_nutritional_info_valid(cream_cheese_info):
    assert get_nutritional_info("cream cheese") == cream_cheese_info

def test_get_nutritional_info_invalid():
    with pytest.raises(ValueError) as exc_info:
        get_nutritional_info("pudding")
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        get_nutritional_info("12")
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        get_nutritional_info(" ")
    assert exc_info.type is ValueError

def test_filter_nutritional_info_valid(cream_cheese_info):
    assert filter_nutritional_info(cream_cheese_info) is not None

def test_filter_nutritional_info_invalid():
    with pytest.raises(ValueError) as exc_info:
        filter_nutritional_info({})
    assert exc_info.type is ValueError

def test_create_pie_chart_valid():
    assert len(create_pie_chart([10, 20, 30], ["A", "B", "C"], [0, 0.1, 0], plt.subplots()[1])[0]) == 3

def test_create_pie_chart_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError) as exc_info:
        create_pie_chart([], [], [], ax)
    assert exc_info.type is ValueError

def test_create_bar_graph_valid():
    assert len((lambda ax: (create_bar_graph(["A", "B", "C"], [10, 20, 30], ax), ax)[1].patches)(plt.subplots()[1])) == 3

def test_create_bar_graph_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError) as exc_info:
        create_bar_graph([], [], ax)
    assert exc_info.type is ValueError

def test_filter_food_by_nutrient_range_valid():
    assert len(filter_food_by_nutrient_range("Fat", 0.1, 0.3)) == 311

def test_filter_food_by_nutrient_range_invalid():
    with pytest.raises(ValueError) as exc_info:
        filter_food_by_nutrient_range("fat", None, 10)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        filter_food_by_nutrient_range("fat", 11, None)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        filter_food_by_nutrient_range("fat", 11, 10)
    assert exc_info.type is ValueError

def test_filter_food_by_nutrient_level_valid():
    assert len(filter_food_by_nutrient_level("Fat", "High")) == 3
    assert len(filter_food_by_nutrient_level("Fat", "Mid")) == 11
    assert len(filter_food_by_nutrient_level("Fat", "Low")) == 2381

def test_filter_food_by_nutrient_level_invalid():
    with pytest.raises(ValueError) as exc_info:
        filter_food_by_nutrient_level("Fat", "loow")
    assert exc_info.type is ValueError

def test_get_food_details_valid(meal_plan):
    food_key, quantity, total_calories = get_food_details('apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 190

def test_get_food_details_invalid(meal_plan):
    with pytest.raises(ValueError) as exc_info:
        get_food_details('nonexistent_food', meal_plan)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        get_food_details(12, meal_plan)
    assert exc_info.type is ValueError

def test_generate_meal_plan_valid(meal_plan):
    generate_meal_plan(meal_plan, 'cream cheese', 2)
    assert meal_plan['cream cheese'] == 2

    generate_meal_plan(meal_plan, 'apple', 3)
    assert meal_plan['apple'] == 5

def test_generate_meal_plan_invalid(meal_plan):
    with pytest.raises(ValueError) as exc_info:
        generate_meal_plan(meal_plan, 'pudding', 2)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        generate_meal_plan(meal_plan, 'apple', -2)
    assert exc_info.type is ValueError

    with pytest.raises(ValueError) as exc_info:
        generate_meal_plan(meal_plan, 'apple', 51)
    assert exc_info.type is ValueError

def test_generate_total_calories_valid(meal_plan):
    assert generate_total_calories(meal_plan) == 324
    assert generate_total_calories({}) == 0

def test_generate_total_calories_invalid(meal_plan):
    with pytest.raises(ValueError) as exc_info:
        generate_total_calories([])
    assert exc_info.type is ValueError

def test_remove_food_from_meal_plan_valid(meal_plan):
    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'apple': 1, 'banana': 1}

    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'banana': 1}

def test_remove_food_from_meal_plan_invalid(meal_plan):
    with pytest.raises(KeyError) as exc_info:
        remove_food_from_meal_plan(meal_plan, 'carrot', 2)
    assert exc_info.type is KeyError

def test_get_number_rows(data_table):
    assert data_table.GetNumberRows() == 3

def test_get_number_cols(data_table):
    assert data_table.GetNumberCols() == 4

def test_get_value_valid(data_table):
    assert data_table.GetValue(0, 0) == 'apple'

def test_get_value_invalid(data_table):
    with pytest.raises(IndexError) as exc_info:
        data_table.GetValue(10, 10)
    assert exc_info.type is IndexError

def test_set_value_valid(data_table):
    data_table.SetValue(0, 0, 10)
    assert data_table.GetValue(0, 0) == 10

def test_set_value_invalid(data_table):
    with pytest.raises(IndexError) as exc_info:
        data_table.SetValue(10, 10, 100)
    assert exc_info.type is IndexError

def test_get_col_label_value_valid(data_table):
    assert data_table.GetColLabelValue(0) == 'food'
    assert data_table.GetColLabelValue(1) == 'Caloric Value'

def test_get_col_label_value_invalid(data_table):
    with pytest.raises(IndexError) as exc_info:
        data_table.GetColLabelValue(10)
    assert exc_info.type is IndexError

def test_get_attr_valid(data_table):
    assert data_table.GetAttr(3, 0, None).GetBackgroundColour() == EVEN_ROW_COLOUR
    assert not data_table.GetAttr(0, 0, None).HasBackgroundColour()

def test_get_attr_invalid(data_table):
    assert data_table.GetAttr(10, 0, None) is not None
    assert data_table.GetAttr(0, 10, None) is not None
