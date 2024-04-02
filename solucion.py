## ingestion de datos - solucion 

import pandas as pd
import os


def read_files(directory):
    phrases = []
    sentiments = []
    
    for subdirectories in os.listdir(directory):
        subdirectory = os.path.join(directory, subdirectories)
        if os.path.isdir(subdirectory):
            
            for file in os.listdir(subdirectory):
                if file.endswith(".txt"):
                    
                    with open(os.path.join(subdirectory, file), "r", encoding="utf-8") as f:
                        
                        for line in f:
                            phrases.append(line.strip())  
                            
                            sentiment = subdirectories
                            sentiments.append(sentiment)
    
    df = pd.DataFrame({"phrase": phrases, "sentiment": sentiments})
    return df


dir_train = "data/train"
dir_test = "data/test"

df_train = read_files(dir_train)
df_test = read_files(dir_test)

train_sentiment_counts = df_train['sentiment'].value_counts()
test_sentiment_counts = df_test['sentiment'].value_counts()

df_train.to_csv("train_dataset.csv", index=False)
df_test.to_csv("test_dataset.csv", index=False)
