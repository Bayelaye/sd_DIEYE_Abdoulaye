# Importation de modules
import csv
import json

import dicttoxml
import xmltodict
import yaml


# ----------------------------------------------------------------------------------------------------------------------

# Cette fonction verifie si un fichier est dans un format valide (csv, json, yaml, xml)
def valide_file(path_file):
    if path_file.split("/")[-1].endswith((".csv", ".json", ".yaml", ".xml")):
        return True
    else:
        return False


# ----------------------------------------------------------------------------------------------------------------------

# Fonction qui convertit un fichier de format valide en dictionnaire
def valide_to_dico(file_path):
    chemin = file_path.split("/")[-1]
    if chemin.endswith(".csv"):
        with open(file_path, mode='r') as inp:
            reader = csv.reader(inp)
            liste_dico = [line for line in reader]
            csv_dict = {liste_dico[0][i]: [liste_dico[j][i] for j in range(1, len(liste_dico))] for i in
                        range(len(liste_dico[0]))}
            return csv_dict
    elif chemin.endswith(".json"):
        # Ouverture du fichier Json avec la fonction open()
        with open(file_path, mode='r') as f:
            # Convertion des données JSON en objet Python
            json_dict = json.load(f)
            return json_dict
    elif chemin.endswith(".yaml"):
        # Ouverture du fichier yaml avec la fonction open
        with open(file_path, mode='r') as f:
            # Convertion des données yaml en objet Python
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)
            return yaml_dict
    elif chemin.endswith(".xml"):
        # Ouverture du fichier xml avec la fonction open
        with open(file_path, 'r', encoding='utf-8') as f:
            my_xml = f.read()

            # Use xmltodict to parse and convert
            # the XML document
            xml_dict = xmltodict.parse(my_xml, dict_constructor=dict)

            # Print the dictionary
            return xml_dict


# ----------------------------------------------------------------------------------------------------------------------
# Cette Fonction convertit un dictionnaire en format valide

def dico_to_valide(dico, file_format):
    if file_format.lower() == "csv":
        with open("new_file.csv", 'w') as f:
            writer = csv.writer(f)
            key_list = list(dico.keys())
            limit = len(dico[key_list[0]])
            writer.writerow(dico.keys())
            for i in range(limit):
                writer.writerow(dico[x][i] for x in key_list)
    elif file_format.lower() == "json":
        with open("new_file.json", 'w') as f:
            json.dump(dico, f)
    elif file_format.lower() == "yaml":
        with open("new_file.json", 'w') as f:
            yaml.dump(dico, f)
    elif file_format.lower() == "xml":
        #  Variable name of Dictionary is data
        my_xml = dicttoxml(dico)
        # Obtain decode string by decode()
        # function
        xml_decode = my_xml.decode()

        xmlfile = open("new_file.xml", "w")
        xmlfile.write(xml_decode)
        xmlfile.close()

# ----------------------------------------------------------------------------------------------------------------------
