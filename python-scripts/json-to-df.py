import pandas as pd
import json

with open('/home/graduate/data-graduates/Introduction_01/data/countries.json') as data_file:
	data = json.load(data_file)


dfp=pd.DataFrame(data)
dfaux=dfp

for i in range(0, len(data)):
	#dfp['name'][i]=dfaux['name'][i]['common']
	dfp['name'][i]=dfaux.loc[:,('name',i)]
dfcsv=pd.read_csv('/home/graduate/data-graduates/Introduction_01/data/countries.csv')

merged=pd.merge(dfp,dfcsv,on='name')
print(merged)
