import library.divicion
import library.estrella
import library.fizzbuz
import library.inicio
import library.multiplicacion
import library.paroimpar
import library.resta
import library.suma
import library.triqui
import library.ahorcados

print("""
=================================
🅱🅸🅴🆅🅴🅽🅸🅳🅾 🅰🅻 🅹🆄🅴🅶🅾!!
=================================
""")
opcion = 1
while opcion!="0":
    
    print("""seleccione un juego
          0 = salir
          1 = ahorcados
          2 = divicion
          3 = estrella
          4 = fizz buz
          5 = inicia seion 
          6 = multiplicacion
          7 = par o impar?
          8 = resta
          9 = suma 
          10 = triqui en tres dimecioneciones""")
    opcion = input()
    if opcion == "1":
        library.ahorcados.main_ahorcados()
    if opcion == "2":
        library.divicion.main_divicion()
    if opcion == "3":        
        library.estrella.main_estrella()
    if opcion == "4":
         library.fizzbuz.main_fizzbuz()
    if opcion == "5":
         library.inicio.main_inicio()
    if opcion == "6":
         library.multiplicacion.main_multiplicacion()
    if opcion == "7":
         library.paroimpar.main_paroimpar()
    if opcion == "8":
         library.resta.main_resta()
    if opcion == "9":
         library.suma.main_suma()
    if opcion == "10":
         library.triqui.main_triqui()