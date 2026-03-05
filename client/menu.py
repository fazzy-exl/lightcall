from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from settings import load_settings


class MenuWindow(QWidget):

    def __init__(self, start_call):
        super().__init__()

        settings = load_settings()

        self.setWindowTitle("LightCall")
        self.setMinimumSize(300, 200)

        layout = QVBoxLayout()

        title = QLabel("Choisir un serveur")
        layout.addWidget(title)

        settings_button = QPushButton("Paramètres")
        layout.addWidget(settings_button)

        gaming_button = QPushButton("Gaming")
        gaming_button.clicked.connect(start_call)

        layout.addWidget(gaming_button)

        self.setLayout(layout)

        self.name_label = QLabel(f"Nom : {settings['username']}")
        layout.addWidget(self.name_label)