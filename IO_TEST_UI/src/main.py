#----------------------------------------------------------------
#   Custom Serial Com GUI, V0.1
#----------------------------------------------------------------
# Dj park, 2023.11
#----------------------------------------------------------------
import sys
from main_ui import Ui_MainWindow

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QFile, QThread

import time

#from myserial import *




class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # setting serial port instance
        self.serial_port = QSerialPort(self)
        
        # close btn init Disable
        self.ui.pushButton_close.setDisabled(True)
        
        # uart baudrate list
        #baudrate = ("9600", "38400", "115200", "921600")
        baudrate = ("115200", )
        self.ui.current_baudrate.addItems(baudrate)
        
        # uart comport list
        port_list = QSerialPortInfo().availablePorts()
        for port_index in port_list :
            self.ui.current_comport.addItem(port_index.portName()) 

        # event function link
        self.ui.pushButton_open.clicked.connect(self.open_port)
        self.ui.pushButton_close.clicked.connect(self.close_port)
        self.ui.send.clicked.connect(self.send_serial)
        self.ui.pushButton_clear.clicked.connect(self.rxclear)
        self.ui.pushButton_scan.clicked.connect(self.scan)
        #self.ui.rxline.textChanged.connect(self.receive_serial)
        # rx thread set
        self.rxThread = ReceiveSerial(self)
        #self.rxThread.daemon = True

    # my serial open methode
    def open_port(self) :
        port_name = self.ui.current_comport.currentText()
        baudrate = int(self.ui.current_baudrate.currentText())
        
        if False :
            self.serial_port.setPortName(port_name)
            self.serial_port.setBaudRate(baudrate, self.serial_port.Direction.AllDirections)
            self.serial_port.setFlowControl(self.serial_port.FlowControl.NoFlowControl)
            self.serial_port.setDataBits(self.serial_port.DataBits.Data8)
            self.serial_port.setParity(self.serial_port.Parity.NoParity)
            self.serial_port.setStopBits(self.serial_port.StopBits.OneStop)
        else :
            self.serial_port.setPortName(port_name)
            self.serial_port.setBaudRate(baudrate) #, QSerialPort.Direction.AllDirections)
            self.serial_port.setFlowControl(QSerialPort.FlowControl.NoFlowControl)
            self.serial_port.setDataBits(QSerialPort.DataBits.Data8)
            self.serial_port.setParity(QSerialPort.Parity.NoParity)
            self.serial_port.setStopBits(QSerialPort.StopBits.OneStop)
        #-------------------------------------------------------------
        # DBG Prin
        #-------------------------------------------------------------
        #if True :
        if False :
            print("port_name ", port_name)
            print("port_name ", baudrate)
            print("Flow ", self.serial_port.FlowControl.NoFlowControl)
        #-------------------------------------------------------------
        
        try :
            #if self.serial_port.open(self.serial_port.OpenModeFlag.ReadWrite) : 
            if not self.serial_port.isOpen() :
                self.serial_port.open(QSerialPort.OpenModeFlag.ReadWrite)
                #self.serial_port.Serial(port_name, baudrate)
                self.statusBar().showMessage(f"OPENED")
                self.ui.pushButton_open.setDisabled(True)
                self.ui.pushButton_close.setEnabled(True)
                
                # Serial Rx Thread Start
                self.rxThread.is_running = True
                self.rxThread.start()
            else :
                self.statusBar().showMessage(f"Failed to Open")
                self.ui.pushButton_open.setEnabled(True)
                self.ui.pushButton_close.setDisabled(True)
        except Exception as e :
            print("Port Open Error 발생", e)
    
    # my serial close methode
    def close_port(self) :
        if self.serial_port.isOpen() :
            self.serial_port.close()
            self.statusBar().showMessage("CLOSED")
            self.ui.pushButton_open.setEnabled(True)
            self.ui.pushButton_close.setDisabled(True)
            self.rxThread.is_running = False
            self.rxThread.quit()
        else :
            self.ui.pushButton_open.setDisabled(True)
            self.ui.pushButton_close.setEnabled(True)
    
    # serial tx
    def send_serial(self) :
        if self.serial_port.isOpen() :
            tx_data = self.ui.txline.text() # copy text_line of gui to tx_data variable for sending the serial string
            tx_data = tx_data + "\n"
            
            try :
                self.serial_port.write(tx_data.encode('ascii')) # send tx data to connected serial port
            except Exception as error :
                print(error)
            
            tx = "\nTX >> " + tx_data
            self.ui.rxline.append(tx)
            #self.ui.rxline.insertPlainText(tx)
            #self.ui.rxline.insertPlainText(str(tx, 'utf-8', 'replace')) # print tx string to rx text line edit
            #print(tx.encode('utf-8')) # print console to see the sent data

    #def receive_serial(self):
    #    # Serial Rx Thread Start
    #    self.rxThread.is_running = True
    #    self.rxThread.start()
    #    #self.ui.rxline.insertPlainText(str(rx_data, 'utf-8', 'replace'))

    # serial rx text all clear
    def rxclear(self) :
        self.ui.rxline.clear()
    
    # comport scan
    def scan(self) :    
        self.ui.current_comport.clear()
        port_list = QSerialPortInfo().availablePorts()
        for port_index in port_list:
            self.ui.current_comport.addItem(port_index.portName()) 
            


class ReceiveSerial(QThread) :
    #def __init__(self, parent=None) :
    def __init__(self, parent=None) :
        super(ReceiveSerial, self).__init__(parent)
        self.serial_monitor = parent
        self.is_running = False

    def __del__(self) :
        self.is_running = False
        self.rxThread.stop()
    
    # QThread for RX Serial Start... from xxx.start() method
    def run(self) :
        while self.is_running :
            if self.serial_monitor.serial_port.isReadable() :
                rx_data = self.serial_monitor.serial_port.readLine()
                if  rx_data :
                    self.serial_monitor.ui.rxline.insertPlainText(str(rx_data, 'utf-8', 'replace'))
                    #self.serial_monitor.ui.rxline.append(str(rx_data))
                    #print(str(rx_data).encode('utf-8'))
                                
            self.msleep(1)

    
    
    
    
 #----------------------
 # System Main Start...
 #----------------------
if __name__ == "__main__" :
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

