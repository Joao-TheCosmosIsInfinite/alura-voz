import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')


def boxplot(p_df_dataframe, p_ax, p_column, p_palette='viridis', p_title='', p_title_size=12, p_title_color='dimgrey') -> None:
    """
    Função que gera um boxplot de acordo com os dados passados

    :param p_df_dataframe: Pandas dataframe
    :param p_ax: Matplotlib axes
    :param p_column: Coluna do dataframe
    :param p_pallete: Paleta de cores

    :return: None
    """
    ax=p_ax
    ## Dataframe com as estatisticas descritivas
    df_summary = pd.DataFrame(p_df_dataframe[p_column].describe())
    
    ## Objeto referente ao boxplot
    sns.boxplot(data=p_df_dataframe[p_column],
                palette=p_palette,
                orient='h',
                ax=ax)
    
    ## deixando os x_ticks com valor em branco
    ax.set(xticklabels = [])
    ax.set(ylabel = None)
    
    ## Titulo do boxplot com o nome da coluna
    ax.set_title(p_title, size=p_title_size, color=p_title_color)
    
    ## Tabela que será gerada junto com o gráfico, onde tera as estatisticas
    statistics_table = plt.table( cellText = df_summary.values,
                                    rowLabels = df_summary.index,
                                    colLabels =  ' ',
                                    cellLoc = 'left', 
                                    rowLoc = 'center',            
                                    loc ='bottom')
    
    ## Tamanho da fonte da tabela
    statistics_table.set_fontsize(14)
    
    ## Escala da tabela
    statistics_table.scale(1, 1.4)
    
    ## Colocar a tabela debaixo do boxplot
    plt.subplots_adjust(left = 0.2, bottom = .1)
    
    ## Exibir figura
    plt.show()