from math import ceil


def tri_insertion(tableau):
    """
    Tri d'un tableau avec le tri par insertion.
    :param tableau: Tableau a trier.
    :return: Le tableau donné en entrée, mais trié
    """



def tri_fusion(tableau):
    """
    Tri d'un tableau avec le tri par fusion.
    :param tableau: Tableau a trier.
    :return: Le tableau donné en entrée, mais trié
    """
    if len(tableau) <= 1:
        return tableau
    elif len(tableau) == 2:
        if tableau[0] > tableau[1]:
            return [tableau[1], tableau[0]]
        return tableau
    elif len(tableau) > 2:
        indice_milieu = ceil(len(tableau) / 2) if len(tableau) % 2 > 0 else len(tableau) / 2
        tableau_gauche = tri_fusion(tableau[indice_milieu:])
        tableau_droite = tri_fusion(tableau[:indice_milieu])
        return fusion(tableau_gauche, tableau_droite)


def fusion(tableau_gauche, tableau_droite):
    """
    Fusion des 2 tableau pour former un gros tableau trié.
    :param tableau_gauche: Tableau a fusionner.
    :param tableau_droite: Tableau a fusionner.
    :return: Un nouveau tableau trié en ordre croissant.
    """
    tableau_triee = []
    indice_tableau = 0
    for element_gauche in tableau_gauche:
        for element_droite in tableau_droite:
            if element_droite < element_gauche:
                tableau_triee[indice_tableau] = element_droite
                indice_tableau += 1
            else:
                break
        tableau_triee[indice_tableau] = element_gauche
        indice_tableau += 1
    return tableau_triee
