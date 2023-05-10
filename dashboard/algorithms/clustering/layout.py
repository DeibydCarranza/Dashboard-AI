import os

with open(os.path.join(os.path.dirname(__file__), '../../', 'templates', 'navbar.jinja2'), 'r') as file:
    navbar = file.read()

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}            
            <title>{%title%}</title>
            {%favicon%}
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/boxicons@latest/css/boxicons.min.css">
            {%css%}
            </head>
            <body class="dash-template">
            <header>
                <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Clustering</h1>
                </a>
                """ + navbar + """
                </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                <script type="text/javascript" src="../../static/js/barra.js"></script>

                {%renderer%}
            </footer>
        </body>
    </html>
"""
