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

# Way 0: Recreates the HTML automatically, but less good if you want to control what parts go where in the HTML document
# print(f'''
# {html_chart}
# ''')


# Way 1: Control parts of the html
import regex

# Remove all newline characters
re_exp = "\n"
html_chart = regex.sub(re_exp, "", html_chart)
# print('html_chart: ', html_chart)

# Replace 2 or more consecutive spaces with one space
re_exp = "\s+"
html_chart1 = regex.sub(re_exp, " ", html_chart)
print('html_chart1: ', html_chart1)

# Assign the correct code to the desired HTML sections
altair_body_output = text[0][0] + '' + text[1][0];
altair_script_output = text[2][0];

print(f'''<!DOCTYPE html>
<html>
<head></head>
<body>
<h1>{title}</h1>
<div id=altair_body_output>{altair_body_output}</div>
</script>
{altair_script_output}
<script>
</script>
</body>
</html>''')
