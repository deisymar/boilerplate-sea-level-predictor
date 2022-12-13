import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', float_precision='legacy')
    #print(df)

    # Create scatter plot
    plt.figure(figsize=(14, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])    
    #plt.show()

    # Create first line of best fit    
    res_lin = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    #print(res_lin)
    plt.plot(range(df['Year'].min(), 2051, 1), res_lin.intercept + (res_lin.slope*range(df['Year'].min(), 2051, 1)),'r', label='fit all')

    # Create second line of best fit
    res_lin_2000 = linregress(df.query('Year >= 2000')['Year'], 
                              df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051, 1), res_lin_2000.intercept + (res_lin_2000.slope*range(2000, 2051, 1)),'g', label ='fit recent')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.ylabel('Sea Level (inches)')
    plt.xlabel('Year')
    plt.plot(df['Year'], df['CSIRO Adjusted Sea Level'], 'o', label='original data')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()