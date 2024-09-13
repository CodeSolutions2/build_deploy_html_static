# -----------------------------

def run_process():
  return 4+4;

# -----------------------------

def display_figure():
  import pandas as pd
  data = pd.DataFrame({'a': list('CCCDDDEEE'),
                     'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})
  
  # make the chart
  import altair as alt

  # make the chart
  alt.Chart(data).mark_point().encode(x='x axis title', y='Miles_per_Gallon', color='Origin').interactive()

  return html_string = chart.to_html();
  
# -----------------------------


# -----------------------------
# Main
# -----------------------------

title = "Display data"

# -----------------------------

# Test 0: Output python computation to HTML
# data = 5+5;

# Test 1: Output function output to HTML
# data = run_process();

# Test 2: Output figure to HTML
data = display_figure();
  
print(f'''<!DOCTYPE html>
<html>
<head></head>
<body><h1>{title}</h1><div>{data}</div><script></script>
</body>
</html>''')
