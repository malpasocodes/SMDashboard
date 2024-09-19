import pandas as pd
import streamlit as st
from analysis.helperfunctions import extract_columns
import plotly.express as px


def get_best_performers():
    
   df = extract_columns('mobility_data', ['name', 'state', 'type','bot20_to_top20', 'bottom20%_fraction', 'parent_median', 'student_median','count'])
   df['bot20_to_top20'] = df['bot20_to_top20'] / 100
   df = df[df['bottom20%_fraction'] >=10]
   df['difference'] = df['student_median'] - df['parent_median']
   df = df.sort_values(by='bot20_to_top20', ascending=False).head(50)
   


   # Reset the index to drop the existing index
   df = df.reset_index(drop=True)

   # Add row numbers starting from 1
   df.index = df.index + 1

   return df

def plot_best_performers():
    df = get_best_performers()

    


    # Define custom color map
    custom_color_map = {
        'Public': 'green',
        'Private not-for-profit': 'blue',
        'Private for-profit': 'red'
    }

    # Create the second scatter plot
    fig = px.scatter(df, 
                      x='bot20_to_top20', 
                      y='parent_median', 
                      color='type',
                      title='Best Colleges for Student Mobility',
                      size='count',
                      hover_name='name',
                      labels={
                          'bot20_to_top20': 'Conditional Mobility Rate - Bottom to Top Quintile',
                          'parent_median': 'Median Parent Income (Institution)',
                          'type': 'Institution Type'  # Label for the legend
                      },
                      color_discrete_map=custom_color_map
                      )

    # Update layout to increase font sizes
    fig.update_layout(
        title_font_size=24,  # Increase title font size
        title_font_family="Arial",  # Set font family that supports italics
        xaxis_title_font_size=18,  # Increase x-axis title font size
        yaxis_title_font_size=18,  # Increase y-axis title font size
        legend_title_font_size=18,  # Increase legend title font size
        legend_font_size=14  # Increase legend font size
    )

    # Format x-axis as percentage
    fig.update_layout(xaxis_tickformat='.0%')

    # Show the plot
    st.write("""The plot below shows the top 50 colleges with the highest conditional mobility rate from the bottom 20% (parental income) to the top 20% (student income approximately ten years later). To appear on the list, a college must enroll at least 10% of their student body from the bottom quintile of parental income.""")
    st.plotly_chart(fig)
    

def list_best_performers():
    df = get_best_performers()
    df = df.drop(columns=['count','bottom20%_fraction'])
    df = df.rename(columns={'bot20_to_top20': 'mobility_rate'})
    st.title("Best Colleges for Student Mobility")

    st.write("""The table below shows the top 50 colleges with the highest conditional mobility rate from the bottom to the top quintile. To appear on the list, a college must enroll at least 10% of their student body from the bottom quintile of parental income.""")
    st.write(df)