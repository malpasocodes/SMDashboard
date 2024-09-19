import streamlit as st
from analysis.helperfunctions import extract_columns
import plotly.express as px


def get_serve_wealthiest():
    
   df = extract_columns('mobility_data', ['name', 'state', 'type','top1%_fraction', 'bottom20%_fraction','parent_median','student_median','count'])
   df['top1%_fraction'] = df['top1%_fraction'] / 100
   df['bottom20%_fraction'] = df['bottom20%_fraction'] / 100
   df['difference'] = df['student_median'] - df['parent_median']
   df = df.sort_values(by='top1%_fraction', ascending=False).head(50)
   


   # Reset the index to drop the existing index
   df = df.reset_index(drop=True)

   # Add row numbers starting from 1
   df.index = df.index + 1

   return df

def plot_serve_wealthiest():
    df = get_serve_wealthiest()
    

    # Define custom color map
    custom_color_map = {
        'Public': 'green',
        'Private not-for-profit': 'blue',
        'Private for-profit': 'red'
    }

    # Create the first scatter plot
    fig1 = px.scatter(df, 
                      x='top1%_fraction', 
                      y='parent_median', 
                      color='type',
                      title='Pctg. of Parents in Top 1% Income vs Median Parent Income',
                      size='count',
                      hover_name='name',
                      labels={
                          'top1%_fraction': 'Fraction of Parents in Top 1%',
                          'parent_median': 'Median Parent Income (Institution)',
                          'type': 'Institution Type'  # Label for the legend
                      },
                      color_discrete_map=custom_color_map
                      )

    # Update layout to increase font sizes
    fig1.update_layout(
        title_font_size=24,  # Increase title font size
        title_font_family="Arial",  # Set font family that supports italics
        xaxis_title_font_size=18,  # Increase x-axis title font size
        yaxis_title_font_size=18,  # Increase y-axis title font size
        legend_title_font_size=18,  # Increase legend title font size
        legend_font_size=14  # Increase legend font size
    )

    # Format x-axis as percentage
    fig1.update_layout(xaxis_tickformat='.0%')

    # Show the first plot
    st.plotly_chart(fig1)

    # Create the second scatter plot
    fig2 = px.scatter(df, 
                      x='top1%_fraction', 
                      y='bottom20%_fraction', 
                      color='type',
                      title='Pctg. of Parents in Top 1% Income vs Pctg. of Parents in Bottom 20% Income',
                      size='count',
                      hover_name='name',
                      labels={
                          'top1%_fraction': 'Fraction of Parents from Top 1%',
                          'bottom20%_fraction': 'Fraction of Parents infrom Bottom 20%',
                          'type': 'Institution Type'  # Label for the legend
                      },
                      color_discrete_map=custom_color_map
                      )

    # Update layout to increase font sizes
    fig2.update_layout(
        title_font_size=24,  # Increase title font size
        title_font_family="Arial",  # Set font family that supports italics
        xaxis_title_font_size=18,  # Increase x-axis title font size
        yaxis_title_font_size=18,  # Increase y-axis title font size
        legend_title_font_size=18,  # Increase legend title font size
        legend_font_size=14  # Increase legend font size
    )

    # Format x-axis as percentage
    fig2.update_layout(xaxis_tickformat='.0%')
    fig2.update_layout(yaxis_tickformat='.0%')

    # Show the first plot
    st.plotly_chart(fig2)


def list_serve_wealthiest():
    df = get_serve_wealthiest()
    df = df.drop(columns=['count'])
    st.write(df)








    
