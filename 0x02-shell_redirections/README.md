#odio este archivo ._.

0-hello_world = uso echo para escribir el mensaje.

1-confused_smiley = uso echo para imprimir y el \ es para que tome bien las comillas

2-hellofile = con cat muestro el contenido del archivo.

3-twofiles = usar cat y poner el resto de la ruta y ya.

4-lastlines = con tail me muestras las ultimas 10.

5-firstlines = con head muestras las primeras 10 lineas.

6-third_line = con | separo para agregar otra combinacion.

7-file = con echo escribo el mensajito y con > lo asigno al archivo que debe tener la frase.

8-cwd_state = > con esto redirijo la sentencia a el archivo.

9-duplicate_last_line = con >> duplico la ultima linea del archivo.

10-no_more_js = -type f es para buscar archivos, find es para buscar con el -name que dice buscar y con -delete elimino.

11-directories = con find . -type d busco archivos que inicien con ., con ! -path . evito los directorios principales y con .print | wc -1 imprimo el dato.

12-newest_files = con ls genero la lista y con -1t genero cada entrada por linea y por orden de tiempo, concateno con | y selecciono los 10 archivos mas recientes.

13-unique = con sort ordeno los archivos y con uniq elimino las lineas del archivo que esten duplicadas, -u imprimo solo las lineas unicas.

14-findthatword = con grep busco el patron osea root y despues pongo la ruta solicita.

15-countthatword = lo mismo que antes solo que ahora puse el comando -c para imprimir un recuento de cooncidencias.

16-whatsnext = despues de haber hecho coincidencia imprime las 3 lineas con -A.

17-hidethisword = -v se seleccionan las lineas que no coinciden.

18-letteronly = para encontrar las coincidencias o patrones uso ^[[:alpha:]].

19-AZ = suprimo el primer caracter concatenado con | el cual el primer caracter despues de | es el que lo reemplaza con tr.

20-hiago = dice eliminar entonces coloco el comando -d.

21-reverse = rev lo hace todo xd.

22-users_and_homes = con sort ordeno lineas de archivos de texto concateno con | y con cut -d pongo de delimitador ':' y con -f selecciono solo los campos que le siguen al mismo.

100-empty_casks = con find -empty busco el archivo o directorio vacio.

101-gifs = con -printf %f\n imprimo el script informando al usuario que el archivo ya existe y la /n es para un salto de linea, con rev invierto la cadena y despues la corto con su respectivo rango y la vuelvo a invertir seguido con LC_ALL = C sobrepongo las config del usuario y el sort -f es para ordenar las lineas de los archivos de min a mayus.

102-acrostic = con cut -c1 selecciono los caracteres y con pastes fusiono las lineas de los archivos y con -s los uno a la vez en vez de paralelo.

103-the_biggest_fan = con tail -n +2 genero el archivo empezando desde el num osea el num 2, con cut -f1 corto unicamente los campos seleccionados, seguido ordeno el resultado con sort y con uniq -c omito las repetidas por el numero de coincidencias, y vuelto a ordenar los resultados con sort -nr para comparar el valor numerico (el cual es invertido), seguido traigo o genera las primeras 11 lineas de la entrada, ya despues con tr -s ' ' reemplazo los caracteres que tengas concurrencia y por ultimo corto usando el delimitador cut -d' ' para que al final seleccione solo los campos que queden con -f3.

