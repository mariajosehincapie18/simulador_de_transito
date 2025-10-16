from lista_doble import DoublyLinkedList

class Vehiculo:
    def __init__(self, placa, tipo, prioridad):
        self.placa = placa
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        return f"PLACA: {self.placa} TIPO: {self.tipo} PRIORIDAD: {self.prioridad}"

class ViaPrincipal:
    def __init__(self):
        self.via_principal = DoublyLinkedList()        

    def insertra_vehiculo(self, placa:str, tipo:str, prioridad:int):
        if ((tipo == "moto") or (tipo== "auto" ) or  (tipo == "camion")) and (( prioridad >=1 )and (prioridad <= 5)):
            vehiculo = Vehiculo(placa,tipo, prioridad )
            self.via_principal.append(vehiculo)
            return True
        else:
            return False


    def paso_preferencial(self):
        if self.via_principal.size < 2:
            return
        
        current_node = self.via_principal.tail
     
        while current_node is not None:
            previo_original = current_node.prev

            if current_node.value.tipo == "moto" and current_node.value.prioridad == 1:
                
                if current_node is not self.via_principal.head:
                    
                    if current_node.prev is not None:
                        current_node.prev.next = current_node.next
                    else:
                        self.via_principal.head = current_node.next

                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev

                    else:
                        self.via_principal.tail = current_node.prev

                    head = self.via_principal.head
                    current_node.prev = None
                    current_node.next = head
                    if head is not None:
                        head.prev = current_node    
                    self.via_principal.head= current_node

            current_node = previo_original
            
    def eliminar_camiones(self):
        current_node = self.via_principal.head

        while current_node is not None:
            siguiente = current_node.next

            if current_node.value.tipo == "camion" and current_node.value.prioridad > 3:

                if current_node.prev is None:
                    self.via_principal.head = current_node.next
                    if current_node.next is not None:
                        current_node.next.prev = None

                elif current_node.next is None:
                    self.via_principal.tail = current_node.prev
                    current_node.prev.next= None

                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev



                current_node.next = None
                current_node.prev = None
            
            current_node = siguiente

        



    

    def __str__(self):
        return str(self.via_principal)




via = ViaPrincipal()
via.insertra_vehiculo("10B","auto", 2)
via.insertra_vehiculo("11A","moto", 1)
via.insertra_vehiculo("84M","camion", 4)
via.insertra_vehiculo("19X","camion", 3)
print(via)
via.eliminar_camiones()
print(via)






