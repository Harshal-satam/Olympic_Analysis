import pandas as pd

def preprocess(df):
    
    
    df = df[df['Season'] == 'Summer']
    
    df.drop_duplicates(inplace=True)
    
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df