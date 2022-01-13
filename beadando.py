#counter-strike: source buy menu
#Eredeti játékban is a 0-val kilép a menüből


# b mint buy menu

b = input()
money = 8000
inventory = {
    "pistol": "Km .45 Tactical",
    "rifel": "none",
    "knife": "Default Knife"
}


fomenu = ''.join(("1. Pisztolyok\n",
                "2. Sörétesek\n",
                "3. Géppisztolyok\n",
                "4. Puskák\n",
                "5. Géppuskák\n",
                "0. Mégse"))  

menu1 = ''.join(( "1. 9x19MM-es Oldalfegyver\n",
                "2. KM .45 Tactical\n",
                "3. 228 compact\n",
                "4. Night Hawk .50C\n",
                "5. ES Five-Seven\n",
                "0. Mégse"))

menu2 = ''.join(("1. Leone 12 Gauge super\n",
                "2. Leone YG1265 Automata sörétes\n",
                "0. Mégse"))

menu3 = ''.join(("1. Schmidt Automata Pisztoly\n",
                "2. KM Géppisztoly\n",
                "3. KM UMP45\n"
                "4. ES C90\n",
                "0. Mégse"))

menu4 = ''.join(("1. Clarion 5.56\n",
                "2. Schmidt Scout\n",
                "3. Maverick M4A1 Karabély\n",
                "4. Bullpup\n",
                "5. Krieg 550 Commando\n",
                "6. Magnum Mesterlövész\n",
                "0. Mégse"))

menu5 = ''.join(("1. M249\n",
                "0. Mégse"))


if b == "b":
    print(fomenu,"\n", money,"$")
    a = input('Válassz: ')


while a != 0:
    if a=='1':
        while True:
            print(menu1,"\n",money,"$")
            pistol = input()
            oldalfegyver = 400
            km45 = 500    
            compact = 600
            hawk = 650
            fiveseven = 750

            if pistol == "1":
                if money >= oldalfegyver:
                    money = money-oldalfegyver
                    inventory["pistol"] = "9x19MM-es Oldalfegyver"
                else:
                    print("nincs elég pénzed!\n")
            elif pistol == "2":
                if money >= km45:
                    money = money-km45
                    inventory["pistol"] = "KM .45 Tactical"
                else:
                    print("nincs elég pénzed!\n")
            elif pistol == "3":
                if money >= compact:
                    money = money-compact
                    inventory["pistol"] = "228 compact"
                else:
                    print("nincs elég pénzed!\n")
            elif pistol == "4":
                if money >= hawk:
                    money = money-hawk
                    inventory["pistol"] = "Night Hawk .50C"
                else:
                    print("nincs elég pénzed!\n")
            elif pistol == "5":
                if money >= fiveseven:
                    money = money-fiveseven
                    inventory["pistol"] = "ES Five-Seven"
                else:
                    print("nincs elég pénzed!\n")
            if pistol == "0":
                exit()

    if a == "2":
        while True:
            print(menu2,"\n",money,"$")
            shotgun = input()
            leone12 = 1700
            leoneyg = 3000
            
            if shotgun == "1":
                if money >= leone12:
                    money = money-leone12
                    inventory["rifel"] = "Leone 12 Gauge Super"
                else:
                    print("nincs elég pénzed!\n")
            if shotgun == "2":
                if money >= leoneyg:
                    money = money-leoneyg
                    inventory["rifel"] = "Leone YG1265 Automata Sörétes"
                else:
                    print("nincs elég pénzed!\n")
            if shotgun == "0":
                exit()

    if a == "3":
        while True:
            print(menu3,"\n",money,"$")
            smg = input()
            schmidt = 1250
            Kmgép = 1500
            KmUmp = 1700
            ESc90 = 2350
            
            if smg == "1":
                if money >= schmidt:
                    money = money-schmidt
                    inventory["rifel"] = "Schmidt Automata Pisztoly"
                else:
                    print("nincs elég pénzed!\n")
            if smg == "2":
                if money >= Kmgép:
                    money = money-Kmgép
                    inventory["rifel"] = "KM Géppisztoly"
                else:
                    print("nincs elég pénzed!\n")
            if smg == "3":
                if money >= KmUmp:
                    money = money-KmUmp
                    inventory["rifel"] = "KM UMP45"
                else:
                    print("nincs elég pénzed!\n")
            if smg == "4":
                if money >= ESc90:
                    money = money-ESc90
                    inventory["rifel"] = "ES C90"
                else:
                    print("nincs elég pénzed!\n")
            if smg =="0":
                exit()

    if a == "4":
        while True:
            print(menu4,"\n",money,"$")
            rifels = input()
            clarion = 2250
            scout = 2750
            m4a1 = 3100
            bullpup = 3500
            krieg = 4200
            magnum = 4750

            if rifels == "1":
                if money>=clarion:
                    money = money-clarion
                    inventory["rifel"] = "Clarion 5.56"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "2":
                if money>=scout:
                    money = money-scout
                    inventory["rifel"] = "Schmidt Scout"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "3":
                if money>=m4a1:
                    money = money-m4a1
                    inventory["rifel"] = "Maverick M4A1 Karabély"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "4":
                if money>=bullpup:
                    money = money-bullpup
                    inventory["rifel"] = "Bullpup"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "5":
                if money>=krieg:
                    money = money-krieg
                    inventory["rifel"] = "Kreig 550 Commando"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "6":
                if money>=magnum:
                    money = money-magnum
                    inventory["rifel"] = "Magnum Mesterlövész"
                else:
                    print("nincs elég pénzed!\n")
            if rifels == "0":
                exit()
    
    if a == "5":
        while True:
            print(menu5,"\n",money,"$")
            m249 = 5750
            machinegun = input()

            if machinegun == "1":
                if money>=m249:
                    money = money-m249
                    inventory["rifel"] = "M249"
                else:
                    print("nincs elég pénzed!")
            if machinegun == "0":
                exit()