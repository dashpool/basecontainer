import importlib.util
import os
import re

# Define the new _default_index content
new_default_index = """<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Dashpool - {%title%}</title>
        {%favicon%}
        {%css%}
        <script>
            function loadAlternativeCSS() {
                var alternativeCSS = document.createElement('link');
                alternativeCSS.rel = 'stylesheet';
                alternativeCSS.href = 'https://dashpool.github.io/assets/bootstrap.css';
                document.head.appendChild(alternativeCSS);
            }
            function loadAlternativeGrid() {
                var alternativeGrid = document.createElement('link');
                alternativeGrid.rel = 'stylesheet';                
                alternativeGrid.href = 'https://dashpool.github.io/assets/grid.css';
                document.head.appendChild(alternativeGrid);
            }
        </script>             
        <link rel="stylesheet" href="/assets/bootstrap.css" onerror="loadAlternativeCSS()">
        <link rel="stylesheet" href="/assets/grid.css" onerror="loadAlternativeGrid()">
    </head>
    <body>
        <!--[if IE]><script>
        alert("Dash v2.7+ does not support Internet Explorer. Please use a newer browser.");
        </script><![endif]-->
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}

       
        </footer>
    </body>
</html>"""

# Dynamically find the path to the dash package
dash_spec = importlib.util.find_spec('dash')
if dash_spec is None:
    raise ImportError("Dash package not found. Please ensure it is installed.")

dash_pkg_path = dash_spec.submodule_search_locations[0]
dash_py_path = os.path.join(dash_pkg_path, 'dash.py')

# Read the current content of dash.py
with open(dash_py_path, 'r') as file:
    dash_py_content = file.read()

# Replace the _default_index variable using a regular expression
new_dash_py_content = re.sub(
    r'_default_index = """(.*?)"""',
    f'_default_index = """{new_default_index}"""',
    dash_py_content,
    flags=re.DOTALL
)

# Write the new content back to dash.py
with open(dash_py_path, 'w') as file:
    file.write(new_dash_py_content)

print("Successfully updated dash")