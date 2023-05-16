import pandas as pd

df = pd.read_csv('country_code.csv')
#['COUNTRY', 'COUNTRY CODE', 'ISO CODES', 'POPULATION', 'AREA KM2','GDP $USD']

cc=dict(zip(list(df['COUNTRY']), list(df['COUNTRY CODE'])))
print(cc)

#for code
name=input("Enter your country name")
code=""
for key,value in cc.items():
    if name.lower()==key.lower() or name.upper()==key.upper():
        code=value
print(code)
