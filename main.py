# -----------------------------

def run_process():
  return 4+4;

# -----------------------------

def display_figure(url_content):
  import pandas as pd
  import requests

  # --------------------------------
  
  res = requests.get(url_content)
  if response.status_code == 200:
      data = response.json()
      data = pd.read_json(data)
      x_axis_variable = 'petal_width' # sepal_length, sepal_width, petal_length, petal_width
      y_axis_variable = 'species'
  else:
      data = pd.DataFrame({'a': list('CCCDDDEEE'), 'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]});
      x_axis_variable = 'a'
      y_axis_variable = 'b'
  
  # --------------------------------
  
  # Make the chart
  import altair as alt
  chart = alt.Chart(data).mark_point().encode(x=x_axis_variable, y=y_axis_variable).interactive()

  return chart.to_html();
  
# -----------------------------


# -----------------------------
# Main
# -----------------------------
import sys
url_content = sys.argv[1]

title = "Display data"

# -----------------------------

# Test 0: Output python computation to HTML
# data = 5+5;

# Test 1: Output function output to HTML
# data = run_process();

# Test 2: Output figure to HTML

# Could do selineum and webscrape the html input


# Could read url_content from a file using GET
html_chart = display_figure(url_content);
  
print(f'''<!DOCTYPE html>
<html>
<head></head>
<body>
<h1>{title}</h1>
<h2>Input a dataset url</h2>
<p>For example, enter https://raw.githubusercontent.com/CodeSolutions2/static_HTML/main/iris.csv.</p>
<input type="text" name="data_url" id="data_url" value="" style="display:block;">
<button id="refresh_plot" onclick="refresh_plot()" style="display:block">Refresh plot</button>
<div>{html_chart}</div>
<script type="module" redirect="follow" mode="no-cors">import {{ run_backend_process, GET_fileDownloadUrl_and_sha }} from "https://codesolutions2.github.io/static_HTML/library_to_run_GitHub_Actions.js";
module.run_backend_process = run_backend_process;
module1.GET_fileDownloadUrl_and_sha = GET_fileDownloadUrl_and_sha;
</script>
<script>
const module = {{}};
async function refresh_plot() {{
var RepoAobj = {{}};
RepoAobj.repoOwner = 'CodeSolutions2';
RepoAobj.repoA_name = 'static_HTML';
RepoAobj.foldername = '';
RepoAobj.filename = "launch.txt";
const random_text = Math.random().toString(16).slice(2);
RepoAobj.input_text = document.getElementById("data_url").value+"|"+RepoAobj.repoA_name+"_"+random_text;
RepoAobj.repoB_name = 'static_HTML';
await module.run_backend_process(RepoAobj);
}}
</script>
</body>
</html>''')
