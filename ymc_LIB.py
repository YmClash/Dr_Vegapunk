import requests
import socket
import torch


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