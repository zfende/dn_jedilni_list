# -*- encoding: utf-8 -*-
meni = {}

while True:
    jed = str(raw_input("Vnesi jed: "))
    cena_jedi = str(raw_input("Vnesi ceno: "))
    meni[jed] = cena_jedi

    nova_jed = raw_input("Dodam novo jed (da/ne): ").lower()

    if nova_jed == "da":
        continue
    elif nova_jed == "ne":
        break
    else:
        print ("Napacen vnos. Vnesi da/ne.")

print "Menu: " + str(meni)

jedilnik = open("jedilni_list.txt", "w")
for jed in meni:
    jedilnik.write("%s, %s €\n" % (jed, meni[jed]))
jedilnik.close()