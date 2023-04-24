#pip install git+https://github.com/pytorch/pytorch.git@v1.9.0
import streamlit as st
#we first want to import all our libraries
import pandas as pd 
import numpy as np 
import geopandas as gpd
import matplotlib.pyplot as plt
# here is the title of what we want to show for our application 
st.title("An Overview of All The Major Airports In the World")
##
# here we clean our AIRLINES data frame and se what data is inside of it
airlines = pd.read_csv('airlines.dat',header=None)
airlines_column_names = ['Airlines_ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']
airlines.columns = airlines_column_names
#now we want to only keep the coumns we interested in 
airlines = airlines.drop(['Alias','IATA','ICAO','Callsign'],axis = 1)
# now we are going to try clean up our second dataset Airports

airports = pd.read_csv("airports.dat",header = None)
airports_column_names = ['Airport_ID','Name','City','Country','IATA','ICAO','LATITUDE','LONGITUDE','Altitude','Timezone','DST','Tz Database Time Zone','Type','Source']
airports.columns = airports_column_names
#now we drop some of our airports columns
airports = airports.drop(['DST','Tz Database Time Zone','Type','Source','Timezone'], axis = 1)


##

# here is the out put of all our data frame
#st.table(airlines)
st.map(airports,zoom=None, use_container_width=True)

# this is just to check if our dataframe is read correctly 
st.write('One is able to zoom in to see all possible airports of any particular country they would like to investigate!')
