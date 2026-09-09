> __Versión en español.__ Esta rama es la traducción de `master`, que está en inglés y es
> la fuente de verdad: los cambios se hacen allí primero y luego se traen aquí. Ante
> cualquier discrepancia, manda `master`. Los criterios y la terminología de la traducción
> están en [`.es/glosario.md`](.es/glosario.md); de qué versión del original viene cada
> fichero, en [`.es/manifest.json`](.es/manifest.json).

Este es el repositorio de la asignatura de Programación Declarativa que se imparte en el
Grado en Inteligencia Artificial de la Universidad Rey Juan Carlos.


# Contenido

El material de la asignatura consiste, básicamente, en varios notebooks sobre los temas siguientes:

* PF-1
  * Tema 1. [Presentación y planificación](PF-1/Intro.pdf) (en español, con los detalles de la URJC)
  * Tema 2. Lenguajes de tipado fuerte y Scala
* PF-2
  * Tema 3. Tipos algebraicos de datos
  * Tema 4. [La correspondencia de Curry-Howard](https://github.com/jserranohidalgo/curry-howard-game)
* PF-3
  * Tema 5. Funciones y tipos de datos recursivos
  * Tema 6. Funciones de orden superior y programación modular
  * Tema 7. Aplicaciones

# El juego de Curry-Howard

El tema 4 viene con un juego: [__The Curry-Howard Game__](https://github.com/jserranohidalgo/curry-howard-game).
Dada una proposición, el objetivo es construir una prueba de ella —o establecer que no existe
ninguna— construyendo paso a paso el programa que habita el tipo correspondiente. Funciona en el
navegador, sin instalar nada; los detalles, en su repositorio.

# Cómo arrancar los notebooks

Para acceder a estos notebooks hay que instalar primero [git](https://git-scm.com/) y clonar este
repositorio en tu disco, en su versión en español:

`> git clone -b es https://github.com/jserranohidalgo/urjc-pd.git pd`

Después, instala `jupyter` (las instrucciones están más abajo) y ejecuta el programa:

`jupyter notebook`  o `jupyter lab`

en el directorio raíz del repositorio.

Como alternativa, puedes saltarte la instalación manual de `jupyter` y ejecutarlo con
[docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows) así:

`docker run -it --rm -p 8888:8888 -p 4040:4040 -m 4g -v "$PWD":/home/jovyan/work almondsh/almond:latest` (LINUX)

`docker run -it --rm -p 8888:8888 -p 4040:4040 -m 4g -v <<c:/ruta/a/la/carpeta/descargada>>:/home/jovyan/work almondsh/almond:latest` (WINDOWS)

(también en el directorio raíz del repositorio)

Por último, nótese que `jupyter` viene ya instalado en el entorno virtual MyApps (solo para
usuarios de la URJC).

# Instalación de jupyter y del kernel de Scala

Para instalar jupyter y poder ejecutar notebooks de Scala, sigue estos pasos:

* Instala el gestor de paquetes [`conda`](https://docs.conda.io/en/latest/miniconda.html), o usa `pip`, el gestor de paquetes de python.
* Instala [`jupyter`](https://jupyter.org/install).
* Como alternativa, jupyter viene incluido al instalar [anaconda](https://www.anaconda.com/products/individual-d).
* Instala [Java 8](https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html#A1096936). Ten en cuenta si tu arquitectura es de 32 o de 64 bits.
* Instala el plugin de Scala [`almond`](https://almond.sh/docs/quick-start-install).

Para este último paso, y con el fin de instalar la versión del kernel de almond para Scala 3, elige estas opciones:

`./coursier launch --fork almond:0.14.0-RC14 --scala 3.3.1 -- --install --id scala33 --display-name "Scala 3.3"`

### Posibles problemas al instalar almond

* En windows no consigo descargar los scripts de instalación del kernel de Scala `almond` con:

	> bitsadmin /transfer downloadCoursierCli https://git.io/coursier-cli "Í%%coursier"
	> ...

Probablemente estés usando powershell; usa `cmd` a secas.

Puede que necesites además privilegios de administrador (es decir, abrir CMD como administrador).


* En el tercer paso (".\coursier launch --fork ...") aparece el siguiente error:

Exception in thream "main" java.lang.Exception: Unrecognized CPU architecture: x86.

Probablemente necesites una versión de java de 64 bits y hayas instalado una de 32. Comprueba qué versión de java tienes escribiendo: "java -d64 -version".

* El comando de instalación se queda colgado (lo más probable, en windows)

Ejecuta el comando de instalación con la opción de detalle activada (`-v -v`):

        .\coursier launch --fork almond -M almond.ScalaKernel -v -v -- --install

Cuando el programa se quede colgado, párralo (C-c C-c). Lo más probable es que el último comando que intentó ejecutar fuese algo parecido a "Running java ...". Copia esa invocación de java y ejecútala a mano:

        java -Dscala-kernel.version=<...> -jar <...> --install

Con suerte, así se completará la instalación del kernel de almond.

* "Cannot find default main class. Specify one with -M or --main-class" (lo más probable, en linux)

Añade la opción `-M almond.ScalaKernel` al comando de instalación, es decir:

        ./coursier launch --fork almond -M almond.ScalaKernel -- --install


<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />Esta obra está publicada bajo una <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">licencia Creative Commons Attribution-ShareAlike 4.0 International</a>.
