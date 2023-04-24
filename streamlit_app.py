#pip install git+https://github.com/pytorch/pytorch.git@v1.9.0
import streamlit as st
#we first want to import all our libraries
import pandas as pd 
import numpy as np 
import geopandas as gpd
import matplotlib.pyplot as plt
# here is the title of what we want to show for our application 
st.title("MAGIC FLIGHTS THE FLYING APPLICATION!!!")
st.subheader("Here is our map of the world showing all the possible airports. Take a gander and see which one is closest to your Home!")
###################################################################################
# Here we clean up our airports columns
airports = pd.read_csv("airports.dat",header = None)
airports_column_names = ['Airport_ID','Name','City','Country','IATA','ICAO','LATITUDE','LONGITUDE','Altitude','Timezone','DST','Tz Database Time Zone','Type','Source']
airports.columns = airports_column_names
#now we drop some of our airports columns
airports = airports.drop(['DST','Tz Database Time Zone','Type','Source','Timezone'], axis = 1)
# here we will add some metrics for airports 
No_airports = airports['Airport_ID'].max()
#######################################################################################
# Here is our airport map!!!
st.map(airports,zoom=None, use_container_width=True)
#####################################################################################
#Here is a caption of our map.
st.caption('One is able to zoom in to see all possible airports of any particular country they would like to investigate!', unsafe_allow_html=False,help=None)
#st.write('One is able to zoom in to see all possible airports of any particular country they would like to investigate!')
st.title("FUN FACT!")
st.metric('The Current Maximum Number of Airports in the world is...', No_airports, delta=None, delta_color="normal", help=None, label_visibility="visible")

# WE want to now show all the interesting facts about all the airlines
# here we clean our AIRLINES data frame and se what data is inside of it
##############################################################################################
airlines = pd.read_csv('airlines.dat',header=None)
airlines_column_names = ['Airlines_ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']
airlines.columns = airlines_column_names
#now we want to only keep the coumns we interested in 
airlines = airlines.drop(['Alias','IATA','ICAO','Callsign'],axis = 1)
# we want to create a bar graph of all the planes that occur in a certain country 
# this was just done to obtaina dependent variable!
airlines2 = airlines.groupby('Country')['Airlines_ID'].count().reset_index()
# Here is our bar chart!!!
st.subheader("Here We Also Have An Interesting Bar Chart Of All The Airlines in World!")
st.write(" Can You guess which country has the most airlines in the world? ")
st.bar_chart(airlines2,x = 'Country', y='Airlines_ID')
st.write(" The united kingdom of course has the most airlines in the world, Now how about that! :)")

########################################################
# now we are going to try clean up our second dataset Airports
st.title("Now we are going to look at some interesting facts about planes")
# first we are going to load in all of our data
#planes = pd.read_csv('planes.dat',header = None)
# Now wea assign some column names
#plane_column_names = ['Plane Model Name','ISO_code','Daffif_code']
#planes.columns = plane_column_names
#st.table(planes)

