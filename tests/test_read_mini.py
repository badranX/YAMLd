import pandas as pd
from unittest.mock import patch, mock_open
from yamld.read import read_onelist_dataframe_from_file

yaml_content = """
config1:
  key1: 'value1'
  key2: 'value2'
  key3: 'value3'

oneval: "onevalue"

oneval_list: [1,2,3,4]

config2:
  keyA: 'valueA'
  keyB: 'valueB'
  keyC: 'valueC'

oneval_float: 3.4

data:
  - - name:
    - age: 
    - city:

  - - 'John Doe'
    - 30
    -  'New York'
  - -  'Jane Smith'
    - -25
    -  'San Francisco'
  - -  'Bob Johnson'
    - 35
    -  'Chicago'
  - -  'Test'
    - -35.0
    -  'Chicago'
"""

def test_read_mini_dataframe():

    with patch("builtins.open", mock_open(read_data=yaml_content)) as mock_file:
    # Test case 1: Check if the function returns a DataFrame
        df = read_onelist_dataframe_from_file('./abc_mocked_path')
        assert isinstance(df, pd.DataFrame)

        # Test case 2: Check if the DataFrame has the correct number of rows
        assert len(df) == 4

        # Test case 3: Check if the DataFrame columns are correct
        expected_columns = ['name', 'age', 'city']
        assert all(col in df.columns for col in expected_columns)


        #Test case 4: Check DataFrame attrs
        meta = {
                'config1' : {
                  'key1': 'value1',
                  'key2': 'value2',
                  'key3': 'value3'},
                'oneval': "onevalue",
                'oneval_list': [1,2,3,4],
                'config2':{
                  'keyA': 'valueA',
                  'keyB': 'valueB',
                  'keyC': 'valueC'},
                'oneval_float': 3.4}
        assert df.attrs == meta

        # Test case 5: Check if the values in the DataFrame are correct
        expected_values = [
            ['John Doe', 30, 'New York'],
            ['Jane Smith', -25, 'San Francisco'],
            ['Bob Johnson', 35, 'Chicago'],
            ['Test', -35.0, 'Chicago']
        ]
        for i, row in enumerate(df.itertuples(index=False)):
            assert list(row) == expected_values[i]


if __name__ == "__main__":
  test_read_mini_dataframe()
