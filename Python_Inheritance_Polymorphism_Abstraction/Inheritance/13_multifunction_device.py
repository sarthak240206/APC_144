class Printer:
    def print_document(self, document):
        print("Printing document:", document)


class Scanner:
    def scan_document(self, document):
        print("Scanning document:", document)


class MultifunctionDevice(Printer, Scanner):
    pass


device = MultifunctionDevice()
device.print_document("Report.pdf")
device.scan_document("ID_Card.png")
