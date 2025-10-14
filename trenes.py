from lista_doble import DoublyLinkedList

class Vehiculo:
    def __init__(self, placa, tipo, prioridad):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

class ViaPrincipal:
    def __init__(self):
        self.via_principal = DoublyLinkedList()
        

    def insertra_vehiculo(self, placa, tipo, prioridad):
        vehiculo = Vehiculo(placa,tipo, prioridad )
        self.via_principal.append(vehiculo)


    def paso_preferencial(self):
        pass


    def __str__(self):
        if self.via_principal.head is None:
            return "No hay vehiculos en la via"
        
        actual = self.via_principal.head
        resultado = "Vehiculos en la via principal : \n"

        while actual is not None:
            vehiculo= actual.value
            resultado += f"Placa: {vehiculo.placa}, Tipo: {vehiculo.tipo}, Prioridad: {vehiculo.prioridad}\n"
            actual = actual.next

        return resultado





via = ViaPrincipal()
print(via)
via.insertra_vehiculo("10B","moto", "1")
via.insertra_vehiculo("11A","auto", "5")
via.insertra_vehiculo("84M","camion", "4")
via.insertra_vehiculo("19X","moto", "3")
print(via)



