import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Define file path (adjust as needed)
file_path = "finger1(pousse).csv"

def prepare_data(file_path):
  data = pd.read_csv(file_path)

  # Perform any necessary data preprocessing or feature engineering here
  # For example, you can handle missing values, scale numerical features, encode categorical features, etc.
  # You can use pandas functions and methods to perform these operations on the data DataFrame
  # Here are some examples:

  # Handle missing values
  data.fillna(0, inplace=True)  # Replace missing values with 0

  # Scale numerical features
  scaler = MinMaxScaler()
  data['flexion'] = scaler.fit_transform(data[['flexion']])

  # Encode categorical features
  data = pd.get_dummies(data, columns=['categorical_feature'])

  # Drop unnecessary columns
  data.drop(['unnecessary_column'], axis=1, inplace=True)

  # Return the prepared data
  return data

# Load and prepare the data 
finger_data = prepare_data(file_path)

# Display the prepared data
print(finger_data.head())


class phrase:
    def __init__(self, nom):
        self.doig_h = nom
    def phrase_pour_doigt(self):
        phrases = {
            'A1': "Phrase pour le premier doigt",
            'A2': "Phrase pour le deuxième doigt",
            'A3': "Phrase pour le troisième doigt",
            'A4': "Phrase pour le quatrième doigt",
            'A5': "Phrase pour le cinquième doigt",
            'A6':"Phrase pour le 6 doigt",
            'A7':"Phrase pour le 7 doigt",
            'A8':"Phrase pour le 8 doigt"
        }
        return phrases.get(self.doig_h, "Doigt non reconnu") #ya3ml kach haja 
    
class Class_1:
    def __init__(self, nom):
        self.doig = nom
    def phrase(self):
      if self.doig =='A5':
           return  #print("erreur") # Tupe 1 n'etulise pas le pouce
      else:       
        a=phrase(self.doig)
        a.phrase_pour_doigt()

class Class_2:
    def __init__(self, nom):
        self.doig = nom
    def phrase(self):       
        a=phrase(self.doig)
        a.phrase_pour_doigt()   

class Class_3:
    def __init__(self, nom,nom2):
        self.doig = nom
        self.doig2 = nom2
    def phrase(self): 
        # print(type(self.doig) )
        if ((self.doig=='A1')&(self.doig2=='A2')): # on peut donne just 1 seul parametre pour la classe  phrase 
          self.doig='A6'
        elif ((self.doig=='A2')&(self.doig2=='A3')):
          self.doig='A7' 
        elif ((self.doig=='A3')&(self.doig2=='A4')):
          self.doig='A8'            
        a=phrase(self.doig)
        a.phrase_pour_doigt() 
         
class general(): #
  def __init__(self,type_nom, valeur_arduino, doigt_utilise,doigt_nmbr):
      self.type=type_nom
      self.val=valeur_arduino
      self.doigt=doigt_utilise
      self.nbr=doigt_nmbr
  def verifier_valeur(self):
     type_classes = ['Tipe 1','Tipe 2']  # Liste de toutes les classes de maladies
     type_trouvee = None
     for type in type_classes:
        print(type)
        if type == self.type: #print('ll')
            type_trouvee = type
            break
     if type_trouvee:
        a = 1     # a et b max et min d'interval
        b = 5
        x=self.nbr
        if a <= self.val <= b:  #en peut le suprime  
          print(x)
          if x==1: 
            # print("kk")
            if self.type=="Tipe 1":
              # print("pp")
              a=Class_1(self.doigt)
              a.phrase()
            elif self.type=='Tipe 2':
               # print("gg")  
               a=Class_2(self.doigt)
               a.phrase() 
            # else :print('le type n'est pas trouve')   
          elif  x==2:
              doigt_utilise2 = input("Entrez le 2eme doigt utilisé (A1, A2, A3, A4, A5) : ")
              a=Class_3(self.doigt,doigt_utilise2)
              a.phrase()   
          #else :print('mouvment doighs n'est pas connue des  ')
        else:
             print("La valeur ne correspond pas aux critères spécifiés.")
     else:
         print("type  non trouvée.")


#type_utilisee=Serial.read
type_utilisee = input("Entrez le type : ") #soit Tupe 1 ou Tupe 2 ou Class 3
# maladie_utilisee = (f1.maladie)

valeur_arduino = float(input("Entrez la valeur du capteur Arduino : ")) #val de flex senseur antre[1,5] exemple
doigt_nmbr =int(input("Entrez le nmbre doigt : ")) # soit 1 , 2 , 3 , 4 , 5
doigt_utilise = input("Entrez le doigt utilisé (A1, A2, A3, A4, A5) : ") # ontre le premier doigh
#if doigt_nmbr==1:
resultat_verification = general(type_utilisee, valeur_arduino,doigt_utilise,doigt_nmbr) 
print(resultat_verification.verifier_valeur())
#elif doigt_nmbr==2:
   #resultat_verification2 = verifier_valeur(type_utilisee, valeur_arduino, doigt_utilisem,doigt_utilisem2,doigt_nmbr)    print(resultat_verification)

