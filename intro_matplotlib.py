#######################################################################################################
# Matplotlib: 
# is a Python 2D plotting library which produces publication quality figures 
# in a variety of hardcopy formats and interactive environments across platforms. 
# Matplotlib can be used in Python scripts, the Python and IPython shell, the jupyter notebook, 
# web application servers, and four graphical user interface toolkits.
#
# Matplotlib.Pyplot:
# One of the core aspects of Matplotlib is matplotlib.pyplot. It is Matplotlib's scripting layer 
# which we studied in details in the videos about Matplotlib.
#######################################################################################################

# we are using the inline backend
%matplotlib inline 

import matplotlib as mpl
import matplotlib.pyplot as plt

print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0
print(plt.style.available)
# ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 
#  'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 
#  'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 
#  'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 
#  'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

mpl.style.use(['ggplot']) # optional: for ggplot-like style

#######################################################################################################
# Plotting in pandas
#     Fortunately, pandas has a built-in implementation of Matplotlib that we can use. 
#     Plotting in pandas is as simple as appending a .plot() method to a series or dataframe.
#######################################################################################################

# Line Pots (Series/Dataframe)
#   What is a line plot and why use it?
#   A line chart or line plot is a type of plot which displays information as a series of data 
#   points called 'markers' connected by straight line segments. It is a basic type of chart common 
#   in many fields. Use line plot when you have a continuous data set. These are best suited for 
#   trend-based visualizations of data over a period of time.

haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
haiti.head()

haiti.plot()

# let's label the x and y axis using plt.title(), plt.ylabel(), and plt.xlabel()

haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

# Quick note on x and y values in plt.text(x, y, label):
# Since the x-axis (years) is type 'integer', we specified x as a year. 
# The y axis (number of immigrants) is type 'integer', so we can just specify 
# the value y = 6000.
#    plt.text(2000, 6000, '2010 Earthquake') # years stored as type int
# If the years were stored as type 'string', we would need to specify x as the 
# index position of the year. Eg 20th index is year 2000 since it is the 20th year 
# with a base year of 1980.
#    plt.text(20, 6000, '2010 Earthquake') # years stored as type int

# Step 1: Get the data set for China and India, and display dataframe.
df_CI = df_can.loc[['India', 'China'], years]
df_CI.head()

# Step 2: Plot graph. We will explicitly specify line plot by passing 
# in kind parameter to plot()
df_CI.plot(kind='line')

# using transpose() method to swap the row and columns.
df_CI = df_CI.transpose()

df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigrants from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()
df_CI.head()

# Step 1: Get the dataset. Recall that we created a Total column that calculates the cumulative immigration by country. \\ We will sort on this column to get our top 5 countries using pandas sort_values() method.
# inplace = True paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

print(df_top5)

# Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size

plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

plt.show()

# passing kind keyword to plot(). The full list of available plots are as follows:
#
#    bar for vertical bar plots
#    barh for horizontal bar plots
#    hist for histogram
#    box for boxplot
#    kde or density for density plots
#    area for area plots
#    pie for pie plots
#    scatter for scatter plots
#    hexbin for hexbin plot

