import numpy as np
import streamlit as slt
import pandas as pd
import keras.models
import pickle
from streamlit_option_menu import option_menu
from csv import writer


#Utility function to transform String
def modify_string(s):
    temp = s.lower()
    temp1 = temp.replace(" ","")
    return temp1

#Function to fetch mood from dataset
def giving_mood(song):
    modified_string = modify_string(song)

    df=pd.read_csv('dataset.csv')
    total_row = df.shape[0]

    for i in range(total_row):
        name = df.loc[i,'Song Name']
        modified_name = modify_string(name)

        if(modified_name == modified_string):
            if(df.loc[i,'Genre / Mood'] == 1):
                return "Happy Song"
            else:
                return "Sad Song"
    return "Song Not Present Please Add to Database in Add Song Page"


#Function to Predict Mood
def predicting_mood(input_array):

    #Converting to numpy_array

    new_model=keras.models.load_model("my_model")
    scaler=pickle.load(open('scaler.pkl','rb'))
    arr = np.array(input_array).reshape(1, -1)
    array_used = pd.DataFrame(scaler.transform(arr),columns=['Mean','Standard Deviation','Danceability','Valence','Loudness(in dB)','KEY_NUM_VAL'],index=None)
    pred1 = (new_model.predict(array_used)>.5).astype(int)
    print(pred1)

    return pred1[0][0]

#Function to add Song to dataset
def add_song(inp_array):
    with open('dataset.csv','a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(inp_array)
        f_object.close()

#Creating Sidebar  
with slt.sidebar:
    selected = option_menu('Options',
                           ['Song Mood','Add Song'],default_index=0)
    
if(selected == 'Song Mood'):
    slt.title('Song Mood Detector Page')

    Name = slt.text_input("Enter Name of Song")

    mood = ''

    #Creating a 'GO' Button
    if slt.button("Give Mood"):
        mood = giving_mood(Name)        
    slt.success(mood)

if(selected == 'Add Song'):
    slt.title("New Song Input Page")

    New_Song = slt.text_input("Enter New Song Name")
    Loudness = slt.text_input("Enter Loudness (in db)")
    Mean = slt.text_input("Enter the Mean of the Song")
    Standard_Deviation = slt.text_input("Enter the Standard Deviation of the song")
    Valence = slt.text_input("Enter Valence")
    Danceability = slt.text_input("Enter Danceability of the song")
    Key = slt.text_input("Enter Key_number_value")


    mood = ''

    if slt.button("Add to Dataset"):
        mood = predicting_mood([Loudness, Mean, Standard_Deviation, Valence, Danceability, Key])
        arr = [New_Song, Loudness, Mean, Standard_Deviation, Valence, Danceability, Key, mood]
        add_song(arr)
        slt.success('Song is Added')
