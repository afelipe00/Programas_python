"""
programacion orientada a objetos (oop)

que es una clase?: es una plantilla dentro de un programa que nos sirve para declarar un objeto de forma
predefinida, una clase suele representar entidades o conceptos tales comos: usuario, estudiante, etc.  
que es un objeto?: es una unidad dentro del programa que contiene un estado y un comportamiento, es decir,
tiene una serie de datos almacenados y una serie de tareas a ejecutar, los objetos se pueden crear instanciando
clases.
que es un metodo?: un metodo es un proceso o una tarea a realizar dentro de una clase. representan las acciones
dentro de los objetos.
que es un atributo?: son la variables o los datos dentro de las clases. representan las caracteristicas de los
objetos
tipos de atributos:
atributo de clase: son los atributos que dan caracteristica a la clase, es decir, todos los objetos creados a partir
de esta clase van a contener este mismo atributo (incluyendo el valor). estos atributos suelen representar las constantes
en los objetos. 
atributo de isntancia: son aquellos atributos que son caracteristicos a cada objeto, es decir segun el objeto creado estos
atributos pueden contener o no diferentes valores que representen al objeto

metodo constructor: el metodo contrsuctor es un metodo "especial" que nos permite instanciar obejtos de esa clase 
(todas las clases lo tienen). se invoca cada vez que se instancia la clase y lo que haces es crear un espacio de memoria
para ese nuevo objeto. si no se define en el codigo se crea de manera predeterminada, tambien nos permite inicializar los
atributos de este objeto.

(en python) parametro self: el parametro self hace referencia (direccion de memoria) al objeto que se esta creando, este 
es importante dado que cada metodo debe recibir como primer parametro el parametro self, para poder hacer referencia a el
 objeto creado. tambien nos permite manejar el alcance que tienen los atributos, es decir:

atributo con self (self.atributo): el alcance de este atributo es a nivel de la clase, es decir cualquier objeto que instancie
esta clase tendra acceso a el.

atributo sin self (nombre_atributo): el alcance de este attributo es a nivel del metodo, es decir que solo se puede acceder a esta
variable a travez del metodo en el cual fue declarada.


atributos publicos en python:  

"""