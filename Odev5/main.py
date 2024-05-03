import sqlite3
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QMessageBox, QFileDialog

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

    authLayout: QVBoxLayout = QVBoxLayout()
    authLayout.addWidget(usernameText)
    authLayout.addWidget(passwordText)
    authLayout.addWidget(loginButton)
    authLayout.addWidget(registerButton)
    authLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    authLayout.setContentsMargins(20, 20, 20, 20)
    authLayout.setSpacing(30)

    authWidget: QWidget = QWidget()
    authWidget.setLayout(authLayout)

    # Menu Widget
    comparisonButton: QPushButton = QPushButton("Karşılaştırma")
    comparisonButton.setFixedHeight(50)
    comparisonButton.setFont(font)

    operationsButton: QPushButton = QPushButton("İşlemler")
    operationsButton.setFixedHeight(50)
    operationsButton.setFont(font)

    logoutButton: QPushButton = QPushButton("Çıkış Yap")
    logoutButton.setFixedHeight(50)
    logoutButton.setFont(font)

    menuLayout: QVBoxLayout = QVBoxLayout()
    menuLayout.addWidget(comparisonButton)
    menuLayout.addWidget(operationsButton)
    menuLayout.addWidget(logoutButton)
    menuLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    menuLayout.setContentsMargins(20, 20, 20, 20)
    menuLayout.setSpacing(30)

    menuWidget: QWidget = QWidget()
    menuWidget.setLayout(menuLayout)

    # Comparison Widget
    jaccardSimilarityButton: QRadioButton = QRadioButton("Jaccard")
    jaccardSimilarityButton.setFont(font)
    jaccardSimilarityButton.setChecked(True)

    wagnerFischerButton: QRadioButton = QRadioButton("Wagner-Fischer")
    wagnerFischerButton.setFont(font)

    algorithmLayout: QHBoxLayout = QHBoxLayout()
    algorithmLayout.addWidget(jaccardSimilarityButton)
    algorithmLayout.addWidget(wagnerFischerButton)
    algorithmLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    file1PathText: QLineEdit = QLineEdit()
    file1PathText.setPlaceholderText("1. Metin Dosyası")
    file1PathText.setFixedHeight(50)
    file1PathText.setFont(font)

    file1PathDialogButton: QPushButton = QPushButton("Dosya Seç")
    file1PathDialogButton.setFont(font)

    file1Layout: QHBoxLayout = QHBoxLayout()
    file1Layout.addWidget(file1PathText)
    file1Layout.addWidget(file1PathDialogButton)
    file1Layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    file2PathText: QLineEdit = QLineEdit()
    file2PathText.setPlaceholderText("2. Metin Dosyası")
    file2PathText.setFixedHeight(50)
    file2PathText.setFont(font)

    file2PathDialogButton: QPushButton = QPushButton("Dosya Seç")
    file2PathDialogButton.setFont(font)

    file2Layout: QHBoxLayout = QHBoxLayout()
    file2Layout.addWidget(file2PathText)
    file2Layout.addWidget(file2PathDialogButton)
    file2Layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

    compareButton: QPushButton = QPushButton("Karşılaştır")
    compareButton.setFixedHeight(50)
    compareButton.setFont(font)

    comparisonGoBackButton: QPushButton = QPushButton("Geri Dön")
    comparisonGoBackButton.setFixedHeight(50)
    comparisonGoBackButton.setFont(font)

    comparisonLayout: QVBoxLayout = QVBoxLayout()
    comparisonLayout.addLayout(file1Layout)
    comparisonLayout.addLayout(file2Layout)
    comparisonLayout.addLayout(algorithmLayout)
    comparisonLayout.addWidget(compareButton)
    comparisonLayout.addWidget(comparisonGoBackButton)
    comparisonLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    comparisonLayout.setContentsMargins(20, 20, 20, 20)
    comparisonLayout.setSpacing(30)

    comparisonWidget: QWidget = QWidget()
    comparisonWidget.setFixedWidth(800)
    comparisonWidget.setFixedHeight(600)
    comparisonWidget.setLayout(comparisonLayout)

    # Operations Widget
    passwordOperationButton: QPushButton = QPushButton("Şifre Değiştirme")
    passwordOperationButton.setFixedHeight(50)
    passwordOperationButton.setFont(font)

    operationsGoBackButton: QPushButton = QPushButton("Geri Dön")
    operationsGoBackButton.setFixedHeight(50)
    operationsGoBackButton.setFont(font)

    operationsLayout: QVBoxLayout = QVBoxLayout()
    operationsLayout.addWidget(passwordOperationButton)
    operationsLayout.addWidget(operationsGoBackButton)
    operationsLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    operationsLayout.setContentsMargins(20, 20, 20, 20)
    operationsLayout.setSpacing(30)

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

    passwordChangeLayout: QVBoxLayout = QVBoxLayout()
    passwordChangeLayout.addWidget(newPasswordText)
    passwordChangeLayout.addWidget(confirmNewPasswordText)
    passwordChangeLayout.addWidget(changePasswordButton)
    passwordChangeLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    passwordChangeLayout.setContentsMargins(20, 20, 20, 20)
    passwordChangeLayout.setSpacing(30)

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
    def comparisonButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(comparisonWidget)

    def operationsButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(operationsWidget)

    def logoutButtonClicked() -> None:
        global username, password
        username = None
        password = None
        window.centralWidget().setParent(None)
        window.setCentralWidget(authWidget)

    comparisonButton.clicked.connect(comparisonButtonClicked)
    operationsButton.clicked.connect(operationsButtonClicked)
    logoutButton.clicked.connect(logoutButtonClicked)

    # Comparison Button Callbacks
    def filePathDialogButtonClicked(filePathText: QLineEdit) -> None:
        file1PathDialog: QFileDialog = QFileDialog()
        file1PathDialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file1PathDialog.setNameFilter("Text Files (*.txt)")
        file1PathDialog.setViewMode(QFileDialog.ViewMode.List)
        if file1PathDialog.exec() == QFileDialog.DialogCode.Accepted:
            filePathText.setText(file1PathDialog.selectedFiles()[0])

    def compareButtonClicked() -> None:
        try:
            with open(file1PathText.text()) as file1:
                file1Content: str = "".join(filter(str.isalnum, file1.read()))
            with open(file2PathText.text()) as file2:
                file2Content: str = "".join(filter(str.isalnum, file2.read()))
        except:
            QMessageBox.warning(window, "Hata", "Dosya okunurken bir hata oluştu", QMessageBox.StandardButton.Ok)
            return

        if jaccardSimilarityButton.isChecked():
            text1Set: set = set(file1Content)
            text2Set: set = set(file2Content)
            intersection: set = text1Set & text2Set
            union: set = text1Set | text2Set
            jaccardSimilarity: float = len(intersection) / len(union)
            QMessageBox.information(window, "Sonuç", f"Jaccard Benzerliği: {jaccardSimilarity}", QMessageBox.StandardButton.Ok)
        elif wagnerFischerButton.isChecked():
            m: int = len(file1Content)
            n: int = len(file2Content)
            currentRow: list[int] = [y for y in range(n + 1)]
            for i in range(1, n + 1):
                previousRow = currentRow
                currentRow = [i] + [0] * m
                for j in range(1, m + 1):
                    add = previousRow[j] + 1
                    delete = currentRow[j - 1] + 1
                    change = previousRow[j - 1] + (file1Content[i - 1] != file2Content[j - 1])
                    currentRow[j] = min(add, delete, change)
            QMessageBox.information(window, "Sonuç", f"Wagner-Fischer (Levenshtein): {currentRow[m]}", QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(window, "Hata", "Algoritma seçilmedi", QMessageBox.StandardButton.Ok)

    def comparisonGoBackButtonClicked() -> None:
        window.centralWidget().setParent(None)
        window.setCentralWidget(menuWidget)

    file1PathDialogButton.clicked.connect(lambda: filePathDialogButtonClicked(file1PathText))
    file2PathDialogButton.clicked.connect(lambda: filePathDialogButtonClicked(file2PathText))
    compareButton.clicked.connect(compareButtonClicked)
    comparisonGoBackButton.clicked.connect(comparisonGoBackButtonClicked)

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
