def main_ahorcados():
    palabra = ("cocodrilo") 
    guess = ["__"]*len(palabra)
    w = 0
    tries = 5
    while True:
      t =input("Ponga la letra ")
     
      flag = False
      for i,p in enumerate(palabra):
        if p == t:
          flag = True
          guess[i] = p
      if not flag:
        w+=1
      print(guess)
      if w==tries:
        print("ahorcado")
        break
        print("".join(guess))
      if "".join(guess) == palabra or t == palabra:
        print("ganador")
        break

