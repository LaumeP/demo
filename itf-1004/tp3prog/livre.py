from document import Document


class Livre(Document):
    """Classe représentant un livre, hérite de Document.

    Attributes:
        titre (str): Titre du livre
        auteur (str): Auteur du livre
        annee (int): Année de publication
        code_unique (str): Code d'identification unique
        disponible (bool): Indique si le livre est disponible pour emprunt (True par défaut)
        editeur (str): Nom de l'éditeur
        isbn (str): Numéro ISBN
        nb_pages (int): Nombre de pages du livre
    """

    def __init__(self, titre, auteur, annee, code_unique, editeur, isbn, nb_pages):
        """Initialise un nouveau livre.

        Args:
            titre (str): Titre du livre
            auteur (str): Auteur du livre
            annee (int): Année de publication
            code_unique (str): Code d'identification unique
            editeur (str): Nom de l'éditeur
            isbn (str): Numéro ISBN
            nb_pages (int): Nombre de pages
        """
        super().__init__(titre, auteur, annee, code_unique)
        self.editeur = editeur
        self.isbn = isbn
        self.nb_pages = nb_pages
        # Appeler le constructeur de la classe parent et initialiser
        # les attributs spécifiques aux livres


def test_initialisation_livre():
    """Teste l'initialisation d'un livre."""
    livre = Livre(
        "Les Fourmis",
        "Bernard Werber",
        1991,
        "LF-1991",
        "Albin Michel",
        "978-2226052414",
        351,
    )

    # Test des attributs hérités de Document
    assert livre.titre == "Les Fourmis", "Le titre n'est pas correctement initialisé"
    assert livre.auteur == "Bernard Werber", "L'auteur n'est pas correctement initialisé"
    assert livre.annee == 1991, "L'année n'est pas correctement initialisée"
    assert livre.code_unique == "LF-1991", "Le code unique n'est pas correctement initialisé"
    assert livre.disponible == True, "Un nouveau livre devrait être disponible par défaut"

    # Test des attributs spécifiques à Livre
    assert livre.editeur == "Albin Michel", "L'éditeur n'est pas correctement initialisé"
    assert livre.isbn == "978-2226052414", "L'ISBN n'est pas correctement initialisé"
    assert livre.nb_pages == 351, "Le nombre de pages n'est pas correctement initialisé"

    print("Test d'initialisation du livre réussi!")


def test_heritage_methodes():
    """Teste que les méthodes héritées de Document fonctionnent correctement."""
    livre = Livre(
        "Les Fourmis",
        "Bernard Werber",
        1991,
        "LF-1991",
        "Albin Michel",
        "978-2226052414",
        351,
    )

    # Test de l'initialisation de l'attribut disponible
    assert livre.disponible == True, "Un nouveau livre devrait être disponible"

    # Test de emprunter()
    assert livre.emprunter() == True, "L'emprunt d'un livre disponible devrait réussir"
    assert livre.disponible == False, "Après emprunt, le livre ne devrait plus être disponible"
    assert livre.emprunter() == False, "L'emprunt d'un livre déjà emprunté devrait échouer"

    # Test de retourner()
    assert livre.retourner() == True, "Le retour d'un livre emprunté devrait réussir"
    assert livre.disponible == True, "Après retour, le livre devrait être disponible"
    assert livre.retourner() == False, "Le retour d'un livre déjà disponible devrait échouer"

    print("Test des méthodes héritées réussi!")


def test_str_redefinition():
    """Teste si la méthode __str__ héritée fonctionne correctement avec les attributs de Livre."""
    livre = Livre(
        "Les Fourmis",
        "Bernard Werber",
        1991,
        "LF-1991",
        "Albin Michel",
        "978-2226052414",
        351,
    )

    representation_str_attendue = "Les Fourmis par Bernard Werber (1991) - disponible"
    assert str(livre) == representation_str_attendue

    # Simuler un emprunt et vérifier changement de statut dans la représentation
    livre.emprunter()
    representation_str_attendue = "Les Fourmis par Bernard Werber (1991) - emprunté"
    assert str(livre) == representation_str_attendue

    print("Test de la représentation textuelle du livre réussi!")


def test_type_instance():
    """Teste les relations d'héritage."""
    livre = Livre(
        "Les Fourmis",
        "Bernard Werber",
        1991,
        "LF-1991",
        "Albin Michel",
        "978-2226052414",
        351,
    )

    # Vérifier que l'instance est bien un Livre
    assert isinstance(livre, Livre), "L'objet devrait être une instance de Livre"

    # Vérifier que l'instance est aussi un Document (héritage)
    assert isinstance(livre, Document), "L'objet devrait aussi être une instance de Document (héritage)"

    print("Test des relations d'héritage réussi!")


def test_scenarios_avances():
    """Teste des scénarios d'utilisation plus avancés."""
    livre = Livre(
        "Les Fourmis",
        "Bernard Werber",
        1991,
        "LF-1991",
        "Albin Michel",
        "978-2226052414",
        351,
    )

    # Scénario d'emprunt/retour multiple
    assert livre.emprunter() == True, "Premier emprunt devrait réussir"
    assert livre.disponible == False, "Le livre ne devrait pas être disponible après emprunt"
    assert livre.retourner() == True, "Premier retour devrait réussir"
    assert livre.disponible == True, "Le livre devrait être disponible après retour"
    assert livre.emprunter() == True, "Deuxième emprunt devrait réussir"
    assert livre.disponible == False, "Le livre ne devrait pas être disponible après deuxième emprunt"
    assert livre.retourner() == True, "Deuxième retour devrait réussir"
    assert livre.disponible == True, "Le livre devrait être disponible après deuxième retour"

    print("Test des scénarios avancés réussi!")


# Exécution des tests
if __name__ == "__main__":
    print("Début des tests pour la classe Livre")
    test_initialisation_livre()
    test_heritage_methodes()
    test_str_redefinition()
    test_type_instance()
    test_scenarios_avances()
    print("Tous les tests pour la classe Livre ont été passés avec succès!")
