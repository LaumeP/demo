class Document:
    """Classe de base pour tous les documents de la bibliothèque.

    Attributes:
        titre (str): Titre du document
        auteur (str): Auteur du document
        annee (int): Année de publication
        code_unique (str): Code d'identification unique
        disponible (bool): Indique si le document est disponible pour emprunt (True par défaut)
    """

    def __init__(self, titre, auteur, annee, code_unique):
        """Initialise un nouveau document.

        Args:
            titre (str): Titre du document
            auteur (str): Auteur du document
            annee (int): Année de publication
            code_unique (str): Code d'identification unique
        """
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.code_unique = code_unique
        self.disponible = True

    def emprunter(self):
        """Marque le document comme emprunté s'il est disponible.

        Returns:
            bool: True si l'emprunt a réussi, False sinon
        """
        if self.disponible:
            self.disponible = False
            return True
        return False
        # Si le document est disponible, le marquer comme non disponible et
        # retourner True, sinon retourner False

    def retourner(self):
        """Marque le document comme retourné/disponible.

        Returns:
            bool: True si le retour a réussi, False sinon
        """
        if not self.disponible:
            self.disponible = True
            return True
        return False
        # Si le document n'est pas disponible (a été emprunté), le marquer comme disponible et
        # retourner True, sinon retourner False

    def __str__(self):
        """Retourne une représentation textuelle du document.

        Returns:
            str: Description du document
        """
        statut = "disponible" if self.disponible else "emprunté"
        return f"{self.titre} par {self.auteur} ({self.annee}) - {statut}"


def test_initialisation():
    """Teste l'initialisation d'un document."""
    doc = Document("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "LPP-1943")

    assert doc.titre == "Le Petit Prince", "Le titre n'est pas correctement initialisé"
    assert doc.auteur == "Antoine de Saint-Exupéry", "L'auteur n'est pas correctement initialisé"
    assert doc.annee == 1943, "L'année n'est pas correctement initialisée"
    assert doc.code_unique == "LPP-1943", "Le code unique n'est pas correctement initialisé"
    assert doc.disponible == True, "Un nouveau document devrait être disponible par défaut"

    print("Test d'initialisation réussi!")


def test_emprunter():
    """Teste la méthode emprunter."""
    doc = Document("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "LPP-1943")

    # Premier emprunt (devrait réussir)
    resultat_emprunt = doc.emprunter()
    assert resultat_emprunt == True, "L'emprunt d'un document disponible devrait réussir"
    assert doc.disponible == False, "Après emprunt, le document ne devrait plus être disponible"

    # Deuxième emprunt (devrait échouer)
    resultat_emprunt_2 = doc.emprunter()
    assert resultat_emprunt_2 == False, "L'emprunt d'un document déjà emprunté devrait échouer"
    assert doc.disponible == False, "Le statut ne devrait pas changer lors d'un emprunt échoué"

    print("Test d'emprunt réussi!")


def test_retourner():
    """Teste la méthode retourner."""
    doc = Document("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "LPP-1943")

    # Simuler un emprunt
    doc.disponible = False

    # Retour du document (devrait réussir)
    resultat_retour = doc.retourner()
    assert resultat_retour == True, "Le retour d'un document emprunté devrait réussir"
    assert doc.disponible == True, "Après retour, le document devrait être disponible"

    # Deuxième retour (devrait échouer)
    resultat_retour_2 = doc.retourner()
    assert resultat_retour_2 == False, "Le retour d'un document déjà disponible devrait échouer"
    assert doc.disponible == True, "Le statut ne devrait pas changer lors d'un retour échoué"

    print("Test de retour réussi!")


def test_str():
    """Teste la méthode __str__."""
    doc = Document("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "LPP-1943")

    # Test avec document disponible
    representation_str_attendue = "Le Petit Prince par Antoine de Saint-Exupéry (1943) - disponible"
    assert str(doc) == representation_str_attendue

    # Test avec document emprunté
    doc.emprunter()
    representation_str_attendue = "Le Petit Prince par Antoine de Saint-Exupéry (1943) - emprunté"
    assert str(doc) == representation_str_attendue

    print("Test de la représentation textuelle réussi!")


def test_cycle_complet():
    """Teste un cycle complet d'emprunt et de retour."""
    doc = Document("L'Étranger", "Albert Camus", 1942, "EC-1942")

    assert doc.disponible == True, "Le document devrait être disponible au départ"

    # Emprunt
    assert doc.emprunter() == True, "L'emprunt devrait réussir"
    assert doc.disponible == False, "Le document ne devrait plus être disponible après emprunt"
    assert doc.emprunter() == False, "Un second emprunt devrait échouer"

    # Retour
    assert doc.retourner() == True, "Le retour devrait réussir"
    assert doc.disponible == True, "Le document devrait être disponible après retour"
    assert doc.retourner() == False, "Un second retour devrait échouer"

    print("Test de cycle complet réussi!")


# Exécution des tests
if __name__ == "__main__":
    print("Début des tests pour la classe Document")
    test_initialisation()
    test_emprunter()
    test_retourner()
    test_str()
    test_cycle_complet()
    print("Tous les tests ont été passés avec succès!")
