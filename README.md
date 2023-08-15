# EjercicioDjango
Ejercicio de Backend de un Sistema de Logística

### Activar entorno virtual

Desde la carpeta raiz activar el entorno virtual con "venv/Scripts/activate"

### Iniciar el servidor

Activar mediante "python sistema_logistica/manage.py runserver"

### Admin

Desde la url de admin: http://localhost:8000/admin/ podran realizarse las acciones de creación, borrado, modificacion de elementos, los cuales fueron creados previamente.

#### Cargado automatico de tipo de paquetes

Al crear un paquete, se podra ver como automaticamente se asigna un tipo de paquete

#### Agregado de items de planilla en una misma pantalla

Al ingresar al "Form" y seleccionar un elemento del modelo se podrá ver un menú para agregar uno o muchos ítems de planilla

#### Accion para pasar a en distribucion

Al ingresar al "Form" se podrá ver una lista despegable de acciones, dentro de la cual se encuentra "Change Package State To Distribution" para cambiar de estado todos los paquetes de una o muchas planillas, las cuales podrán ser filtradas con el menú de la derecha para saber si tiene paquetes EN DEPOSITO.

### Endpoint

#### Consulta del tracking

En la URL http://localhost:8000/consultTracking se podrá consultar el tracking de un paquete, habrá una lista despegable de los paquetes existentes para facilitar la prueba.