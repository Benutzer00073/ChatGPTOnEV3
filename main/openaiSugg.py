import sys
import os

import openai
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QWidget, QGridLayout)

openai.api_key = open(os.getcwd() + '/api_key.txt', 'r').readline().rstrip()


class GPT3App(QWidget):
    def __init__(self):
        super().__init__()

        self.input_text = QLineEdit(self)
        self.input_text.returnPressed.connect(self.get_response)
        self.output_text = QLabel(self)
        self.output_text.setWordWrap(True)
        self.get_response_button = QPushButton("Get Response", self)
        self.get_response_button.clicked.connect(self.get_response)

        vbox = QVBoxLayout(self)
        vbox.addWidget(QLabel("User Input:"))
        vbox.addWidget(self.input_text)
        vbox.addWidget(QLabel("GPT-3 Response:"))
        vbox.addWidget(self.output_text)
        vbox.addWidget(self.get_response_button)

        self.setLayout(vbox)

        self.setWindowTitle("GPT-3 App")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def get_response(self):
        user_input = self.input_text.text()
        response = openai.Completion.create(
            api_key=openai.api_key,
            engine="text-davinci-003",
            prompt=user_input,
            temperature=1,
            max_tokens=4000
        )
        self.output_text.setText(response["choices"][0]["text"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gpt3_app = GPT3App()
    sys.exit(app.exec_())
