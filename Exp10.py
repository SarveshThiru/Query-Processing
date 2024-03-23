import pandas as pd
import numpy as np

# Create a DataFrame with random values
np.random.seed(20)  # Set seed for reproducibility
data = np.random.randn(10, 4)  # Generate random numbers
df = pd.DataFrame(data, columns=list('ABCD'))

# Define a function to apply color based on value
def color_red_negative(val):
  color = 'red' if val < 0 else 'black'
  return 'color: %s' % color

# Apply color formatting to the DataFrame with style.applymap()
styled_df = df.style.applymap(color_red_negative)

# Display the styled DataFrame
print(styled_df.to_string())
