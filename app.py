# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:53:46 2021

@author: samuels
"""

import streamlit as st
from calc import monthly_compounding

st.title("Compound Interest Calculator")

initial = st.number_input("Initial Investment", min_value = 0, max_value = 1000000000, step = 1)
monthly = st.number_input("Monthly Contribution", min_value = 0, max_value = 1000000000, step = 1)
years = st.number_input("Investment Duration (Years)", min_value = 0, max_value = 100, step = 1)
annual_rate = st.slider("Annual Interest Percentage", min_value = 0, max_value = 15, step = 1)

sum  = round(monthly_compounding(initial, monthly, years, annual_rate),2)

st.markdown("After 5 yeasr your would have £" + sum)