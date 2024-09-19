import streamlit as st
from analysis.bestperformers import plot_best_performers, list_best_performers
from analysis.servewealthiest import plot_serve_wealthiest, list_serve_wealthiest
from analysis.differential import plot_differential 

# Sidebar navigation
selection = st.sidebar.radio("Select", ["Home", "Best Colleges for Student Mobility", "Colleges Serving the Wealthiest", "Differential"], index=0)

# Default message on the main page
if selection == "Home":
    st.title("Student Mobility Dashboard")
    st.write("""Welcome to the Student Mobility Dashboard. This dashboard provides insights into student mobility data.
             It is based on data from the [Opportunity Insights project](https://opportunityinsights.org/). The site is work in progress.
             Please send comments and suggestions to [malpaso@alfredcodes.com](mailto:malpaso@alfredcodes.com).
             """)
    ()
    st.write("Also check out the NY Times [College Mobility Site](https://www.nytimes.com/interactive/projects/college-mobility/city-college-of-new-york) based on the same data.")



# Selection of the Best Performing Colleges 


elif selection == "Best Colleges for Student Mobility":
    st.sidebar.subheader("Select")
    bpc_selection = st.sidebar.radio("Select", ["Visualization", "Table"], index=0)
    
    if bpc_selection == "Visualization":
        plot_best_performers()

    elif bpc_selection == "Table":
        list_best_performers()

# Selection of the Colleges Serving the Wealthiest

elif selection == "Colleges Serving the Wealthiest":
    st.sidebar.subheader("Select")
    bpc_selection = st.sidebar.radio("Select", ["Visualization", "Table"], index=0)

    if bpc_selection == "Visualization":
        plot_serve_wealthiest()

    elif bpc_selection == "Table":
        list_serve_wealthiest()

# Selection of the Differential

elif selection == "Differential":
    st.sidebar.subheader("Select")
    bpc_selection = st.sidebar.radio("Select", ["Visualization", "Table"], index=0)

    if bpc_selection == "Visualization":
        plot_differential()
    elif bpc_selection == "Table":
        st.write("Differential Table")
