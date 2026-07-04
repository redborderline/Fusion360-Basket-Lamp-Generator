from .basketLamp import entry as basketLamp

commands = [
    basketLamp
]

def start():
    for command in commands:
        command.start()

def stop():
    for command in commands:
        command.stop()