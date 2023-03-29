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

    # df['Applicant_Income_group'] = pd.cut(df['Applicant_Income'], bins)
    # print(df['Applicant_Income_group'].value_counts().sort_index())

    # labels = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k-600k', '600k-700k', '700k-800k', '800k-900k', '900k-1M', '>1M']
    # group = df['Applicant_Income_group'].value_counts(sort=False)
    # ShowHistogram(labels, group, 'Renda do requerente')

    classe_cor = {0 : 'red', 1 : 'green'}
    cores = [classe_cor[nome] for nome in df.Status]

    df['Total_Income'] = df['Applicant_Income'] + df['Coapplicant_Income']

    # df.plot(kind='scatter', x='Area', y='Term', c=cores)

    # data = df
    # data = df.drop('Status', axis=1)
    # data = data.drop('Gender', axis=1)
    # data = data.drop('Married', axis=1)
    # data = data.drop('Dependents', axis=1)
    # data = data.drop('Education', axis=1)
    # data = data.drop('Self_Employed', axis=1)
    # data = data.drop('Applicant_Income', axis=1)
    # data = data.drop('Coapplicant_Income', axis=1)
    # data = data.drop('Loan_Amount', axis=1)
    # data = data.drop('Term', axis=1)
    # data = data.drop('Credit_History', axis=1)
    # data = data.drop('Area', axis=1)

    # pd.plotting.scatter_matrix(data, color=cores)
    plt.show()
    

def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n")

def ShowHistogram(label, group, labelx):
    ax = group.plot.bar(color='blue')
    plt.xticks(np.arange(11),label)
    plt.show()
    


if __name__ == "__main__":
    main()