 #funkcja input(), str(), int()

print('Hi, \nwhat is your nickname?') #Pyta o imie.
name = input()


name = name.title()
if name: #pusty string ma wartość falsey.
    print('Nice to meet you, ', name)
else:
    print('Noname is no name :(')



while True:
    print(name + ', how old are you?') #pyta o wiek
    Wiek = input() #podajesz wiek

    try: 
        int(wiek)
        if int(wiek) <= 99 and int(wiek) > 0: #sprawdza czy jest to liczba od 0 do 99 i przerywa pętle
            break
        else:
            print('Are you sure?') #podaje komunikat jeśli jest poza przedziałem
    except ValueError:    
        print('it is not a number.') 


print('You born in ' + str(2020 - int(wiek))) #podaje datę urodzenia

#Radziu pamietaj o prawidlowym nazywaniu zmiennych malymi_literami_z_daszami

