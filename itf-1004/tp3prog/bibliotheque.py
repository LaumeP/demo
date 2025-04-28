class Bibliotheque:
    """Classe gérant une collection de documents et d'utilisateurs.

    Attributes:
        nom (str): Nom de la bibliothèque
        documents (list): Liste des documents disponibles dans la bibliothèque (liste vide par défaut)
        utilisateurs (list): Liste des utilisateurs inscrits à la bibliothèque (liste vide par défaut)
    """

    def __init__(self, nom):
        """Initialise une nouvelle bibliothèque.

        Args:
            nom (str): Nom de la bibliothèque
        """
        self.nom = nom
        self.document = []
        self.utilisateur = []

    def ajouter_document(self, document):
        """Ajoute un document à la collection.

        Args:
            document (Document): Document à ajouter
        """
        self.document.append(document)

    def ajouter_utilisateur(self, utilisateur):
        """Ajoute un utilisateur à la bibliothèque.

        Args:
            utilisateur (Utilisateur): Utilisateur à ajouter
        """
        self.utilisateur.append(utilisateur)

    def rechercher_documents(self, critere, valeur):
        """Recherche des documents selon un critère: retourne la liste des documents
        dont l'attribut spécifié par le critère correspond à la valeur recherchée.

        Args:
            critere (str): Attribut sur lequel effectuer la recherche ("titre", "auteur", etc.)
            valeur: Valeur recherchée

        Returns:
            list: Liste des documents correspondant au critère
        """
        resultats = []
        for doc in self.documents:
            if hasattr(doc, critere):
                attr_value = getattr(doc, critere)
                # Recherche insensible à la casse pour les chaînes
                if isinstance(attr_value, str) and isinstance(valeur, str):
                    if valeur.lower() in attr_value.lower():
                        resultats.append(doc)
                # Recherche exacte pour les autres types
                elif attr_value == valeur:
                    resultats.append(doc)
        return resultats

    def documents_disponibles(self):
        """Retourne la liste des documents disponibles.

        Returns:
            list: Liste des documents disponibles
        """
        return [doc for doc in self.documents if doc.disponible]
