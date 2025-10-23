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
        if self.via_principal.head is None or self.via_principal.head.next is None:
            return
        
        current_node = self.via_principal.head
        fin_bloque = None
        while current_node is not None:
            next_original= current_node.next
            if current_node.value.tipo == "moto" and current_node.value.prioridad == 1:
                if fin_bloque is None:
                    if current_node is not self.via_principal.head:
                        if current_node.prev is not None:
                            current_node.prev.next = current_node.next
                        else:
                            self.via_principal.head = current_node.next

                        if current_node.next is not None:
                            current_node.next.prev = current_node.prev
                        else:
                            self.via_principal.tail = current_node.prev

                        current_node.prev= None
                        current_node.next = self.via_principal.head
                        if self.via_principal.head is not None:
                            self.via_principal.head.prev = current_node
                        self.via_principal.head = current_node
                    fin_bloque = self.via_principal.head

                else:
                    if current_node is fin_bloque.next:
                        fin_bloque = current_node
                    elif current_node is not self.via_principal.head:
                        if current_node.prev is not None:
                            current_node.prev.next = current_node.next
                        else:
                            self.via_principal.head=  current_node.next

                        
                        if current_node.next is not None:
                            current_node.next.prev = current_node.prev
                        else:
                            self.via_principal.tail = current_node.prev

                        anterior = fin_bloque.next
                        current_node.prev = fin_bloque
                        current_node.next = anterior
                        fin_bloque.next = current_node
                        if anterior is not None:
                            anterior.prev = current_node
                        else:
                            self.via_principal.tail = current_node

                        
                        fin_bloque = current_node
                    
                    else:

                        if current_node is fin_bloque:
                            pass
                        else:
                            pass

            current_node = next_original


                        
               
            
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

    def choque(self, placa1, placa2):
        if placa1 == placa2:
            return print("las placas son iguales")
        

        p1= None
        current_node = self.via_principal.head
        while current_node is not None:
            if current_node.value.placa == placa1 or current_node.value.placa == placa2:
                p1 = current_node
                break
        
            
            current_node = current_node.next

        if p1 is None:
            return print("No existe la placa")
            
        p2= None            
        current_node_2 = p1.next
        while current_node_2 is not None:
            if current_node_2.value.placa == placa1 or current_node_2.value.placa == placa2:
                p2 = current_node_2
                break

            current_node_2 = current_node_2.next

        if p2 is None:
            return print("No existe la placa para comparar")

        inicio = p1.next
        if inicio is p2:
            return print("son placas adyacentes no tiene autos en el medio")
        

        while inicio is not p2:
            siguiente = inicio.next
            inicio.next = None
            inicio.prev = None


            inicio = siguiente

        p1.next = p2
        p2.prev = p1
    
    def invertir_via(self):
        cont1 = 0
        current_1= self.via_principal.head
        head = self.via_principal.head
        tail = self.via_principal.tail
        while current_1 is not None:
            if current_1.value.tipo == "auto":
                cont1 += 1
                       
            current_1= current_1.next
        
        cont2 =0
        current_2 = self.via_principal.head
        while current_2 is not None:
            if current_2.value.tipo == "moto":
                cont2 += 1
                
            current_2 = current_2.next
        
        if cont2 > cont1:
            current = head
            while current is not None:
                siguiente = current.next
                current.next = current.prev
                current.prev = siguiente
                current = siguiente


            self.via_principal.head = tail
            self.via_principal.tail = head

        else:
            print("no hay suficientes motos para invertir el orden de la via")


    def reorganizar_por_prioridades(self):
        fin_segmento = None
        for p in range(1, 6):

            if fin_segmento is None:
                current = self.via_principal.head
            else:
                current= fin_segmento.next
            
            while current is not None:
                next_current = current.next

                if current.value.prioridad == p:
                    if fin_segmento is None:
                        if current is not self.via_principal.head:
                            if current.prev is not None:
                                current.prev.next = current.next
                            if current.next is not None:
                                current.next.prev = current.prev
                            else:
                                self.via_principal.tail= current.prev

                        

                            current.prev= None
                            current.next= self.via_principal.head
                            self.via_principal.head.prev= current
                            self.via_principal.head= current

                        fin_segmento= current

                    elif current is fin_segmento.next:
                        fin_segmento= current
                    else:
                        if current.prev is not  None:
                            current.prev.next = current.next

                        if current.next is not None:
                            current.next.prev = current.prev

                        else:
                            self.via_principal.tail = current.prev



                        despues= fin_segmento.next
                        current.prev= fin_segmento
                        current.next = despues

                        fin_segmento.next = current
                        if despues is not None:
                            despues.prev= current
                        else:
                            self.via_principal.tail = current


                        fin_segmento= current

                current= next_current


 

    

     

    def __str__(self):
        return str(self.via_principal)




via = ViaPrincipal()
via.insertra_vehiculo("1","auto", 2)
via.insertra_vehiculo("2","moto", 1)
via.insertra_vehiculo("3","moto", 3)
via.insertra_vehiculo("4","camion",2)
via.insertra_vehiculo("5","moto", 1)
print("Via principal: ",via)
via.paso_preferencial()
print("Paso preferencial: ",via)
via.reorganizar_por_prioridades()
print("Reorganizar por prioridades: ",via)
via.insertra_vehiculo("11","moto", 5)
via.insertra_vehiculo("10","moto", 3)
via.invertir_via()
print("Inveritir via: ",via)
via.choque("2","4")
print("Choque: ",via)
via.insertra_vehiculo("6","auto", 1)
via.insertra_vehiculo("7","camion", 3)
via.insertra_vehiculo("8","camion",2)
via.insertra_vehiculo("9","auto", 1)
via.eliminar_camiones()
print("Camiones eliminados: ",via)






