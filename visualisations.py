import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

def plot_market_cap_dist(df, top_n=20):
    df_sorted= df.sort_values(by='Market Cap (USD) Numerical', ascending=False)
    top= df_sorted.head(top_n)
    fig, ax= plt.subplots(figsize=(20, top_n))
    ax.barh(top['Company'], top['Market Cap (USD) Numerical'])
    ax.set_xlabel('Market Cap (USD)')
    ax.set_ylabel('Company')
    ax.set_title(f'Top {top_n} Companies by Market Cap in Billions')
    ax.invert_yaxis() #company with highest market cap is on top
    return fig

def sector_donut(df):
    sector_counts= df['Sector'].value_counts().reset_index()
    sector_counts.columns= ['Sector', 'NumberOfCompanies']
    fig= px.pie(sector_counts, names='Sector', values='NumberOfCompanies', hole=0.3, title='Distribution of Companies by Sector')
    return fig

def industry_donut(df):
    industry_counts=df['Industry'].value_counts().reset_index()
    industry_counts.columns=['Industry', 'NumberOfCompanies']
    fig=px.pie(industry_counts, names='Industry', values='NumberOfCompanies', hole=0.5, title='Distribution of Companies by Industry')
    return fig

def country_donut(df):
    country_counts=df['Country'].value_counts().reset_index()
    country_counts.columns=['Country', 'NumberOfCompanies']
    fig=px.pie(country_counts, names='Country', values='NumberOfCompanies', hole=0.1, title='Distribution of Companies by Country')
    return fig

def global_dist_map(df):
    country_counts=df['Country'].value_counts().reset_index()   
    country_counts.columns=['Country', 'NumberOfCompanies']
    fig=px.choropleth(country_counts, locations='Country', locationmode='country names', color='NumberOfCompanies', title='Global Distribution of Companies', hover_name='Country', color_continuous_scale=px.colors.carto.Temps, projection='orthographic', width=1000, height=600)
    return fig

def stacked_bar(df):
    industry_counts=df.groupby(['Country', 'Industry']).size().reset_index(name='Counts')
    wide_df=industry_counts.pivot(index='Country', columns='Industry', values='Counts')
    fig=px.bar(wide_df, x=wide_df.index, y=wide_df.columns, title='Number of Companies by Country and Industry')
    fig.update_layout(barmode='stack', xaxis_title='Country', yaxis_title='Number of Companies')
    fig.update_traces(hovertemplate='%{y} Companies in %{x}')
    return fig

def market_cap_vs_sector(df):
    sector_aggregates=df.groupby('Sector').agg(SumMarketCap=('Market Cap (USD) Numerical', 'sum'), CompanyCount=('Sector', 'count')).reset_index()
    fig=px.scatter(sector_aggregates, x='CompanyCount', y='SumMarketCap', size='SumMarketCap', color='Sector', hover_name='Sector', title='market_cap_vs_sector')
    fig.update_xaxes(title='Number of Companies')
    fig.update_yaxes(title='Total Market Cap (USD)')
    return fig

