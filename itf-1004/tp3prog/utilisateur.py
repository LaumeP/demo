class Utilisateur:
    """Classe représentant un utilisateur de la bibliothèque.

    Attributes:
        nom (str): Nom de famille de l'utilisateur
        prenom (str): Prénom de l'utilisateur
        id_utilisateur (str): Identifiant unique de l'utilisateur
        documents_empruntes (list): Liste des documents empruntés par l'utilisateur (liste vide par défaut)
    """

    def __init__(self, nom, prenom, id_utilisateur):
        """Initialise un nouvel utilisateur.

        Args:
            nom (str): Nom de famille
            prenom (str): Prénom
            id_utilisateur (str): Identifiant unique
        """
        self.nom = nom
        self.prenom = prenom
        self.id_utilisateur = id_utilisateur
        self.documents_empruntes = []

    def emprunter_document(self, document):
        """Permet à l'utilisateur d'emprunter un document.

        Args:
            document (Document): Le document à emprunter

        Returns:
            bool: True si l'emprunt a réussi, False sinon
        """
        if document.emprunter():
            self.documents_empruntes.append(document)
            return True
        return False
        # Vérifier si le document est disponible, l'emprunter et
        # l'ajouter à la liste des documents empruntés par l'utilisateur

    def retourner_document(self, document):
        """Permet à l'utilisateur de retourner un document.
        Args:
            document (Document): Le document à retourner
        Returns:
            bool: True si le retour a réussi, False sinon
        """
        if document in self.documents_empruntes:
            if document.retourner():
                self.documents_empruntes.remove(document)
                return True
        return False
        # Vérifier si le document fait partie des documents empruntés par l'utilisateur,
        # le retourner et le retirer de la liste des documents empruntés par l'utilisateur

    def __str__(self):
        """Retourne une représentation textuelle de l'utilisateur.

        Returns:
            str: Description de l'utilisateur
        """
        return f"{self.prenom} {self.nom} (ID: {self.id_utilisateur})"


# Exécution des tests
if __name__ == "__main__":
    print("Début des tests pour la classe Utilisateur")
    # TODO: Ajouter des tests pour toutes les méthodes de la classe Utilisateur.
    #
    # - Inspirez-vous de la structure des tests déjà présents dans les modules document, livre et revue.
    # - Créez des objets Utilisateur et Document (fictifs ou réels, selon vos besoins de test).
    # - Testez l'emprunt d'un document disponible :
    #     - Vérifiez que la méthode retourne True
    #     - Vérifiez que le document est ajouté à la liste des documents empruntés
    #     - Vérifiez que le document n'est plus disponible
    # - Testez le cas où un utilisateur essaie d'emprunter un document non disponible :
    #     - Vérifiez que la méthode retourne False
    # - Testez le retour d'un document précédemment emprunté :
    #     - Vérifiez que la méthode retourne True
    #     - Vérifiez que le document est retiré de la liste des documents empruntés
    #     - Vérifiez que le document est à nouveau disponible
    # - Testez le retour d'un document qui n'a pas été emprunté :
    #     - Vérifiez que la méthode retourne False
    # - Testez la méthode __str__ pour vous assurer que l'affichage correspond aux attentes
    print("Tous les tests ont été passés avec succès!")
