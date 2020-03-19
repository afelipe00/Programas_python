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

visibilidad de los elementos dentro de una clase:
publicos: cuando un atributo o un metodo se declara de manera publica se puede acceder a este desde cualquier lugar, es decir,
desde la clase instanciada, clase heredada y otras clases.
privado: cuando un atributo o un metodo se declara de manera privada se puede acceder a este solo desde la clase que lo define. para 
poder obtener los valores de estos atributos se crean metodos conocidos como get (obtener) y set (enviar).
protegidos: cuando un atributo o un metodo se declara de manera protegida se puede acceder a este desde la clase que lo define o las
clases que lo heredan.

python no distingue entre atributos o metodos publicos y privados, si no que todos los elementos dentro de una clase pueden ser
accedidos por fuera de ellos. no obstante como convencion se prefija un guion bajo para indicar que dicho elemento debe ser privado.

abstraccion: la abstraccion en poo es poder tomar un concepto de la vida real y poder tranformarlo en el paradigma de poo, es decir, 
poder traducirlo o convertirlo en una clase con atributos y metodos. a parte de esto se pueden crear clases abstractas:
clases abstractas: una clase abstracta es una clase cuyo concepto del cual fue creada es (como su nombre lo indica) abstracto, es 
decir, no respresentan a un obejto fisico o a algo en especifico. estas clases abstractas las podemos utilizar para crear otras
clases que hereden los metodos y atributos de esta, pero las clases abstractas no pueden ser instanciadas. ejemplo: supongamos que
se crea una clase abstracta (animal) que tiene sus metodos comer, ivernar, etc. con esta clase se pueden crear otras a partir de las
cuales se crearan objetos como lo serian pajaro, perros, oso, etc.

encapsulamiento: este es el ocultamiento del estado de cada objeto, es decir, es la forma en la que la poo rige la manera en como los
objetos comparten los datos entre si y en como el programador encapsula estos datos dandole diferentes formas de acceso, estas pueden
ser pueblicas, privadas o protegidas.

polimorfismo: el polimorfismo es la capacidad que tiene este paradigma de que por medio de una clase (madre) las clases heredadas pueden
hacer la misma funcion pero aplicada a cada uno de los casos especificos de cada objeto, es decir, si tenemos una clase madre en la que
se tiene un metodo enviar mensaje, cada clase que herede esta clase madre puede aplicar la accion de enviar mensaje pero especifico 
para cada objeto que instancio la clase madre. es como que la clase madre envie una "orden" y cada objeto que la hereda la ejecuta a su
manera.

herencia: tal cual como en la vida real el concepto de herencia es cuando una clase (hija) hereda los meotodos o atributos de la clase
(padre) aprovechando asi las caracteristicas de esta clase (padre), esto no significa que la clase que heredo estos metodos o atributos
sea igual a la clase madre, pueden ser diferentes.
 
pass: es una palabra reservada que denota un "contenido vacio" 
"""


if __name__ == "__main__":
    pass