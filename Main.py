
import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets

"""
ZAPAS ZIFER NA POTOM
        '0':
            [
                " 00000 ",
                "0     0",
                "0     0",
                "0     0",
                "0     0",
                "0     0",
                " 00000 "
            ],
        '1':
            [
                "      1",
                "     11",
                "    1 1",
                "   1  1",
                "      1",
                "      1",
                "      1"
            ],
        '2':
            [
                "  22222",
                " 22   2",
                "     2 ",
                "    2  ",
                "  2   ",
                " 2    ",
                "2222222"
            ],
        '3':
            [
                "3333333",
                "      3",
                "      3",
                "3333333",
                "      3",
                "      3",
                "3333333"
            ],
        '4':
            [
                "4     4",
                "4     4",
                "4     4",
                "4444444",
                "      4",
                "      4",
                "      4"
            ],
        '5':
            [
                "5555555",
                "5      ",
                "5      ",
                "5555555",
                "      5",
                "      5",
                "5555555"
            ],
        '6':
            [
                "6666666",
                "6      ",
                "6      ",
                "6666666",
                "6     6",
                "6     6",
                "6666666"
            ],
        '7':
            [
                "7777777",
                "      7",
                "     7 ",
                "    7  ",
                "  7     ",
                " 7     ",
                "7       "
            ],
        '8':
            [
                "8888888",
                "8     8",
                "8     8",
                "8888888",
                "8     8",
                "8     8",
                "8888888"
            ],
        '9':
            [
                "9999999",
                "9     9",
                "9     9",
                "9999999",
                "      9",
                "      9",
                "9999999"
            ]
            """


letters = \
    {
        'a':
            [
                "   A   ",
                "  A A  ",
                " A   A ",
                "A     A",
                "AAAAAAA",
                "A     A",
                "A     A"
            ],
        'b':
            [
                "BBBBBB ",
                "B     B",
                "B     B",
                "BBBBBB ",
                "B     B",
                "B     B",
                "BBBBBB "
            ],
        'c':
            [
                " CCCCC ",
                "C     C",
                "C      ",
                "C      ",
                "C      ",
                "C     C",
                " CCCCC "
            ],
        'd':
            [
                "DDDDDD ",
                "D     D",
                "D     D",
                "D     D",
                "D     D",
                "D     D",
                "DDDDDD "
            ],
        'e':
            [
                "EEEEEEE",
                "E      ",
                "E      ",
                "EEEEEEE",
                "E      ",
                "E      ",
                "EEEEEEE"
            ],
        'f':
            [
                "FFFFFFF",
                "F      ",
                "F      ",
                "FFFF   ",
                "F      ",
                "F      ",
                "F      "
            ],
        'g':
            [
                " GGGGG ",
                "G     G",
                "G      ",
                "G      ",
                "G  GGGG",
                "G     G",
                " GGGGGG"
            ],
        'h':
            [
                "H     H",
                "H     H",
                "H     H",
                "HHHHHHH",
                "H     H",
                "H     H",
                "H     H"
            ],
        'i':
            [
                "IIIIIII",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "   I   ",
                "IIIIIII"
            ],
        'j':
            [
                "JJJJJJJ",
                "      J",
                "      J",
                "      J",
                "      J",
                "J     J",
                " JJJJJ "
            ],
        'k':
            [
                "K    KK",
                "K   K  ",
                "K  K   ",
                "KKK    ",
                "K  K   ",
                "K   K  ",
                "K    KK"
            ],
        'l':
            [
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "L      ",
                "LLLLLLL"
            ],
        'm':
            [
                "M     M",
                "MM   MM",
                "M M M M",
                "M  M  M",
                "M     M",
                "M     M",
                "M     M"
            ],
        'n':
            [
                "N     N",
                "NN    N",
                "N N   N",
                "N  N  N",
                "N   N N",
                "N    NN",
                "N     N"
            ],
        'o':
            [
                " OOOOO ",
                "O     O",
                "O     O",
                "O     O",
                "O     O",
                "O     O",
                " OOOOO "
            ],
        'p':
            [
                "PPPPPP ",
                "P     P",
                "P     P",
                "PPPPPP ",
                "P      ",
                "P      ",
                "P      "
            ],
        'q':
            [
                " QQQQQ ",
                "Q     Q",
                "Q     Q",
                "Q     Q",
                "Q   Q Q",
                "Q    QQ",
                " QQQQQQ"
            ],
        'r':
            [
                "RRRRRR ",
                "R     R",
                "R     R",
                "RRRRRR ",
                "R   R  ",
                "R    R ",
                "R     R"
            ],
        's':
            [
                " SSSSS ",
                "S     S",
                "S      ",
                " SSSSS ",
                "      S",
                "S     S",
                " SSSSS "
            ],
        't':
            [
                "TTTTTTT",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   ",
                "   T   "
            ],
        'u':
            [
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                "U     U",
                " UUUUU "
            ],
        'v':
            [
                "V     V",
                "V     V",
                "V     V",
                "V     V",
                " V   V ",
                "  V V  ",
                "   V   "
            ],
        'w':
            [
                "W     W",
                "W     W",
                "W     W",
                "W  W  W",
                "W W W W",
                "WW   WW",
                "W     W"
            ],
        'x':
            [
                "X     X",
                " X   X ",
                "  X X  ",
                "   X   ",
                "  X X  ",
                " X   X ",
                "X     X"
            ],
        'y':
            [
                "Y     Y",
                "Y     Y",
                " Y   Y ",
                "  Y Y  ",
                "   Y   ",
                "   Y   ",
                "   Y   "
            ],
        'z':
            [
                "ZZZZZZZ",
                "     Z ",
                "    Z  ",
                "   Z   ",
                "  Z    ",
                " Z     ",
                "ZZZZZZZ"
            ],
        ' ':
            [
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       ",
                "       "
            ]

    }

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setWindowTitle('Lazy_Bukovi')
        self.setFixedSize(800, 800)

        self.Trbuttun = QtWidgets.QPushButton('Translate', self)
        self.Trbuttun.setGeometry(610, 5, 150, 50)
        self.Trbuttun.clicked.connect(self.TrbuttunClicked)

        self.Output = QtWidgets.QTextEdit(self)
        self.Output.move(20, 60)
        self.Output.resize(740, 640)
        self.Output.setFont(QtGui.QFont("Courier", 9))

        self.Input = QtWidgets.QLineEdit(self)
        self.Input.setPlaceholderText("Paste your bukovi  here")
        self.Input.move(20, 5)
        self.Input.resize(580, 50)

        self.Save = QtWidgets.QPushButton('Save', self)
        self.Save.setGeometry(470, 720, 250, 70)
        self.Save.clicked.connect(self.saveClicked)

        self.Open = QtWidgets.QPushButton('Open', self)
        self.Open.setGeometry(70, 720, 250, 70)
        self.Open.clicked.connect(self.openClicked)


        self.show()

    def TrbuttunClicked(self):
        textContent = self.Input.text().lower()
        self.OutText = ""
        self.Output.setText("")
        CBukovi =math.ceil(len(self.Input.text())/12)
        B = 0
        try:
          for l in range(CBukovi):
                for j in range(7):
                    for [i] in textContent[12*B:12*(B+1)]:
                        self.OutText += letters[i][j] + " "
                    self.OutText += '\n'
                self.OutText += '\n'
                B+=1
        except TypeError:
            BtnAn = QtWidgets.QMessageBox.question(self, 'Error(OSIBKA)', "TYPE ERROR(TUPAIA OSIBKA)",
                                                         QtWidgets.QMessageBox.Ok)
        except LookupError:
            BtnAn = QtWidgets.QMessageBox.question(self, 'Error(OSIBKA)', "WRONG BUKOVA(PROSTO OSIBKA)",
                                                         QtWidgets.QMessageBox.Ok)
        self.Output.setText(self.OutText)

    def saveClicked(self):
        try:
            file = open('output.txt', 'w')
            file.write(self.OutText)
            file.close()
        except Exception:
            file.close()

    def openClicked(self):
        output = ""
        try:
            file = open('output.txt', 'r')
            for line in file.readlines():
                output += line
            self.Output.setText(output)
        except FileNotFoundError:
            BtnAn  = QtWidgets.QMessageBox.question(self, 'Error(OSIBKA)', "FILE \"output.txt\" NET. EGO SCIGANILY CIGANE AND UVEZLY V TABOR",
                                                         QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
sys.exit(app.exec_())