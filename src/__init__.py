import os
from decimal import Decimal

actual_folder = os.path.dirname(__file__)
graph_folder = os.path.join(actual_folder, r"Graphes")

def update_infos():
    graph_paths = os.listdir(graph_folder)
    return graph_paths, len(graph_paths)


def choix_graphe():
    graph_paths, total_graph = update_infos()

    if total_graph == 0:
        print('Aucun graphe trouvé dans le dossier')
        return None

    valid_response = False
    while not valid_response:
        print("Choisissez un graphe :")
        for i in range(len(graph_paths)):
            print(f"\t{i+1}) {graph_paths[i]}")
        try:
            choice = int(input('> '))
            if not 1 <= choice <= total_graph:
                raise IndexError(f'Veuillez entrer un entier entre 1 et {total_graph} (bornes comprises)\n')
            valid_response = True
        except IndexError as e:
            print(e)
        except Exception as e:
            print(f"Veuillez entrer un nombre entier\n")
    return os.path.join(graph_folder, graph_paths[choice-1])


def lecture_graphe(path):
    f = open(path)

# Parse du nombre de sommets
    try:
        nb_sommets = Decimal(f.readline())
        if nb_sommets.as_integer_ratio()[1] != 1:
            raise Exception
        nb_sommets = int(nb_sommets)
        if nb_sommets <= 0:
            raise Exception
    except:
        print('SyntaxError:', 'Erreur à la ligne 1, le nombre de sommets doit être un nombre entier positif non nul')
        f.close()
        return None

# Parse du nombre d'arcs
    try:
        nb_arcs = Decimal(f.readline())
        if nb_arcs.as_integer_ratio()[1] != 1:
            raise Exception
        nb_arcs = int(nb_arcs)
        if nb_arcs < 0:
            raise Exception
    except:
        print('SyntaxError:', 'Erreur à la ligne 2, le nombre de d\'arcs doit être un nombre entier')
        f.close()
        return None

    arcs = []
    i = 2

# Déclaration des arcs
    for line in f.readlines():
        i += 1

        line = line.strip().split(' ')

# Nombre d'arguments dans la lignes
        if len(line) != 3:
            print('SyntaxError:', f'Erreur à la ligne {i}, l\'arc ne contient pas le bon nombre de valeurs')
            f.close()
            return None

# Parse de l'argument 1
        try:
            line[0] = Decimal(line[0])
            if line[0].as_integer_ratio()[1] != 1:
                raise Exception
            line[0] = int(line[0])
            if not 0 <= line[0] < nb_sommets:
                raise Exception
        except:
            print('SyntaxError:', f'Erreur à la ligne {i}, le sommet de départ n\'existe pas')
            f.close()
            return None

# Parse de l'argument 2
        try:
            line[1] = Decimal(line[1])
            if line[1].as_integer_ratio()[1] != 1:
                raise Exception
            line[1] = int(line[1])
            if not 0 <= line[1] < nb_sommets:
                raise Exception
        except:
            print('SyntaxError:', f'Erreur à la ligne {i}, le sommet d\'arrivée n\'existe pas')
            f.close()
            return None

# Parse de l'argument 3
        try:
            line[2] = Decimal(line[2])
        except:
            print('SyntaxError:', f'Erreur à la ligne {i}, la pondération de l\'arc doit être un nombre')
            f.close()
            return None

# Ajout de l'arc à la liste
        arcs.append(line)

# Vérification du nombre d'arcs
    difference_arcs = len(arcs) - nb_arcs
    if (difference_arcs != 0):
        accord_pluriel = "s" if abs(difference_arcs) > 1 else ""
        print('SyntaxError:', f'{abs(difference_arcs)} arc{accord_pluriel} {"manquant" if difference_arcs < 0 else "supplémentaire"}{accord_pluriel} dans la déclaration du graphe')
        f.close()
        return None

    f.close()
    return nb_sommets, nb_arcs, arcs


graphe = choix_graphe()
if graphe is not None:
    graphe = lecture_graphe(graphe)
    if graphe is not None:
        print(graphe)
