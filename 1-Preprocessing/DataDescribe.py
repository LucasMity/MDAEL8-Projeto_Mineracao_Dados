import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def main():
    # Faz a leitura do arquivo
    input_file = '0-Datasets/loan_trainClear.csv'
    names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Applicant_Income', 'Coapplicant_Income', 'Loan_Amount', 'Term','Credit_History', 'Area', 'Status']
    features =  ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Applicant_Income', 'Coapplicant_Income', 'Loan_Amount', 'Term', 'Credit_History', 'Area']
    target = 'Status'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    # Separating out the features
    x = df.loc[:, features].values

    # Separating out the target
    y = df.loc[:,[target]].values

    # Distribuição de frequência
    min = df['Applicant_Income'].min()
    max = df['Applicant_Income'].max()
    
    print(min, max)
    bins = []
    for x in range(0, 1000001, 100000):
        bins.append(x)
    bins.append(max)

    df['Applicant_Income_group'] = pd.cut(df['Applicant_Income'], bins)
    print(df['Applicant_Income_group'].value_counts().sort_index())
    ShowHistogram(df, 'Applicant_Income_group')
    
    


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")

def ShowHistogram(df, column):
    n, bins, patches = plt.hist(x=df[column].value_counts().sort_index(), bins=11, color='#0504aa', alpha=0.7, rwidth=0.85)

    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    maxfreq = n.max()
    plt.show()


if __name__ == "__main__":
    main()