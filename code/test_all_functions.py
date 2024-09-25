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

def test_DataTable_GetNumberRows_valid(data_table):
    assert data_table.GetNumberRows() == 3

def test_DataTable_GetNumberRows_invalid():
    with pytest.raises(AttributeError) as exc_info:
        invalid_data_table = DataTable()
        invalid_data_table.GetNumberRows()
    assert exc_info.type is AttributeError

def test_DataTable_GetNumberCols_valid(data_table):
    assert data_table.GetNumberCols() == 4

def test_DataTable_GetNumberCols_invalid():
    with pytest.raises(AttributeError) as exc_info:
        invalid_data_table = DataTable()
        invalid_data_table.GetNumberCols()
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
        invalid_data_table = DataTable()
        invalid_data_table.GetColLabelValue(-1)
    assert exc_info.type is AttributeError

def test_DataTable_GetAttr_valid(data_table):
    attr = data_table.GetAttr(1, 0, None)
    assert attr.GetBackgroundColour() == EVEN_ROW_COLOUR

def test_DataTable_GetAttr_invalid(data_table):
    attr = data_table.GetAttr(0, 0, None)
    assert not attr.HasBackgroundColour()

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

def test_filter_food_by_nutrient_range_valid(sample_data):
    filtered = filter_food_by_nutrient_range(sample_data, "Fat", 0.1, 0.3)
    assert len(filtered) == 3
    assert "apple" in filtered["food"].values
    assert "banana" in filtered["food"].values
    assert "carrot" in filtered["food"].values

def test_filter_food_by_nutrient_range_invalid(sample_data):
    with pytest.raises(KeyError):
        filter_food_by_nutrient_range(sample_data, "pudding", 50, 90)

def test_filter_food_by_nutrient_level_valid(sample_data):
    filtered = filter_food_by_nutrient_level(sample_data, "Fat", "High")
    assert len(filtered) == 2
    assert "banana" in filtered["food"].values
    assert "carrot" in filtered["food"].values

    filtered = filter_food_by_nutrient_level(sample_data, "Fat", "Mid")
    assert len(filtered) == 1
    assert "apple" in filtered["food"].values

    filtered = filter_food_by_nutrient_level(sample_data, "Fat", "Low")
    assert len(filtered) == 0

def test_get_food_details(sample_data, meal_plan):
    food_key, quantity, total_calories = get_food_details(sample_data, 'apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 104

def test_generate_meal_plan_new_item(meal_plan):
    name, quantity = generate_meal_plan(meal_plan, 'fig', 2)
    assert meal_plan['fig'] == 2
    assert name == 'fig'
    assert quantity == 2

def test_generate_meal_plan_existing_item(meal_plan):
    name, quantity = generate_meal_plan(meal_plan, 'apple', 3)
    assert meal_plan['apple'] == 5
    assert name == 'apple'
    assert quantity == 3

def test_generate_total_calories_valid(meal_plan):
    total_calories = generate_total_calories(meal_plan)
    assert total_calories == 324

def test_remove_food_from_meal_plan_valid(meal_plan):
    remove_food_from_meal_plan(meal_plan, 'apple')
    assert 'fig' not in meal_plan
    assert meal_plan == {'banana': 1}

def test_remove_food_from_meal_plan_invalid(meal_plan):
    with pytest.raises(KeyError):
        remove_food_from_meal_plan(meal_plan, 'carrot')