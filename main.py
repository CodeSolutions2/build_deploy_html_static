def display_figure(json_str):
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

html_chart = display_figure(json_str);
  
print(f'''<!DOCTYPE html>
<html>
<head></head>
<body>
<h1>{title}</h1>
<div>{html_chart}</div>
</script>
<script>
</script>
</body>
</html>''')
