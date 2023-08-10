(Spanish)
Para ejecutar el programa se debe utilizar Python 3.10.6 o superior
Se deben instalar las dependencias especificadas en el archivo 'requirements.txt', por ejemplo, 
mediante el comando 'pip install -r requirements.txt' en línea de comandos o PowerShell.
Se debe modificar/crear un archivo .env en la raíz del directorio donde se encuentra el archivo "main.py", en este archivo .env se debe completar el usuario y la contraseña de LinkedIn para poder registrarse, caso contrario, LinkedIn no permite el scraping de información.

En el archivo de "constants.py", para evitar hardcodear, se definieron valores constantes que se usan a lo largo del script.
Por ejemplo "LOGIN_PAGE", la url de login de LinkedIn.
"RECOMMENDATIONS_URL", la url del perfil del cual se desean recolectar las recomendaciones.
"PROFILE_IMAGES_PATH" el path donde se quieren guardar las imágenes de los perfiles. 
Y "WAIT_TIME_LOAD" que es el tiempo en segundos que se espera para que una página termine de cargar.

El archivo 'main.py' es el punto de entrada al programa. Para correr el software, se debe ejecutar este archivo.
Por ejemplo, mediante el comando 'python3 main.py' en la línea de comandos o PowerShell.

El archivo 'LinkedinScraper.py' contiene la clase cuyo objetivo es obtener el código fuente de la página de recomendaciones.
Para esto se registra en LinkedIn, entra a la página de recomendaciones, hace un scroll hasta el final para asegurarse que 
la página esté completamente cargada, y extrae el código fuente.

Por último, el archivo 'LinkedinParser.py' contiene la clase cuyo objetivo es extraer toda la información requerida del 
archivo HTML de la página de recomendaciones, para luego exportar los resultados.

La salida del programa es:
* Un archivo recommendations.csv que contiene las columnas:
    * recommendation_id (Id de la recomendación)
    * profile_filename (Ubicacion de la imagen de perfil descargada)
    * name (Nombre de quien hizo la recomendación)
    * role (Rol de quien hizo la recomendación)
    * date (Fecha de la recomendación)
    * description (Descripción de la recomendación / Recomendación en sí misma)
* La descarga de todas las imágenes de perfil de las recomendaciones.

Link de una demostración del programa: 
https://youtu.be/7XZzOeh04Qo


(English)
To run the program you must use Python 3.10.6 or higher
The dependencies specified in the 'requirements.txt' file must be installed, for example,
using the command 'pip install -r requirements.txt' in command line or PowerShell.
An .env file must be modified/created in the root of the directory where the "main.py" file is located, in this .env file the LinkedIn username and password must be completed in order to register, otherwise, LinkedIn does not allow information scraping.

In the "constants.py" file, to avoid hardcoding, constant values were defined that are used throughout the script.
For example "LOGIN_PAGE", the LinkedIn login url.
"RECOMMENDATIONS_URL", the url of the profile from which you want to collect recommendations.
"PROFILE_IMAGES_PATH" the path where you want to save the profile images.
And "WAIT_TIME_LOAD" which is the time in seconds that is expected for a page to finish loading.

The 'main.py' file is the entry point to the program. To run the software, this file must be executed.
For example, by using the 'python3 main.py' command on the command line or PowerShell.

The 'LinkedinScraper.py' file contains the class whose purpose is to get the source code of the recommendations page.
For this, he registers on LinkedIn, enters the recommendations page, scrolls to the end to make sure that
the page is fully loaded, and extracts the source code.

Finally, the 'LinkedinParser.py' file contains the class whose objective is to extract all the required information from the
HTML file of the recommendations page, to later export the results.

The output of the program is:
* A recommendations.csv file containing the columns:
    * recommendation_id (Id of the recommendation)
    * profile_filename (Location of downloaded profile image)
    * name (Name of the person who made the recommendation)
    * role (Role of the person who made the recommendation)
    * date (Date of recommendation)
    * description (Description of the recommendation / Recommendation itself)
* Downloading all profile images from recommendations.

Link of a demo of the program:
https://youtu.be/7XZzOeh04Qo