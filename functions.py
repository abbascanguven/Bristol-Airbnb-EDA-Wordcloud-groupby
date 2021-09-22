import matplotlib.pyplot as plt
from scipy.stats import shapiro
import pandas as pd 

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(15, 12))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");
    

# normality test
def shapiro_wilk(data):
    columns = data.columns
    int_columns = []
    normality_column_name = []
    normality_statistic = []
    normality_result = []
    for column_type in columns:
        if data[column_type].dtypes == "int64" or data[column_type].dtypes == "float64":
            int_columns.append(column_type)
    for column in int_columns:
        stat, p = shapiro(data[column])
        statistic = ('Statistics=%.5f, p=%.5f' % (stat, p))
        #print('Statistics=%.3f, p=%.3f' % (stat, p))
        # interpret
        alpha = 0.05
        if p > alpha:
            normality_column_name.append(column)
            normality_statistic.append(statistic)
            normality_result.append("Sample looks Gaussian")
                    
        else:
            normality_column_name.append(column)
            normality_statistic.append(statistic)
            normality_result.append("Sample does not look Gaussian")
        
    normality_column_name = pd.DataFrame(normality_column_name, columns =['Column Name'])
    normality_statistic = pd.DataFrame(normality_statistic, columns =['Statistic']) 
    normality_result = pd.DataFrame(normality_result, columns =['Result']) 


    result = pd.concat([normality_column_name, normality_statistic, normality_result], axis=1, sort=False)
    
    return result

