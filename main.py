import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, 
    QRadioButton, QPushButton, QCheckBox, QFrame, QMessageBox
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtGui import QFont, QPalette, QColor

class LiquidGlassWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('CyberSec iOS 27 Toolkit')
        self.setFixedSize(850, 550)
        
        # Liquid Glass Style Sheet
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #0f172a, stop:0.5 #1e1b4b, stop:1 #312e81);
                color: #f8fafc;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto;
            }
            QFrame#GlassCard {
                background-color: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 20px;
            }
            QLabel {
                color: #e2e8f0;
            }
            QRadioButton {
                color: #f1f5f9;
                font-size: 14px;
                spacing: 10px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border-radius: 9px;
                border: 2px solid #38bdf8;
                background: rgba(0, 0, 0, 0.2);
            }
            QRadioButton::indicator:checked {
                background: #38bdf8;
            }
            QCheckBox {
                color: #cbd5e1;
                font-size: 13px;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 16px;
                height: 16px;
                border-radius: 4px;
                border: 2px solid #38bdf8;
                background: rgba(0, 0, 0, 0.2);
            }
            QCheckBox::indicator:checked {
                background: #38bdf8;
            }
            QPushButton#StartBtn {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0284c7, stop:1 #2563eb);
                color: white;
                font-size: 16px;
                font-weight: bold;
                border-radius: 12px;
                padding: 12px;
                border: 1px solid rgba(255, 255, 255, 0.2);
            }
            QPushButton#StartBtn:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0ea5e9, stop:1 #3b82f6);
            }
            QPushButton#StartBtn:pressed {
                background: #0369a1;
            }
        """)
        
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Left side: 30% Phone Graphic Frame
        left_frame = QFrame()
        left_frame.setObjectName("GlassCard")
        left_layout = QVBoxLayout(left_frame)
        
        phone_mockup = QLabel("📱\n[ iPhone 27 Pro ]\nLiquid Glass Edition")
        phone_mockup.setAlignment(Qt.AlignCenter)
        phone_mockup.setStyleSheet("font-size: 16px; color: #38bdf8; font-weight: bold;")
        left_layout.addWidget(phone_mockup)
        
        main_layout.addWidget(left_frame, 30)
        
        # Right side: 70% Phone info and controls
        right_frame = QFrame()
        right_frame.setObjectName("GlassCard")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(30, 30, 30, 30)
        right_layout.setSpacing(20)
        
        # Phone Info Section
        info_title = QLabel("Connected Device Telemetry")
        info_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #38bdf8;")
        right_layout.addWidget(info_title);
        
        sn_val = f"SN: C39X{random.randint(1000,9999)}HDV"
        icloud_val = "iCloud: a***@icloud.com"
        ios_val = "iOS Version: 27.0.1 (Liquid Core)"
        
        self.lbl_sn = QLabel(sn_val)
        self.lbl_icloud = QLabel(icloud_val)
        self.lbl_ios = QLabel(ios_val)
        
        for lbl in (self.lbl_sn, self.lbl_icloud, self.lbl_ios):
            lbl.setStyleSheet("font-size: 14px; color: #94a3b8; background: rgba(0,0,0,0.1); padding: 8px; border-radius: 8px;")
            right_layout.addWidget(lbl)
            
        # Radio Buttons Section
        self.rb_screen_time = QRadioButton("1: Remove Screen Time")
        self.rb_screen_time.setChecked(True)
        self.rb_account = QRadioButton("2: Remove Screen Time & Account (Hide)")
        
        right_layout.addWidget(self.rb_screen_time)
        right_layout.addWidget(self.rb_account)
        
        # Start Button (Blue Button with Start text)
        self.btn_start = QPushButton("START BYPASS")
        self.btn_start.setObjectName("StartBtn")
        self.btn_start.clicked.connect(self.execute_action)
        right_layout.addWidget(self.btn_start)
        
        # Checkbox under Start Button
        self.cb_block_ota = QCheckBox("Block OTA & Enable Fake Reset")
        right_layout.addWidget(self.cb_block_ota)
        
        main_layout.addWidget(right_frame, 70)
        
    def execute_action(self):
        ota_blocked = self.cb_block_ota.isChecked()
        
        if self.rb_screen_time.isChecked():
            msg = "Success: Screen Time successfully removed via OpenMenuX exploit vector!"
            if ota_blocked:
                msg += "\nOTA Updates blocked & Fake Reset safety layer armed."
            QMessageBox.information(self, "Bypass Status (iOS 27)", msg)
            
        elif self.rb_account.isChecked():
            msg = "Success: Screen Time removed & iCloud Account safely hidden/bypassed!"
            if ota_blocked:
                msg += "\nOTA Updates blocked & Fake Reset safety layer armed."
            QMessageBox.warning(self, "Advanced Bypass Status (iOS 27)", msg)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LiquidGlassWindow()
    ex.show()
    sys.exit(app.exec_())
