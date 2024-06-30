import pandas as pd
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import numpy as np

mood_music = pd.read_csv("data/data_moods.csv")
mood_music = mood_music[['name','artist','mood','id']]

def recommend(mood,n):
    name = []
    artist = []
    link = []
    if mood == 'Angry':
        filter1=mood_music['mood']=='Calm'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n)
        f2.reset_index(inplace=True)
        name = list(f2['name'])
        artist = list(f2['artist'])
        link = list(f2['id'])
    elif mood == 'Happy' or mood == 'Neutral':
        filter1=mood_music['mood']=='Happy'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n)
        f2.reset_index(inplace=True)
        name = list(f2['name'])
        artist = list(f2['artist'])
        link = list(f2['id'])
    elif mood == 'Sad':
        filter1=mood_music['mood']=='Sad'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n)
        f2.reset_index(inplace=True)
        name = list(f2['name'])
        artist = list(f2['artist'])
        link = list(f2['id'])
    elif mood == 'Surprise':
        filter1=mood_music['mood']=='Energetic'
        f1=mood_music.where(filter1)
        f1=f1.dropna()
        f2 =f1.sample(n)
        f2.reset_index(inplace=True)
        name = list(f2['name'])
        artist = list(f2['artist'])
        link = list(f2['id'])
    links=[]
    for i in link:
        links.append('https://open.spotify.com/track/'+i)

    return [name,artist,links]

