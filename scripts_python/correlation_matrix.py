import pandas as pd

data_file = 'Data/data.csv'
correlation_matrix_data_file = 'scripts_python/Preprocessing/correlationMatrix.csv'
reader = pd.read_csv(data_file, header=0)
"""
La idea es ir quitando los atributos que están altamente correlacionados, pues los mismos no aportan
individualmente información en el proceso de clasificación.

*Si la Correlación(el valor) es negativa indica que cuando una variable aumenta la otra disminuye y viceversa
*Si la Correlación es positiva(0<r<1) indica que cuando una variable aumenta la otra también y viceversa
*Si r=1 quiere decir que hay una correlación positiva perfecta  indica una dependencia total entre las dos
 variables denominada relación directa: cuando una de ellas aumenta,
 la otra también lo hace en proporción constante.
*Si r = 0, no existe relación lineal.
"""
print("Matriz de correlacion de Pearson")
data_csv=reader._get_values
columns = reader.columns
data=pd.DataFrame(data=data_csv,columns=columns)
correlation_matrix=data.corr()
print(correlation_matrix)
df=pd.DataFrame(correlation_matrix)
df.to_csv(correlation_matrix_data_file, index=False)
