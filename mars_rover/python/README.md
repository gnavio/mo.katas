# 🛸 ​Solución - Mars rover kata

He escogido el lenguaje Python para el desarrollo de esta prueba.

## 🔷​ Rover
La clase Rover contiene el método constructor, los diferentes métodos para el movimiento del Rover y también para la detección de obstáculos, que se detallará a continuación.


                       N
        --------------------------------
        |   0,2   |   1,2   |   2,2    |
        -------------------------------- 
    W   |   0,1   |   1,1   |   2,1    |    E
        -------------------------------- 
        |   0,0   |   1,0   |   2,0    |
        --------------------------------
                       S

### 🚗 **move**
Este método se encarga de procesar los posibles movimientos del Rover ('f', 'b', 'r', 'l'). Se recorre el array de movimientos y se comprueba si coincide con alguno de los casos posibles.

Cada uno de los casos llama al método de movimiento o giro que hace desplazarse al Rover. **Para los movimientos 'f' y 'b' se comprueba si existen obstáculos en el camino** antes de llamar a los métodos de movimiento.

**Si existe un obstáculo, el Rover para e informa de su posición**. También se informa de la posición en la que se encuentra el obstáculo.

### 🔄 **turn_right / turn_left**
Estos métodos cambian la orientación del Rover. Si la orientación del Rover es 'N' y se rota una vez a la derecha, pasará a ser 'E'. Si es 'N' y rotamos a la izquierda, entonces pasa a 'W', así sucesivamente.

    def turn_right(self):
        c_points = ['N', 'E', 'S', 'W']
        self.orientation = c_points[c_points.index(self.orientation) + 1] 

    def turn_left(self):
        c_points = ['N', 'E', 'S', 'W']
        self.orientation = c_points[c_points.index(self.orientation) - 1]  

Para esto he creado un array con las diferentes orientaciones (puntos cardinales) en orden. Se busca el índice que ocupa la orientación actual del Rover en ese array y se le suma o se le se resta 1 (derecha o izquierda). La nueva variable orientación será igual al contenido del array que ocupa ese nuevo índice.

### ↕️ ​**forward / backward**
Este método comprueba la orientación del Rover y le suma uno a su variable x o y para que avance una casilla hacia delante.

**Para que el Rover nunca se salga del mapa 3x3 se utiliza el operador módulo en la variable que se está modificando**. Ejemplo: (self.y + 1) % 3
```
def forward(self):
    if self.orientation == 'N':
        self.y = (self.y + 1) % 3
    elif self.orientation == 'S':
        self.y = (self.y - 1) % 3
    elif self.orientation == 'E':
        self.x = (self.x + 1) % 3
    elif self.orientation == 'W':
        self.x = (self.x - 1) % 3
```
El método backdward es similar al forward, pero realiza el movimiento inverso en cada una de las orientaciones.
```
def backward(self):
    if self.orientation == 'N':
        self.y = (self.y - 1) % 3
    elif self.orientation == 'S':
        self.y = (self.y + 1) % 3
    elif self.orientation == 'E':
        self.x = (self.x - 1) % 3
    elif self.orientation == 'W':
        self.x = (self.x + 1) % 3
```
### 🚧 **detect_obstacle**
He creado una clase simple para los obstáculos. Cada objeto de la clase contiene dos variables (x e y) que indican la posición del obstáculo en el mapa.

#### 🔶 **Obstacle**
    class Obstacle():
    
    def __init__(self, obs_x = 0, obs_y = 0):
        self.x = obs_x
        self.y = obs_y

En el constructor del Rover he añadido un nuevo parámetro para poder pasarle una lista de obstáculos.

En detect_obstacle se comprueba si la posición a la que va a moverse el Rover coincide con la posición de alguno de los obstáculos. Si esto es así se devuelve True y se gestiona que el Rover pare en el método move. Hay un caso creado para cada una de las orientaciones que puede tener el Rover.

Este es el caso para la orientación 'N'.
```
case 'N':
    if (next_move == 'f' and (obs.x == self.x and obs.y == (self.y + 1) % 3) or 
        next_move == 'b' and (obs.x == self.x and obs.y == (self.y - 1) % 3)):
            print('Obstacle detected at: x = ' + str(obs.x) + ', y = ' + str(obs.y))
            return True
    else:
        return False
```
## 🧪 Tests
En los tests se comprueba que cada uno de los casos posibles para estos métodos funcione correctamente. Estos son los apartados del test:
 - Movement
 - Turn
 - Wrapping
 - Obstacles

Para ejecutar los tests:

```
python -m unittest mars_rover_test_case
```
