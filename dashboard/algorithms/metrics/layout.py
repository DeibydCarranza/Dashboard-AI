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
            <header class="header-top">
                <div class="nav-wrapper">
                    <a href="/">
                        <h1>Métricas de distancia</h1>
                    </a>
                </div>
            </header>         
            """ + navbar + """

            <div class="content-container">
                <div>
                    <h1>Título del algoritmo</h1>
                    <p>Agregar introducción y cosas random</p>
                </div>
                
                {%app_entry%}
            </div>
            <footer>
                {%config%}
                {%scripts%}
                <script type="text/javascript" src="../../static/js/barra.js"></script>

                {%renderer%}
            </footer>
        </body>
    </html>
"""