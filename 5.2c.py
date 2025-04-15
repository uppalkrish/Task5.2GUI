import sys
import RPi.GPIO as GPIO
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor

# Set up GPIO
GPIO.setmode(GPIO.BCM)
LED1, LED2, LED3 = 17, 18, 27
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# Set up PWM for LEDs
pwm1 = GPIO.PWM(LED1, 1000)
pwm2 = GPIO.PWM(LED2, 1000)
pwm3 = GPIO.PWM(LED3, 1000)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

class LEDApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LED Brightness Control")
        layout = QVBoxLayout()

        # Red LED
        self.label1 = QLabel("Red LED")
        self.set_label_color(self.label1, "red")
        self.slider1 = QSlider(Qt.Orientation.Horizontal)
        self.slider1.setRange(0, 100)
        self.slider1.valueChanged.connect(lambda value: self.change_brightness(pwm1, value))
        layout.addWidget(self.label1)
        layout.addWidget(self.slider1)

        # Green LED
        self.label2 = QLabel("Green LED")
        self.set_label_color(self.label2, "green")
        self.slider2 = QSlider(Qt.Orientation.Horizontal)
        self.slider2.setRange(0, 100)
        self.slider2.valueChanged.connect(lambda value: self.change_brightness(pwm2, value))
        layout.addWidget(self.label2)
        layout.addWidget(self.slider2)

        # Blue LED
        self.label3 = QLabel("Blue LED")
        self.set_label_color(self.label3, "blue")
        self.slider3 = QSlider(Qt.Orientation.Horizontal)
        self.slider3.setRange(0, 100)
        self.slider3.valueChanged.connect(lambda value: self.change_brightness(pwm3, value))
        layout.addWidget(self.label3)
        layout.addWidget(self.slider3)

        # Exit button
        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.close_app)
        layout.addWidget(exit_btn)

        self.setLayout(layout)

    def set_label_color(self, label, color):
        palette = label.palette()
        palette.setColor(QPalette.ColorRole.WindowText, QColor(color))
        label.setPalette(palette)

    def change_brightness(self, pwm, value):
        pwm.ChangeDutyCycle(value)

    def close_app(self):
        pwm1.stop()
        pwm2.stop()
        pwm3.stop()
        GPIO.cleanup()
        self.close()

app = QApplication(sys.argv)
window = LEDApp()
window.show()
sys.exit(app.exec())
