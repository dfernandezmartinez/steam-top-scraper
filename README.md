# steam-top-scraper

## Sobre el proyecto

Este proyecto permite obtener un top con los juegos más jugados actualmente en la plataforma Steam (con un máximo de 100).

Las siguientes bibliotecas serán necesarias para ejecutar correctamente el proyecto:
```
beautifulsoup4==4.10.0
certifi==2021.10.8
charset-normalizer==2.0.7
idna==3.3
requests==2.26.0
requests-futures==1.0.0
soupsieve==2.2.1
urllib3==1.26.7
```

Se pueden importar todas las bibliotecas mencionadas guardando el texto anterior en un fichero y ejecutando:
```
python3 -m pip install -r bibliotecas.txt
```

Para poder generar un documento CSV con los datos de Steam actuales, el proyecto se debe ejecutar de la siguiente manera:
```
python3 src/main.py
```

Opcionalmente, se puede indicar el número de juegos del top, siempre sin sobrepasar el máximo de 100, de la siguiente forma:
```
python3 src/main.py --top 10
```

## Sobre el repositorio

Este repositorio contiene 3 directorios:
- **about**: contiene un documento describiendo distintos aspectos del proyecto y el dataset generado.
- **example**: contiene un output de ejemplo del top 100 juegos más jugados a día 29/10/2021.
- **src**: contiene los archivos necesarios para la ejecución del proyecto.

## Datos obtenidos
El fichero CSV generado contendrá las siguientes columnas:
- **Steam id**: identificador único del juego en la plataforma de Steam.
- **Game**: nombre del juego
- **Current players**: jugadores en el momento de la ejecución del programa.
- **Peak players today**: jugadores máximos en el día de la ejecución del programa.
- **Release date**: fecha en la que salió el juego.
- **Review summary**: texto resumen de las _reviews_ de los usuarios.
- **Total reviews**: _reviews_ de usuarios totales para el juego. 
- **Tags**: conjunto de etiquetas que describen el juego.

Se puede acceder al dataset publicado en Zenodo mediante este [enlace](https://zenodo.org/record/5655273#.YYlzIGDMKUk) (10.5281/zenodo.5655273).

## Miembros del equipo

Este proyecto ha sido desarrollado individualmente por **Daniel Fernández Martínez**.
