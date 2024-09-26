# Unit Testing Report

Please provide your GitHub repository link.
### GitHub Repository URL: https://github.com/UniKatya/Milestone2_Group19.git


---

The testing report should focus solely on <span style="color:red"> testing all the self-defined functions related to 
the five required features.</span> There is no need to test the GUI components. Therefore, it is essential to decouple your code and separate the logic from the GUI-related code.


## 1. **Test Summary**
list all tested functions related to the five required features and the corresponding test functions designed to test 
those functions, for example:

| **Tested Functions**                                                 | **Test Functions**                                                                                           |
|----------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `load_data(file_path)`                                               | `test_load_data_valid()` <br> `test_load_data_invalid()`                                                     |
| `search_food_by_name(food_name)`                                     | `test_search_food_by_name_valid()` <br> `test_search_food_by_name_invalid()`                                 |
| `get_nutritional_info(food_name)`                                    | `test_get_nutritional_info_valid(cream_cheese_info)` <br> `test_get_nutritional_info_invalid()`              |
| `filter_nutritional_info(categories, sizes)`                         | `test_filter_nutritional_info_valid()`<br> `test_filter_nutritional_info_invalid()`                          |
| `create_pie_chart(filtered_sizes, filtered_categories, explode, ax)` | `test_create_pie_chart_valid()` <br> `test_create_pie_chart_invalid()`                                       |
| `create_bar_graph(filtered_categories, filtered_sizes, ax)`          | `test_create_bar_graph_valid()` <br> `test_create_bar_graph_invalid()`                                       |
| `filter_food_by_nutrient_range(nutrient, min_val, max_val)`          | `test_filter_food_by_nutrient_range_valid()` <br> `test_filter_food_by_nutrient_range_invalid()`             |
| `filter_food_by_nutrient_level(nutrient, level)`                     | `test_filter_food_by_nutrient_level_valid()` <br> `test_filter_food_by_nutrient_level_invalid()`             |
| `get_food_details(food_name, meal_plan)`                             | `test_get_food_details_valid(meal_plan)` <br> `test_get_food_details_invalid(meal_plan)`                     |
| `generate_meal_plan(meal_plan, food_name, quantity)`                 | `test_generate_meal_plan_valid(meal_plan)` <br> `test_generate_meal_plan_invalid(meal_plan)`                 |
| `generate_total_calories(meal_plan)`                                 | `test_generate_total_calories_valid(meal_plan)` <br> `test_generate_total_calories_invalid(meal_plan)`       |
| `remove_food_from_meal_plan(meal_plan, food_name, quantity)`         | `test_remove_food_from_meal_plan_valid(meal_plan)` <br> `test_remove_food_from_meal_plan_invalid(meal_plan)` |
| `DataTable.GetNumberRows()`                                          | `test_DataTable_GetNumberRows_valid(data_table)` <br> `test_DataTable_GetNumberRows_invalid()`               |
| `DataTable.GetNumberCols()`                                          | `test_DataTable_GetNumberCols_valid(data_table)` <br> `test_DataTable_GetNumberCols_invalid()`               |
| `DataTable.GetValue()`                                               | `test_DataTable_GetValue_valid(data_table)` <br> `test_DataTable_GetValue_invalid(data_table)`               |
| `DataTable.SetValue()`                                               | `test_DataTable_SetValue_valid(data_table)` <br> `test_DataTable_SetValue_invalid(data_table)`               |
| `DataTable.GetColLabelValue()`                                       | `test_DataTable_GetColLabelValue_valid(data_table)` <br> `test_DataTable_GetColLabelValue_invalid()`         |
| `DataTable.GetAttr()`                                                | `test_DataTable_GetAttr_valid(data_table)` <br> `test_DataTable_GetAttr_invalid(data_table)`                 |
---

## 2. **Test Case Details**

### Test Case 1:
- **Test Function/Module**
- `test_load_data_valid()`
- `test_load_data_invalid()`

- **Tested Function/Module**
  - `load_data(file_path)`
- **Description**
  - The function reads the CSV file and returns a pandas dataframe. The input is the file path, and the output is the dataframe.
- **1) Valid Input and Expected Output**  

| **Valid Input**                           | **Expected Output** |
|-------------------------------------------|---------------------|
| `load_data('Food_Nutrition_Dataset.csv')` | `pd.DataFrame`      |

- **1) Code for the Test Function**
```python
def test_load_data_valid():
    df = load_data('Food_Nutrition_Dataset.csv')
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                    | **Expected Output** |
|--------------------------------------|---------------------|
| `load_data('non_existent_file.csv')` | `FileNotFoundError` |

- **2) Code for the Test Function**
```python
def test_load_data_invalid():
    with pytest.raises(FileNotFoundError) as exc_info:
        load_data('non_existent_file.csv')
    assert exc_info.type is FileNotFoundError
```

### Test Case 2:
- **Test Function/Module**
- `test_search_food_by_name_valid()`
- `test_search_food_by_name_invalid()`

- **Tested Function/Module**
  - `search_food_by_name(food_name)`
- **Description**
  -The function reads the CSV file and checks if the specified food name exists in the dataset. A string name representing the food item to search for is the input. While the output is a boolean value (True if the food item exists, False otherwise).
- **1) Valid Input and Expected Output**  

| **Valid Input**                 | **Expected Output** |
|---------------------------------|---------------------|
| `search_food_by_name('apple')`  | `True`              |
| `search_food_by_name('banana')` | `True`              |

- **1) Code for the Test Function**
```python
def test_search_food_by_name_valid():
    assert search_food_by_name('apple') == True
    assert search_food_by_name('banana') == True
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                | **Expected Output** |
|----------------------------------|---------------------|
| `search_food_by_name('pudding')` | `False`             |
| `search_food_by_name('12')`      | `False`             |
| `search_food_by_name(' ')`       | `False`             |

- **2) Code for the Test Function**
```python
def test_search_food_by_name_invalid():
    assert search_food_by_name('pudding') == False
    assert search_food_by_name('12') == False
    assert search_food_by_name(' ') == False
```

### Test Case 3:
- **Test Function/Module**
  - `get_nutritional_info_valid(cream_cheese_info)`
  - `get_nutritional_info_invalid()`
- **Tested Function/Module**
  - `get_nutritional_info(food_name)`
- **Description**
  - This function retrieves the nutritional information of the food selected by the user. The input is the food name, which identifies which food must be fetched from the database. And the output is nutritional_info (dictionary) which is the nutritional information of the chosen food.
- **1) Valid Input and Expected Output**  

| **Valid Input**                        | **Expected Output** |
|----------------------------------------|---------------------|
| `get_nutritional_info('cream cheese')` | `cream_cheese_info` |

- **1) Code for the Test Function**
```python
def test_get_nutritional_info_valid(cream_cheese_info):
    information = get_nutritional_info("cream cheese")
    assert information == cream_cheese_info
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                 | **Expected Output** |
|-----------------------------------|---------------------|
| `get_nutritional_info('pudding')` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_get_nutritional_info_invalid():
    with pytest.raises(ValueError):
        get_nutritional_info("pudding")
```

### Test Case 4:
- **Test Function/Module**
  - `filter_nutritional_info_valid(cream_cheese_info)`
  - `filter_nutritional_info_invalid()`
- **Tested Function/Module**
  - `filter_nutritional_info(nutritional_info)`
- **Description**
  - This function filters the nutritional information to exclude zero values and returns the filtered categories, sizes, and explode values for charting.
- **1) Valid Input and Expected Output**  

| **Valid Input**                              | **Expected Output**          |
|----------------------------------------------|------------------------------|
| `filter_nutritional_info(cream_cheese_info)` | `categories, sizes, explode` |

- **1) Code for the Test Function**
```python
def test_filter_nutritional_info_valid(cream_cheese_info):
    categories, sizes, explode = filter_nutritional_info(cream_cheese_info)
    assert categories == ['Caloric Value', 'Selenium', 'Potassium', 'Cholesterol', 'Copper', 'Water', 'Nutrition Density', 'Fat', 'Others']
    assert sizes == [51, 19.1, 15.5, 14.6, 14.1, 7.6, 7.07, 5, 8.984999999999996]
    assert explode == [0.1] + [0.0] * (len(categories) - 1)
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `filter_nutritional_info({})` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_filter_nutritional_info_invalid():
    with pytest.raises(ValueError):
        filter_nutritional_info({})
```

### Test Case 5:
- **Test Function/Module**
  - `test_create_pie_chart_valid()`
  - `test_create_pie_chart_invalid()`
- **Tested Function/Module**
  - `create_pie_chart(filtered_sizes, filtered_categories, explode, ax)`
- **Description**
  - This function creates a pie chart using the filtered nutritional information. The input is the filtered sizes, categories, explode values, and ax. The output is a pie chart.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                                    | **Expected Output** |
|--------------------------------------------------------------------|---------------------|
| `create_pie_chart([10, 20, 30], ["A", "B", "C"], [0, 0.1, 0], ax)` | `3`                 |

- **1) Code for the Test Function**
```python
def test_create_pie_chart_valid():
    fig, ax = plt.subplots()
    wedges, texts, autotexts = create_pie_chart([10, 20, 30], ["A", "B", "C"], [0, 0.1, 0], ax)
    assert len(wedges) == 3
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                       | **Expected Output** |
|-----------------------------------------|---------------------|
| `test_create_pie_chart([], [], [], ax)` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_create_pie_chart_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        create_pie_chart([], [], [], ax)
```


### Test Case 6:
- **Test Function/Module**
- `test_create_bar_graph_valid()`
- `test_create_bar_graph_invalid()`
- **Tested Function/Module**
  - `create_bar_graph(filtered_categories, filtered_sizes, ax)`
- **Description**
  - This function creates a bar graph using the filtered nutritional information. The input is the filtered categories, sizes, and ax. The output is a bar graph.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                       | **Expected Output** |
|-------------------------------------------------------|---------------------|
| `create_bar_graph(["A", "B", "C"], [10, 20, 30], ax)` | `3`                 |

- **1) Code for the Test Function**
```python
def test_create_bar_graph_valid():
    fig, ax = plt.subplots()
    create_bar_graph(["A", "B", "C"], [10, 20, 30], ax)
    assert len(ax.patches) == 3
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**              | **Expected Output** |
|--------------------------------|---------------------|
| `create_bar_graph([], [], ax)` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_create_bar_graph_invalid():
    fig, ax = plt.subplots()
    with pytest.raises(ValueError):
        create_bar_graph([], [], ax)
```

### Test Case 7:
- **Test Function/Module**
- `filter_food_by_nutrient_range_valid()`
- `filter_food_by_nutrient_range_invalid()`
- **Tested Function/Module**
  - `filter_food_by_nutrient_range(df, nutrient, min_val, max_val)`
- **Description**
  - This function filters foods by a nutrient range. The input is the dataframe, nutrient, min_val, and max_val. The output is the filtered dataframe.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                  | **Expected Output** |
|--------------------------------------------------|---------------------|
| `filter_food_by_nutrient_range("Fat", 0.1, 0.3)` | `311`               |


- **1) Code for the Test Function**
```python
def test_filter_food_by_nutrient_range_valid():
    filtered = filter_food_by_nutrient_range("Fat", 0.1, 0.3)
    assert len(filtered) == 311
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                  | **Expected Output** |
|----------------------------------------------------|---------------------|
| `filter_food_by_nutrient_range("pudding", 11, 10)` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_filter_food_by_nutrient_range_invalid():
    with pytest.raises(ValueError):
        filter_food_by_nutrient_range("pudding", 11, 10)
```

### Test Case 8:
- **Test Function/Module**
- `test_filter_food_by_level_valid()`
- `test_filter_food_by_level_invalid()`
- **Tested Function/Module**
  - `filter_food_by_nutrient_level(df, nutrient, level)`
- **Description**
  - This function filters foods by nutrient level (Low, Mid, High). The input is the dataframe, nutrient, and level. The output is the filtered dataframe.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                | **Expected Output** |
|------------------------------------------------|---------------------|
| `filter_food_by_nutrient_level("Fat", "High")` | `3`                 |
| `filter_food_by_nutrient_level("Fat", "Mid")`  | `11`                |
| `filter_food_by_nutrient_level("Fat", "Low")`  | `2381`              |

- **1) Code for the Test Function**
```python
def test_filter_food_by_nutrient_level_valid():
    filtered = filter_food_by_nutrient_level("Fat", "High")
    assert len(filtered) == 3
    filtered = filter_food_by_nutrient_level("Fat", "Mid")
    assert len(filtered) == 11
    filtered = filter_food_by_nutrient_level("Fat", "Low")
    assert len(filtered) == 2381
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                              | **Expected Output** |
|------------------------------------------------|---------------------|
| `filter_food_by_nutrient_level("Fat", "loow")` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_filter_food_by_nutrient_level_invalid():
    with pytest.raises(ValueError):
        filter_food_by_nutrient_level("Fat", "loow")
```

### Test Case 9:
- **Test Function/Module**
- `test_get_food_details_valid()`
- `test_get_food_details_invalid()`
- **Tested Function/Module**
  - `get_food_details(df, food_name, meal_plan)`
- **Description**
  - This function retrieves food details from the meal plan. The input is the dataframe, food_name, and meal_plan. The output is the food details.
- **1) Valid Input and Expected Output**  

| **Valid Input**                        | **Expected Output** |
|----------------------------------------|---------------------|
| `get_food_details('apple', meal_plan)` | `'apple'`           |
| `get_food_details('apple', meal_plan)` | `2`                 |
| `get_food_details('apple', meal_plan)` | `190`               |

- **1) Code for the Test Function**
```python
def test_get_food_details_valid(meal_plan):
    food_key, quantity, total_calories = get_food_details('apple', meal_plan)
    assert food_key == 'apple'
    assert quantity == 2
    assert total_calories == 190
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                 | **Expected Output** |
|---------------------------------------------------|---------------------|
| `get_food_details('nonexistent_food', meal_plan)` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_get_food_details_invalid(meal_plan):
    with pytest.raises(ValueError):
        get_food_details('nonexistent_food', meal_plan)
```

### Test Case 10:
- **Test Function/Module**
- `test_generate_meal_plan_valid()`
- `test_generate_meal_plan_invalid()`
- **Tested Function/Module**
  - `generate_meal_plan(meal_plan, name, quantity)`
- **Description**
  - This function generates a meal plan by adding food items and their quantities. The input is the meal_plan, name, and quantity. The output is the updated meal plan.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                    | **Expected Output** |
|----------------------------------------------------|---------------------|
| `generate_meal_plan(meal_plan, 'cream cheese', 2)` | `2`                 |
| `generate_meal_plan(meal_plan, 'cream cheese', 2)` | `cream cheese`      |
| `generate_meal_plan(meal_plan, 'cream cheese', 2)` | `2`                 |
| `generate_meal_plan(meal_plan, 'apple', 3)`        | `5`                 |
| `generate_meal_plan(meal_plan, 'apple', 3)`        | `'apple'`           |
| `generate_meal_plan(meal_plan, 'apple', 3)`        | `3`                 |

- **1) Code for the Test Function**
```python
def test_generate_meal_plan_valid(meal_plan):
    name, quantity = generate_meal_plan(meal_plan, 'cream cheese', 2)
    assert meal_plan['cream cheese'] == 2
    assert name == 'cream cheese'
    assert quantity == 2

    name, quantity = generate_meal_plan(meal_plan, 'apple', 3)
    assert meal_plan['apple'] == 5
    assert name == 'apple'
    assert quantity == 3
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                               | **Expected Output** |
|-------------------------------------------------|---------------------|
| `generate_meal_plan(meal_plan, 'pudding', 2)`   | `ValueError`        |
| `generate_meal_plan(meal_plan, 'apple', -2)`    | `ValueError`        |
| `generate_meal_plan(meal_plan, 'apple', 0)`     | `ValueError`        |
| `generate_meal_plan(meal_plan, 'apple', 'two')` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_generate_meal_plan_invalid(meal_plan):
    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'pudding', 2)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', -2)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', 0)

    with pytest.raises(ValueError):
        generate_meal_plan(meal_plan, 'apple', 'two')
```

### Test Case 11:
- **Test Function/Module**
- `test_generate_total_calories_valid()`
- `test_generate_total_calories_invalid()`
- **Tested Function/Module**
  - `generate_total_calories(meal_plan)`
- **Description**
  - This function calculates the total calories in the meal plan. The input is the meal plan. The output is the total calories.
- **1) Valid Input and Expected Output**  

| **Valid Input**                      | **Expected Output** |
|--------------------------------------|---------------------|
| `generate_total_calories(meal_plan)` | `324`               |

- **1) Code for the Test Function**
```python
def test_generate_total_calories_valid(meal_plan):
    total_calories = generate_total_calories(meal_plan)
    assert total_calories == 324
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `generate_total_calories({})` | `ValueError`        |

- **2) Code for the Test Function**
```python
def test_generate_total_calories_invalid():
    with pytest.raises(ValueError):
        generate_total_calories({})
```

### Test Case 12:
- **Test Function/Module**
- `test_remove_food_from_meal_plan_valid()`
- `test_remove_food_from_meal_plan_invalid()`
- **Tested Function/Module**
  - `remove_food_from_meal_plan(meal_plan, selected_meal_food)`
- **Description**
  - This function removes a food item from the meal plan. The input is the meal plan and the selected meal food. The output is the updated meal plan.
- **1) Valid Input and Expected Output**  

| **Valid Input**                                     | **Expected Output**         |
|-----------------------------------------------------|-----------------------------|
| `remove_food_from_meal_plan(meal_plan, 'apple', 1)` | `{'apple': 1, 'banana': 1}` |
| `remove_food_from_meal_plan(meal_plan, 'apple', 1)` | `{'banana': 1}`             |

- **1) Code for the Test Function**
```python
def test_remove_food_from_meal_plan_valid(meal_plan):
    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'apple': 1, 'banana': 1}

    remove_food_from_meal_plan(meal_plan, 'apple', 1)
    assert meal_plan == {'banana': 1}
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                                    | **Expected Output** |
|------------------------------------------------------|---------------------|
| `remove_food_from_meal_plan(meal_plan, 'carrot', 2)` | `KeyError`          |

- **2) Code for the Test Function**
```python
def test_remove_food_from_meal_plan_invalid(meal_plan):
    with pytest.raises(KeyError):
        remove_food_from_meal_plan(meal_plan, 'carrot', 2)
```

### Test Case 13:
- **Test Function/Module**
- `test_DataTable_GetNumberRows_valid(data_table)`
- `test_DataTable_GetNumberRows_invalid()`
- **Tested Function/Module**
  - `DataTable.GetNumberRows()`
- **Description**
  - This functions obtains the number of rows in the data table. The input is the data table. The output is the number of rows.
- **1) Valid Input and Expected Output**  

| **Valid Input**              | **Expected Output** |
|------------------------------|---------------------|
| `data_table.GetNumberRows()` | `3`                 |

- **1) Code for the Test Function**
```python
def test_DataTable_GetNumberRows_valid(data_table):
    assert data_table.GetNumberRows() == 3
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `DataTable().GetNumberRows()` | `AttributeError`    |

- **2) Code for the Test Function**
```python
def test_DataTable_GetNumberRows_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetNumberRows()
    assert exc_info.type is AttributeError
```

### Test Case 14:
- **Test Function/Module**
- `test_DataTable_GetNumberCols_valid(data_table)`
- `test_DataTable_GetNumberCols_invalid()`
- **Tested Function/Module**
  - `DataTable.GetNumberCols()`
- **Description**
  - This functions obtains the number of columns in the data table. The input is the data table. The output is the number of columns.
- **1) Valid Input and Expected Output**  

| **Valid Input**              | **Expected Output** |
|------------------------------|---------------------|
| `data_table.GetNumberCols()` | `4`                 |

- **1) Code for the Test Function**
```python
def test_DataTable_GetNumberCols_valid(data_table):
    assert data_table.GetNumberCols() == 4
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `DataTable().GetNumberCols()` | `AttributeError`    |

- **2) Code for the Test Function**
```python
def test_DataTable_GetNumberCols_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetNumberCols()
    assert exc_info.type is AttributeError
```

### Test Case 15:
- **Test Function/Module**
- `test_DataTable_GetValue_valid(data_table)`
- `test_DataTable_GetValue_invalid(data_table)`
- **Tested Function/Module**
  - `DataTable.GetNumberCols()`
- **Description**
  - The function retrieves the value at the specified row and column in the data table. The input is the row and column. The output is the value.
- **1) Valid Input and Expected Output**  

| **Valid Input**             | **Expected Output** |
|-----------------------------|---------------------|
| `data_table.GetValue(0, 0)` | `'apple'`           |
| `data_table.GetValue(1, 1)` | `89`                |

- **1) Code for the Test Function**
```python
def test_DataTable_GetValue_valid(data_table):
    assert data_table.GetValue(0, 0) == 'apple'
    assert data_table.GetValue(1, 1) == 89
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `data_table.GetValue(10, 10)` | `IndexError`        |

- **2) Code for the Test Function**
```python
def test_DataTable_GetValue_invalid(data_table):
    with pytest.raises(IndexError):
        data_table.GetValue(10, 10)
```

### Test Case 16:
- **Test Function/Module**
- `test_DataTable_SetValue_valid(data_table)`
- `test_DataTable_SetValue_valid(data_table)`
- **Tested Function/Module**
  - `DataTable.SetValue()`
- **Description**
  - The function sets the value at the specified row and column in the data table. The input is the row, column, and value. The output is the updated data table.
- **1) Valid Input and Expected Output**  

| **Valid Input**                      | **Expected Output** |
|--------------------------------------|---------------------|
| `data_table.SetValue(0, 0, 'grape')` | `'grape'`           |

- **1) Code for the Test Function**
```python
def test_DataTable_SetValue_valid(data_table):
    data_table.SetValue(0, 0, 'grape')
    assert data_table.GetValue(0, 0) == 'grape'
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                         | **Expected Output** |
|-------------------------------------------|---------------------|
| ` data_table.SetValue(10, 10, 'Invalid')` | `IndexError`        |

- **2) Code for the Test Function**
```python
def test_DataTable_SetValue_invalid(data_table):
    with pytest.raises(IndexError):
        data_table.SetValue(10, 10, 'Invalid')
```

### Test Case 17:
- **Test Function/Module**
- `test_DataTable_GetColLabelValue_valid(data_table)`
- `test_DataTable_GetColLabelValue_invalid()`
- **Tested Function/Module**
  - `DataTable.GetColLabelValue()`
- **Description**
  - The function retrieves the column label value at the specified column index in the data table. The input is the column index. The output is the column label value.
- **1) Valid Input and Expected Output**  

| **Valid Input**                  | **Expected Output** |
|----------------------------------|---------------------|
| `data_table.GetColLabelValue(0)` | `'food'`            |
| `data_table.GetColLabelValue(1)` | `'Caloric Value'`   |

- **1) Code for the Test Function**
```python
def test_DataTable_GetColLabelValue_valid(data_table):
    assert data_table.GetColLabelValue(0) == 'food'
    assert data_table.GetColLabelValue(1) == 'Caloric Value'
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**                  | **Expected Output** |
|------------------------------------|---------------------|
| `DataTable().GetColLabelValue(-1)` | `AttributeError`    |

- **2) Code for the Test Function**
```python
def test_DataTable_GetColLabelValue_invalid():
    with pytest.raises(AttributeError) as exc_info:
        DataTable().GetColLabelValue(-1)
    assert exc_info.type is AttributeError
```

### Test Case 18:
- **Test Function/Module**
- `test_DataTable_GetAttr_valid(data_table)`
- `test_DataTable_GetAttr_invalid(data_table)`
- **Tested Function/Module**
  - `DataTable.GetColLabelValue()`
- **Description**
  - The function retrieves the attribute at the specified row and column in the data table. The input is the row, column, and default attribute. The output is the attribute.
- **1) Valid Input and Expected Output**  

| **Valid Input**              | **Expected Output** |
|------------------------------|---------------------|
| `attr.GetBackgroundColour()` | `EVEN_ROW_COLOUR`   |

- **1) Code for the Test Function**
```python
def test_DataTable_GetAttr_valid(data_table):
    attr = data_table.GetAttr(1, 0, None)
    assert attr.GetBackgroundColour() == EVEN_ROW_COLOUR
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**            | **Expected Output** |
|------------------------------|---------------------|
| `attr.HasBackgroundColour()` | `False`             |

- **2) Code for the Test Function**
```python
def test_DataTable_GetAttr_invalid(data_table):
    attr = data_table.GetAttr(0, 0, None)
    assert not attr.HasBackgroundColour()
```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./images/Unit_test.png)
