from PySide2 import QtCore, QtGui, QtWidgets
import sys
from test import Ui_MainWindow
import json
from math import *
 
#Create application
app = QtWidgets.QApplication(sys.argv)
#Create form and init UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
#Hook logic

def RJ():
    with open('case.tsp', 'r', encoding='utf-8') as fh: 
        dat = json.load(fh)
    ui.lineEdit_pw1.setText(str(dat['PW']['Inner diameter NKT']))
    ui.lineEdit_pw2.setText(str(dat['PW']['External diameter NKT']))
    ui.lineEdit_pw3.setText(str(dat['PW']['Thermal conductivity NKT']))
    ui.lineEdit_pw4.setText(str(dat['PW']['Inner diameter K']))
    ui.lineEdit_pw5.setText(str(dat['PW']['External diameter K']))
    ui.lineEdit_pw6.setText(str(dat['PW']['Thermal conductivity K']))
    ui.lineEdit_pw7.setText(str(dat['PW']['Diameter well']))
    ui.lineEdit_pw8.setText(str(dat['PW']['External cement']))
    ui.lineEdit_pw9.setText(str(dat['PW']['Depth NKT']))
    
    ui.lineEdit_prj1.setText(str(dat['PRJ']['Surface temperature']))
    ui.lineEdit_prj2.setText(str(dat['PRJ']['Specific heat']))
    ui.lineEdit_prj3.setText(str(dat['PRJ']['Density']))
    ui.lineEdit_prj4.setText(str(dat['PRJ']['Thermal conductivity']))
    ui.lineEdit_prj5.setText(str(dat['PRJ']['Dynamic viscosity']))
    ui.lineEdit_prj6.setText(str(dat['PRJ']['Volumetric flow rate']))
    
    ui.lineEdit_pp1.setText(str(dat['PP']['Temperature of the neutral layer']))
    ui.lineEdit_pp2.setText(str(dat['PP']['Thermal conductivity formation']))
    ui.lineEdit_pp3.setText(str(dat['PP']['Specific heat formation']))
    ui.lineEdit_pp4.setText(str(dat['PP']['Density formation']))
    ui.lineEdit_pp5.setText(str(dat['PP']['Geothermal gradient']))
    
ui.pushButton.clicked.connect(RJ)


def WJ():
    data = {
    "PW": {
		"Inner diameter NKT":ui.lineEdit_pw1.text(),
		"External diameter NKT":ui.lineEdit_pw2.text(),
		"Thermal conductivity NKT":ui.lineEdit_pw3.text(),
        "Inner diameter K":ui.lineEdit_pw4.text(),
        "External diameter K": ui.lineEdit_pw5.text(),
        "Thermal conductivity K":ui.lineEdit_pw6.text(),
        "Diameter well":ui.lineEdit_pw7.text(),
        "External cement":ui.lineEdit_pw8.text(),
        "Depth NKT":ui.lineEdit_pw9.text(),
        },
    "PRJ":{
        "Surface temperature":ui.lineEdit_prj1.text(),
		"Specific heat":ui.lineEdit_prj2.text(),
		"Density":ui.lineEdit_prj3.text(),
        "Thermal conductivity":ui.lineEdit_prj4.text(),
        "Dynamic viscosity": ui.lineEdit_prj5.text(),
        "Volumetric flow rate":ui.lineEdit_prj6.text(),
        },
    "PP":{
        "Temperature of the neutral layer":ui.lineEdit_pp1.text(),
		"Thermal conductivity formation":ui.lineEdit_pp2.text(),
		"Specific heat formation":ui.lineEdit_pp3.text(),
        "Density formation":ui.lineEdit_pp4.text(),
        "Geothermal gradient": ui.lineEdit_pp5.text(),
        }
    }
		
    with open("data_file.tsp", "w") as write_file:
        json.dump(data, write_file)
    
ui.pushButton_2.clicked.connect(WJ)

def gr():
    #import matplotlib.pyplot as plt
    #img = plt.imread('graf.jpg')
    ui.label_graf.setPicture(plt)
    
ui.pushButton_graf.clicked.connect(gr)  

#Run main loop
sys.exit(app.exec_()) 

