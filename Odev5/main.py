import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QFormLayout, QPushButton, QMessageBox

if __name__ == "__main__":
    # State
    username: str = None
    password: str = None

    # App
    app: QApplication = QApplication([])

    connection: sqlite3.Connection = sqlite3.connect("database.db")
    cursor: sqlite3.Cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Users (Username TEXT, Password TEXT)")
    connection.commit()

    # Resources
    font: QFont = QFont("Arial", 30)

    # Auth Widget
    usernameText: QLineEdit = QLineEdit()
    usernameText.setPlaceholderText("Kullanıcı Adı")
    usernameText.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    usernameText.setFixedHeight(50)
    usernameText.setFont(font)

    passwordText: QLineEdit = QLineEdit()
    passwordText.setPlaceholderText("Şifre")
    passwordText.setEchoMode(QLineEdit.EchoMode.Password)
    passwordText.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    passwordText.setFixedHeight(50)
    passwordText.setFont(font)

    loginButton: QPushButton = QPushButton("Giriş Yap")
    loginButton.setFixedHeight(50)
    loginButton.setFont(font)

    registerButton: QPushButton = QPushButton("Kayıt Ol")
    registerButton.setFixedHeight(50)
    registerButton.setFont(font)

    authLayout: QFormLayout = QFormLayout()
    authLayout.addRow(usernameText)
    authLayout.addRow(passwordText)
    authLayout.addRow(loginButton)
    authLayout.addRow(registerButton)
    authLayout.setContentsMargins(20, 200, 20, 200)
    authLayout.setSpacing(40)

    authWidget: QWidget = QWidget()
    authWidget.setLayout(authLayout)

    # Menu Widget
    compareButton: QPushButton = QPushButton("Karşılaştır")
    compareButton.setFixedHeight(50)
    compareButton.setFont(font)

    operationsButton: QPushButton = QPushButton("İşlemler")
    operationsButton.setFixedHeight(50)
    operationsButton.setFont(font)

    logoutButton: QPushButton = QPushButton("Çıkış Yap")
    logoutButton.setFixedHeight(50)
    logoutButton.setFont(font)

    menuLayout: QFormLayout = QFormLayout()
    menuLayout.addRow(compareButton)
    menuLayout.addRow(operationsButton)
    menuLayout.addRow(logoutButton)
    menuLayout.setContentsMargins(20, 200, 20, 200)
    menuLayout.setSpacing(40)

    menuWidget: QWidget = QWidget()
    menuWidget.setLayout(menuLayout)

    # Operations Widget
    passwordOperationButton: QPushButton = QPushButton("Şifre Değiştirme")
    passwordOperationButton.setFixedHeight(50)
    passwordOperationButton.setFont(font)

    operationsGoBackButton: QPushButton = QPushButton("Geri Dön")
    operationsGoBackButton.setFixedHeight(50)
    operationsGoBackButton.setFont(font)

    operationsLayout: QFormLayout = QFormLayout()
    operationsLayout.addRow(passwordOperationButton)
    operationsLayout.addRow(operationsGoBackButton)
    operationsLayout.setContentsMargins(20, 200, 20, 200)
    operationsLayout.setSpacing(40)

    operationsWidget: QWidget = QWidget()
    operationsWidget.setLayout(operationsLayout)

    # Password Change Widget
    newPasswordText: QLineEdit = QLineEdit()
    newPasswordText.setPlaceholderText("Yeni Şifre")
    newPasswordText.setEchoMode(QLineEdit.EchoMode.Password)
    newPasswordText.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    newPasswordText.setFixedHeight(50)
    newPasswordText.setFont(font)

    confirmNewPasswordText: QLineEdit = QLineEdit()
    confirmNewPasswordText.setPlaceholderText("Yeni Şifre Tekrar")
    confirmNewPasswordText.setEchoMode(QLineEdit.EchoMode.Password)
    confirmNewPasswordText.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    confirmNewPasswordText.setFixedHeight(50)
    confirmNewPasswordText.setFont(font)

    changePasswordButton: QPushButton = QPushButton("Şifre Değiştir")
    changePasswordButton.setFixedHeight(50)
    changePasswordButton.setFont(font)

    passwordChangeLayout: QFormLayout = QFormLayout()
    passwordChangeLayout.addRow(newPasswordText)
    passwordChangeLayout.addRow(confirmNewPasswordText)
    passwordChangeLayout.addRow(changePasswordButton)
    passwordChangeLayout.setContentsMargins(20, 200, 20, 200)
    passwordChangeLayout.setSpacing(40)

    passwordChangeWidget: QWidget = QWidget()
    passwordChangeWidget.setLayout(passwordChangeLayout)

    # Window
    window: QMainWindow = QMainWindow()
    window.setWindowTitle("Python Odev 5")
    window.setFixedWidth(800)
    window.setFixedHeight(600)

    window.setCentralWidget(authWidget)

    # Auth Button Callbacks
    def loginButtonClicked() -> None:
        cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (usernameText.text(), passwordText.text()))
        if (user := cursor.fetchone()) is not None and usernameText.text() == user[0] and passwordText.text() == user[1]:
            global username, password
            username = usernameText.text()
            password = passwordText.text()
            usernameText.clear()
            passwordText.clear()
            window.centralWidget().setParent(None)
            window.setCentralWidget(menuWidget)
        else:
            QMessageBox.warning(window, "Hata", "Kullanıcı adı veya şifre hatalı", QMessageBox.StandardButton.Ok)

    def registerButtonClicked() -> None:
        cursor.execute("SELECT * FROM Users WHERE Username = ?", (usernameText.text(),))
        if cursor.fetchone() is not None:
            QMessageBox.warning(window, "Hata", "Kullanıcı adı zaten kayıtlı", QMessageBox.StandardButton.Ok)
            return
        cursor.execute("INSERT INTO Users VALUES (?, ?)", (usernameText.text(), passwordText.text()))
        connection.commit()
        QMessageBox.information(window, "Başarılı", "Kayıt Başarılı", QMessageBox.StandardButton.Ok)
        usernameText.clear()
        passwordText.clear()

    loginButton.clicked.connect(loginButtonClicked)
    registerButton.clicked.connect(registerButtonClicked)

    # Menu Button Callbacks
    def compareButtonClicked() -> None:
        pass

    def operationsButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(operationsWidget)

    def logoutButtonClicked() -> None:
        global username, password
        username = None
        password = None
        window.centralWidget().setParent(None)
        window.setCentralWidget(authWidget)

    compareButton.clicked.connect(compareButtonClicked)
    operationsButton.clicked.connect(operationsButtonClicked)
    logoutButton.clicked.connect(logoutButtonClicked)

    # Operations Button Callbacks
    def passwordOperationButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(passwordChangeWidget)

    def operationsGoBackButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(menuWidget)

    passwordOperationButton.clicked.connect(passwordOperationButtonClicked)
    operationsGoBackButton.clicked.connect(operationsGoBackButtonClicked)

    # Password Change Button Callbacks
    def changePasswordButtonClicked() -> None:
        global password
        if newPasswordText.text() != confirmNewPasswordText.text():
            QMessageBox.warning(window, "Hata", "Şifreler eşleşmiyor", QMessageBox.StandardButton.Ok)
        elif newPasswordText.text() == password:
            QMessageBox.warning(window, "Hata", "Yeni şifre eskisiyle aynı olamaz", QMessageBox.StandardButton.Ok)
        else:
            password = newPasswordText.text()
            cursor.execute("UPDATE Users SET Password = ? WHERE Username = ?", (password, username))
            connection.commit()
            QMessageBox.information(window, "Başarılı", "Şifre değiştirme başarılı", QMessageBox.StandardButton.Ok)
            newPasswordText.clear()
            confirmNewPasswordText.clear()
            window.centralWidget().setParent(None)
            window.setCentralWidget(operationsWidget)

    changePasswordButton.clicked.connect(changePasswordButtonClicked)

    # Run
    window.show()
    code = app.exec()
    connection.close()
    exit(code)
