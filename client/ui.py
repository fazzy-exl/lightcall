import cv2
from camera import Camera
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QPushButton
)


class VideoWidget(QLabel):
    def __init__(self, name):
        super().__init__()

        self.setText(name)

        self.setStyleSheet("""
            background-color: #2c2c2c;
            color: white;
            border: 2px solid #444;
        """)

        self.setAlignment(Qt.AlignCenter)

    def update_frame(self, frame):

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w, ch = frame.shape
        bytes_per_line = ch * w

        qt_image = QImage(
            frame.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888
        )

        self.setPixmap(QPixmap.fromImage(qt_image))


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.camera = Camera(0)

        self.camera_enabled = True

        self.setWindowTitle("LightCall")
        self.setMinimumSize(600, 400)

        main_layout = QVBoxLayout()

        title = QLabel("Serveur : Gaming")
        main_layout.addWidget(title)

        grid = QGridLayout()

        grid.setSpacing(10)
        grid.setContentsMargins(10, 10, 10, 10)

        self.jeremy_video = VideoWidget("Jeremy")
        self.theo_video = VideoWidget("Theo")
        self.caleb_video = VideoWidget("Caleb")

        grid.addWidget(self.jeremy_video, 0, 0)
        grid.addWidget(self.theo_video, 0, 1)
        grid.addWidget(self.caleb_video, 1, 0)

        main_layout.addLayout(grid)

        controls = QVBoxLayout()

        self.mic_button = QPushButton("🎤 Micro")
        self.cam_button = QPushButton("📷 Caméra ON")
        self.screen_button = QPushButton("🖥 Partage écran")

        self.cam_button.clicked.connect(self.toggle_camera)

        controls.addWidget(self.mic_button)
        controls.addWidget(self.cam_button)
        controls.addWidget(self.screen_button)

        main_layout.addLayout(controls)

        self.setLayout(main_layout)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(30)

    def update_camera(self):

        if not self.camera_enabled:
            self.jeremy_video.setText("Caméra désactivée")
            return

        frame = self.camera.get_frame()

        if frame is not None:
            self.jeremy_video.update_frame(frame)

    def toggle_camera(self):

        if self.camera_enabled:
            self.camera_enabled = False
            self.cam_button.setText("📷 Caméra OFF")

        else:
            self.camera_enabled = True
            self.cam_button.setText("📷 Caméra ON")


def start_ui():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()