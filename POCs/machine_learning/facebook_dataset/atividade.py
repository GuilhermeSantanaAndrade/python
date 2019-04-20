import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

dt = pd.read_csv('.\dataset_Facebook.csv')
dt_values = dt.values
print(dt_values)

dt_fil = []
id_aux = -1
for item in dt_values:
    if not np.isnan(item[6]):
        if (item[1] == 'Photo'):
            id_aux = 0
        elif (item[1] == 'Status'):
            id_aux = 1
        elif (item[1] == 'Video'):
            id_aux = 2
        elif (item[1] == 'Link'):
            id_aux = 3            
        item[1] = id_aux
        dt_fil.append(item[0:7])
print(dt_fil)        

min_max_scaler = MinMaxScaler()
seletor_atributos = VarianceThreshold(threshold=.08)
data_norm = min_max_scaler.fit_transform(dt_fil)
data_result = seletor_atributos.fit_transform(data_norm)
print(data_result)

pca = PCA(n_components=3)
m_out = pca.fit_transform(data_result)
print(m_out)

xx = m_out[:,0]
yy = m_out[:,1]

plt.xlim([-20,30])
plt.ylim([-20,30])
plt.scatter(xx,yy)
plt.show()