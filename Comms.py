import serial

class Comms:
    def __init__(self, COM):
        self.esp = serial.Serial(COM)


    def SendData(self, data):
        if self.esp.writable():
            data = str(data)
            self.esp.write(data.encode())
            print("Wrote: ", data)

    def ReadData(self):
        if self.esp.readable():
            return self.esp.read_all()
