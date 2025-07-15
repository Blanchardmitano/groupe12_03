# Demander Les informations
age= int(input( "Entrez votre âge : "))
pays= input ("Entrez votre pays: ") .lower()
if age>= 18 and (pays == "conga" or pays == "Cameroun"):
    print("Inscription autorisée." )
elif age< 18:
    print("vous êtes trop jeune pour vous inscrire." )
else :
    print( "Désolé, programme réservé aux ressortissants du Congo ou Cameroun." )