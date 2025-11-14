from abc import ABC, abstractmethod

class NetworkPrinter(ABC):
    @abstractmethod
    def print_doc(self, doc):
        pass

    @abstractmethod
    def scan_doc(self, doc):
        pass
    @abstractmethod
    def copy_doc(self, doc):
        pass
class Printer(NetworkPrinter):
    def print_doc(self, doc):
        print(f"Друк: {doc}")
    def scan_doc(self, doc):
        pass
    def copy_doc(self, doc):
        pass
class Scanner(NetworkPrinter):
    def print_doc(self, doc):
        pass
    def scan_doc(self, doc):
        print(f"Сканування: {doc}")
    def copy_doc(self, doc):
        pass
printer = Printer()
scanner = Scanner()
printer.print_doc("Документ 1")
scanner.scan_doc("Документ 2")
