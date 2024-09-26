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
- `test_search_food_by_name_valid()`
- `test_search_food_by_name_invalid()`

- **Tested Function/Module**
  - `search_food_by_name(name)`
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
### Test Case 2:
- **Test Function/Module**
  - `get_nutritional_info_valid()`
  - `get_nutritional_info_invalid()`
- **Tested Function/Module**
  - `get_nutritional_info(name)`
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
| `get_nutritional_info('pudding')` | `{}`                |

- **2) Code for the Test Function**
```python
def test_get_nutritional_info_invalid():
    information = get_nutritional_info("pudding")
    assert information == {}
```

### Test Case 3:
- **Test Function/Module**
  - `filter_nutritional_info_valid()`
  - `filter_nutritional_info_invalid()`
- **Tested Function/Module**
  - `filter_nutritional_info(nutritional_info)`
- **Description**
  - This function filters the nutritional information to exclude zero values and returns the filtered categories, sizes, and explode values for charting.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `filter_nutritional_info({})` | `[], [], []`        |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 4:
- **Test Function/Module**
  - `test_create_pie_chart_valid()`
  - `test_create_pie_chart_invalid()`
- **Tested Function/Module**
  - `create_pie_chart(filtered_sizes, filtered_categories, explode, ax)`
- **Description**
  - This function creates a pie chart using the filtered nutritional information. The input is the filtered sizes, categories, explode values, and ax. The output is a pie chart.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```


### Test Case 5:
- **Test Function/Module**
- `test_create_bar_graph_valid()`
- `test_create_bar_graph_invalid()`
- **Tested Function/Module**
  - `create_bar_graph(filtered_categories, filtered_sizes, ax)`
- **Description**
  - This function creates a bar graph using the filtered nutritional information. The input is the filtered categories, sizes, and ax. The output is a bar graph.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 6:
- **Test Function/Module**
- `filter_food_by_nutrient_range_valid()`
- `filter_food_by_nutrient_range_invalid()`
- **Tested Function/Module**
  - `filter_food_by_nutrient_range(df, nutrient, min_val, max_val)`
- **Description**
  - This function filters foods by a nutrient range. The input is the dataframe, nutrient, min_val, and max_val. The output is the filtered dataframe.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 7:
- **Test Function/Module**
- `test_filter_food_by_level_valid()`
- `test_filter_food_by_level_invalid()`
- **Tested Function/Module**
  - `filter_food_by_nutrient_level(df, nutrient, level)`
- **Description**
  - This function filters foods by nutrient level (Low, Mid, High). The input is the dataframe, nutrient, and level. The output is the filtered dataframe.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 8:
- **Test Function/Module**
- `test_get_food_details_valid()`
- `test_get_food_details_invalid()`
- **Tested Function/Module**
  - `get_food_details(df, food_name, meal_plan)`
- **Description**
  - This function retrieves food details from the meal plan. The input is the dataframe, food_name, and meal_plan. The output is the food details.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 9:
- **Test Function/Module**
- `test_generate_meal_plan_valid()`
- `test_generate_meal_plan_invalid()`
- **Tested Function/Module**
  - `generate_meal_plan(meal_plan, name, quantity)`
- **Description**
  - This function generates a meal plan by adding food items and their quantities. The input is the meal_plan, name, and quantity. The output is the updated meal plan.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 10:
- **Test Function/Module**
- `test_generate_total_calories_valid()`
- `test_generate_total_calories_invalid()`
- **Tested Function/Module**
  - `generate_total_calories(meal_plan)`
- **Description**
  - This function calculates the total calories in the meal plan. The input is the meal plan. The output is the total calories.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

### Test Case 11:
- **Test Function/Module**
- `test_remove_food_from_meal_plan_valid()`
- `test_remove_food_from_meal_plan_invalid()`
- **Tested Function/Module**
  - `remove_food_from_meal_plan(meal_plan, selected_meal_food)`
- **Description**
  - This function removes a food item from the meal plan. The input is the meal plan and the selected meal food. The output is the updated meal plan.
- **1) Valid Input and Expected Output**  

| **Valid Input**               | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 2)`               | `5`                 |
| `divide(10, -2)`              | `-5`                |
| `add more cases in necessary` | `...`               |

- **1) Code for the Test Function**
```python
def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(10, -2) == -5
```
- **2) Invalid Input and Expected Output**

| **Invalid Input**             | **Expected Output** |
|-------------------------------|---------------------|
| `divide(10, 0)`               | `Handle Exception`  |
| `add more cases in necessary` | `...`               |

- **2) Code for the Test Function**
```python
def test_divide_invalid():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    assert exc_info.type is ValueError
```

## 3. **Testing Report Summary**
Include a screenshot of unit_test.html showing the results of all the above tests. 

You can use the following command to run the unit tests and generate the unit_test.html report.

```commandline
pytest test_all_functions.py --html=unit_test.html --self-contained-html
```
Note: test_all_functions.py should contain all the test functions designed to test the self-defined functions related 
to the five required features.

![unit_test_summary](./Unit_test.png)
