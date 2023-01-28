import openai
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget)

openai.api_key = "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"

class GPT3App(QWidget):
    def __init__(self):
        super().__init__()

        self.input_text = QLineEdit(self)
        self.input_text.returnPressed.connect(self.get_response)
        self.output_text = QLabel(self)
        self.output_text.setWordWrap(True)
        self.get_response_button = QPushButton("Get Response", self)
        self.get_response_button.clicked.connect(self.get_response)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("User Input:"))
        layout.addWidget(self.input_text)
        layout.addWidget(QLabel("GPT-3 Response:"))
        layout.addWidget(self.output_text)
        layout.addWidget(self.get_response_button)

        self.setWindowTitle("GPT-3 App")
        self.show()

    def get_response(self):
        user_input = self.input_text.text()
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            temperature=1,
            max_tokens=4000
        )
        self.output_text.setText(response["choices"][0]["text"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gpt3_app = GPT3App()
    sys.exit(app.exec_())
