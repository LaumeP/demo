import tkinter as tk
from tkinter import ttk, messagebox
from livre import Livre
from utilisateur import Utilisateur
from datetime import datetime, timedelta


class BibliothequeApp(tk.Tk):
    """Interface graphique pour le système de gestion de bibliothèque."""

    def __init__(self, bibliotheque):
        """Initialise l'interface graphique.

        Args:
            bibliotheque (Bibliotheque): Instance de bibliothèque à gérer
        """
        super().__init__()

        self.bibliotheque = bibliotheque
        self.title(f"Gestion de la bibliothèque: {self.bibliotheque.nom}")
        self.geometry("900x600")

        self.creer_interface()

    def creer_interface(self):
        """Crée les widgets de l'interface."""
        # Création d'un notebook (conteneur d'onglets)
        self.conteneur_onglets = ttk.Notebook(self)
        self.conteneur_onglets.pack(fill="both", expand=True, padx=10, pady=10)

        # Onglet des documents
        self.onglet_documents = ttk.Frame(self.conteneur_onglets)
        self.conteneur_onglets.add(self.onglet_documents, text="Documents")

        # Onglet des utilisateurs
        self.onglet_utilisateurs = ttk.Frame(self.conteneur_onglets)
        self.conteneur_onglets.add(self.onglet_utilisateurs, text="Utilisateurs")

        # Onglet des emprunts
        self.onglet_emprunts = ttk.Frame(self.conteneur_onglets)
        self.conteneur_onglets.add(self.onglet_emprunts, text="Emprunts/Retours")

        # Configuration des onglets
        self.configurer_onglet_documents()
        self.configurer_onglet_utilisateurs()
        self.configurer_onglet_emprunts()

    def configurer_onglet_documents(self):
        """Configure l'onglet d'affichage et de recherche des documents."""
        # Frame pour la recherche
        frame_recherche = ttk.LabelFrame(
            self.onglet_documents, text="Recherche de documents"
        )
        frame_recherche.pack(fill="x", padx=10, pady=10)

        # Critères de recherche
        ttk.Label(frame_recherche, text="Critère:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.critere_var = tk.StringVar()
        criteres = ttk.Combobox(frame_recherche, textvariable=self.critere_var)
        criteres["values"] = ("titre", "auteur", "annee")
        criteres.grid(row=0, column=1, padx=5, pady=5)
        criteres.current(0)

        ttk.Label(frame_recherche, text="Valeur:").grid(row=0, column=2, padx=5, pady=5)
        self.valeur_var = tk.StringVar()
        ttk.Entry(frame_recherche, textvariable=self.valeur_var).grid(
            row=0, column=3, padx=5, pady=5
        )

        ttk.Button(
            frame_recherche, text="Rechercher", command=self.rechercher_documents
        ).grid(row=0, column=4, padx=5, pady=5)

        # TODO: À compléter
        # Ajouter un bouton "Réinitialiser" à la droite du champ de recherche.
        # Ce bouton devra appeler la méthode `self.reinitialiser` lorsqu'il est cliqué.

        # Liste des documents
        frame_liste = ttk.LabelFrame(self.onglet_documents, text="Liste des documents")
        frame_liste.pack(fill="both", expand=True, padx=10, pady=10)

        # Création du Treeview
        colonnes = ("type", "titre", "auteur", "annee", "statut")
        self.arbre_documents = ttk.Treeview(
            frame_liste, columns=colonnes, show="headings"
        )

        # Configuration des en-têtes
        self.arbre_documents.heading("type", text="Type")
        self.arbre_documents.heading("titre", text="Titre")
        self.arbre_documents.heading("auteur", text="Auteur")
        self.arbre_documents.heading("annee", text="Année")
        self.arbre_documents.heading("statut", text="Statut")

        # Configuration des colonnes
        self.arbre_documents.column("type", width=100)
        self.arbre_documents.column("titre", width=200)
        self.arbre_documents.column("auteur", width=150)
        self.arbre_documents.column("annee", width=80)
        self.arbre_documents.column("statut", width=100)

        # Ajout d'une scrollbar (barre de défilement)
        scrollbar = ttk.Scrollbar(
            frame_liste, orient="vertical", command=self.arbre_documents.yview
        )
        self.arbre_documents.configure(yscrollcommand=scrollbar.set)

        # Placement des widgets
        self.arbre_documents.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Actualisation initiale des documents
        self.actualiser_liste_documents()

    def configurer_onglet_utilisateurs(self):
        """Configure l'onglet de gestion des utilisateurs."""
        # Section pour ajouter un utilisateur
        frame_ajout = ttk.LabelFrame(
            self.onglet_utilisateurs, text="Ajout d'un utilisateur"
        )
        frame_ajout.pack(fill="x", padx=10, pady=10)

        # Champs pour les informations de l'utilisateur
        ttk.Label(frame_ajout, text="Nom:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.nom_var = tk.StringVar()
        ttk.Entry(frame_ajout, textvariable=self.nom_var).grid(
            row=0, column=1, padx=5, pady=5
        )

        ttk.Label(frame_ajout, text="Prénom:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.prenom_var = tk.StringVar()
        ttk.Entry(frame_ajout, textvariable=self.prenom_var).grid(
            row=1, column=1, padx=5, pady=5
        )

        ttk.Label(frame_ajout, text="ID:").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.id_var = tk.StringVar()
        ttk.Entry(frame_ajout, textvariable=self.id_var).grid(
            row=2, column=1, padx=5, pady=5
        )

        ttk.Button(frame_ajout, text="Ajouter", command=self.ajouter_utilisateur).grid(
            row=3, column=0, columnspan=2, pady=10
        )

        # Liste des utilisateurs
        frame_liste = ttk.LabelFrame(
            self.onglet_utilisateurs, text="Liste des utilisateurs"
        )
        frame_liste.pack(fill="both", expand=True, padx=10, pady=10)

        # Création du Treeview
        colonnes = ("id", "nom", "prenom", "emprunts")
        self.arbre_utilisateurs = ttk.Treeview(
            frame_liste, columns=colonnes, show="headings"
        )

        # Configuration des en-têtes
        self.arbre_utilisateurs.heading("id", text="ID")
        self.arbre_utilisateurs.heading("nom", text="Nom")
        self.arbre_utilisateurs.heading("prenom", text="Prénom")
        self.arbre_utilisateurs.heading("emprunts", text="Nbr. Emprunts")

        # Configuration des colonnes
        self.arbre_utilisateurs.column("id", width=100)
        self.arbre_utilisateurs.column("nom", width=150)
        self.arbre_utilisateurs.column("prenom", width=150)
        self.arbre_utilisateurs.column("emprunts", width=100)

        # Ajout d'une scrollbar (barre de défilement)
        scrollbar = ttk.Scrollbar(
            frame_liste, orient="vertical", command=self.arbre_utilisateurs.yview
        )
        self.arbre_utilisateurs.configure(yscrollcommand=scrollbar.set)

        # Placement des widgets
        self.arbre_utilisateurs.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Actualisation initiale des utilisateurs
        self.actualiser_liste_utilisateurs()

    def configurer_onglet_emprunts(self):
        """Configure l'onglet de gestion des emprunts et retours."""
        # Section pour les emprunts
        frame_emprunt = ttk.LabelFrame(self.onglet_emprunts, text="Nouvel emprunt")
        frame_emprunt.pack(fill="x", padx=10, pady=10)

        # Sélection utilisateur
        ttk.Label(frame_emprunt, text="Utilisateur:").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        self.utilisateur_emprunt_var = tk.StringVar()
        self.combo_utilisateur = ttk.Combobox(
            frame_emprunt, textvariable=self.utilisateur_emprunt_var
        )
        self.combo_utilisateur.grid(row=0, column=1, padx=5, pady=5)

        # Sélection document
        ttk.Label(frame_emprunt, text="Document:").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        self.document_emprunt_var = tk.StringVar()
        self.combo_document = ttk.Combobox(
            frame_emprunt, textvariable=self.document_emprunt_var
        )
        self.combo_document.grid(row=1, column=1, padx=5, pady=5)

        # Boutons pour emprunter/retourner
        ttk.Button(
            frame_emprunt, text="Emprunter", command=self.enregistrer_emprunt
        ).grid(row=2, column=0, padx=5, pady=10)
        ttk.Button(
            frame_emprunt, text="Retourner", command=self.enregistrer_retour
        ).grid(row=2, column=1, padx=5, pady=10)

        # Liste des emprunts en cours
        frame_liste = ttk.LabelFrame(self.onglet_emprunts, text="Emprunts en cours")
        frame_liste.pack(fill="both", expand=True, padx=10, pady=10)

        # Création du Treeview
        colonnes = ("utilisateur", "document", "date")
        self.arbre_emprunts = ttk.Treeview(
            frame_liste, columns=colonnes, show="headings"
        )

        # Configuration des en-têtes
        self.arbre_emprunts.heading("utilisateur", text="Utilisateur")
        self.arbre_emprunts.heading("document", text="Document")
        self.arbre_emprunts.heading("date", text="Date d'emprunt")

        # Configuration des colonnes
        self.arbre_emprunts.column("utilisateur", width=150)
        self.arbre_emprunts.column("document", width=250)
        self.arbre_emprunts.column("date", width=150)

        # Ajout d'une scrollbar (barre de défilement)
        scrollbar = ttk.Scrollbar(
            frame_liste, orient="vertical", command=self.arbre_emprunts.yview
        )
        self.arbre_emprunts.configure(yscrollcommand=scrollbar.set)

        # Placement des widgets
        self.arbre_emprunts.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Actualisation des listes déroulantes
        self.actualiser_listes_emprunts()

    def rechercher_documents(self):
        """Effectue une recherche de documents et actualise l'affichage."""
        critere = self.critere_var.get()
        valeur = self.valeur_var.get()

        if critere and valeur:
            # Conversion en entier pour l'année
            if critere == "annee":
                try:
                    valeur = int(valeur)
                except ValueError:
                    messagebox.showerror(
                        "Erreur", "L'année doit être un nombre entier", parent=self
                    )
                    return

            # Recherche des documents
            resultats = self.bibliotheque.rechercher_documents(critere, valeur)

            # Affichage des résultats
            self.actualiser_liste_documents(resultats)
        else:
            messagebox.showwarning(
                "Recherche",
                "Veuillez spécifier un critère et une valeur",
                parent=self
            )

    def reinitialiser(self):
        """Réinitialise les champs de recherche à leurs valeurs par défaut
        et met à jour la liste des documents affichés.

        Cette méthode est appelée lorsque l'utilisateur clique sur le bouton "Réinitialiser".
        Elle remet le critère de recherche à 'titre', vide le champ de valeur,
        puis actualise l'affichage pour refléter ces modifications.
        """
        # TODO: Implémenter cette méthode
        # Aide :
        # - Utilisez la méthode `set` sur `self.critere_var` et `self.valeur_var`
        # - Appelez la méthode `self.actualiser_liste_documents()` pour refléter les changements

    def actualiser_liste_documents(self, documents=None):
        """Actualise la liste des documents affichés.

        Args:
            documents (list, optional): Liste des documents à afficher.
                Si None, affiche tous les documents de la bibliothèque.
        """
        # Effacer les éléments actuels
        for item in self.arbre_documents.get_children():
            self.arbre_documents.delete(item)

        # Si aucune liste n'est fournie, utiliser tous les documents
        if documents is None:
            documents = self.bibliotheque.documents

        # Ajouter les documents à l'arbre
        for doc in documents:
            # Déterminer le type de document
            type_doc = "Livre" if isinstance(doc, Livre) else "Revue"

            # Déterminer le statut
            statut = "Disponible" if doc.disponible else "Emprunté"

            # Ajouter à l'arbre
            self.arbre_documents.insert(
                "", "end", values=(type_doc, doc.titre, doc.auteur, doc.annee, statut)
            )

    def ajouter_utilisateur(self):
        """Ajoute un nouvel utilisateur à la bibliothèque."""
        nom = self.nom_var.get()
        prenom = self.prenom_var.get()
        id_utilisateur = self.id_var.get()

        if nom and prenom and id_utilisateur:
            # Vérifier si l'ID existe déjà
            for utilisateur in self.bibliotheque.utilisateurs:
                if utilisateur.id_utilisateur == id_utilisateur:
                    messagebox.showerror(
                        "Erreur",
                        "Cet identifiant utilisateur existe déjà",
                        parent=self
                    )
                    return

            # Créer et ajouter le nouvel utilisateur
            utilisateur = Utilisateur(nom, prenom, id_utilisateur)
            self.bibliotheque.ajouter_utilisateur(utilisateur)

            # Effacer les champs
            self.nom_var.set("")
            self.prenom_var.set("")
            self.id_var.set("")

            # Actualiser la liste des utilisateurs
            self.actualiser_liste_utilisateurs()
            self.actualiser_listes_emprunts()

            messagebox.showinfo(
                "Succès",
                f"L'utilisateur {prenom} {nom} a été ajouté avec succès",
                parent=self
            )
        else:
            messagebox.showwarning(
                "Avertissement", "Tous les champs sont obligatoires", parent=self
            )

    def actualiser_liste_utilisateurs(self):
        """Actualise la liste des utilisateurs affichés."""
        # Effacer les éléments actuels
        for item in self.arbre_utilisateurs.get_children():
            self.arbre_utilisateurs.delete(item)

        # Ajouter les utilisateurs à l'arbre
        for utilisateur in self.bibliotheque.utilisateurs:
            # Ajouter à l'arbre
            self.arbre_utilisateurs.insert(
                "",
                "end",
                values=(
                    utilisateur.id_utilisateur,
                    utilisateur.nom,
                    utilisateur.prenom,
                    len(utilisateur.documents_empruntes),
                ),
            )

    def actualiser_listes_emprunts(self):
        """Actualise les listes déroulantes des utilisateurs et documents pour les emprunts."""
        # Actualiser la liste des utilisateurs
        utilisateurs = [
            f"{u.prenom} {u.nom} ({u.id_utilisateur})"
            for u in self.bibliotheque.utilisateurs
        ]
        self.combo_utilisateur["values"] = utilisateurs

        # Actualiser la liste des documents disponibles
        documents = [
            f"{d.titre} - {d.code_unique}"
            for d in self.bibliotheque.documents_disponibles()
        ]
        self.combo_document["values"] = documents

        # Actualiser la liste des emprunts en cours
        for item in self.arbre_emprunts.get_children():
            self.arbre_emprunts.delete(item)

        date = datetime.now().strftime("%d/%m/%Y")

        # Ajouter les documents empruntés par chaque utilisateur
        for utilisateur in self.bibliotheque.utilisateurs:
            for doc in utilisateur.documents_empruntes:
                self.arbre_emprunts.insert(
                    "",
                    "end",
                    values=(
                        f"{utilisateur.prenom} {utilisateur.nom}",
                        f"{doc.titre} ({doc.code_unique})",
                        date,
                    ),
                )

    def enregistrer_emprunt(self):
        """Enregistre un nouvel emprunt."""
        utilisateur_str = self.utilisateur_emprunt_var.get()
        document_str = self.document_emprunt_var.get()

        if not utilisateur_str or not document_str:
            messagebox.showwarning(
                "Avertissement",
                "Veuillez sélectionner un utilisateur et un document",
                parent=self
            )
            return

        # Récupérer l'ID utilisateur
        id_utilisateur = utilisateur_str.split("(")[-1].strip(")")

        # Récupérer le code du document
        code_document = document_str.split("-")[-1].strip()

        # Trouver l'utilisateur
        utilisateur_trouve = None
        for utilisateur in self.bibliotheque.utilisateurs:
            if utilisateur.id_utilisateur == id_utilisateur:
                utilisateur_trouve = utilisateur
                
        if not utilisateur_trouve:
            messagebox.showerror("Erreur", "Utilisateur introuvable", parent=self)
            return

        # Trouver le document
        document = None
        for doc in self.bibliotheque.documents:
            if doc.code_unique.strip() == code_document.strip():
                document = doc
                
        if not document:
            messagebox.showerror("Erreur", "Document introuvable", parent=self)
            return

        # Effectuer l'emprunt
        if utilisateur_trouve.emprunter_document(document):
            messagebox.showinfo(
                "Succès",
                f'Le document "{document.titre}" a été emprunté par {utilisateur_trouve.prenom} {utilisateur_trouve.nom}',
                parent=self
            )

            # Réinitialiser les champs
            self.utilisateur_emprunt_var.set("")
            self.document_emprunt_var.set("")

            # Actualiser les listes
            self.actualiser_liste_documents()
            self.actualiser_liste_utilisateurs()
            self.actualiser_listes_emprunts()
        else:
            messagebox.showerror(
                "Erreur",
                "L'emprunt a échoué. Le document est peut-être déjà emprunté.",
                parent=self
            )

    def enregistrer_retour(self):
        """Enregistre un retour de document."""
        selection = self.arbre_emprunts.selection()

        if not selection:
            messagebox.showwarning(
                "Avertissement",
                "Veuillez sélectionner un emprunt à retourner",
                parent=self
            )
            return

        # Récupérer les informations de l'emprunt sélectionné
        item = self.arbre_emprunts.item(selection[0])
        utilisateur_str = item["values"][0]
        document_str = item["values"][1]

        # Récupérer le code du document
        code_document = document_str.split("(")[-1].strip(")")

        # Récupérer le nom et prénom de l'utilisateur
        nom_prenom = utilisateur_str.split()
        if len(nom_prenom) < 2:
            messagebox.showerror(
                "Erreur", "Format de nom d'utilisateur incorrect", parent=self
            )
            return

        prenom = nom_prenom[0]
        nom = nom_prenom[1]

        # Trouver l'utilisateur
        utilisateur_trouve = None
        for utilisateur in self.bibliotheque.utilisateurs:
            if utilisateur.prenom == prenom and utilisateur.nom == nom:
                utilisateur_trouve = utilisateur
                
        if not utilisateur_trouve:
            messagebox.showerror("Erreur", "Utilisateur introuvable", parent=self)
            return

        # Trouver le document
        document = None
        for doc in utilisateur_trouve.documents_empruntes:
            if doc.code_unique == code_document:
                document = doc
                
        if not document:
            messagebox.showerror(
                "Erreur",
                "Document introuvable dans les emprunts de l'utilisateur",
                parent=self
            )
            return

        # Effectuer le retour
        if utilisateur_trouve.retourner_document(document):
            messagebox.showinfo(
                "Succès",
                f'Le document "{document.titre}" a été retourné par {utilisateur_trouve.prenom} {utilisateur_trouve.nom}',
                parent=self
            )

            # Actualiser les listes
            self.actualiser_liste_documents()
            self.actualiser_liste_utilisateurs()
            self.actualiser_listes_emprunts()
        else:
            messagebox.showerror("Erreur", "Le retour a échoué", parent=self)
