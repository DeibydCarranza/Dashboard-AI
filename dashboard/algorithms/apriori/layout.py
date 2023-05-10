o
    B[d#  �                   @   s`   d dl Z ee j�e j�e�ddd�d��Ze�� ZW d  � n1 s#w   Y  de d Z	dS )�    Nz..�	templatesznavbar.jinja2�ru6  
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
                    <h1>Asociación</h1>
                </a>
                a<  
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
)
�os�open�path�join�dirname�__file__�file�readZnavbar�html_layout� r   r   �`/home/david/Descargas/plotlydash-flask-tutorial-master/plotly_flask_tutorial/dashboard/layout.py�<module>   s    "
���