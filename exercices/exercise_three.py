'''
Ejercicio 3:
Escriba un programa donde cree una lista con los siguientes personajes del Señor de los anillos.
Nombre: Aragon  
Clase: Guerrero
Raza: Dúnadan del Norte

Nombre: Gandalf
Clase: Mago
Raza: Istar

Nombre: Legolas
Clase: Arquero
Raza: Elfo Sindar
'''

personages = {
        "Nombre":"Aragon", "Clase":"Guerrero", "Raza":"Dúnadan del Norte"
    }, {
        "Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"
    }, {
        "Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo Sindar"
    }
personages = list(personages)
print(personages)