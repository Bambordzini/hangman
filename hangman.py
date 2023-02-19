while True:
  print("Witamy w grze 'HangMan' ")
  print()
  start=input("Czy chcesz rozpocząć nową grę? tak/nie: ")
  start= start.lower()
  print("(Wpisz Quit aby zakończyć w dowolnym momencie)")
  if start == "nie":
      print()  
      print("Dziękujemy za grę! ")
      break
     
 
  if start == "tak":    
    import random
    print()
    trafione_litery = []
    nie_trafione_litery = []
    nie_dozwolone = ("1", "2","3","4","5","6","7","8","9","ó","ą","ś","ż","ź","ę","!", "@", "#", "$", "%", "^", "&", "*","(", ")", "_","-","=","+","]","[","{","}",":",";","|", "<","''",">",",",".","?","/","~","`"," ")
    wyjscie = ["quit","Quit","QUIT"]
    with open('slowa.txt') as plik:
      lista_slow = plik.read().splitlines()
    lista=('ala', 'pies')
    mistery = random.choice(lista)
    liczba_prób = liczba_prób=len(mistery)
    for l in mistery:
        print("_",end="")
  else:
      print()
      print("** Wybierz wyłącznie tak lub nie aby rozpocząć grę: **")
      print()
      continue
   
  while True:
      print()
      print()
      litera = input(" [ " + "Podaj literę (bez cyfr i znaków): " + "] ")
      litera = litera.lower()    
      if litera in wyjscie:
        koniec = print("GOOD BYE!")
        quit()
      if len(litera) != 1:
        print()
        print("Wpisuj tylko pojedyńcze litery! ")
        print()
        print("Pozostało prób: ",liczba_prób)
        continue
      if litera in nie_trafione_litery:
        print()
        print("Ta litera została użyta, spróbuj innej: ")
        print()
        print("Pozostało prób: ", liczba_prób)
        continue
      if litera in trafione_litery:
        print()
        print("Ta litera została użyta, spróbuj innej: ")
        print("Pozostało prób: ",liczba_prób)
        continue
   
      if litera in nie_dozwolone:
        print()
        print()
        print("Używaj tylko alfabetu, bez cyfr, znaków specjalnych i polskich liter!")
        print()  
        print("Pozostało prób:", liczba_prób)
        continue
      if litera in mistery:
        print()
        print("Odgadłeś literę!")
        print()
        trafione_litery.append(litera)
        print("Trafione litery: ", trafione_litery, )
        print("Nietrafione litery: ", nie_trafione_litery)
        print("Twoja liczba prób: ", liczba_prób)
     
      else:
        liczba_prób -= 1
        print()
        print("Niestety, pudło!")
        print()
        nie_trafione_litery.append(litera)
        print("Trafione litery: ", trafione_litery)
        print("Nietrafione litery: ", nie_trafione_litery)
        print("Pozostało ci", liczba_prób, "prób")
       
      for l in mistery:
        if l in trafione_litery:
          print(l, end="")
        else:
          print("_", end="")  

      if set(mistery) == set(trafione_litery):
        print()
        print()
        print("Zgadłeś wszystkie litery i wygrałeś grę!")
        print()
        print()
        break
      if liczba_prób == 0:
        print()
        print("Nie udało się! Spróbuj jeszcze raz! ")
        break