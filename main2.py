from jinja2 import Template

# Define a Jinja2 template
template_str = """
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
"""

# Create a Jinja2 template object
template = Template(template_str)

# Render the template with data
html_output = template.render(title="Jinja2 Example", name="webapp_name")

# Save the rendered HTML to a file
# with open("index.html", "w") as file:
#     file.write(html_output)
# OR
print(html_output)
