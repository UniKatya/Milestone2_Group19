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
    assert search_food_by_name(' ') == False

def test_get_nutritional_info_valid(cream_cheese_info):
    information = get_nutritional_info("cream cheese")
    assert information == cream_cheese_info

def test_get_nutritional_info_invalid():
    with pytest.raises(ValueError):
        get_nutritional_info("pudding")

def test_filter_nutritional_info_valid(cream_cheese_info):
    categories, sizes, explode = filter_nutritional_info(cream_cheese_info)
    assert categories == ['Caloric Value', 'Selenium', 'Potassium', 'Cholesterol', 'Copper', 'Water', 'Nutrition Density', 'Fat', 'Others']
    assert sizes == [51, 19.1, 15.5, 14.6, 14.1, 7.6, 7.07, 5, 8.984999999999996]
    assert explode == [0.1] + [0.0] * (len(categories) - 1)

def test_filter_nutritional_info_invalid():
    with pytest.raises(ValueError):
        filter_nutritional_info({})

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

def test_filter_food_by_nutrient_range_valid():
    filtered = filter_food_by_nutrient_range("Fat", 0.1, 0.3)
    assert len(filtered) == 311

def test_filter_food_by_nutrient_range_invalid():
    with pytest.raises(ValueError):
        filter_food_by_nutrient_range("pudding", 11, 10)

def test_filter_food_by_nutrient_level_valid():
    filtered = filter_food_by_nutrient_level("Fat", "High")
    assert len(filtered) == 3
    filtered = filter_food_by_nutrient_level("Fat", "Mid")
    assert len(filtered) == 11
    filtered = filter_food_by_nutrient_level("Fat", "Low")
    assert len(filtered) == 2381

def test_filter_food_by_nutrient_level_invalid():
    with pytest.raises(ValueError):
        filter_food_by_nutrient_level("Fat", "loow")

def test_get_food_details_valid(meal_plan):
    food_key, quantity, total_calories = get_food_details('apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 190

def test_get_food_details_invalid(meal_plan):
    with pytest.raises(ValueError):
        get_food_details('nonexistent_food', meal_plan)

def test_generate_meal_plan_valid(meal_plan):
    name, quantity = generate_meal_plan(meal_plan, 'cream cheese', 2)
    assert meal_plan['cream cheese'] == 2
    assert name == 'cream cheese'
    assert quantity == 2

    name, quantity = generate_meal_plan(meal_plan, 'apple', 3)
    assert meal_plan['apple'] == 5
    assert name == 'apple'
    assert quantity == 3

def test_generate_meal_plan_invalid(meal_plan):
    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'pudding', 2)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', -2)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', 0)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', 'two')

def test_generate_total_calories_valid(meal_plan):
    total_calories = generate_total_calories(meal_plan)
    assert total_calories == 324

def test_generate_total_calories_invalid():
    with pytest.raises(ValueError):
        generate_total_calories({})

def test_remove_food_from_meal_plan_valid(meal_plan):
    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'apple': 1, 'banana': 1}

    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'banana': 1}

def test_remove_food_from_meal_plan_invalid(meal_plan):
    with pytest.raises(KeyError):
        remove_food_from_meal_plan(meal_plan, 'carrot', 2)

def test_DataTable_GetNumberRows_valid(data_table):
    assert data_table.GetNumberRows() == 3

def test_DataTable_GetNumberRows_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetNumberRows()
    assert exc_info.type is AttributeError

def test_DataTable_GetNumberCols_valid(data_table):
    assert data_table.GetNumberCols() == 4

def test_DataTable_GetNumberCols_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetNumberCols()
    assert exc_info.type is AttributeError

def test_DataTable_GetValue_valid(data_table):
    assert data_table.GetValue(0, 0) == 'apple'
    assert data_table.GetValue(1, 1) == 89

def test_DataTable_GetValue_invalid(data_table):
    with pytest.raises(IndexError):
        data_table.GetValue(10, 10)

def test_DataTable_SetValue_valid(data_table):
    data_table.SetValue(0, 0, 'grape')
    assert data_table.GetValue(0, 0) == 'grape'

def test_DataTable_SetValue_invalid(data_table):
    with pytest.raises(IndexError):
        data_table.SetValue(10, 10, 'Invalid')

def test_DataTable_GetColLabelValue_valid(data_table):
    assert data_table.GetColLabelValue(0) == 'food'
    assert data_table.GetColLabelValue(1) == 'Caloric Value'

def test_DataTable_GetColLabelValue_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetColLabelValue(-1)
    assert exc_info.type is AttributeError

def test_DataTable_GetAttr_valid(data_table):
    attr = data_table.GetAttr(1, 0, None)
    assert attr.GetBackgroundColour() == EVEN_ROW_COLOUR

def test_DataTable_GetAttr_invalid(data_table):
    attr = data_table.GetAttr(0, 0, None)
    assert not attr.HasBackgroundColour()
