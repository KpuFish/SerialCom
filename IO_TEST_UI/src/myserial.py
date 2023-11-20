"""
from PySide6.QtSerialPort import * 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QFile
from main_ui import Ui_MainWindow



"""
 # 시리얼포트 상수 값
    BAUDRATES = (
        QSerialPort.BaudRate.Baud1200,
        QSerialPort.BaudRate.Baud2400,
        QSerialPort.BaudRate.Baud4800,
        QSerialPort.BaudRate.Baud9600,
        QSerialPort.BaudRate.Baud19200,
        QSerialPort.BaudRate.Baud38400,
        QSerialPort.BaudRate.Baud57600,
        QSerialPort.BaudRate.Baud115200,
    )

    DATABITS = (
        QSerialPort.DataBits.Data5,
        QSerialPort.DataBits.Data6,
        QSerialPort.DataBits.Data7,
        QSerialPort.DataBits.Data8,
    )

    FLOWCONTROL = (
        QSerialPort.FlowControl.NoFlowControl,
        QSerialPort.FlowControl.HardwareControl,
        QSerialPort.FlowControl.SoftwareControl,
    )

    PARITY = (
        QSerialPort.Parity.NoParity,
        QSerialPort.Parity.EvenParity,
        QSerialPort.Parity.OddParity,
        QSerialPort.Parity.SpaceParity,
        QSerialPort.Parity.MarkParity,
    )

    STOPBITS = (
        QSerialPort.StopBits.OneStop,
        QSerialPort.StopBits.OneAndHalfStop,
        QSerialPort.StopBits.TwoStop,

    )
"""


#class MySerialPort(Ui_MainWindow) :
class MySerialPort(Ui_MainWindow) :
    def __init__(self, parent = None) :
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        super(MySerialPort, self).__init__(parent)
        self.serial_port = QSerialPort(self)
        
        # close btn disable
        self.ui.pushButton_close.setDisabled(True)
        
        # uart baudrate list
        baudrate = ["9600", "38400", "115200", "921600"]
        self.ui.current_baudrate.addItems(baudrate)
        
        # uart comport list
        port_list = QSerialPortInfo().availablePorts()
        for port_index in port_list:
            self.ui.current_comport.addItem(port_index.portName()) 
 
        self.ui.pushButton_open.clicked.connect(self.open_port)
        self.ui.pushButton_close.clicked.connect(self.close_port)
    
    def open_port(self) :
        port_name = self.ui.current_comport.currentText()
        self.serial_port.setPortName(port_name)
        
        #if self.serial_port.isOpen() : 
        if self.serial_port.open(QSerialPort.ReadWrite) :
            self.statusBar().showMessage(f"OPENED")
            self.ui.pushButton_open.setDisabled(True)
            self.ui.pushButton_close.setEnabled(True)
        else :
            self.statusBar().showMessage(f"Failed to Open")
            self.ui.pushButton_open.setEnabled(True)
            self.ui.pushButton_close.setDisabled(True)
            
    def close_port(self) :
        if self.serial_port.isOpen() :
            self.serial_port.close()
            self.statusBar().showMessage("CLOSED")
            self.ui.pushButton_open.setEnabled(True)
            self.ui.pushButton_close.setDisabled(True)
        else :
            self.ui.pushButton_open.setDisabled(True)
            self.ui.pushButton_close.setEnabled(True)

"""