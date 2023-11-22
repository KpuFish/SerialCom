"""
from PySide6.QtSerialPort import * 
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from PySide6.QtCore import QFile
from main_ui import Ui_MainWindow

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




