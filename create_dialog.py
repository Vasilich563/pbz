# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from enum import Enum


class Connection(Enum):
    CREATE_CLASS = 1
    CREATE_SUBCLASS = 2
    CREATE_INDIVIDUAL = 3
    CREATE_OBJECT_PROPERTY = 4
    CREATE_DATA_PROPERTY = 5
    PROVIDE_OBJECT_PROPERTY = 6
    PROVIDE_DATA_PROPERTY = 7
    REMOVE_OBJECT_PROPERTY_FROM_INDIVIDUAL = 8
    REMOVE_DATA_PROPERTY_FROM_INDIVIDUAL = 9


PARAM = {
    Connection.CREATE_CLASS: {
        "title": "Create new class",
        "edit1_text": "Name of new class",
        "edit2_enabled": False,
        "edit2_text": "",
        "edit3_enabled": False,
        "edit3_text": "",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.CREATE_SUBCLASS: {
        "title": "Create as subclass",
        "edit1_text": "Name of class",
        "edit2_enabled": True,
        "edit2_text": "Name of subclass (name of another class)",
        "edit3_enabled": False,
        "edit3_text": "",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.CREATE_INDIVIDUAL: {
        "title": "Create new individual",
        "edit1_text": "Name of class",
        "edit2_enabled": True,
        "edit2_text": "Name of individual",
        "edit3_enabled": False,
        "edit3_text": "",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.CREATE_OBJECT_PROPERTY: {
        "title": "Create new object property",
        "edit1_text": "Name of property",
        "edit2_enabled": True,
        "edit2_text": "Name of domain (name of class)",
        "edit3_enabled": True,
        "edit3_text": "Name of range (name of class)",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.CREATE_DATA_PROPERTY: {
        "title": "Create new data property",
        "edit1_text": "Name of property",
        "edit2_enabled": True,
        "edit2_text": "Name of domain (name of class)",
        "edit3_enabled": True,
        "edit3_text": "Name of range (name of data type)",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.PROVIDE_OBJECT_PROPERTY: {
        "title": "Provide new object property for individuals",
        "edit1_text": "Name of individual from domain",
        "edit2_enabled": True,
        "edit2_text": "Name of property",
        "edit3_enabled": True,
        "edit3_text": "Name of individual from range",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.PROVIDE_DATA_PROPERTY: {
        "title": "Provide new data property for individual",
        "edit1_text": "Name of individual from domain",
        "edit2_enabled": True,
        "edit2_text": "Name of property",
        "edit3_enabled": True,
        "edit3_text": "Data type from range",
        "edit4_enabled": True,
        "edit4_text": "Value"
    },
    Connection.REMOVE_OBJECT_PROPERTY_FROM_INDIVIDUAL: {
        "title": "Remove object property from individual",
        "edit1_text": "Name of individual",
        "edit2_enabled": True,
        "edit2_text": "Name of object property to remove",
        "edit3_enabled": False,
        "edit3_text": "",
        "edit4_enabled": False,
        "edit4_text": ""
    },
    Connection.REMOVE_DATA_PROPERTY_FROM_INDIVIDUAL: {
        "title": "Remove data property from individual",
        "edit1_text": "Name of individual",
        "edit2_enabled": True,
        "edit2_text": "Name of data property to remove",
        "edit3_enabled": False,
        "edit3_text": "",
        "edit4_enabled": False,
        "edit4_text": ""
    }

}


class CustomDialog(QtWidgets.QDialog):
    formDoneSignal = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)


class UiCreateDialog(object):
    def setupUi(self, Dialog: CustomDialog, connection: Connection):
        self.connection = connection

        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 310)
        Dialog.setMinimumSize(QtCore.QSize(0, 0))
        Dialog.setStyleSheet("background-color: rgb(232, 248, 255);")

        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEdit2.setClearButtonEnabled(True)
        self.lineEdit2.setObjectName("lineEdit2")
        self.lineEdit2.setStyleSheet("background-color: rgb(175, 226, 255);")
        self.lineEdit2.setEnabled(PARAM[self.connection]["edit2_enabled"])
        self.lineEdit2.setVisible(PARAM[self.connection]["edit2_enabled"])
        self.gridLayout.addWidget(self.lineEdit2, 3, 0, 1, 1)

        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setMinimumSize(QtCore.QSize(500, 20))
        self.label3.setObjectName("label3")
        self.label3.setEnabled(PARAM[self.connection]["edit3_enabled"])
        self.label3.setVisible(PARAM[self.connection]["edit3_enabled"])
        self.gridLayout.addWidget(self.label3, 4, 0, 1, 1)

        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEdit1.setClearButtonEnabled(True)
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit1.setStyleSheet("background-color: rgb(175, 226, 255);")
        self.gridLayout.addWidget(self.lineEdit1, 1, 0, 1, 1)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setStyleSheet("background-color: rgb(175, 226, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 0, 1, 1)

        self.lineEdit3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit3.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEdit3.setClearButtonEnabled(True)
        self.lineEdit3.setObjectName("lineEdit3")
        self.lineEdit3.setStyleSheet("background-color: rgb(175, 226, 255);")
        self.lineEdit3.setEnabled(PARAM[self.connection]["edit3_enabled"])
        self.lineEdit3.setVisible(PARAM[self.connection]["edit3_enabled"])
        self.gridLayout.addWidget(self.lineEdit3, 5, 0, 1, 1)

        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setMinimumSize(QtCore.QSize(500, 20))
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setMinimumSize(QtCore.QSize(500, 20))
        self.label2.setObjectName("label2")
        self.label2.setEnabled(PARAM[self.connection]["edit2_enabled"])
        self.label2.setVisible(PARAM[self.connection]["edit2_enabled"])
        self.gridLayout.addWidget(self.label2, 2, 0, 1, 1)

        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setMinimumSize(QtCore.QSize(500, 20))
        self.label4.setObjectName("label4")
        self.label4.setEnabled(PARAM[self.connection]["edit4_enabled"])
        self.label4.setVisible(PARAM[self.connection]["edit4_enabled"])
        self.gridLayout.addWidget(self.label4, 6, 0, 1, 1)

        self.lineEdit4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit4.setMinimumSize(QtCore.QSize(500, 30))
        self.lineEdit4.setClearButtonEnabled(True)
        self.lineEdit4.setObjectName("lineEdit4")
        self.lineEdit4.setStyleSheet("background-color: rgb(175, 226, 255);")
        self.lineEdit4.setEnabled(PARAM[self.connection]["edit4_enabled"])
        self.lineEdit4.setVisible(PARAM[self.connection]["edit4_enabled"])
        self.gridLayout.addWidget(self.lineEdit4, 7, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(lambda: self.make_form_dict(Dialog))  # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        self.connect_text_changed()
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)

        Dialog.resize(Dialog.minimumSize())

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def text_changed_handler(self):
        if not self.lineEdit1.text().strip():
            self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
            return
        if PARAM[self.connection]["edit2_enabled"] and not self.lineEdit2.text().strip():
            self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
            return
        if PARAM[self.connection]["edit3_enabled"] and not self.lineEdit3.text().strip():
            self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
            return
        if PARAM[self.connection]["edit4_enabled"] and not self.lineEdit4.text().strip():
            self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(False)
            return
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def connect_text_changed(self):
        self.lineEdit1.textChanged.connect(self.text_changed_handler)
        self.lineEdit2.textChanged.connect(self.text_changed_handler)
        self.lineEdit3.textChanged.connect(self.text_changed_handler)
        self.lineEdit4.textChanged.connect(self.text_changed_handler)

    def make_form_dict(self, Dialog):
        if self.connection == Connection.CREATE_CLASS:
            form_dict = {
                'classname': self.lineEdit1.text()
            }
        elif self.connection == Connection.CREATE_SUBCLASS:
            form_dict = {
                'classname': self.lineEdit1.text(),
                'parent': self.lineEdit2.text()
            }
        elif self.connection == Connection.CREATE_INDIVIDUAL:
            form_dict = {
                'instance_name': self.lineEdit2.text(),
                'instance_type': self.lineEdit1.text()
            }
        elif self.connection == Connection.CREATE_OBJECT_PROPERTY:
            form_dict = {
                'object_property': self.lineEdit1.text(),
                'domain_1': self.lineEdit2.text(),
                'domain_2': self.lineEdit3.text()
            }
        elif self.connection == Connection.CREATE_DATA_PROPERTY:
            form_dict = {
                'data_property': self.lineEdit1.text(),
                'domain': self.lineEdit2.text(),
                'xs_range': self.lineEdit3.text()
            }
        elif self.connection == Connection.PROVIDE_OBJECT_PROPERTY:
            form_dict = {
                'subject': self.lineEdit1.text(),
                'predicate': self.lineEdit2.text(),
                'object': self.lineEdit3.text()
            }
        elif self.connection == Connection.PROVIDE_DATA_PROPERTY:
            form_dict = {
                'subject': self.lineEdit1.text(),
                'predicate': self.lineEdit2.text(),
                'object': self.lineEdit4.text(),
                "data_type": self.lineEdit3.text()
            }
        elif self.connection == Connection.REMOVE_OBJECT_PROPERTY_FROM_INDIVIDUAL:
            form_dict = {
                'individual_name': self.lineEdit1.text(),
                'property_name': self.lineEdit2.text()
            }
        elif self.connection == Connection.REMOVE_DATA_PROPERTY_FROM_INDIVIDUAL:
            form_dict = {
                'individual_name': self.lineEdit1.text(),
                'property_name': self.lineEdit2.text()
            }

        Dialog.formDoneSignal.emit(form_dict)
        Dialog.accept()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", PARAM[self.connection]["title"]))
        self.lineEdit2.setPlaceholderText(
            _translate("Dialog", f"Input {PARAM[self.connection]["edit2_text"].lower()}...")
        )
        self.label3.setText(_translate("Dialog", PARAM[self.connection]["edit3_text"]))
        self.lineEdit1.setPlaceholderText(
            _translate("Dialog", f"Input {PARAM[self.connection]["edit1_text"].lower()}...")
        )
        self.lineEdit3.setPlaceholderText(
            _translate("Dialog", f"Input {PARAM[self.connection]["edit3_text"].lower()}...")
        )
        self.label1.setText(_translate("Dialog", PARAM[self.connection]["edit1_text"]))
        self.label2.setText(_translate("Dialog", PARAM[self.connection]["edit2_text"]))
        self.label4.setText(_translate("Dialog", PARAM[self.connection]["edit4_text"]))
        self.lineEdit4.setPlaceholderText(
            _translate("Dialog", f"Input {PARAM[self.connection]["edit4_text"].lower()}...")
        )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = CustomDialog()
    ui = UiCreateDialog()
    ui.setupUi(Dialog, Connection.PROVIDE_DATA_PROPERTY)
    Dialog.show()
    sys.exit(app.exec_())
