import pandas as pd
import numpy as np 
from datetime import date
import random
import networkx as nx

class data_to_graph():
    def __init__(
        self,
        path_to_file='../data/historical_data.csv',
        size=100,
        date=date.today().strftime("%Y-%m-%d"),
        price='Open',
        max_spread_pct=0.05
    ):
        self.path_to_file = path_to_file
        self.size = size
        self.date = date
        self.price = price
        self.max_spread_pct = max_spread_pct

    def get_graph(self):
        '''
        Pipeline to get graph object
        param:
            dataframe
        return:
            dataframe
        '''
        self.read_data()
        self.filter_data()
        self.exchange_rate_matrix()
        self.log_transformed_rep()
        self.build_graph()
        
        return self
    
    def read_data(self):
        '''
        Read data from file
        param:
            dataframe
        return:
            dataframe
        '''
        self.data = pd.read_csv(self.path_to_file)
        return self
    
    def filter_data(self):
        '''
        Filter data
        param:
            dataframe
        return:
            dataframe
        '''
        self.read_data()
        df = self.data.copy()
        df_date = df[df['Date'] == self.date]
        
        assert (df_date.shape[0] != 0), 'No hay datos para esa fecha'
        
        df_date = df_date[
            df_date[self.price] > 0
        ]
        
        if(self.size == None):
            self.filter_data = df_date
        else:
    
            self.filter_data = df_date.sample(
                n = self.size
            )
        
        self.filter_data = self.filter_data.reset_index()[
                [
                    "ticker", 
                    self.price
                ]
            ].rename(
                columns = {
                    "ticker":'Símbolo',
                    self.price:'Precio'
                }
            )
        
        return self
    
    def exchange_rate_matrix(self):
        """
        Exchange Rate Matrix Representation
        param:
            dataframe
        return:
            dataframe
        """
        n = self.filter_data.shape[0]

        c1 = self.filter_data[['Precio']].copy()
        aux = c1.copy()
        random.seed(10)
        for i in range(n):
            c1[i] = aux/c1[['Precio']].values[i]*(1+random.uniform(0,self.max_spread_pct))
        c1.drop(columns=['Precio'],inplace=True)
        for i in range(len(c1.index)):
            for j in range(len(c1.columns)):
                if i==j:
                    c1.loc[i,j] = 1
        self.exchange_rate_matrix = c1
        
        return self
    
    def log_transformed_rep(self):
        """
        Log-Transformed Representations
        param:
            dataframe
        return:
            dataframe
        """

        self.log_exchange_rate_matrix = np.round(-np.log(self.exchange_rate_matrix),2)
        
        return self
    
    def build_graph(self):
        """
        Crea grafo a partir de los datos de cripomonedas y precio
        param:
            dataframe
        return:
            grafo
        """
        n = self.log_exchange_rate_matrix.shape[0]

        edge = []
        # Covert to format to use a graph
        for i in range(n):
            for j in range(n):
                if (i != j):
                    edge.append([str(i), str(j), self.log_exchange_rate_matrix.loc[i][j]])

        G = nx.DiGraph()        
        G.add_weighted_edges_from(edge)
        self.graph = G

        return self


