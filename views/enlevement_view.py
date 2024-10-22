from PyQt6.QtWidgets import QWidget, QGridLayout, QLineEdit, QLabel, QHBoxLayout, QComboBox, QGroupBox, QVBoxLayout, QPushButton, QDateEdit, QScrollArea, QTableWidget, QDialog, QGraphicsBlurEffect
from PyQt6.QtCore import Qt
from datetime import time

class EnlevementView(QWidget):
    """
    Interface de la formulaire de la phase Enlevement
    """
    def __init__(self):
        super().__init__()
        
        # titre de la page
        self.setWindowTitle('ENLEVEMENT')
        
        ## -------------------------------------------------------------------TRANSPORTEUR-----------------------------------------------------------------------
        self.groupbox_transporteurs = QGroupBox("TRANSPORTEUR")
        
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
        grid_transporteur.addWidget(self.label_nom_transporteur, 0, 0)
        grid_transporteur.addWidget(self.edit_nom_transporteur, 0, 1)
        
        grid_transporteur.addWidget(self.label_nom_chauffeur, 1, 0)
        grid_transporteur.addWidget(self.edit_nom_chauffeur, 1, 1)
        grid_transporteur.addWidget(self.label_permis_de_conduire, 1, 2)
        grid_transporteur.addWidget(self.edit_permis_de_conduire, 1, 3)
        grid_transporteur.addWidget(self.label_num_telephone, 1, 4)
        grid_transporteur.addWidget(self.edit_num_telephone, 1, 5)
        
        grid_transporteur.addWidget(self.label_num_camion, 2, 0)
        grid_transporteur.addWidget(self.edit_num_camion, 2, 1)
        grid_transporteur.addWidget(self.label_num_remorque, 2, 2)
        grid_transporteur.addWidget(self.edit_num_remorque, 2, 3)
        
        vbox_transporteur = QVBoxLayout()
        vbox_transporteur.addLayout(grid_transporteur)
        
        self.groupbox_transporteurs.setLayout(vbox_transporteur)
        
        
        ## -------------------------------------------------------------------CONTENEURS-----------------------------------------------------------------------
        self.groupbox_conteneurs = QGroupBox("CONTENEURS")
        
        self.label_num_tc = QLabel("Numéro TC:")
        self.edit_num_tc = QLineEdit()
        self.label_num_plomb = QLabel("Numéro Plomb:")
        self.edit_num_plomb = QLineEdit()
        self.label_type_conteneur = QLabel("Type Conteneur:")
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
        
        
        # layout grid
        grid_conteneurs = QGridLayout()
        
        grid_conteneurs.addWidget(self.label_num_tc, 0, 0)
        grid_conteneurs.addWidget(self.edit_num_tc, 0, 1)
        grid_conteneurs.addWidget(self.label_num_plomb, 0, 2)
        grid_conteneurs.addWidget(self.edit_num_plomb, 0, 3)
        grid_conteneurs.addWidget(self.label_type_conteneur, 0, 4)
        grid_conteneurs.addWidget(self.cb1, 0, 5)
        
        grid_conteneurs.addWidget(self.label_etat_tc, 1, 0)
        grid_conteneurs.addWidget(self.cb2, 1, 1)
        grid_conteneurs.addWidget(self.label_observation, 1, 2)
        grid_conteneurs.addWidget(self.edit_observation, 1, 3)
        
        grid_conteneurs.addWidget(self.label_num_bl, 2, 0)
        grid_conteneurs.addWidget(self.edit_num_bl, 2, 1)
        grid_conteneurs.addWidget(self.label_compagnie_de_navigation, 2, 2)
        grid_conteneurs.addWidget(self.edit_compagnie_de_navigation, 2, 3)
          
        # layout verticale
        vbox_conteneurs = QVBoxLayout()
        vbox_conteneurs.addLayout(grid_conteneurs)
        
        self.groupbox_conteneurs.setLayout(vbox_conteneurs)
        
        
        ## -------------------------------------------------------------------DOCUMENTS-----------------------------------------------------------------------
        self.groupbox_documents = QGroupBox("DOCUMENTS")
        
        self.label_num_bon_de_sortie = QLabel("Numéro Bon de Sortie:")
        self.edit_num_bon_de_sortie = QLineEdit()
        self.label_date_bon_de_sortie = QLabel("Date Bon De Sortie:")
        self.edit_date_bon_de_sortie = QDateEdit()
        self.edit_date_bon_de_sortie.setCalendarPopup(True)
        self.label_num_dossier = QLabel("Num Dossier:")
        self.edit_num_dossier = QLineEdit()
        
        self.label_lieu_enlevement = QLabel("Lieu d'Enlevement:")
        self.edit_lieu_enlevement = QLineEdit()
        self.label_date_enlevement = QLabel("Date d'Enlevement:")
        self.edit_date_enlevement = QDateEdit()
        self.edit_date_enlevement.setCalendarPopup(True)
        
        self.label_ref_get_pass = QLabel("Rèf Get Pass:")
        self.edit_ref_get_pass = QLineEdit()
        self.label_date_get_pass = QLabel("Date Get ¨Pass:")
        self.edit_date_get_pass = QDateEdit()
        self.edit_date_get_pass.setCalendarPopup(True)
        
        self.label_ref_bad = QLabel("Rèf BAD:")
        self.edit_ref_bad = QLineEdit()
        self.label_date_bad = QLabel("Date BAD:")
        self.edit_date_bad = QDateEdit()
        self.edit_date_bad.setCalendarPopup(True)
        
        # Ajouter autres documents
        self.btn_ajouter_autres_documents = QPushButton("Ajouter Autres Documents")
        self.btn_ajouter_autres_documents.clicked.connect(self.ajouter_documents)
        
        # # redimensement pour le bouton ajouter
        # self.btn_ajouter_autres_documents.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        # self.btn_ajouter_autres_documents.setMaximumWidth(200)
        # self.btn_ajouter_autres_documents.setMinimumHeight(30)
        
        # Supprimer autres documents
        self.btn_supprimer_autres_documents= QPushButton("Supprimer Autres Documents")
        
        # layout grid
        grid_documents = QGridLayout()
        grid_documents.addWidget(self.label_num_bon_de_sortie, 0, 0)
        grid_documents.addWidget(self.edit_num_bon_de_sortie, 0, 1)
        grid_documents.addWidget(self.label_date_bon_de_sortie, 0, 2)
        grid_documents.addWidget(self.edit_date_bon_de_sortie, 0, 3)
        grid_documents.addWidget(self.label_num_dossier, 0, 4)
        grid_documents.addWidget(self.edit_num_dossier, 0, 5)
        
        grid_documents.addWidget(self.label_lieu_enlevement, 1, 0)
        grid_documents.addWidget(self.edit_lieu_enlevement, 1, 1)
        grid_documents.addWidget(self.label_date_enlevement, 1, 2)
        grid_documents.addWidget(self.edit_date_enlevement, 1, 3)
        
        grid_documents.addWidget(self.label_ref_get_pass, 2, 0)
        grid_documents.addWidget(self.edit_ref_get_pass, 2, 1)
        grid_documents.addWidget(self.label_date_get_pass, 2, 2)
        grid_documents.addWidget(self.edit_date_get_pass, 2, 3)
        
        grid_documents.addWidget(self.label_ref_bad, 3, 0)
        grid_documents.addWidget(self.edit_ref_bad, 3, 1)
        grid_documents.addWidget(self.label_date_bad, 3, 2)
        grid_documents.addWidget(self.edit_date_bad, 3, 3)
        
        grid_documents.addWidget(self.btn_ajouter_autres_documents, 5, 1,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        self.btn_ajouter_autres_documents.clicked.connect(self.ajouter_documents)
        grid_documents.addWidget(self.btn_supprimer_autres_documents, 5, 4,
                                 alignment=Qt.AlignmentFlag.AlignRight)
        
        
        # layout verticale
        vbox_documents = QVBoxLayout()
        vbox_documents.addLayout(grid_documents)
        
        self.groupbox_documents.setLayout(vbox_documents)
        
        
        ## -------------------------------------------------------------------CALCUL-----------------------------------------------------------------------
        self.groupbox_calculs = QGroupBox("")
        
        self.label_eta = QLabel("ETA:")
        self.edit_eta = QLineEdit()
        self.label_date_surestaries = QLabel("Date Surestaries")
        self.edit_date_surestaries = QLineEdit()
        self.label_depassement_surestaries = QLabel("Dépassement(jours)")
        self.edit_depassement_surestaries = QLineEdit()
        self.label_surestaries = QLabel("Surestaries")
        self.edit_surestaries = QLineEdit("0.00")
        
        self.label_date_magasinage = QLabel("Date Magasinage")
        self.edit_date_magasinage = QLineEdit()
        self.label_depassement_magasinage = QLabel("Dépassement(jours)")
        self.edit_depassement_magasinage = QLineEdit()
        self.label_frais_magasinage = QLabel("Frais Magasinage")
        self.edit_frais_magasinage = QLineEdit("0.00")
        
        # layout grid
        grid_calculs = QGridLayout()
        grid_calculs.addWidget(self.label_eta, 0, 0)
        grid_calculs.addWidget(self.edit_eta, 0, 1)
        grid_calculs.addWidget(self.label_date_surestaries, 0, 2)
        grid_calculs.addWidget(self.edit_date_surestaries, 0, 3)
        grid_calculs.addWidget(self.label_depassement_surestaries, 0, 4)
        grid_calculs.addWidget(self.edit_depassement_surestaries, 0, 5)
        grid_calculs.addWidget(self.label_surestaries, 0, 6)
        grid_calculs.addWidget(self.edit_surestaries, 0, 7)
        
        grid_calculs.addWidget(self.label_date_magasinage, 1, 2)
        grid_calculs.addWidget(self.edit_date_magasinage, 1, 3)
        grid_calculs.addWidget(self.label_depassement_magasinage, 1, 4)
        grid_calculs.addWidget(self.edit_depassement_magasinage, 1, 5)
        grid_calculs.addWidget(self.label_frais_magasinage, 1, 6)
        grid_calculs.addWidget(self.edit_frais_magasinage,1, 7)
        
        # layout verticale
        vbox_calculs = QVBoxLayout()
        vbox_calculs.addLayout(grid_calculs)
        
        self.groupbox_calculs.setLayout(vbox_calculs)
        
        ## -------------------------------------------------------------------BOUTON SOUMISSION-----------------------------------------------------------------------
        self.groupbox_bouton = QGroupBox("")
        
        self.btn_valider = QPushButton("Valider")
        # self.btn_valider.clicked.connect(self.creer_enlevement)
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
        
        
        ## -------------------------------------------------------------------LAYOUT VERTICALE-----------------------------------------------------------------------
        layout_vmix1 = QVBoxLayout()
        layout_vmix1.addWidget(self.groupbox_transporteurs)
        layout_vmix1.addWidget(self.groupbox_conteneurs)
        layout_vmix1.addWidget(self.groupbox_documents)
        layout_vmix1.addWidget(self.groupbox_calculs)
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
    def selection_change_type_conteneur(self, i):
        """
        Changer le type du conteneur
        """
        
        print("items in the list are:")
        for count in range(self.cb1.count()):
            print(self.cb1.itemText(count))
        print ("Current index",i,"selection changed ",self.cb1 .currentText())
    
    def selection_change_etat_conteneur(self, i):
        """
        Changer l'etat du conteneur
        """
        print("items in the list are:")
        for count in range(self.cb2.count()):
            print(self.cb2.itemText(count))
        print ("Current index",i,"selection changed ",self.cb2.currentText())
    
    def get_document_data(self):
        """ 
        Récupère les donnnées du document depuis l'interface 
        """
        document_data = {
            'num_bon_de_sortie': self.edit_num_bon_de_sortie.text(),
            'date_bon_de_sortie': self.edit_date_bon_de_sortie.date().toPyDate(),
            'num_dossier': self.edit_num_dossier.text()
        }
        for v in document_data.values():
            print(v)
        return document_data
      
    def get_enlevement_specific_document_data(self):
        """
        Cette méthode récupère les données spécifiques au document enlèvement
        """
        enlevement_specific_data = {
            'ref_get_pass': self.edit_ref_get_pass.text(),
            'date_get_pass': self.edit_date_get_pass.date().toPyDate(),
            'ref_BAD': self.edit_ref_bad.text(),
            'date_BAD': self.edit_date_bad.date().toPyDate()
        }
        for v in enlevement_specific_data.values():
            print(v)
        return enlevement_specific_data
    
    # def get_date_lieu_enlevement(self):
    #     """
    #     Cette méthode récupère la date et lieu d'enlèvement
    #     """
    #     date_lieu_enlevement = {
    #         'lieu_enlevement': self.edit_lieu_enlevement.text(),
    #         'date_enlevement': self.edit_date_enlevement.date().toPyDate()
    #     }
    #     for v in date_lieu_enlevement.values():
    #         print(v)
    #     return date_lieu_enlevement
        
    def get_transporteur_data(self):
        """
        Cette méthode récupère les données du transporteur depuis l'interface
        """
        transporteur_data = {
            'nom_transporteur': self.edit_nom_transporteur.text(),
            'nom_chauffeur': self.edit_nom_chauffeur.text(),
            'permis_de_conduire': self.edit_permis_de_conduire.text(),
            'num_telephone': self.edit_num_telephone.text(),
            'num_camion': self.edit_num_camion.text(),
            'num_remorque': self.edit_num_remorque.text()
        }
        return transporteur_data
    
    def get_conteneur_data(self):
        """
        Récupère les données du conteneurs depuis l'interface
        """
        conteneur_data = {
            'num_TC': self.edit_num_tc.text(),
            'plomb': self.edit_num_plomb.text(),
            'type_conteneur': self.cb1.currentText(),
            'etat_TC': self.cb2.currentText(),
            'observation': self.edit_observation.text(),
            'num_BL': self.edit_num_bl.text(),
            'compagnie_de_navigation': self.edit_compagnie_de_navigation.text()
        }
        return conteneur_data
    
    def get_date(self):
        """
        recuperer la date de l'enlevement
        """
        return self.edit_lieu_enlevement.text()
    
    def get_lieu(self):
        """
        recuperer le lieu d'enlevement
        """
        return self.edit_date_enlevement.date().toPyDate()
    
    def get_eta(self):
        """
        recuperer l'eta de la phase d'enlevement
        """
        return self.edit_eta
    
    def get_date_surestaries(self):
        """
        recuperer la date surestaries
        """
        self.edit_date_surestaries = self.edit_date_surestaries.text()
        
        # self.edit_date_surestaries.setText("0.00")
        # return self.edit_date_surestaries.date().toPyDate()
    
    def get_depassement_jours1(self):
        """
        recuperer la date de depassement du surestaries
        """
        
        self.edit_depassement_surestaries.setText(time.strftime("%d/%m/%y"))
        return self.edit_depassement_surestaries.date().toPyDate()
    
    def get_frais_surestaries(self):
        """
        recuperer la frais de surestaries
        """
        self.edit_surestaries.setText("0.00")
        return self.edit_surestaries
    
    def get_date_magasinage(self):
        """
        recuperer la date magasinage
        """
        self.edit_date_magasinage.setText(time.strftime("%d/%m/%y"))
        return self.edit_date_magasinage.date().toPyDate()
    
    def get_depassement_jouurs2(self):
        """
        recuperer la date de depassement magasinage
        """
        self.edit_depassement_magasinage.setText(time.strftime("%d/%m/%y"))
        return self.edit_depassement_magasinage.date().toPyDate()
    
    def get_frais_magasinage(self):
        """
        recuperer le frais de magasinage
        """
        self.edit_frais_magasinage.setText("0.00")
        return self.edit_frais_magasinage
    
    # def creer_enlevement(self):
        """
        methode pour creer un nouvel enlevement; il sert pour récuperer le data saisies par l'utilisateur
        """
    #     print("creer un nouvele enlevement") 
    #     data_enlevement = self.get_date_lieu_enlevement()
    #     data_conteneur = self.get_conteneur_data()
    #     data_transporteur = self.get_transporteur_data()
    #     data_document = self.get_document_data()
    #     data_specific_document_enlevement = self.get_enlevement_specific_document_data()
        
        
    #     print(data_enlevement)
    #     print(data_conteneur)
    #     print(data_transporteur)
    #     print(data_document)
    #     print(data_specific_document_enlevement)
        
    
    def ajouter_documents(self):
        """
        Ajouter d'autres documents
        """
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(10)
        self.setGraphicsEffect(self.blur_effect)
        self.ajouter_documents = AjouterDocuments(self)
        self.ajouter_documents.finished.connect(self.remove_blur_effect)
        self.ajouter_documents.show()
    
    def remove_blur_effect(self):
        """ remove Blur effect """
        
        self.setGraphicsEffect(None)
    
    
    
class AjouterDocuments(QDialog):
    """
    interface pour ajouter d'autre document
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Ajouter autres documents')
        
        # barre de recherche
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Rechercher...")
    
        # creation du tableau
        
        # layout pour la barre de recherche
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_bar)
        
        # layout principal 
        main_layout = QVBoxLayout()
        main_layout.addLayout(search_layout)
        self.create_table()
        main_layout.addWidget(self.table_widget)
        
        self.setLayout(main_layout)
        
        # ajuster la taille de la fenetre AjouterDocuments
        self.adjustSize()
        
        
    def create_table(self):
        """
        Creation de la table notificateur
        """
        self.table_widget = QTableWidget()
        
        # definir une taille fixe
        self.setFixedSize(700, 500)
        
        # definir le nombre de lignes et le nombres de colonnes
        self.table_widget.setRowCount(6)
        self.table_widget.setColumnCount(4)
        # masquer le numero de ligne
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setColumnWidth(0, 200)
        self.table_widget.setColumnWidth(1, 300)
        
        # ajouter l'en-tete du tableau
        self.table_widget.setHorizontalHeaderLabels(["Code doc", "Libelllé", "Reference doc", "date doc"])
        
        # ajuster la taille des lignes 
        self.table_widget.resizeRowsToContents()
        
        # desactiver le sroll vertical pour que tout soit visisble
        
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
    