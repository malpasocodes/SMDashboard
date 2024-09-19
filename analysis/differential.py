import streamlit as st
from analysis.helperfunctions import extract_columns
import plotly.express as px


def get_differential():
    
   df = extract_columns('mobility_data', ['name', 'state', 'type','parent_median', 'student_median'])
   df['difference'] = df['student_median'] - df['parent_median']
   df = df.sort_values(by='difference', ascending=False).head(15)
   


   # Reset the index to drop the existing index
   df = df.reset_index(drop=True)

   # Add row numbers starting from 1
   df.index = df.index + 1

   return df

def plot_differential():
   
    df = get_differential()
    
    
    # Define custom color map
    custom_color_map = {
         'Public': 'green',
         'Private not-for-profit': 'blue',
         'Private for-profit': 'red'
    }
    
    # Create the first scatter plot
    fig1 = px.scatter(df, 
                        x='parent_median', 
                        y='student_median', 
                        color='type',
                        title='Differential',
                        size='difference',
                        hover_name='name',
                        labels={
                             'parent_median': 'Median Parent Income (Institution)',
                             'student_median': 'Median Student Income (Institution)',
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
    fig1.update_xaxes(tickformat=".0%")
    
    st.plotly_chart(fig1)