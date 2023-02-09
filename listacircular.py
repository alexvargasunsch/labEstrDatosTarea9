class Nodo:
    def init (self,data):
        self.data = data
        self.siguente= None

class ListaCircular():
    def init (self):
        self.primero = None
        self.ultimo = None
        
    #agregar ultimo
    def agregarUltimo (self,data):
        if self.vacia():
            self.primero = self.primero = Nodo(data)
            self.ultimo.siguiente = self.primero       
        else:
            aux=self.ultimo
            self.ultimo = aux.siguiente = Nodo(data)
            self.ultimo.siguiente = self.primero

    #eliminar ultimo
    def eliminarUltimo(self):
        if self.vacia():
            print("lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            aux = self.primero
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente
            aux.siguiente = self.primero
            self.ultimo = aux

    #lista vacia   
    def vacia(self):
        return self.primero == None
    #agragar primero
    def agregarPrimero(self,data):
        if self.vacia():
            self.primero = self.ultimo == Nodo(data)
        else:
            aux = Nodo(data)
            aux.siguente = self.primero
            self.primero = aux
            self.ultimo.siguiente = self.primero

    #eliminar primero
    def eliminarPrimero(self):
        if self.vacia():
            print("Lista vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.ultimo.siguiente = self.primero

    #mostrar datos
    def mostrar(self):
        aux = self.primero 
        while aux:
            print(aux.data)
            aux = aux.siguiente
            if aux == self.primero:
                break
try:
    if __name__ == '__main__':
        opcion = 0
        lista = ListaCircular()
        while opcion !=6:
            print('lista simple enlazada: \n\n1. Agregar Final: \n2. Eliminar Final: \n3. Agregar inicio: \n4. Eliminar inicio: \n5. Mostar:  \n6. Lista Vacia?: \n7. Salir')

            opcion = int(input('Ingrese su opcion: '))
            if opcion== 1:                
                data = input('Ingrese un dato: ')
                lista.agregarUltimo(data)
            elif opcion==2:
                lista.eliminarUltimo()
            elif opcion==3:
                data = input('Ingrese un dato:')
                lista.agregarPrimero(data)
            elif opcion==4:
                lista.eliminarPrimero()
            elif opcion==5:
                lista.mostrar()
            elif opcion==6:
                print('si' if lista.vacia() else 'no')
            elif opcion==7:
                break
            else: 
                print('ingrse una de la opciones de la lista')
except Exception as e:
    print(e)