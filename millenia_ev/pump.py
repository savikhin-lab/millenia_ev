import sys
import click
from serial import Serial


class Pump:
    def __init__(self, port_name):
        self.ser = Serial(port_name,
                          timeout=5,
                          baudrate=115_200,)

    def turn_on(self):
        msg = b"ON\n"
        self.ser.write(msg)

    def turn_off(self):
        msg = b"OFF\n"
        self.ser.write(msg)

    def open_shutter(self):
        msg = b"SHT:1\n"
        self.ser.write(msg)

    def close_shutter(self):
        msg = b"SHT:0\n"
        self.ser.write(msg)

    def set_power(self, watts):
        msg = f"P:{watts}\n".encode("utf-8")
        self.ser.write(msg)

    def diode_is_on(self):
        msg = b"?D\n"
        self.ser.reset_input_buffer()
        self.ser.write(msg)
        resp = self.ser.read(2)
        if (resp != b"1\n") and (resp != b"0\n"):
            sys.exit(1)
        is_on = resp == b"1\n"
        return is_on

    def shutter_is_open(self):
        msg = b"?SHT\n"
        self.ser.reset_input_buffer()
        self.ser.write(msg)
        resp = self.ser.read(2)
        if (resp != b"1\n") and (resp != b"0\n"):
            sys.exit(1)
        is_open = resp == b"1\n"
        return is_open

    def current_power(self):
        msg = b"?P\n"
        self.ser.reset_input_buffer()
        self.ser.write(msg)
        resp = self.ser.read_until()
        resp_data = resp.decode().strip()
        try:
            power = float(resp_data)
        except ValueError:
            sys.exit(1)
        return power
