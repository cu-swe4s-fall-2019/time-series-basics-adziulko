# time-series-basics & Pandas
time-series-basics Objectives : Import multiple csv data files from a folder, clean data and match on time stamps,
work with datetime data type

Pandas Objectives : Work with Pandas DataFrames and Series objects. Import multiple files, match on
indexes, clean and print. (You are re-doing assignment 5, but with pandas dataframes instead
of lists. You should find this much easier & speedier!)

## File instruction
To test for python Pep8 style, you will need to:
1. Install pycodestyle
2. Run pycodestyle on desired file (in this case it is 'data_import.py')
```
pip install pycodestyle
pycodestyle data_import.py
```

To implement desired time series:
1. Have Python3 installed
2. In command line specify:
    - input folder name
    - output folder name
    - file to sort on (key)
    - number of files (integer)

```
python data_import.py --folder_name hr_small --output_file out_hr --sort_key meal_small --number_of_files 1
```
