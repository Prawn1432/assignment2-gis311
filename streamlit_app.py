#pip install git+https://github.com/pytorch/pytorch.git@v1.9.0
import streamlit as st
we first want to import all our libraries
import pandas as pd 
import numpy as np 
import geopandas as gpd
import matplotlib.pyplot as plt

st.title(" libraries not installed but stream lit works")
airlines = pd.read_csv('airlines.dat'header=None)
st.write('the airlines file has been read')
