import streamlit as st
import pandas as pd
import warnings
import re
from visualisations import (plot_market_cap_dist, sector_donut, industry_donut, country_donut, global_dist_map, stacked_bar, market_cap_vs_sector)
from data_utils import (load_csv, filter_df)

warnings.filterwarnings('ignore')

st.set_page_config(layout="wide")

def main():
    st.title('Company Data Visualisation')

    chart_type = st.sidebar.radio('Select Chart Type', ['Data Table', 'Market Cap Distribution', 'Sector-Wise Donut Chart', 'Industry-Wise Donut Chart', 'Country-Wise Donut Chart', 'Global Distribution Map', 'Number of Companies by Country and Industy', 'Market Cap vs Sector'])
    df = load_csv('companies_data.csv')
    exclude_companies=st.text_input("Enter company names to exclude (underscore separated)")
    df_filtered = filter_df(df, exclude_companies)

    if chart_type == 'Data Table':
        # st.dataframe(df)
        st.dataframe(df_filtered)
        # st.balloons()
    elif chart_type == 'Market Cap Distribution':
        top_n=st.slider("Select number of companies to display:", max_value=50, min_value=10)
        fig= plot_market_cap_dist(df_filtered, top_n)
        st.pyplot(fig)
    elif chart_type == 'Sector-Wise Donut Chart':
        fig= sector_donut(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == 'Industry-Wise Donut Chart':
        fig= industry_donut(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == 'Country-Wise Donut Chart':
        fig= country_donut(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == 'Global Distribution Map':
        fig= global_dist_map(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == 'Number of Companies by Country and Industy':
        fig= stacked_bar(df_filtered)
        st.plotly_chart(fig)
    elif chart_type == 'Market Cap vs Sector':
        fig= market_cap_vs_sector(df_filtered)
        st.plotly_chart(fig)
    
    

if __name__ == '__main__':
    main() 