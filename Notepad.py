#QTPY

#참조
#https://www.youtube.com/watch?v=Ss7dDDS-DhU&list=PLnIaYcDMsScwsKo1rQ18cLHvBdjou-kb5&ab_channel=%EC%9E%AC%EC%A6%90%EB%B3%B4%ED%94%84
#https://wikidocs.net/35478
#https://appia.tistory.com/298


import sys


from PyQt5.QtWidgets import* #QApplication, QMainWindow, QAction, qApp, QFileDialog, QTextEdit, QHBoxLayout, QVBoxLayout , QMessageBox
from PyQt5.QtGui import*
from PyQt5 import uic

class findWindow(QDialog):
    def __init__(self, parent):
        super(findWindow, self).__init__(parent)
        uic.loadUi("C:\\Users\\wlsrn\\OneDrive\\바탕 화면\\Coding_Test-master\\PyQT\\actionfind.ui", self)
        self.show()

class QtGUI(QMainWindow):


    def __init__(self):
        super().__init__()
        self.resize(800, 800)
        self.setWindowTitle("Notepad")
        menubar = self.menuBar()

        self.opened = False
        self.opened_file_path = '제목 없음'

        Filemenu = menubar.addMenu("파일")
        Filemenu1 = menubar.addMenu("편집")
        Filemenu2 = menubar.addMenu("서식")
        Filemenu3 = menubar.addMenu("기타")


        loadfile = QAction('불러오기', self)
        savefile = QAction('저장', self)
        saveasfile = QAction('다른이름으로저장', self)
        exit = QAction('종료', self)
        #========================================

        actionundo = QAction('실행 취소', self)
        cut = QAction('잘라내기 ', self)
        copy = QAction('복사', self)
        paste = QAction('붙여넣기', self)
        selectall = QAction('모두선택', self)
        #==========================================

        find = QAction('찾기', self)


        photo = QAction('사진 불러오기', self)


        loadfile.triggered.connect(self.add_open)
        savefile.triggered.connect(self.add_save)
        saveasfile.triggered.connect(self.add_save)
        exit.triggered.connect(self.close)
        #===========================================

        actionundo.triggered.connect(self.add_actionundo)
        cut.triggered.connect(self.add_cut)
        paste.triggered.connect(self.add_paste)
        copy.triggered.connect(self.add_copy)
        selectall.triggered.connect(self.add_selectall)
        #=============================================
        find.triggered.connect(self.add_find)



        photo.triggered.connect(self.add_photo)

        Filemenu.addAction(loadfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(saveasfile)
        Filemenu.addAction(exit)
        #======================================

        Filemenu1.addAction(actionundo)
        Filemenu1.addAction(cut)
        Filemenu1.addAction(copy)
        Filemenu1.addAction(paste)
        Filemenu1.addAction(selectall)
        #======================================
        Filemenu2.addAction(find)


        Filemenu3.addAction(photo)

        self.text1 = QTextEdit(self)
        self.text1.setAcceptRichText(True)
        self.setCentralWidget(self.text1)
        self.show()

    def save_file(self, File):  #저장 기능
        textcontent = self.text1.toPlainText()
        f = open(File, 'w')
        f.write(textcontent)

        self.opened = True
        self.opened_file_path = File

    def load_file(self, File): #로드 기능
        f = open(File, encoding='UTF8')
        textcontenct = f.read()
        self.text1.setText(textcontenct)

        self.opened = True
        self.opened_file_path = File

    def add_open(self): # 불러오기
        File = QFileDialog.getOpenFileName(self)
        if File[0]:
            self.load_file(File[0])

    def add_save(self): #저장
        if self.opened:
            self.save_file(self.opened_file_path)
        else:
            File = QFileDialog.getSaveFileName(self, '저장', './')
            if File[0]:
                self.save_file(File[0])

    def add_assave(self): #다른 이름으로 저장
        File = QFileDialog.getSaveFileName(self, '저장', './')
        if File[0]:
            self.save_file(File[0])

    def save_chaged_data(self): # 닫을 때 저장 여부
        msgBox = QMessageBox()
        msgBox.setText("변경 내용을 {}에 저장하시겠습니까?".format(self.opened_file_path))
        msgBox.addButton('저장', QMessageBox.YesRole)
        msgBox.addButton('저장 안 함',QMessageBox.NoRole)
        msgBox.addButton('취소',QMessageBox.RejectRole)
        ret = msgBox.exec_()
        if ret == 0:
            self.add_save()
        else:
            return ret





    def closeEvent(self, event): #종료 이벤트
        ret = self.save_chaged_data()
        if ret == 2:
            event.ignore()

        print("close test")


    def add_actionundo(self):
        self.text1.undo()

    def add_cut(self):
        self.text1.cut()

    def add_paste(self):
        self.text1.paste()

    def add_copy(self):
        self.text1.copy()

    def add_selectall(self):
        self.text1.selectAll()

    def add_photo(self):
        #self.sid = QImage("C:\\Users\\wlsrn\\OneDrive\\바탕 화면\\Coding_Test-master\\PyQT\\TFT1.png")
        File, _ = QFileDialog.getOpenFileName(self, "불러올 이미지를 선택하세요.", "", "All Files (*);;Python Files (*.py)")

        if File:
            print(File)
            self.sid = QImage(File).scaled(200, 200)
            print(self.sid)

        painter = QPainter()
        painter.drawImage(200, 200, self.sid)
        self.show()

    def add_find(self):
       findWindow(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtGUI()
    app.exec_()
