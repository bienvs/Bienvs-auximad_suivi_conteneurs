from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QToolButton, QComboBox, QGroupBox, QVBoxLayout, QPushButton, QDateEdit, QToolButton, QTableWidget, QTimeEdit, QScrollArea
from PyQt6.QtCore import Qt


class ReceptionView(QWidget):
    """
    Interface de la formulaire de la phase Expedition
    """
    def __init__(self):
        super().__init__()
        
        # titre de la page
        self.setWindowTitle('RECEPTION')
    
    ## -------------------------------------------------------------------TRANSPORTEUR-----------------------------------------------------------------------
        self.groupbox_transporteurs = QGroupBox("TRANSPORTEUR")
        
        self.label_date_arrivee = QLabel("Date Arrivee:")
        self.edit_date_arrivee = QDateEdit()
        self.label_heure_arrivee = QLabel("Heure Arrivee:")
        self.edit_heure_arrivee = QTimeEdit()
        self.label_nom_transporteur = QLabel("Nom Transporteur:")
        self.edit_nom_transporteur = QLineEdit()
        self.label_nom_chauffeur = QLabel("Nom Chauffeur:")
        self.edit_nom_chauffeur = QLineEdit()
        self.label_permis_de_conduire = QLabel("Permis de Conduire:")
        self.edit_permis_de_conduire = QLineEdit()
        self.label_num_telephone = QLabel("Numéro Téléphone:")
        self.edit_num_telephone = QLineEdit()
        self.label_num_camion = QLabel("Numéro Camion:")
        self.edit_num_camion = QLineEdit()
        self.label_num_remorque = QLabel("Numéro Rémorque:")
        self.edit_num_remorque = QLineEdit()
        
        grid_transporteur = QGridLayout()
        
        grid_transporteur.addWidget(self.label_date_arrivee, 0, 0)
        grid_transporteur.addWidget(self.edit_date_arrivee, 0, 1)
        grid_transporteur.addWidget(self.label_heure_arrivee, 0, 2)
        grid_transporteur.addWidget(self.edit_heure_arrivee, 0, 3)
        
        grid_transporteur.addWidget(self.label_nom_transporteur, 1, 0)
        grid_transporteur.addWidget(self.edit_nom_transporteur, 1, 1)
        
        grid_transporteur.addWidget(self.label_nom_chauffeur, 2, 0)
        grid_transporteur.addWidget(self.edit_nom_chauffeur, 2, 1)
        grid_transporteur.addWidget(self.label_permis_de_conduire, 2, 2)
        grid_transporteur.addWidget(self.edit_permis_de_conduire, 2, 3)
        grid_transporteur.addWidget(self.label_num_telephone, 2, 4)
        grid_transporteur.addWidget(self.edit_num_telephone, 2, 5)
        
        grid_transporteur.addWidget(self.label_num_camion, 3, 0)
        grid_transporteur.addWidget(self.edit_num_camion, 3, 1)
        grid_transporteur.addWidget(self.label_num_remorque, 3, 2)
        grid_transporteur.addWidget(self.edit_num_remorque, 3, 3)
        
        vbox_transporteur = QVBoxLayout()
        vbox_transporteur.addLayout(grid_transporteur)
        
        self.groupbox_transporteurs.setLayout(vbox_transporteur)
        
        
        ## -------------------------------------------------------------------CONTENEURS-----------------------------------------------------------------------
        self.groupbox_conteneurs = QGroupBox("CONTENEURS")
        
        self.label_num_tc = QLabel("Numéro TC:")
        self.edit_num_tc = QLineEdit()
        self.tool_btn_num_tc = QToolButton()
        self.label_num_plomb = QLabel("Numéro Plomb:")
        self.edit_num_plomb = QLineEdit()
        self.label_type_conteneur = QLabel("Type Conteneur:")
        self.edit_type_conteneur = QLineEdit()
        self.cb1 = QComboBox()
        self.cb1.addItems(['20ft', '40ft', 'Reefer'])
        self.cb1.currentIndexChanged.connect(self.selection_change_type_conteneur)
        self.label_etat_tc = QLabel("Etat TC:")
        self.edit_etat_tc = QLineEdit()
        self.cb2 = QComboBox()
        self.cb2.addItems(['FULL IN', 'EMPTY IN'])
        self.cb2.currentIndexChanged.connect(self.selection_change_etat_conteneur)
        self.label_observation = QLabel("Observation:")
        self.edit_observation = QLineEdit()
        self.label_num_bl = QLabel("Numéro BL:")
        self.edit_num_bl = QLineEdit()
        self.label_compagnie_de_navigation = QLabel("Compagnie de Navigation:")
        self.edit_compagnie_de_navigation = QLineEdit()
        self.label_eta = QLabel("ETA:")
        self.edit_eta = QLineEdit()
        
        
        # layout grid
        grid_conteneurs = QGridLayout()
        
        grid_conteneurs.addWidget(self.label_num_tc, 0, 0)
        grid_conteneurs.addWidget(self.edit_num_tc, 0, 1)
        grid_conteneurs.addWidget(self.tool_btn_num_tc, 0, 2)
        grid_conteneurs.addWidget(self.label_num_plomb, 0, 3)
        grid_conteneurs.addWidget(self.edit_num_plomb, 0, 4)
        grid_conteneurs.addWidget(self.label_type_conteneur, 0, 5)
        grid_conteneurs.addWidget(self.cb1, 0, 6)
        
        grid_conteneurs.addWidget(self.label_etat_tc, 1, 0)
        grid_conteneurs.addWidget(self.cb2, 1, 1)
        grid_conteneurs.addWidget(self.label_observation, 1, 2)
        grid_conteneurs.addWidget(self.edit_observation, 1, 3)
        
        grid_conteneurs.addWidget(self.label_num_bl, 2, 0)
        grid_conteneurs.addWidget(self.edit_num_bl, 2, 1)
        grid_conteneurs.addWidget(self.label_compagnie_de_navigation, 2, 2)
        grid_conteneurs.addWidget(self.edit_compagnie_de_navigation, 2, 3)
        
        grid_conteneurs.addWidget(self.label_eta, 3, 0)
        grid_conteneurs.addWidget(self.edit_eta, 3, 1)
        
        # layout verticale
        vbox_conteneurs = QVBoxLayout()
        vbox_conteneurs.addLayout(grid_conteneurs)
        
        self.groupbox_conteneurs.setLayout(vbox_conteneurs)
        
        
        ## -------------------------------------------------------------------DOCUMENTS-----------------------------------------------------------------------
        self.groupbox_documents = QGroupBox("DOCUMENTS")
        
        self.label_num_bon_de_livraison = QLabel("Numéro Bon De Livraison:")
        self.edit_num_bon_de_livraison = QLineEdit()
        self.label_date_bon_de_livraison = QLabel("Date Bon De Livraison:")
        self.edit_date_bon_de_livraison = QDateEdit()
        self.edit_date_bon_de_livraison.setCalendarPopup(True)
        self.label_num_dossier = QLabel("Num Dossier:")
        self.edit_num_dossier = QLineEdit()
        self.label_num_bon_de_sortie = QLabel("Numéro Bon de Sortie:")
        self.edit_num_bon_de_sortie = QLineEdit()
        self.tool_btn_num_bon_de_sortie = QToolButton()
        self.label_date_bon_de_sortie = QLabel("Date Bon De Sortie:")
        self.edit_date_bon_de_sortie = QDateEdit()
        self.edit_date_bon_de_sortie.setCalendarPopup(True)
        self.label_num_eir_plein = QLabel("Numéro EIR Plein:")
        self.edit_num_eir_plein = QLineEdit()
        self.label_date_eir_plein = QLabel("Date EIR Plein:")
        self.edit_date_eir_plein = QDateEdit()
        self.edit_date_eir_plein.setCalendarPopup(True)
        self.label_lieu_de_livraison = QLabel("Lieu de Livraison:")
        self.edit_lieu_de_livraison = QLineEdit()
        self.label_lieu_de_restitution = QLabel("Lieu de Restitution:")
        self.edit_lieu_de_restitution = QLineEdit()
        self.label_date_limite_de_restitution = QLabel("Date Limite de Restitution:")
        self.edit_date_limite_de_restitution = QDateEdit()
        self.edit_date_limite_de_restitution.setCalendarPopup(True)
        self.label_date_envoi = QLabel("Date d'Envoi:")
        self.edit_date_envoi = QDateEdit()
        self.edit_date_envoi.setCalendarPopup(True)
        self.label_lieu_envoi = QLabel("à:")
        self.edit_lieu_envoi = QLineEdit()
        
        # Ajouter autres documents
        self.btn_ajouter_autres_documents = QPushButton("Ajouter Autres Documents")
        
        # Supprimer autres documents
        self.btn_supprimer_autres_documents= QPushButton("Supprimer Autres Documents")
        
        # layout grid
        grid_documents = QGridLayout()
        grid_documents.addWidget(self.label_num_bon_de_livraison, 0, 0)
        grid_documents.addWidget(self.edit_num_bon_de_livraison, 0, 1)
        grid_documents.addWidget(self.label_date_bon_de_livraison, 0, 2)
        grid_documents.addWidget(self.edit_date_bon_de_livraison, 0, 3)
        grid_documents.addWidget(self.label_num_dossier, 0, 4)
        grid_documents.addWidget(self.edit_num_dossier, 0, 5)
        grid_documents.addWidget(self.label_num_bon_de_sortie, 1, 0)
        grid_documents.addWidget(self.edit_num_bon_de_sortie, 1, 1)
        grid_documents.addWidget(self.tool_btn_num_bon_de_sortie, 1, 2)
        grid_documents.addWidget(self.label_date_bon_de_sortie, 1, 3)
        grid_documents.addWidget(self.edit_date_bon_de_sortie, 1, 4)
        grid_documents.addWidget(self.label_num_eir_plein, 2, 0)
        grid_documents.addWidget(self.edit_num_eir_plein, 2, 1)
        grid_documents.addWidget(self.label_date_eir_plein, 2, 2)
        grid_documents.addWidget(self.edit_date_eir_plein, 2, 3)
        grid_documents.addWidget(self.label_lieu_de_livraison, 3, 0)
        grid_documents.addWidget(self.edit_lieu_de_livraison, 3, 1)
        grid_documents.addWidget(self.label_lieu_de_restitution, 4, 0)
        grid_documents.addWidget(self.edit_lieu_de_restitution, 4, 1)
        grid_documents.addWidget(self.label_date_limite_de_restitution, 4, 2)
        grid_documents.addWidget(self.edit_date_limite_de_restitution, 4, 3)
        grid_documents.addWidget(self.label_date_envoi, 5, 0)
        grid_documents.addWidget(self.edit_date_envoi, 5, 1)
        grid_documents.addWidget(self.label_lieu_envoi, 5, 2)
        grid_documents.addWidget(self.edit_lieu_envoi, 5, 3)
        grid_documents.addWidget(self.btn_ajouter_autres_documents, 6, 1,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        grid_documents.addWidget(self.btn_supprimer_autres_documents, 6, 4,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        
        
        # layout verticale
        vbox_documents = QVBoxLayout()
        vbox_documents.addLayout(grid_documents)
        
        self.groupbox_documents.setLayout(vbox_documents)

        
        
        ## -------------------------------------------------------------------A NOTIFIER-----------------------------------------------------------------------
        self.groupbox_notifier = QGroupBox("A NOTIFIER")
        
        grid_notifier = QGridLayout()
        self.create_table()
        grid_notifier.addWidget(self.table_widget, 0, 0, 1, 7)
        
        # layout verticale
        vbox_notifier = QVBoxLayout()
        vbox_notifier.addLayout(grid_notifier)
        
        self.groupbox_notifier.setLayout(vbox_notifier)
    
    def create_table(self):
        """
        Creation de la table notificateur
        """
        self.table_widget = QTableWidget()
        # definir le nombre de lignes et le nombres de colonnes
        self.table_widget.setRowCount(4)
        self.table_widget.setColumnCount(2)
        # masquer le numero de ligne
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 300)
        
        # ajouter l'en-tete du tableau
        self.table_widget.setHorizontalHeaderLabels(["Propriétaire", "Adresse Mail"])
        
        
        ## -------------------------------------------------------------------BOUTON SOUMISSION-----------------------------------------------------------------------
        self.groupbox_bouton = QGroupBox("")
        
        self.btn_valider = QPushButton("Valider")
        self.btn_annuler = QPushButton("Annuler")
        
        # layout grid
        grid_bouton = QGridLayout()
        grid_bouton.addWidget(self.btn_valider, 0, 1,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        grid_bouton.addWidget(self.btn_annuler, 0, 4,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        
        # layout verticale
        vbox_bouton = QVBoxLayout()
        vbox_bouton.addLayout(grid_bouton)
        
        self.groupbox_bouton.setLayout(vbox_bouton)
        
        ## ------------------------------------------------------------------- Layout contenir le formulaire -----------------------------------------------------------------------
        layout_vmix1 = QVBoxLayout()
        layout_vmix1.addWidget(self.groupbox_transporteurs)
        layout_vmix1.addWidget(self.groupbox_conteneurs)
        layout_vmix1.addWidget(self.groupbox_documents)
        layout_vmix1.addWidget(self.groupbox_notifier)
        layout_vmix1.addWidget(self.groupbox_bouton)
        
        ## ----------------------------------------------------------------creer un widget pour contenir le layout-----------------------------------------------------------------------
        container_widget = QWidget()
        container_widget.setLayout(layout_vmix1)
        
        ## -------------------------------------------------------------------Ajouter une zone de defilement -----------------------------------------------------------------------
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(container_widget)
        
        ## -------------------------------------------------------------------LAYOUT PRINCIPALE-----------------------------------------------------------------------
        layout_vmix2 = QVBoxLayout()
        layout_vmix2.addWidget(scroll_area)
        
        self.setLayout(layout_vmix2)
        
        
    
    # methode
    def selection_change_type_conteneur(self):
        """
        Changer le type du conteneur
        """
        pass
    
    def selection_change_etat_conteneur(self):
        """
        Changer l'etat du conteneur
        """
        pass
    
    
    
            
        
        
        
        