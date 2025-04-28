from document import Document


class Revue(Document):
    """Classe représentant une revue, hérite de Document.

    Attributes:
        titre (str): Titre de la revue
        auteur (str): Éditeur de la revue
        annee (int): Année de publication
        code_unique (str): Code d'identification unique
        disponible (bool): Indique si la revue est disponible pour emprunt (True par défaut)
        numero (int): Numéro de la revue
        frequence (str): Fréquence de publication (mensuelle, trimestrielle, etc.)
    """

    def __init__(self, titre, auteur, annee, code_unique, numero, frequence):
        """Initialise une nouvelle revue.

        Args:
            titre (str): Titre de la revue
            auteur (str): Éditeur de la revue
            annee (int): Année de publication
            code_unique (str): Code d'identification unique
            numero (int): Numéro de la revue
            frequence (str): Fréquence de publication (mensuelle, trimestrielle, etc.)
        """
        super().__init__(titre, auteur, annee, code_unique)
        self.numero = numero
        self.frequence = frequence
        # Appeler le constructeur de la classe parent et initialiser
        # les attributs spécifiques aux revues

    def __str__(self):
        """Retourne une représentation textuelle de la revue.

        Returns:
            str: Description de la revue
        """
        """Retourne une représentation textuelle de la revue."""
        statut = "disponible" if self.disponible else "empruntée"
        return f"{self.titre} (n°{self.numero}) - {self.frequence} - {self.annee} - {statut}"


def test_initialisation_revue():
    """Teste l'initialisation d'une revue."""
    revue = Revue(
        "National Geographic", 
        "National Geographic Society", 
        2022, 
        "NG-2022-12",
        276, 
        "mensuelle"
    )
    
    # Test des attributs hérités de Document
    assert revue.titre == "National Geographic", "Le titre n'est pas correctement initialisé"
    assert revue.auteur == "National Geographic Society", "L'éditeur n'est pas correctement initialisé"
    assert revue.annee == 2022, "L'année n'est pas correctement initialisée"
    assert revue.code_unique == "NG-2022-12", "Le code unique n'est pas correctement initialisé"
    assert revue.disponible == True, "Une nouvelle revue devrait être disponible par défaut"
    
    # Test des attributs spécifiques à Revue
    assert revue.numero == 276, "Le numéro n'est pas correctement initialisé"
    assert revue.frequence == "mensuelle", "La fréquence n'est pas correctement initialisée"
    
    print("Test d'initialisation de la revue réussi!")

def test_heritage_methodes():
    """Teste que les méthodes héritées de Document fonctionnent correctement."""
    revue = Revue(
        "National Geographic", 
        "National Geographic Society", 
        2022, 
        "NG-2022-12",
        276, 
        "mensuelle"
    )
    
    # Test de l'initialisation de l'attribut disponible
    assert revue.disponible == True, "Une nouvelle revue devrait être disponible"
    
    # Test de emprunter()
    assert revue.emprunter() == True, "L'emprunt d'une revue disponible devrait réussir"
    assert revue.disponible == False, "Après emprunt, la revue ne devrait plus être disponible"
    assert revue.emprunter() == False, "L'emprunt d'une revue déjà empruntée devrait échouer"
    
    # Test de retourner()
    assert revue.retourner() == True, "Le retour d'une revue empruntée devrait réussir"
    assert revue.disponible == True, "Après retour, la revue devrait être disponible"
    assert revue.retourner() == False, "Le retour d'une revue déjà disponible devrait échouer"
    
    print("Test des méthodes héritées réussi!")

def test_str_redefinition():
    """Teste si la méthode __str__ surchargée fonctionne correctement."""
    revue = Revue(
        "National Geographic", 
        "National Geographic Society", 
        2022, 
        "NG-2022-12",
        276, 
        "mensuelle"
    )
    
    representation_str_attendue = "National Geographic (n°276) - mensuelle - 2022 - disponible"
    assert str(revue) == representation_str_attendue
    
    # Simuler un emprunt et vérifier changement de statut dans la représentation
    revue.emprunter()
    representation_str_attendue = "National Geographic (n°276) - mensuelle - 2022 - empruntée"
    assert str(revue) == representation_str_attendue
    
    print("Test de la représentation textuelle de la revue réussi!")

def test_type_instance():
    """Teste les relations d'héritage."""
    revue = Revue(
        "National Geographic", 
        "National Geographic Society", 
        2022, 
        "NG-2022-12",
        276, 
        "mensuelle"
    )
    
    # Vérifier que l'instance est bien une Revue
    assert isinstance(revue, Revue), "L'objet devrait être une instance de Revue"
    
    # Vérifier que l'instance est aussi un Document (héritage)
    assert isinstance(revue, Document), "L'objet devrait aussi être une instance de Document (héritage)"
    
    print("Test des relations d'héritage réussi!")

def test_scenarios_avances():
    """Teste des scénarios d'utilisation plus avancés."""
    revue = Revue(
        "National Geographic", 
        "National Geographic Society", 
        2022, 
        "NG-2022-12",
        276, 
        "mensuelle"
    )
    
    # Scénario d'emprunt/retour multiple
    assert revue.emprunter() == True, "Premier emprunt devrait réussir"
    assert revue.disponible == False, "La revue ne devrait pas être disponible après emprunt"
    assert revue.retourner() == True, "Premier retour devrait réussir"
    assert revue.disponible == True, "La revue devrait être disponible après retour"
    assert revue.emprunter() == True, "Deuxième emprunt devrait réussir"
    assert revue.disponible == False, "La revue ne devrait pas être disponible après deuxième emprunt"
    assert revue.retourner() == True, "Deuxième retour devrait réussir"
    assert revue.disponible == True, "La revue devrait être disponible après deuxième retour"
    
    print("Test des scénarios avancés réussi!")

def test_comparaison_avec_document():
    """Compare le comportement d'une revue par rapport à un Document standard."""
    # Créer un Document et une Revue avec les mêmes attributs de base
    doc = Document("Titre Test", "Auteur Test", 2023, "CODE-TEST")
    revue = Revue("Titre Test", "Auteur Test", 2023, "CODE-TEST", 42, "mensuelle")
    
    # Vérifier que leur comportement de base est identique
    assert doc.disponible == revue.disponible, "Comportement de disponibilité devrait être identique"
    
    # Les emprunter tous les deux
    doc.emprunter()
    revue.emprunter()
    assert doc.disponible == revue.disponible, "Comportement après emprunt devrait être identique"
    
    # Vérifier que la redefinition de __str__ fonctionne différemment
    assert str(doc) != str(revue), "La représentation textuelle devrait être différente"
    assert "n°42" in str(revue), "La représentation de la revue devrait inclure le numéro"
    assert "mensuelle" in str(revue), "La représentation de la revue devrait inclure la fréquence"
    
    print("Test de comparaison avec Document réussi!")

# Exécution des tests
if __name__ == "__main__":
    print("Début des tests pour la classe Revue")
    test_initialisation_revue()
    test_heritage_methodes()
    test_str_redefinition()
    test_type_instance()
    test_comparaison_avec_document()
    test_scenarios_avances()
    print("Tous les tests pour la classe Revue ont été passés avec succès!")
