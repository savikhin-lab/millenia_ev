import os
import sys
import click
from .pump import Pump


@click.group()
def cli():
    pass


@click.command()
def on():
    """Begin emission without opening or closing the shutter.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    laser.turn_on()
    return


@click.command()
def off():
    """Stop emission without opening or closing the shutter.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    laser.turn_off()
    return


@click.command()
@click.option("-s", "setpower", type=click.FLOAT, help="Set the power to a value in the range [0, 5]W.")
def power(setpower):
    """Report or set the power.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    if setpower is None:
        current_power = laser.current_power()
        print(f"{current_power:.2f}W")
    else:
        laser.set_power(setpower)
    return


@click.command()
@click.option("-s", "command", type=click.Choice(["open", "close"]), help="Open or close the shutter.")
def shutter(command):
    """Report or set the shutter state.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    if command is None:
        if laser.shutter_is_open():
            print("OPEN")
        else:
            print("CLOSED")
    else:
        if command == "open":
            laser.open_shutter()
        else:
            laser.close_shutter()
    return


@click.command()
def start():
    """Begin emission with the shutter open.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    laser.turn_on()
    laser.open_shutter()
    return


@click.command()
def stop():
    """Stop emission and close the shutter.
    """
    try:
        port = os.environ["PUMPPORT"]
    except KeyError:
        port_not_found()
        sys.exit(-1)
    laser = Pump(port)
    laser.close_shutter()
    laser.turn_off()
    return


def port_not_found():
    print("Port name not found. Please set the PUMPPORT environment variable.")


cli.add_command(on)
cli.add_command(off)
cli.add_command(power)
cli.add_command(shutter)
cli.add_command(start)
cli.add_command(stop)
