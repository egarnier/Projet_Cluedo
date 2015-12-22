################################################################################
#					                    									   #
# 				                CODE DU JEU - CLUEDO	        	 		   #
#					                    									   #
################################################################################

# IMPORT DES PACKAGES
import random
import numpy as np

#-------------------------- ECRITURE DES DONNEES DU JEU -----------------------#
# Pour les donnees je ne savais pas trop ce dont on aurait besoin donc 
# pour l instant je les ai ecrites sous differentes formes, on pourra les 
# supprimer au besoin. je les ai faites faciles a modifier mais du coup c est un
# peu lourd...

## Et j ai tout ecris en anglais parce que les accents c est chiant


# Definition des personnages si on veut les changer plus tard sans tout reecrire
Perso1 = "Sandra"
Perso2 = "Ed"
Perso3 = "a 4BIM student"
Perso4 = "Fabrice"
Persos = [Perso1, Perso2, Perso3, Perso4]

# Definition des lieus
Lieu1 = "lab"
Lieu2 = "library"
Lieu3 = "cellar"
Lieu4 = "stairs"
Lieux = [Lieu1, Lieu2, Lieu3, Lieu4]

# Definition des armes
Arme1 = "killed by a syringe with poison"
Arme2 = "poisoned by remains of cockroaches"
Arme3 = "strangled by a mouse over"
Arme4 = "struck by a statistics book"
Armes = [Arme1, Arme2, Arme3, Arme4]

# 4 jeu de donnees (pas besoin de les modifier)
jeu1 = [Perso1, Lieu1, Arme1]
jeu2 = [Perso2, Lieu2, Arme2]
jeu3 = [Perso3, Lieu3, Arme3]
jeu4 = [Perso4, Lieu4, Arme4]

# Liste des questions a poser aux perso (pas besoin de les modifier)
Question1 = "What were you doing at the time of the murder?"
Question2 = "What were your relationship the victim ?"
Question3 = "What is your opinion about the statistics ?"

# Liste des questions personnalisees par perso (preimer chiffre = question4; 
# deuxieme chiffre = personnage interroge)
Question41 = "How did you handle your husband's popularity ?"
Question42 = "Did you have some disagreements ?"
Question43 = "Do you like insects ?"
Question44 = "How far would you be willing to go for the love of statistics?"

# Liste des questions finales par personnage
Question_1 = [Question1, Question2, Question3, Question41]
Question_2 = [Question1, Question2, Question3, Question42]
Question_3 = [Question1, Question2, Question3, Question43] 
Question_4 = [Question1, Question2, Question3, Question44] 

# Liste des reponses personnage 1 NG 
Reponse_NG11 = "I was participating in the end-of-year jury."
Reponse_NG12 = "He was my beloved husband !"
Reponse_NG13 = "I prefer by far the differential equations !"
Reponse_NG14 = "He should have been the one worrying about that." 

# Liste des reponses personnage 1 G 
Reponse_G11 = "I was in my office in the university writing an email to the 3BIM students !"
Reponse_G12 = "He was my beloved husband !"
Reponse_G13 = "I prefer by far the differential equations !"
Reponse_G14 = "I wish I could have kept an eye on him more often." 

# Liste des reponses personnage 2 NG 
Reponse_NG21 = "I was at the premiere of Star Wars with my son."
Reponse_NG22 = "Strictly professional."
Reponse_NG23 = "I don't really care..."
Reponse_NG24 = "No." 

# Liste des reponses personnage 2 G 
Reponse_G21 = "I was participating in the end-of-year jury."
Reponse_G22 = "Strictly professional."
Reponse_G23 = "I don't really care but I think that Fabrice is a better teacher."
Reponse_G24 = "No except when it comes to the department's leadership." 

# Liste des reponses personnage 3 NG 
Reponse_NG31 = "I was working on my network project."
Reponse_NG32 = "He was a dedicated teacher in BIM."
Reponse_NG33 = "I like it but I would rather work on my other projects."
Reponse_NG34 = "I crush cockroaches ..." 

# Liste des reponses personnage 3 G 
Reponse_G31 = "I was drinking a beer in the kfet."
Reponse_G32 = "He was my favourite teacher !"
Reponse_G33 = "I loved his classes whatever subject it was on..."
Reponse_G34 = "I prefer mouses -or cats- ..." 

# Liste des reponses personnage 4 NG 
Reponse_NG41 = "I was giving a private lesson to a 3BIM student."
Reponse_NG42 = "We were both statistics teachers."
Reponse_NG43 = "It's my life !"
Reponse_NG44 = "Giving private lesson until late at night to help students." 

# Liste des reponses personnage 4 G 
Reponse_G41 = "I saw him right after my 3BIM lesson."
Reponse_G42 = "I replace him when he can not provide a statistics course."
Reponse_G43 = "I love statistics more than anything !"
Reponse_G44 = "Everything." 



#-------------------- INITIALISATION DES JEUX DE DONNEES ----------------------#
alea = random.randint(1,4)
if alea == 1:
    Meurtrier = np.copy(jeu1).tolist()
    Reponse1 = [Reponse_G11, Reponse_G12, Reponse_G13, Reponse_G14]
    Reponse2 = [Reponse_NG21, Reponse_NG22, Reponse_NG23, Reponse_NG24]
    Reponse3 = [Reponse_NG31, Reponse_NG32, Reponse_NG33, Reponse_NG34]
    Reponse4 = [Reponse_NG41, Reponse_NG42, Reponse_NG43, Reponse_NG44]
elif alea == 2:
    Meurtrier = np.copy(jeu2).tolist()
    Reponse1 = [Reponse_NG11, Reponse_NG12, Reponse_NG13, Reponse_NG14]
    Reponse2 = [Reponse_G21, Reponse_G22, Reponse_G23, Reponse_G24]
    Reponse3 = [Reponse_NG31, Reponse_NG32, Reponse_NG33, Reponse_NG34]
    Reponse4 = [Reponse_NG41, Reponse_NG42, Reponse_NG43, Reponse_NG44]
elif alea == 3:
    Meurtrier = np.copy(jeu3).tolist()
    Reponse1 = [Reponse_NG11, Reponse_NG12, Reponse_NG13, Reponse_NG14]
    Reponse2 = [Reponse_NG21, Reponse_NG22, Reponse_NG23, Reponse_NG24]
    Reponse3 = [Reponse_G31, Reponse_G32, Reponse_G33, Reponse_G34]
    Reponse4 = [Reponse_NG41, Reponse_NG42, Reponse_NG43, Reponse_NG44]
elif alea == 4:
    Meurtrier = np.copy(jeu4).tolist()
    Reponse1 = [Reponse_NG11, Reponse_NG12, Reponse_NG13, Reponse_NG14]
    Reponse2 = [Reponse_NG21, Reponse_NG22, Reponse_NG23, Reponse_NG24]
    Reponse3 = [Reponse_NG31, Reponse_NG32, Reponse_NG33, Reponse_NG34]
    Reponse4 = [Reponse_G41, Reponse_G42, Reponse_G43, Reponse_G44]
    


#------------------------ DEFINITION DES FONCTIONS ----------------------------#

def PhraseFinale(coupable, lieu, arme):
    return "I think Charles was %s in the %s by %s."%(arme, lieu, coupable)





#----------------------------------- MAIN -------------------------------------#
print alea
print Meurtrier
print PhraseFinale(Meurtrier[0], Meurtrier[1], Meurtrier[2])
