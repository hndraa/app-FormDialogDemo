
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QLineEdit, QFormLayout, QInputDialog, QFrame,
    QMessageBox, QSizePolicy
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class ClickableInput(QLineEdit):
    """A read-only input that opens a dialog when clicked."""

    def __init__(self, placeholder, callback, parent=None):
        super().__init__(parent)

        self.callback = callback
        self.setReadOnly(True)
        self.setPlaceholderText(placeholder)
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(46)
        self.setFocusPolicy(Qt.StrongFocus)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.callback()

        super().mousePressEvent(event)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter, Qt.Key_Space):
            self.callback()
            return

        super().keyPressEvent(event)


class FormDialogDemo(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Form Dialog Studio")
        self.resize(760, 720)
        self.setMinimumSize(600, 620)

        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 28, 30, 28)
        main_layout.setSpacing(18)

        # Header
        header = QVBoxLayout()
        header.setSpacing(6)

        eyebrow = QLabel("INTERACTIVE FORM • PYQT5")
        eyebrow.setObjectName("eyebrow")

        title = QLabel("Form Dialog Studio")
        title.setObjectName("title")

        subtitle = QLabel(
            "Complete your profile using interactive input dialogs."
        )
        subtitle.setObjectName("subtitle")
        subtitle.setWordWrap(True)

        header.addWidget(eyebrow)
        header.addWidget(title)
        header.addWidget(subtitle)

        main_layout.addLayout(header)

        # Form card
        self.form_card = QFrame()
        self.form_card.setObjectName("card")

        card_layout = QVBoxLayout(self.form_card)
        card_layout.setContentsMargins(24, 24, 24, 24)
        card_layout.setSpacing(18)

        section_title = QLabel("Personal Information")
        section_title.setObjectName("sectionTitle")

        section_description = QLabel(
            "Select each field to enter or choose your information."
        )
        section_description.setObjectName("sectionDescription")
        section_description.setWordWrap(True)

        card_layout.addWidget(section_title)
        card_layout.addWidget(section_description)

        # Form fields
        form = QFormLayout()
        form.setSpacing(16)
        form.setLabelAlignment(Qt.AlignLeft)
        form.setFormAlignment(Qt.AlignTop)
        form.setFieldGrowthPolicy(QFormLayout.ExpandingFieldsGrow)

        self.nama_input = ClickableInput(
            "Click to enter your name", self.edit_nama
        )
        self.nim_input = ClickableInput(
            "Click to enter your student ID", self.edit_nim
        )
        self.bahasa_input = ClickableInput(
            "Click to select a language", self.edit_bahasa
        )

        self.nama_input.setObjectName("formInput")
        self.nim_input.setObjectName("formInput")
        self.bahasa_input.setObjectName("formInput")

        form.addRow("Full Name", self.nama_input)
        form.addRow("Student ID", self.nim_input)
        form.addRow("Favorite Language", self.bahasa_input)

        card_layout.addLayout(form)

        # Helper text
        helper = QLabel(
            "TIP  •  Click an input field to open its dialog."
        )
        helper.setObjectName("helper")
        card_layout.addWidget(helper)

        # Action buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(12)

        self.reset_btn = QPushButton("Reset Form")
        self.reset_btn.setObjectName("secondaryButton")
        self.reset_btn.setMinimumHeight(46)
        self.reset_btn.clicked.connect(self.reset_form)

        self.submit_btn = QPushButton("Submit Profile")
        self.submit_btn.setObjectName("primaryButton")
        self.submit_btn.setMinimumHeight(46)
        self.submit_btn.clicked.connect(self.show_result)

        button_layout.addWidget(self.reset_btn)
        button_layout.addWidget(self.submit_btn)

        card_layout.addLayout(button_layout)
        main_layout.addWidget(self.form_card)

        # Result card
        self.result_card = QFrame()
        self.result_card.setObjectName("resultCard")

        result_layout = QVBoxLayout(self.result_card)
        result_layout.setContentsMargins(22, 18, 22, 18)
        result_layout.setSpacing(10)

        result_header = QHBoxLayout()

        self.result_title = QLabel("Profile Summary")
        self.result_title.setObjectName("resultTitle")

        self.status_label = QLabel("NOT SUBMITTED")
        self.status_label.setObjectName("statusLabel")

        result_header.addWidget(self.result_title)
        result_header.addStretch()
        result_header.addWidget(self.status_label)

        result_layout.addLayout(result_header)

        self.result_label = QLabel(
            "Your submitted information will appear here."
        )
        self.result_label.setObjectName("resultText")
        self.result_label.setWordWrap(True)
        self.result_label.setTextInteractionFlags(
            Qt.TextSelectableByMouse
        )

        result_layout.addWidget(self.result_label)
        main_layout.addWidget(self.result_card)

        # Footer
        footer = QLabel("Hndraa Apps")
        footer.setObjectName("footer")
        footer.setAlignment(Qt.AlignCenter)

        main_layout.addStretch()
        main_layout.addWidget(footer)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #0f172a;
                color: #e2e8f0;
                font-family: "Segoe UI";
                font-size: 10pt;
            }

            QLabel#eyebrow {
                color: #a5b4fc;
                font-size: 9pt;
                font-weight: bold;
                letter-spacing: 2px;
            }

            QLabel#title {
                color: #f8fafc;
                font-size: 27pt;
                font-weight: bold;
            }

            QLabel#subtitle {
                color: #94a3b8;
                font-size: 10pt;
            }

            QFrame#card, QFrame#resultCard {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 16px;
            }

            QLabel#sectionTitle {
                background: transparent;
                color: #f8fafc;
                font-size: 15pt;
                font-weight: bold;
            }

            QLabel#sectionDescription {
                background: transparent;
                color: #94a3b8;
                font-size: 9pt;
            }

            QFormLayout QLabel {
                background-color: transparent;
                color: #cbd5e1;
                font-weight: bold;
                border: none;
                padding: 0px;
            }

            QLineEdit#formInput {
                background-color: #0f172a;
                color: #f8fafc;
                border: 1px solid #475569;
                border-radius: 9px;
                padding: 10px 12px;
                selection-background-color: #6366f1;
            }

            QLineEdit#formInput:hover {
                border: 1px solid #818cf8;
            }

            QLineEdit#formInput:focus {
                border: 2px solid #818cf8;
            }

            QLineEdit#formInput:read-only {
                background-color: #0f172a;
            }

            QLabel#helper {
                background: transparent;
                color: #818cf8;
                font-size: 9pt;
            }

            QPushButton {
                border: none;
                border-radius: 9px;
                padding: 10px 16px;
                font-weight: bold;
            }

            QPushButton#primaryButton {
                background-color: #6366f1;
                color: white;
            }

            QPushButton#primaryButton:hover {
                background-color: #4f46e5;
            }

            QPushButton#primaryButton:pressed {
                background-color: #4338ca;
            }

            QPushButton#secondaryButton {
                background-color: #334155;
                color: #e2e8f0;
                border: 1px solid #475569;
            }

            QPushButton#secondaryButton:hover {
                background-color: #475569;
            }

            QLabel#resultTitle {
                background: transparent;
                color: #f8fafc;
                font-size: 12pt;
                font-weight: bold;
            }

            QLabel#statusLabel {
                background-color: #312e81;
                color: #c7d2fe;
                border-radius: 6px;
                padding: 5px 8px;
                font-size: 8pt;
                font-weight: bold;
            }

            QLabel#resultText {
                background: transparent;
                color: #cbd5e1;
                line-height: 1.5;
            }

            QLabel#footer {
                background: transparent;
                color: #64748b;
                font-size: 9pt;
            }

            QMessageBox, QInputDialog {
                background-color: #1e293b;
            }

            QMessageBox QLabel, QInputDialog QLabel {
                color: #e2e8f0;
            }

            QInputDialog QLineEdit, QInputDialog QComboBox {
                background-color: #0f172a;
                color: #f8fafc;
                border: 1px solid #475569;
                border-radius: 6px;
                padding: 7px;
            }

            QInputDialog QPushButton, QMessageBox QPushButton {
                background-color: #6366f1;
                color: white;
                min-width: 75px;
            }
            /* Remove background from form labels */
            QLabel {
                background: transparent;
                background-color: rgba(0, 0, 0, 0);
                border: none;
            }
        """)

    def edit_nama(self):
        text, ok = QInputDialog.getText(
            self,
            "Full Name",
            "Enter your full name:",
            text=self.nama_input.text()
        )

        if ok and text.strip():
            self.nama_input.setText(text.strip())
            self.mark_as_unsubmitted()

    def edit_nim(self):
        text, ok = QInputDialog.getText(
            self,
            "Student ID",
            "Enter your student ID:",
            text=self.nim_input.text()
        )

        if ok and text.strip():
            self.nim_input.setText(text.strip())
            self.mark_as_unsubmitted()

    def edit_bahasa(self):
        languages = [
            "Python", "Java", "C++", "JavaScript", "Go"
        ]

        current = self.bahasa_input.text()
        initial_index = (
            languages.index(current) if current in languages else 0
        )

        item, ok = QInputDialog.getItem(
            self,
            "Favorite Language",
            "Choose your favorite programming language:",
            languages,
            initial_index,
            False
        )

        if ok and item:
            self.bahasa_input.setText(item)
            self.mark_as_unsubmitted()

    def mark_as_unsubmitted(self):
        self.status_label.setText("NOT SUBMITTED")
        self.result_label.setText(
            "Your information has changed. Submit again to update "
            "the profile summary."
        )

    def show_result(self):
        nama = self.nama_input.text().strip()
        nim = self.nim_input.text().strip()
        bahasa = self.bahasa_input.text().strip()

        if not nama or not nim or not bahasa:
            QMessageBox.warning(
                self,
                "Incomplete Form",
                "Please complete all three fields before submitting."
            )
            return

        self.result_label.setText(
            f"Full Name: {nama}\n"
            f"Student ID: {nim}\n"
            f"Favorite Language: {bahasa}"
        )

        self.status_label.setText("SUBMITTED")

    def reset_form(self):
        reply = QMessageBox.question(
            self,
            "Reset Form",
            "Are you sure you want to clear all fields?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            self.nama_input.clear()
            self.nim_input.clear()
            self.bahasa_input.clear()

            self.status_label.setText("NOT SUBMITTED")
            self.result_label.setText(
                "Your submitted information will appear here."
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = FormDialogDemo()
    window.show()

    sys.exit(app.exec_())
