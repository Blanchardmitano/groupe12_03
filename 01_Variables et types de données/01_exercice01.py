#Demande d'information a l'informateur
prenom = input(" Entrez votre prenom :")
age = int(input("Entrez votre age :"))
ville = input(" Entrez votre ville : ")
metier = input(" Entrez votre metier : ")

#Approximation desjours vecus
jours_vecus = age * 365

# Affichage formaté

print("\n=== PROFIL UTILISATEUR ===")
print(f"prenom : {prenom}")
print(f"Age :{age} ans ({jours_vecus} jours vecus environ)")
print(f"ville : {ville}")
print(f"Metier : {metier}")