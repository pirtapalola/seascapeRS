import os
import pandas as pd

os.chdir(r'C:/Users/pirtapalola/Documents/iop_data/data/forward_model')
the_list = []

# Create a list that contains the paths of all the csv files in a folder
for root, dirs, files in os.walk(r'C:/Users/pirtapalola/Documents/iop_data/data/forward_model'):
    for file in files:
        if file.endswith('.csv'):
            the_list.append(file)


# Define a function that takes a list of paths, reads all the csv files,
# and adds the first column to a new pandas dataframe
def readdataframe(list_paths):
    df = pd.DataFrame()  # define df as an empty pandas DataFrame
    for element in list_paths:
        # print(element)
        df[element] = pd.read_csv(element, sep=',', header=0, usecols=[1])
    return df


fm_reflectance = readdataframe(the_list)
fm_reflectance.to_csv('C:/Users/pirtapalola/Documents/iop_data/data/fm_reflectance.csv')