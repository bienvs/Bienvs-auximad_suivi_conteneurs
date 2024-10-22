import sys
from PyQt6.QtWidgets import QApplication
from config import create_session
from views.enlevement_view import EnlevementView
from views.expedition_view import ExpeditionView
from views.reception_view import ReceptionView
from views.restitution_view import RestitutionView
from controllers.enlevement_controller import EnlevementController

def main():
    """" 
    applcation principale
    """
    app = QApplication(sys.argv)
    
    app.setStyleSheet("""
                      QLabel {
                          font-size: 14px;
                          color: #2c3e50;
                          font-weight: 600;
                      }
                      QLineEdit, QDateEdit, QComboBox {
                          border: 1px solid transparent;
                          background-color: #e0e0e0;
                          border-radius: 5px;
                          padding: 5px;
                          font-size: 12px;
                      }
                      QLineEdit:focus, QDateEdit:focus{
                          border-color: #2980b9;
                          background-color: #ecf0f1;
                      }
                      QPushButton {
                          background-color: #4CAF50;
                          border: none;
                          color: white;
                          padding: 10px 28px;
                          text-align: center;
                          text-decoration: none;
                          font-size: 14px;
                          border-radius: 10px;
                      }
                       QPushButton:hover {
                           background-color: #45a049;
                       }
                       QPushButton:pressed {
                           background-color: #3e8e41;
                       }
                       QComboBox {
                           background-color: #ffffff;
                           border: 1px solid #4CAF50;
                           padding: 5px;
                           border-radius: 5px;
                       }
                       QComboBox QAbstractIemVew {
                           background-color: #f9f9f9;
                           border: 1px solid #4CAF50;
                           selection-background-color: #4CAF50;
                           selection-color: white;
                       }
                       QComboBox:hover {
                           border: 1px solid #45a049;
                       }
                       QComboBox:drop-down {
                           subcontrol-origin: padding;
                           subcontrol-position: top right;
                           width: 20px;
                           border-left: 1px solid #4CAF50;   
                       }
                       QComboBox::down-arrow {
                           
                       }
                       QGroupBox {
                            border: 1px solid #3498db;
                            border-radius: 5px;
                            margin-top: 10px;
                            margin-left: 10px;
                            background-color: white;
                        }
                        QGroupBox::title {
                            subcontrol-origin: margin;
                            subcontrol-position: top center;
                            padding: 0 2px;
                            color: green; 
                            border-radius: 2px;
                        }
                        QTableWidget {
                            background-color: #f0f0f0;
                            gridline-color: #dcdcdc;
                            font-size: 14px;
                        }
                        QTableWidget::item {
                            padding: 5px;
                        }
                        QHeaderView::section {
                            background-color: white;
                            color: blue;
                            padding: 5px;
                            font-weight: bold;
                            border: 1px solid #dcdcdc;
                        }
                        QTableWidget::item:hover {
                            background-color: #e0e0e0;
                        }
                      """)
    
    session = create_session()
    enlevement_view = EnlevementView()
    expedition_view = ExpeditionView()
    reception_view = ReceptionView()
    restitution_view = RestitutionView()
    controller = EnlevementController(session, enlevement_view)
    enlevement_view.show()
    expedition_view.show()
    reception_view.show()
    restitution_view.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
