import os
from config import PATH as path 
from PyQt6.QtWidgets import QLabel, QToolBar, QMainWindow, QVBoxLayout, QComboBox, QWidget, QLineEdit, QHBoxLayout, QPushButton, QTableWidget
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import *

class MainWindow(QMainWindow):
    """
    page d'accueil de l'application suivi_de_conteneurs
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accueil")
        
        
        # créer la toolbar
        self.create_toolbar()
        
        # créer les contenus principal
        self.create_main()
        
        
    def create_toolbar(self):
        """
        creer un toolbar
        """
        toolbar = QToolBar("ma toolbar")
        self.addToolBar(toolbar)
        
        # ajouter une action pour l'admin
        admin = QAction("Administration", self)
        admin.triggered.connect(self.admin_clicked)
        toolbar.addAction(admin)
        
        # ajouter une action pour l'application
        application = QAction("Application", self)
        application.triggered.connect(self.app_clicked)
        toolbar.addAction(application)
        
        # ajouter une action pour l'application
        aide = QAction("Aide", self)
        aide.triggered.connect(self.aide_clicked)
        toolbar.addAction(aide)
        
    def create_main(self):
        """
        interface pour la barre de filtrage et de la recherche
        """
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # layout
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        btn_layout = QHBoxLayout()
        
        # logo
        logo_label = QLabel(self)
        sary = QPixmap("auximad.png")
        logo_label.setPixmap(sary)
        logo_label.setScaledContents(True)
        h_layout.addWidget(logo_label)
        
        # barre de filtrage
        filter_bar = QComboBox(self)
        filter_bar.addItems(["filtre1", "filtre2", "filtre3"])
        h_layout.addWidget(filter_bar)
        
        # barre de recherche
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Rechercher ici...")
        h_layout.addWidget(search_bar)
        
        # bouton pour chaque phase 
        home_btn = QPushButton("Accueil", self)
        btn_layout.addWidget(home_btn)
        
        enlevement_btn = QPushButton("Enlèvement", self)
        btn_layout.addWidget(enlevement_btn)
        
        expedition_btn = QPushButton("Expédition", self)
        btn_layout.addWidget(expedition_btn)
        
        reception_btn = QPushButton("Réception", self)
        btn_layout.addWidget(reception_btn)
        
        restitution_btn = QPushButton("Restitution", self)
        btn_layout.addWidget(restitution_btn)
        
        notification_btn = QPushButton("Notification", self)
        btn_layout.addWidget(notification_btn)
        
        choisir_btn = QPushButton("Choisir Fichier", self)
        btn_layout.addWidget(choisir_btn)
        choisir_btn.clicked.connect(self.choisir_clicked)
        
        
        # créer un tableau de bord
        self.create_table()
        
        
        
        
        #--------------------------------------------- ajout layout------------------------------------------------------------
        v_layout.addLayout(h_layout)
        v_layout.addLayout(btn_layout)
        v_layout.addWidget(self.table_widget)
        
        #---------------------------------------------layout principal------------------------------------------------------------
        main_layout = QVBoxLayout()
        main_layout.addLayout(v_layout)
        central_widget.setLayout(main_layout)
    
        
    def choisir_clicked(self):
        """
        choisir un fichier et exporter en excel
        """
        file = './BonSortie2024.csv'  
        if os.path.exists(path):
            os.system(f"start excel.exe {path + file}") # afaka atao: start pdf.exe CV.pdf
        else:
            print('Incorrecte')
        
        
    def admin_clicked(self):
        """
        methode pour l'administration
        """
        self.label.setText("Nouvelle action selectionnée")
        
    def app_clicked(self):
        """
        methode pour l'application
        """
        self.label.setText("Nouvelle action selectionnée")
        
    def aide_clicked(self):
        """
        methode pour l'aide
        """
        self.label.setText("Nouvelle action selectionnée")
        
    def create_table(self):
        """
        Creation de la table notificateur
        """
        self.table_widget = QTableWidget()
        
        # definir une taille fixe
        # self.setFixedSize(700, 500)
        
        # definir le nombre de lignes et le nombres de colonnes
        self.table_widget.setRowCount(6)
        self.table_widget.setColumnCount(5)
        
        # masquer le numero de ligne
        self.table_widget.verticalHeader().setVisible(False)
        # self.table_widget.setColumnWidth(0, 200)
        # self.table_widget.setColumnWidth(1, 300)
        
        # ajouter l'en-tete du tableau
        self.table_widget.setHorizontalHeaderLabels(["Conteneur", "Transporteur", "Phase actuel", "Frais surestaries", "Frais magasinage"])
        
        # ajuster la taille des lignes 
        # self.table_widget.resizeRowsToContents()
        
        # desactiver le sroll vertical pour que tout soit visisble
        
        # self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
      