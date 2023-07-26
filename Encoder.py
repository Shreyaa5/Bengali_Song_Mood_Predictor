import pandas as pd

def num_val(s):                              #TO TYPECAST INTO STRING TO USE STRING FUNC
    s = s.lower()                       #A FUNCTION TO CONVERT KEYs INTO THEIR NUMERIC VALUE
    if(s == 'c major' or s == 'b minor'):
        return 1
    elif(s == 'c minor' or s == 'd major'):
        return 2
    elif(s == 'd minor' or s == 'e major'):
        return 3
    elif(s == 'e minor' or s == 'f major'):
        return 4
    elif(s == 'f minor' or s == 'g major'):
        return 5
    elif(s == 'g minor' or s == 'a major'):
        return 6
    elif(s == 'a minor' or s == 'b major'):
        return 7

'''
C Major = B Minor = 1     ENCODING USED TO WRITE THE ABOVE FUNCTION
C Minor = D Major = 2
D Minor = E Major = 3
E Minor = F Major = 4 
F Minor = G Major = 5
G Minor = A Major = 6
A Minor = B Major = 7

'''

df = pd.read_csv('train.csv')
df.head()
#df=df.dropna(inplace=True)  #MAKES A DATAFRAME FROM THE CSV FILE
num_val_of_key = []           #STORES ALL THE NUMERIC VALUE
count_row = df.shape[0]   #GIVES THE NUMBER OF ROWS IN DATAFRAME

for i in range(count_row):
    key = str(df.loc[i,'KEY'])
    val = num_val(key)
    num_val_of_key.append(val)
    
df['KEY_NUM_VAL'] = num_val_of_key
print(df.head())
df.to_csv("train.csv")