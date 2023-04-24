#pip install git+https://github.com/pytorch/pytorch.git@v1.9.0
import streamlit as st
#we first want to import all our libraries
import pandas as pd 
import numpy as np 
import geopandas as gpd
import matplotlib.pyplot as plt

st.title(" libraries not installed but stream lit works")
airlines = pd.read_csv('airlines.dat',header=None)
airlines_column_names = ['Airlines','Alias','IATA','ICAO','Callsign','Country','Active']
airlines.columns = airlines_column_names
#now we want to only keep the coumns we interested in 
airlines = airlines.drop(['Alias','IATA','ICAO','Callsign'],axis = 1)
st.write('the airlines file has been read')

