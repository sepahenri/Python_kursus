print("Mis on su eesnimi?")

eesnimi = input() # Henri

print("Tere, " + eesnimi)

print("\nMis on su perekonnanimi?")

perekonnanimi = input() # Sepp

print("\nSinu täisnimi on: " + eesnimi + " " + perekonnanimi)

vanus = input("Kui vana sa oled?") # 27
bot_vanus = 100
vahe = bot_vanus - int(vanus) # int() loob tekstist numbritüübi - vajalik matemaatilisteks teheteks

print("\nSa oled minust " + str(vahe) + " aastat noorem") # str() loob numbrist tekstitüübi - vajalik tekstide kokku kleepimiseks