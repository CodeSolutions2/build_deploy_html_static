def display_figure():
  import pandas as pd
  
  data = pd.DataFrame({'a': list('CCCDDDEEE'), 'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]});
  x_axis_variable = 'a'
  y_axis_variable = 'b'

  # Make the chart
  import altair as alt
  chart = alt.Chart(data).mark_point().encode(x=x_axis_variable, y=y_axis_variable).interactive()

  return chart.to_html();
  
# -----------------------------

# -----------------------------
# Main
# -----------------------------
title = "Display data"

html_chart = display_figure();
  
print(f'''
{html_chart}
''')
