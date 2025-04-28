import tkinter as tk

from bibliotheque import Bibliotheque
from bibliotheque_app import BibliothequeApp

# Le module suivant n'existe pas encore, on vous demande de le créer, incluant les
# trois fonctions «charger_...» accompagnées de leur documentation.
#
# IMPORTANT : Il est normal que l'ajout d'un nouvel utilisateur via l'interface graphique ne modifie pas
# le fichier utilisateurs.txt. Vous n'avez pas à gérer la sauvegarde automatique des nouvelles données
# dans les fichiers texte.
from gestion_fichiers import charger_livres, charger_revues, charger_utilisateurs


def creer_donnees_bibliotheque():
    """Crée un objet Bibliotheque contenant des données de test.

    Cette fonction instancie un objet de la classe Bibliotheque avec le nom "Bibliothèque Municipale".
    Elle crée ensuite :
      - Trois objets Livre, dont les informations doivent être lues à partir d'un fichier texte "livres.txt" qui
       vous est fourni.

      - Au moins deux objets Revue, dont les informations doivent être lues à partir d'un fichier texte "revues.txt" que
      vous devez créer (à vous de choisir le format précis du fichier).

      - Au moins trois objets Utilisateurs, dont les informations doivent être lues à partir d'un fichier texte
      "utilisateurs.txt" que vous devez créer (à vous de choisir le format précis du fichier).

    IMPORTANT: Vous devez obligatoirement utiliser des opérations classiques de lecture sur fichiers texte dans les
        trois fonctions «charger_...». L'utilisation de modules tels que csv, json, pickle ou équivalents n'est
        pas permise.

    Returns:
        Bibliotheque: L'objet bibliothèque contenant les données de test.
    """
    bibliotheque = Bibliotheque("Bibliothèque Municipale")

    # Ajout des livres
    livres = charger_livres("donnees/livres.txt")
    for element in livres:
        bibliotheque.ajouter_document(element)

    # Ajout des revues
    revues = charger_revues("donnees/revues.txt")
    for element in revues:
        bibliotheque.ajouter_document(element)

    # Ajout des utilisateurs
    utilisateurs = charger_utilisateurs("donnees/utilisateurs.txt")
    for element in utilisateurs:
        bibliotheque.ajouter_utilisateur(element)

    return bibliotheque


def main():
    """Point d'entrée du programme."""
    # Création de la bibliothèque avec des données de test
    biblio = creer_donnees_bibliotheque()

    # Création de l'interface graphique
    app = BibliothequeApp(biblio)

    app.mainloop()


if __name__ == "__main__":
    main()
