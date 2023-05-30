import requests
import socket
import torch
import random


#affiche l'adresse IP
def ip_adresse():
    hostname = socket.gethostname()
    ip_adresse = socket.gethostbyname(hostname)
    print(f'votre ip adresse es {ip_adresse}')


#liste tou les  methode d'un pacquet
def method_list(*args):
    for method in dir(*args):
        if '__' not in method:
            print(method)



def compare_list(list:list,list2:list):
    resultat = set(list) & set(list2)
    if len(resultat) > 0:
        print(f'IL ya {len(resultat)} element en commun: {resultat}')
    if len(resultat) == 0:
        print("pas d'element en commun ")



# generateur de Nom et prenom
def generateur_nom(nombre:int):

    noms_fictif = []
    liste_noms = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller",
                  "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White",
                  "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson","Toure"]

    liste_prenoms = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia",
                     "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth",
                     "Mila", "Ella", "Avery", "Sofia", "Camila","Mohamed Ali"]


    for _ in range(nombre):
        nom = random.choice(liste_noms)
        prenom = ''.join(random.choices(liste_prenoms))
        noms_fictif.append(f"{prenom} {nom}")

    print(noms_fictif)





#fonction pour connaitre  la taille  de  la  sortie  OUTSIZE dans un reseau de neurone
def output_size(input,kernel_size):
    input_size = input
    stride = 1
    padding = 0
    get_output_size = (input_size - kernel_size + 2 * padding ) // stride +1
    output_size = get_output_size
    output_size = get_output_size
    output_size = get_output_size
    output_size = get_output_size
    print(f'Output size afer conv Layers: {output_size}')


output_size(28,3)







# resultat = set(Afro_quote_1) & set(Afro_quote_2)
#
#
# if len(resultat) > 0:
#     print(f'il ya {len(resultat)}, element commun : {resultat}')
# else:
#     print("il n'ya pas d'element commun ")