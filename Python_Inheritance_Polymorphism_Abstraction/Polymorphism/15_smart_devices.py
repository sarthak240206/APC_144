class SmartDevice:
    def turn_on(self):
        print("Device turned on.")

    def turn_off(self):
        print("Device turned off.")


class Light(SmartDevice):
    def turn_on(self):
        print("Light is on.")

    def turn_off(self):
        print("Light is off.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is spinning.")

    def turn_off(self):
        print("Fan stopped.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is cooling.")

    def turn_off(self):
        print("AC is off.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is displaying a picture.")

    def turn_off(self):
        print("TV is off.")


for device in [Light(), Fan(), AC(), TV()]:
    device.turn_on()
    device.turn_off()
