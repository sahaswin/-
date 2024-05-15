import numpy as np
import streamlit as st
import plotly.graph_objects as go

def f(x, a):
    e = np.e  # Euler's number
    inner_expression = 3.154 - x**2
    sqrt_term = np.sqrt(np.maximum(inner_expression, 0))  # Take maximum with 0 to avoid sqrt of negative
    return x**(2/3) + (e/3) * sqrt_term * np.sin(a * 3.154 * x)

def generate_data(a_value):
    # Generate x-values for positive and negative range
    x_positive = np.linspace(0, 3, 500)  # Positive range from 0 to 3
    x_negative_shifted = np.linspace(0, -3, 500)  # Negative range from 0 to -3 (shifted)

    # Calculate corresponding y-values for positive x-values
    y_positive = f(x_positive, a_value)

    return x_positive, y_positive, x_negative_shifted

def plot_function(x_positive, y_positive, x_negative_shifted):
    # Create a Plotly figure
    fig = go.Figure()

    # Plot the function for x >= 0
    fig.add_trace(go.Scatter(x=x_positive, y=y_positive, mode='lines', name='f(x) for x >= 0', line=dict(color='red')))

    # Plot the mirrored function for x < 0
    fig.add_trace(go.Scatter(x=x_negative_shifted, y=y_positive, mode='lines', name='f(x) for x < 0', line=dict(color='red')))

    # Update layout for mobile optimization
    fig.update_layout(
        width=400,  # Set plot width for mobile screens
        height=300,  # Set plot height for mobile screens
        xaxis_title='x',
        yaxis_title='f(x)',
        title='Graph of f(x)',
        plot_bgcolor='black'
    )

    return fig

def main():
    st.title('Function Visualization')

    # Sidebar for parameter selection
    a_value = st.slider('Select a value for "a"', min_value=-1.4, max_value=19.0, value=-0.30, step=0.1)

    # Generate data based on the selected 'a' value
    x_positive, y_positive, x_negative_shifted = generate_data(a_value)

    # Plot the function using Plotly
    fig = plot_function(x_positive, y_positive, x_negative_shifted)

    # Display the Plotly figure using Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
