# simulador_de_transito
practica 3 listas enlazadas
Simulador de tránsito urbano
Restricciones Técnicas
Únicamente se pueden utilizar las clases de listas enlazadas que fueron construidas
en clase. El uso de otra clase base afectará la nota en –2 unidades.
No se permite documentación sobre el código, de ningún tipo.
Únicamente se permite como colección de datos listas doblemente enlazadas,
presentar la práctica sobre otra colección no cumple con lo solicitado por lo
que la nota será de 0. Tampoco está permitido el uso de listas, diccionarios,
tuplas etc como colecciones asi sean auxiliares o temporales.
La práctica debe cumplir con la totalidad de los puntos solicitados, cada punto que
no se presente, disminuirá la nota en 1 por punto no presentado.
El entregable de la práctica debe estar de modo tal que con la ejecución del código
se ejecute de forma autónoma cada uno de los puntos, no cumplir con este punto
afectará la nota en –2 unidades.
Descripción:
Una ciudad tiene una vía principal representada como una lista doblemente enlazada
de vehículos. Cada nodo contiene:
• placa: str
• tipo: str (auto, moto, camion)
• prioridad: int (a menor número, más prioridad), de 1 hasta 5.
Requerimientos:
1. Insertar vehículos al final de la vía.
2. Dar paso preferencial: mover al frente todos los vehículos de tipo moto con
prioridad 1.(revisar)
3. Eliminar todos los camiones con prioridad mayor a 3 (por inspección
técnica).
4. Simular un accidente entre dos placas dadas: deben eliminarse todos los
vehículos entre ellas.
5. Invertir el orden de la vía solo si hay más autos que motos.
6. Reorganizar la vía según prioridad, sin estructuras auxiliares, deben quedar
al inicio todos los vehículos con prioridad 1, luego prioridad 2, y así hasta la
prioridad 5.
Entrega y sustentación:
• La fecha de entrega y sustentación es el 16 de octubre durante
clase (grupo martes y jueves) ó 17 de octubre durante clase
(grupo miércoles y viernes).
TODOS SIN EXCEPCIÓN DEBEN ASISTIR ESTE DIA, SI NO LA NOTA DE LA
SUSTENTACIÓN SERÁ 0 (DE 4 PUNTOS POSIBLES)
La práctica debe ser enviada a más tardar el 15/16 de octubre (dependiendo del
grupo), es decir el día anterior.
Se pueden hacer solos o en parejas, teniendo en cuenta La sustentación será
práctica y oral, y se hará de forma individual.
Detalle de las notas:
 La implementación valdrá un 20%
 La sustentación práctica un 40%. --> se realizará de 6 am a 6:40 am en la
fecha de entrega.
 La sustentación oral un 40%. --> de 6:40 am en adelante, ese día se indicará
el orden de sustentación.
Tener en cuenta las restricciones de la práctica que pueden afectar la nota