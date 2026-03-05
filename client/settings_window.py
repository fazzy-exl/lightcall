from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from settings import load_settings, save_settings


class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paramètres")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nom d'utilisateur"))

        self.name_input = QLineEdit()

        settings = load_settings()
        self.name_input.setText(settings["username"])

        layout.addWidget(self.name_input)

        save_button = QPushButton("Sauvegarder")
        save_button.clicked.connect(self.save)

        layout.addWidget(save_button)

        self.setLayout(layout)

    def save(self):

        save_settings({
            "username": self.name_input.text()
        })

        self.close()