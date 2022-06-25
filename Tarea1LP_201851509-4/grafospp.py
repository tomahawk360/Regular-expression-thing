import re

"""Nombre de la función
———————–
Parametro 1 : Tipo
Parametro 2 : Tipo
Parametro 3 : Tipo
————————
Breve descripcion de la wea y lo que retorna
"""

"""open
———————–
Parametro 1 : String
Parametro 2 : Char
————————
Abren los archivos input y errores en dos instancias distintas. La primera mantiene el archivo abierto solo mientras se lee y se almacena en la variable
'prueba', luego se cierra automaticamente. La segunda crea el archivo errores.txt y lo guarda en la variable 'errores', manteniendo el archivo abierto
durante hasta que se termine de ejecutar la totalidad del codigo para su correspondiente edición.
"""
with open('input.txt','r') as f:
    prueba = f.read()

errores = open('errores.txt', 'w')

"""Class Calle
————————
Tipo de dato abstracto que contiene las características y métodos de una calle.
"""
class Calle:
    """__init__
    ———————–
    self : Calle
    nombre : String
    id : String
    personas : List
    ————————
    Le asigna valores a sus propiedades según los parámetros ingresados; a cada propiedad se le asigna el parámetro con el mismo nombre. 
    Se llama implícitamente cuando se inicializa una instancia de la clase, y retorna dicha instancia.
    """
    def __init__(self, nombre, id, personas):
        self.nombre = nombre
        self.id = id
        self.personas = personas

    """getNombre
    ———————–
    self : Calle
    ————————
    Retorna la propiedad 'nombre' de la instancia self
    """   
    def getNombre(self):
        return self.nombre
    
    """getID
    ———————–
    self : Calle
    ————————
    Retorna la propiedad 'id' de la instancia self
    """
    def getID(self):
        return self.id

    """getPersonas
    ———————–
    self : Calle
    ————————
    Retorna la propiedad 'personas' de la instancia self
    """
    def getPersonas(self):
        return self.personas

    """getNombrePersonas
    ———————–
    self : Calle
    ————————
    Extrae el/los nombre/s de las personas referidas en la propiedad 'personas' de la instancia self, luego guarda los nombres
    en una lista y retorna dicha lista.
    """
    def getNombrePersonas(self):
        nombres = []
        for p in self.personas:
            nombres.append(p[0])
        return nombres
    
    """getApellidoPersonas
    ———————–
    self : Calle
    ————————
    Extrae el/los apellido/s de las personas referidas en la propiedad 'personas' de la instancia self, luego guarda los apellidos
    en una lista y retorna dicha lista.
    """
    def getApellidoPersonas(self):
        apellidos = []
        for p in self.personas:
            apellidos.append(p[1])
        return apellidos

    """getTelefonoPersonas
    ———————–
    self : Calle
    ————————
    Extrae el número de telefono de las personas referidas en la propiedad 'personas' de la instancia self, luego guarda los números
    en una lista y retorna dicha lista.
    """
    def getTelefonoPersonas(self):
        telefonos = []
        for p in self.personas:
            telefonos.append(p[2])
        return telefonos

    """getRutPersonas
    ———————–
    self : Calle
    ————————
    Extrae el número rut de las personas referidas en la propiedad 'personas' de la instancia self, luego guarda los números
    en una lista y retorna dicha lista.
    """
    def getRutPersonas(self):
        ruts = []
        for p in self.personas:
            ruts.append(p[3])
        return ruts

"""Class Grafo
————————
Tipo de dato abstracto que contiene las características y métodos del grafo que contiene las calles.
"""
class Grafo:
    """__init__
    ———————–
    self : Grafo
    ————————
    Crea una lista 'calle' para almacenar las instancias de Calle y un diccionario 'caminos' para almacenar los caminos que conectan las instancias. 
    Se llama implícitamente cuando se inicializa una instancia de la clase, y retorna dicha instancia.
    """
    def __init__(self):
        self.calles = []
        self.caminos = {}

    """existeCalle
    ———————–
    self : Grafo
    calleid : String
    ————————
    Revisa si alguna de estas Calles posee 'calleid' como su propiedad 'id'. Si alguna de estas Calles tiene 'calleid' como su respectiva id,
    retorna True, caso contrario, retorna False.
    """
    def existeCalle(self, calleid):
        for x in self.calles:
            if(x.getID() == calleid):
                return True
        return False
    
    """insertarCalle
    ———————–
    self : Grafo
    calle1 : Calle
    ————————
    Revisa si 'calle1' es una instancia de clase Calle. En caso de serlo, lo añade a 'calles' de self y crea una key en 'caminos' de self con la id de 'calle1',
    asignandole una lista vacia a la key, la cual almacenará las calles a las que se puede llegar desde 'calle1. Si 'calle1' no es una instancia de Calle, 
    se retorna un String señalando la invalidez del input.
    """
    def insertarCalle(self, calle1):
        try:
            id = calle1.getID()
        except:
            return 'Input no valido: No es TDA Calle'

        self.calles.append(calle1)
        self.caminos[id] = []

    """actualizarCalle
    ———————–
    self : Grafo
    calleid : String
    nucalle : Calle
    ————————
    Revisa si 'nucalle' es una instancia de clase Calle. En caso de serlo, se busca en 'calles' el elemento con 'calleid' como su id y se elimina. Luego se añade 'nucalle' a 'calles'
    en la misma posición donde estaba el elemento eliminado. Luego en 'caminos' se crea una key con la id de 'nucalles' y se apropia de la lista de calles conectadas de la calle que se
    desea actualizar, la cual es borrada. Finalmente, se reemplaza la id de la calle a actualizar de todas las listas de calles conectadas en 'caminos' con la id de 'nucalle'.
    """
    def actualizarCalle(self, calleid, nucalle):
        try:
            nuid = nucalle.getID()
        except:
            return 'Input no valido: No es TDA Calle'
        
        for x in self.calles:
            if(x.getID() == calleid):
                oldcalle = self.calles.index(x)
                self.calles.remove(x)
        
        self.calles.insert(oldcalle, nucalle)

        self.caminos[nuid] = self.caminos[calleid]
        self.caminos.pop(calleid, None)

        for key in self.caminos.keys():
            if(calleid in self.caminos[key]):
                self.caminos[key].remove(calleid)
                self.caminos[key].append(nuid)

    """obtenerCalle
    ———————–
    self : Grafo
    idcalle : String
    ————————
    Si existe una calle en 'calles' que tiene como id a 'idcalle', se extraen sus propiedades y se almacenan en una lista, la cual es retornada. Caso contrario,
    se retorna un String señalando la invalidez del input.
    """
    def obtenerCalle(self, idcalle):
        if(self.existeCalle(idcalle)):
            for k in self.calles:
                if(k.getID() == idcalle):
                    key = k

            info = []
            info.append(key.getNombre())
            info.append(key.getID())
            info.append(key.getPersonas())

            return info
        else:
            return 'Input no valido: No se tiene registro de la calle ingresada'

    """obtenerTodaCalle
    ———————–
    self : Grafo
    ————————
    Se extraen las propiedades de todas las calles en 'calles' y se guardan en respectivas listas, las cuales a su vez se almacenan en una lista mayor.
    Se retorna la lista mayor.
    """
    def obtenerTodaCalle(self):
        recalles = []
        for x in self.calles:
            calle = self.obtenerCalle(x.getID())
            recalles.append(calle)

        return recalles

    """insertarCamino
    ———————–
    self : Grafo
    id1 : String
    id2 : String
    ————————
    Si 'id1' e 'id2' existen en 'caminos' como keys, se añade 'id2' a la lista de calles conectadas de la key 'id1', indicando así que existe un camino
    que parte de 'id1' y llega a 'id2'. Si ninguno de las ids estan en 'caminos', se retornan Strings señalando la invalidez del input.
    """
    def insertarCamino(self, id1, id2):
        if((id1 and id2) in self.caminos):
            self.caminos[id1].append(id2)
        
        elif(id1 not in self.caminos):
            return 'Calle %s no se encuentra en el Grafo. Registela antes de crear Camino' % id1
       
        elif(id2 not in self.caminos):
            return 'Calle %s no se encuentra en el Grafo. Registela antes de crear Camino' % id2

    """existeCamino
    ———————–
    self : Grafo
    id1 : String
    id2 : String
    ————————
    Si 'id1' e 'id2' están en 'caminos', se revisa si 'id2' está en la lista de calles conectadas de 'id1' en el diccionario. Si no, entonces se realiza una Búsqueda a lo Profundo
    en 'caminos' partiendo desde 'id1', donde las calles visitadas se almacenan en una lista, y finalmente se revisa si 'id2' se encuentra en dicha lista. Sean cualquiera de estos dos
    casos afirmativos, se retorna True. Caso contrario, se retorna False. Si, además, los parámetros no están en 'caminos', se retorna un String señalando la invalidez de los input.
    """
    def existeCamino(self, id1, id2):

        if((id1 and id2) in self.caminos):

            if(id2 in self.caminos[id1]):
                return True

            elif(id2 not in self.caminos[id1]):
                visitas = []
                stack = []
                stack.append(id1)
                while(len(stack) != 0):
                    nodo = stack.pop()
                    if(nodo not in visitas):
                        visitas.append(nodo)
                        for x in self.caminos[nodo]:
                            stack.append(x)
                if(id2 in visitas):
                    return True
                else:
                    return False
        else:
            return 'No existe con %s o %s' % (id1,id2)

    """inicioCamino
    ———————–
    self : Grafo
    calleid : String
    ————————
    Si 'calleid' esta en 'calles', se realiza una Busqueda a lo Ancho en 'caminos' con la key 'calleid' como inicio. Esta busqueda retornará una lista con caminos binarios,
    por lo que luego se revisan aquellos caminos que no tengan 'calleid' como inicio y se unen a caminos que terminen con sus calles de inicio, formando caminos más grandes
    hasta que solo queden caminos que tengan 'calleid' de inicio. Finalmente, se elminan los duplicados de la lista y se retorna. Si 'calleid' no esta en 'calles', se retorna 
    un String señalando la invalidez del input.
    """
    def inicioCamino(self, calleid):
        if(self.existeCalle(calleid)):

            roads = []
            visitado = []
            queue = []
            queue.insert(0, calleid)

            while(len(queue) != 0):
                x = queue.pop()
                if(x not in visitado):
                    visitado.append(x)
                    for node in self.caminos[x]:
                        if(node not in visitado):
                            queue.insert(0,node)
                            roads.append([x,node])

            for cam in roads:
                if(cam[0] != calleid):
                    for cam2 in roads:
                        if(cam2[len(cam2) - 1] == cam[0]):
                            cam3 = cam2.copy()
                            cam3.append(cam[1])
                            roads.append(cam3)

            plusroads = []
            for com in roads:
                if(com[0] == calleid and com not in plusroads):
                    plusroads.append(com)

            return plusroads
        else:
            return 'Input no valido: No se tiene registro de la calle ingresada'

    """callesPorNombre
    ———————–
    self : Grafo
    nombre : String
    ————————
    Se revisan en todas las calles de 'calles' si en su propiedad 'personas' está 'nombre'. Aquellas que lo tengan, son añadidan en una lista, la cual se 
    retorna en caso de no estar vacia. De estarlo, se retorna un String señalando que no existen calles que contengan 'nombre'.
    """
    def callesPorNombre(self, nombre):
        roads = []

        for calle in self.calles:
            personas = calle.getNombrePersonas()

            for sus in personas:
                nombres = sus.split(',')
                if(nombre in nombres):
                    roads.append(calle.getNombre())

        if(len(roads) == 0):
            return 'No existen calles con personas con ese nombre'
        
        return roads

    """callesPorApellido
    ———————–
    self : Grafo
    apellido : String
    ————————
    Se revisan en todas las calles de 'calles' si en su propiedad 'personas' está 'apellido'. Aquellas que lo tengan, son añadidan en una lista, la cual se 
    retorna en caso de no estar vacia. De estarlo, se retorna un String señalando que no existen calles que contengan 'apellido'.
    """
    def callesPorApellido(self, apellido):
        roads = []

        for calle in self.calles:
            personas = calle.getApellidoPersonas()

            for sus in personas:
                apellidos = sus.split(',')
                if(apellido in apellidos):
                    roads.append(calle.getNombre())
        
        if(len(roads) == 0):
            return 'No existen calles con personas con ese apellido'

        return roads

    """callesPorRUT
    ———————–
    self : Grafo
    rut : String
    ————————
    Se revisan en todas las calles de 'calles' si en su propiedad 'personas' está 'rut'. Aquellas que lo tengan, son añadidan en una lista, la cual se 
    retorna en caso de no estar vacia. De estarlo, se retorna un String señalando que no existen calles que contengan 'rut'.
    """
    def callesPorRUT(self, rut):
        roads = []

        for calle in self.calles:
            personas = calle.getRutPersonas()

            for sus in personas:
                if(sus == rut):
                    roads.append(calle.getNombre())
        
        if(len(roads) == 0):
            return 'No existen calles con personas con ese RUT'
        
        return roads

    """callesPorTelefono
    ———————–
    self : Grafo
    telefono : String
    ————————
    Se revisan en todas las calles de 'calles' si en su propiedad 'personas' está 'telefono'. Aquellas que lo tengan, son añadidan en una lista, la cual se 
    retorna en caso de no estar vacia. De estarlo, se retorna un String señalando que no existen calles que contengan 'telefono'.
    """
    def callesPorTelefono(self, telefono):
        roads = []

        for calle in self.calles:
            personas = calle.getTelefonoPersonas()

            for sus in personas:
                if(sus == telefono):
                    roads.append(calle.getNombre())

        if(len(roads) == 0):
            return 'No existen calles con personas con ese telefono'
        
        return roads

"""Declaración de Instancia
————————
Se declara la instancia grafopp de la clase Grafo.
"""
grafopp = Grafo()

"""Declaracion de Patrones
————————
Se declaran múltiples String que sirvan de patrones para su posterior uso en la identificación de expresiones regulares.
"""
nombre_persona = r'[A-Z][a-z- ]+'
apellido_persona = r'[A-Z][a-z- ]+'
telefono = r'[+][1-9][0-9]{5}'
rut = r'[1-9][0-9]+-[0-9k]'

nombre_calle = r'[A-Z][a-zA-Z0-9- ]*'
id_calle = r'#[A-Z]{2}[0-9]{2}'

persona = '((?:%s)(?:\,%s)*)_((?:%s)(?:\,%s)*)_(%s)_(%s)' % (nombre_persona,nombre_persona,apellido_persona,apellido_persona,telefono,rut)

calle = '(%s).(%s).((%s)(\/%s)*)' % (nombre_calle, id_calle, persona, persona)

"""Recursion
———————–
n : Int
————————
Forma un String patrón de forma recursiva, una cantidad 'n' veces. Luego lo retorna.
"""
def Recursion(n):
    if(n == 1):
        return('\((%s|%s)\:(%s|%s)\)' % (calle, id_calle, calle, id_calle))
    else:
        return('\((%s|%s|%s)\:(%s|%s|%s)\)' % (Recursion(n-1), calle, id_calle, Recursion(n-1), calle, id_calle))

"""Modulo 11
———————–
rut : String
————————
Toma la forma numérica de 'rut' previo al guión y le aplica el algoritmo Módulo 11 para obtener su digito verificador. Luego, compara el digito verificador 
obtenido con el digito verificador existente en 'rut' y retorna True si ambos son el mismo. Caso contrario, retorna False.
"""
def Modulo11(rut):

    limit = len(rut)-2
    sum = 0
    plus = 0
    for i in range(limit-1, -1, -1):
        sum += int(rut[i]) * (2 + plus)

        if(plus < 5):
            plus += 1
        else:
            plus = 0
    
    factor = 11 - (sum % 11)
    if(factor == 11):
        factor = 0

    try: 
        dv = int(rut[-1])
    except ValueError:
        if(rut[-1] == 'k'):
            dv = 10

    if(dv == factor):
        return True
    else: 
        return False

"""crearCalle
———————–
comcalle : Match
grafo : Grafo
————————
Obtiene los grupos de 'comcalle' y los usa como parámetros para crear una instancia de Calle. Luego, verifica que el 'rut' de la instancia sea válido según
Módulo 11. De serlo, se añade la instancia a 'grafo' y se retorna la instancia. Caso contrario, se retorna False.
"""
def crearCalle(comcalle, grafo):
    comcallel = comcalle.groups()

    calleNombre = comcallel[0]
    calleID = comcallel[1]
    callePersonas = comcallel[2]

    insPersona = re.findall(persona,callePersonas)

    instancia_calle = Calle(calleNombre,calleID,[x for x in insPersona])

    rolunico = instancia_calle.getRutPersonas()
    rutvalido = list(map(Modulo11, rolunico))
    
    if(sum(rutvalido) == len(rutvalido)):
        grafo.insertarCalle(instancia_calle)

        return instancia_calle

    return False

"""crearCaminos
———————–
comcaminopt : Match
grafo : Grafo
————————
Cuenta la cantidad de '\:' en el match de 'comcaminopt' y luego forma un patron usando la función Recursion(cantidad de '\:' en el match). Corrobora que el match de 
'comcaminopt' calze con el patrón, y de hacerlo, desglosa el match en una lista mostrando una sucesión de calles e ids. Se van añadiendo caminos binarios a 'grafo' 
según la sucesión antes obtenida. Las calles de la sucesión, además, son añadidas a 'grafo'. Luego se retorna la lista con la sucesión. Si el match de 'comcaminopt' 
no calza con el patron creado por la Recursion, se retorna False.
"""
def crearCaminos(comcaminopt, grafo):
    comcamino_str = comcaminopt.group(0)
    dosPuntos = re.findall('\:', comcamino_str)
    numero = sum(1 for _ in dosPuntos)
    patron = Recursion(numero)
    comcaminos = re.match(patron, comcamino_str)
    if(comcaminos):
        seg = re.split('\:', comcaminos.group(0))
        resto = 0
        for elemento in seg:
            matchcalle = re.search(calle, elemento)
            matchid = re.search('(\A|\()(%s)' % id_calle, elemento)
            if(matchcalle):
                nova_calle = crearCalle(matchcalle, grafo)
                nova_id = nova_calle.getID()
                if(resto != 0):
                    grafo.insertarCamino(resto, nova_id)
                resto = nova_id
            elif(matchid):
                nova_id = matchid.group(2)
                if(resto != 0):
                    grafo.insertarCamino(resto, nova_id)
                resto = nova_id
        
        return seg

    return False

"""printID
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprintl' y busca en 'grafo' la calle cuya id sea la presente en el match de 'comprintl'. Si existe dicha calle, se imprime en la
consola las propiedades de la calle. Caso contrario, se imprime en la consola que dicha calle no existe.
"""
def printID(comprint, grafo):
    comprintl = comprint.groups()
    calle_obtenida = grafo.obtenerCalle(comprintl[0])
    if(type(calle_obtenida) == list):
        print('CALLE:')
        print('%s' % calle_obtenida[0])
        print('%s' % calle_obtenida[1])
        for j in calle_obtenida[2]:
            print('%s' % j[0])
            print('%s' % j[1])
            print('%s' % j[2])
            print('%s' % j[3])
    elif(type(calle_obtenida) == str):
        print('No existe esa calle')
    
    return True

"""printAll
———————–
grafo : Grafo
————————
Se extrae una lista que contenga, a su vez, listas con las propiedades de cada calle en 'grafo'. Luego se imprime en la consola los contenidos de cada
lista. Finalmente, se retorna True para confirmar que la función fue realizada.
"""
def printAll(grafo):
    calles_obtenidas = grafo.obtenerTodaCalle()
    for x in calles_obtenidas:
        print('CALLE:')
        print('%s' % x[0])
        print('%s' % x[1])
        for y in x[2]:
            print('%s' % y[0])
            print('%s' % y[1])
            print('%s' % y[2])
            print('%s' % y[3])
    
    return True

"""printCaminos
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprint' y extrae de ellos la id de la calle de inicio. Luego, se busca en 'grafo' la lista de caminos que comiencen en dicha calle.
Una vez obtenida la lista, se imprimen los caminos en la consola usando el formato del enunciado. Retorna True para confirmar el término de la función.
"""
def printCaminos(comprint, grafo):
    inicio_camino = comprint.groups()[0]
    caminos = grafo.inicioCamino(inicio_camino)
    
    print('CAMINOS DESDE %s:' % inicio_camino)
    if(len(caminos) != 0):
        for cl in caminos:
            for i in range(len(cl)-1):
                print('%s->' % cl[i], end='')
            print('%s' % cl[len(cl)-1])
    else:
        print('Ninguno')
    
    return True

"""printByNombre
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprint' y extrae de ellos el 'nombre' deseado. Luego, se busca en 'grafo' la lista de calles cuyas personas tengan el 'nombre' deseado.
Una vez obtenida la lista, se imprimen las calles en la consola usando el formato del enunciado. Retorna True para confirmar el término de la función.
"""
def printByNombre(comprint, grafo):
    name = comprint.groups()[0]
    caminos = grafo.callesPorNombre(name)
    if(type(caminos) == list):
        print('CALLES CON PERSONAS DE NOMBRE %s:' % name)
        for cn in caminos:
            print(cn)
    else:
        print(caminos)

    return True

"""printByApellido
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprint' y extrae de ellos el 'apellido' deseado. Luego, se busca en 'grafo' la lista de calles cuyas personas tengan el 'apellido' deseado.
Una vez obtenida la lista, se imprimen las calles en la consola usando el formato del enunciado. Retorna True para confirmar el término de la función.
"""
def printByApellido(comprint, grafo):
    surname = comprint.groups()[0]
    caminos = grafo.callesPorApellido(surname)
    if(type(caminos) == list):
        print('CALLES CON PERSONAS DE APELLIDO %s:' % surname)
        for cn in caminos:
            print(cn)
    else:
        print(caminos)

    return True

"""printByRut
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprint' y extrae de ellos el 'rut' deseado. Luego, se busca en 'grafo' la lista de calles cuyas personas tengan el 'rut' deseado.
Una vez obtenida la lista, se imprimen las calles en la consola usando el formato del enunciado. Retorna True para confirmar el término de la función.
"""
def printByRut(comprint, grafo):
    run = comprint.groups()[0]
    caminos = grafo.callesPorRUT(run)
    if(type(caminos) == list):
        print('CALLES CON PERSONAS DE RUT %s:' % run)
        for cn in caminos:
            print(cn)
    else:
        print(caminos)

    return True

"""printByTelefono
———————–
comprint : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comprint' y extrae de ellos el 'telefono' deseado. Luego, se busca en 'grafo' la lista de calles cuyas personas tengan el 'telefono' deseado.
Una vez obtenida la lista, se imprimen las calles en la consola usando el formato del enunciado. Retorna True para confirmar el término de la función.
"""
def printByTelefono(comprint, grafo):
    phone = comprint.groups()[0]
    caminos = grafo.callesPorTelefono(phone)
    if(type(caminos) == list):
        print('CALLES CON PERSONAS DE TELEFONO %s:' % phone)
        for cn in caminos:
            print(cn)
    else:
        print(caminos)

    return True

"""update
———————–
comupdate : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comupdate' y los usa como parámetros para crear una instancia de Calle. Luego, verifica que el 'rut' de la instancia sea válido según
Módulo 11. De serlo, se actualiza la calle con la id indicada en el match con la nueva instancia de Calle creada, y se retorna la instancia. Caso contrario, se retorna False.
"""
def update(comupdate, grafo):
    comupdatel = comupdate.groups()

    novo_nombre = comupdatel[2]
    nova_id = comupdatel[3]
    nova_personas = comupdatel[4]

    nu_ins_persona = re.findall(persona,nova_personas)

    nova_calle = Calle(novo_nombre,nova_id,[x for x in nu_ins_persona])

    novo_rol = nova_calle.getRutPersonas()
    rutvalido = list(map(Modulo11, novo_rol))
    
    if(sum(rutvalido) == len(rutvalido)):
        grafo.actualizarCalle(comupdatel[0],nova_calle)
        return nova_calle

    return False

"""validCamino
———————–
comvalid : Match
grafo : Grafo
————————
Obtiene los grupos del match de 'comvalid' y extrae las ids deseadas. Luego, se corrobora si existe un camino en 'grafo' que conecte las calles correspondientes
a las ids deseadas. Si se obtiene un Booleano del método, se retorna si es posible o no dependiendo de si el Booleano es True o False, respectivamente. Si se obtiene
un String del método, entonces no existen calles con las ids deseadas.
"""
def validCamino(comvalid, grafo):
    comvalidcaminol = comvalid.groups()
    validez = grafo.existeCamino(comvalidcaminol[0],comvalidcaminol[1])
    if(type(validez) == bool):
        if(validez):
            print('Si se puede')
        else:
            print('No se puede')
    if(type(validez) == str):
        print(validez)
    
    return True

"""Reconocimiento de los comandos
————————
Se aplica un Finditer a todo el archivo en prueba para reconocer los comandos y almacenarlos en un iterador para su posterior revisión individual.
Luego, en la cadena if-else se reconoce cada comando según su respectiva expresión regular y se ejecutan las funciones apropiadas.
"""
for comand in re.finditer('(.*?)(\Z|\;)',prueba):

    comand = comand.group(0)

    #Match comando calle
    if(re.match(calle,comand)):
        comcalle = re.match(calle,comand)
        nucalle = crearCalle(comcalle, grafopp)
        if(type(nucalle) == bool):
            errores.write(comand)

    #Match comando camino
    elif(re.match('(\().+', comand)):
        comcaminos_proto = re.match('(\().+', comand)
        nucaminos = crearCaminos(comcaminos_proto, grafopp)
        if(type(nucaminos) == bool):
            errores.write(comand)
        
    #Match comando print ID
    elif(re.match('print (%s)' % id_calle,comand)):
        comprint = re.match('print (%s)' % id_calle,comand)
        printID(comprint, grafopp)

    #Match comando print_all
    elif(re.match('print\_all',comand)):
        comprintall = re.match('print\_all',comand)
        printAll(grafopp)

    #Match comando print_caminos ID
    elif(re.match('print_caminos (%s)' % (id_calle),comand)):
        comprintcaminos = re.match('print_caminos (%s)' % (id_calle),comand)
        printCaminos(comprintcaminos, grafopp)
        
    #Match comando print_by_nombre nombre
    elif(re.match('print_by_nombre (%s)' % (nombre_persona),comand)):
        comprintnombre = re.match('print_by_nombre (%s)' % (nombre_persona),comand)
        printByNombre(comprintnombre, grafopp)

    #Match comando print_by_apellido apellido
    elif(re.match('print_by_apellido (%s)' % (apellido_persona),comand)):
        comprintapellido = re.match('print_by_apellido (%s)' % (apellido_persona),comand)
        printByApellido(comprintapellido, grafopp)

    #Match comando print_by_rut rut
    elif(re.match('print_by_rut (%s)' % (rut),comand)):
        comprintrut = re.match('print_by_rut (%s)' % (rut),comand)
        printByRut(comprintrut, grafopp)

    #Match comando print_by_telefono telefono
    elif(re.match('print_by_telefono (%s)' % (telefono),comand)):
        comprinttelefono = re.match('print_by_telefono (%s)' % (telefono),comand)
        printByTelefono(comprinttelefono, grafopp)

    #Match comando update ID calle
    elif(re.match('update (%s) (%s)' % (id_calle,calle),comand)):
        comupdate = re.match('update (%s) (%s)' % (id_calle,calle),comand)
        update(comupdate, grafopp)

    #Match comando valid_camino ID1 ID2
    elif(re.match('valid_camino (%s) (%s)' % (id_calle,id_calle),comand)):
        comvalidcamino = re.match('valid_camino (%s) (%s)' % (id_calle,id_calle),comand)
        validCamino(comvalidcamino, grafopp)

    #Manda comando a errores.txt
    else:
        comando = re.sub('\;','\n',comand)
        errores.write(comando)

errores.close()
