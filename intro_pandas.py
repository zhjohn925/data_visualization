import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

# pandas requires xlrd to read in excel files.
# to install the xlrd module:
#      !conda install -c anaconda xlrd --yes

df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

# view the top 5 rows of the dataset using the head() function.
# or specify the number of rows you'd like to see as follows: df_can.head(10)
df_can.head()

#    	Type	Coverage	OdName	AREA	AreaName	REG	RegName	DEV	DevName	1980	...	2004	2005	2006	2007	2008	2009	2010	2011	2012	2013
# 0	Immigrants	Foreigners	Afghanistan	935	Asia	5501	Southern Asia	902	Developing regions	16	...	2978	3436	3009	2652	2111	1746	1758	2203	2635	2004
# 1	Immigrants	Foreigners	Albania	908	Europe	925	Southern Europe	901	Developed regions	1	...	1450	1223	856	702	560	716	561	539	620	603
# :::::::::::::::::::::::

# veiw the bottom 5 rows of the dataset using the tail() function.
df_can.tail()

# get basic information about your dataframe.
df_can.info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 195 entries, 0 to 194
# Data columns (total 43 columns):
#  #   Column    Non-Null Count  Dtype 
# ---  ------    --------------  ----- 
#  0   Type      195 non-null    object
#  1   Coverage  195 non-null    object
#  2   OdName    195 non-null    object
#  3   AREA      195 non-null    int64 
#  4   AreaName  195 non-null    object
#  5   REG       195 non-null    int64 
#  6   RegName   195 non-null    object
#  7   DEV       195 non-null    int64 
#  8   DevName   195 non-null    object
#  9   1980      195 non-null    int64 
#  :::::::::::::::::::::::::::::::
#  42  2013      195 non-null    int64 
# dtypes: int64(37), object(6)
# memory usage: 65.6+ KB

# To get the list of column headers
df_can.columns.values 

# array(['Type', 'Coverage', 'OdName', 'AREA', 'AreaName', 'REG', 'RegName',
#        'DEV', 'DevName', 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987,
#        1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998,
#        1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
#        2010, 2011, 2012, 2013], dtype=object)

# to get the list of indicies
df_can.index.values

# array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
#         ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#        182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194])

# To get the index and columns as lists
df_can.columns.tolist()
df_can.index.tolist()

# To view the dimensions of the dataframe. size of dataframe (rows, columns)
df_can.shape   

# clean the data set to remove a few unnecessary columns by using pandas drop()
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_can.head(2)

#	    OdName	AreaName	RegName	DevName	1980	1981	1982	1983	1984	1985	...	2004	2005	2006	2007	2008	2009	2010	2011	2012	2013
# 0	Afghanistan	Asia	Southern Asia	Developing regions	16	39	39	47	71	340	...	2978	3436	3009	2652	2111	1746	1758	2203	2635	2004
# 1	Albania	Europe	Southern Europe	Developed regions	1	0	0	0	0	0	...	1450	1223	856	702	560	716	561	539	620	603

# rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns

# Index([  'Country', 'Continent',    'Region',   'DevName',        1980,
#               1981,        1982,        1983,        1984,        1985,
#               :::::::::::::::::::::::::::::::::::::::::::::::::::
#               2011,        2012,        2013],
#       dtype='object')

# add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013
df_can['Total'] = df_can.sum(axis=1)

# check to see how many null objects we have in the dataset 
df_can.isnull().sum()

# view a quick summary of each column in our dataframe
df_can.describe()

####################################################################
# Indexing and Selection (slicing)
# Select Column:
#    df.column_name 
#    df['column'] 
#    df[['column 1', 'column 2']] 
# Select Row:
#    df.loc[label]    #filters by the labels of the index/column          
#    df.iloc[index]   #filters by the positions of the index/column        
####################################################################

print(df_can.Country)  # returns a series

# 0         Afghanistan
# 1             Albania
#             ...      
# 193            Zambia
# 194          Zimbabwe
# Name: Country, Length: 195, dtype: object

# filtering on the list of countries ('OdName') and the data for years: 1980 - 1985
df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]] # returns a dataframe

# 	Country	1980	1981	1982	1983	1984	1985
# 0	Afghanistan	16	39	39	47	71	340
# 1	Albania	1	0	0	0	0	0
# ...	...	...	...	...	...	...	...
# 193	Zambia	11	17	11	7	16	9
# 194	Zimbabwe	72	114	102	44	32	29
# 195 rows × 7 columns

# The defaul index of the dataset is a numeric range from 0 to 194. 
# This can be fixed very easily by setting the 'Country' column as the index 
# Tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()
df_can.set_index('Country', inplace=True)

df_can.head(3)
#	        Continent	Region	DevName	1980	1981	1982	1983	1984	1985	1986	...	2005	2006	2007	2008	2009	2010	2011	2012	2013	Total
# Country																					
# Afghanistan	Asia	Southern Asia	Developing regions	16	39	39	47	71	340	496	...	3436	3009	2652	2111	1746	1758	2203	2635	2004	58639
# Albania	Europe	Southern Europe	Developed regions	1	0	0	0	0	0	1	...	1223	856	702	560	716	561	539	620	603	15699
# Algeria	Africa	Northern Africa	Developing regions	80	67	71	69	63	44	69	...	3626	4807	3623	4005	5393	4752	4325	3774	4331	69439
# 3 rows × 38 columns

# optional: to remove the name (title) of the index
# ie.  no "Country" is printed above
df_can.index.name = None
df_can.head(3)

# view the number of immigrants from Japan (row 87) for the following scenarios: 
# 1. The full row data (all columns) 
# 2. For year 2013 
# 3. For years 1980 to 1985

# 1. the full row data (all columns)
print(df_can.loc['Japan'])
# alternate methods
print(df_can.iloc[87])
print(df_can[df_can.index == 'Japan'].T.squeeze())

# 2. for year 2013
print(df_can.loc['Japan', 2013])
# alternate method
print(df_can.iloc[87, 36]) # year 2013 is the last column, with a positional index of 36

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])
print(df_can.iloc[87, [3, 4, 5, 6, 7, 8]])

# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.
df_can.columns = list(map(str, df_can.columns))

# After converting the years to string, let's declare a variable that will allow us to easily 
# call upon the full range of years:
# useful for plotting later on
years = list(map(str, range(1980, 2014)))
years

# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# Afghanistan        True
# Albania           False
#                   ...  
# Yemen              True
# Zambia            False
# Zimbabwe          False
# Name: Continent, Length: 195, dtype: bool

# 2. pass this condition into the dataFrame
df_can[condition]

# we can pass mutliple criteria in the same line. 
# let's filter for AreaNAme = Asia and RegName = Southern Asia
df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

print('data dimensions:', df_can.shape)
print(df_can.columns)
df_can.head(2)



