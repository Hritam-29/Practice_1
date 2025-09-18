'''
#SRP

class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item['price'] for item in self.items)


class InvoicePrinter:
    def print_invoice(self, invoice):
        for item in invoice.items:
            print(f"{item['name']}: Rs{item['price']}")
        print(f"Total: Rs{invoice.calculate_total()}")


# Usage
items = [{'name': 'Book', 'price': 12}, {'name': 'Pen', 'price': 2}]


invoice = Invoice(items)
printer = InvoicePrinter()
printer.print_invoice(invoice)'''

#OCP
'''
from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total


class TenPercentDiscount(DiscountStrategy):
    def apply_discount(self, total):
        return total * 0.9


class Checkout:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def calculate_total(self, items):
        total = sum(item['price'] for item in items)
        return self.discount_strategy.apply_discount(total)


# Usage
items = [{'price': 100}, {'price': 50}]
checkout = Checkout(TenPercentDiscount())
print(checkout.calculate_total(items))  # Output: 135.0

#LSP

class Bird:
    def fly(self):
        print("Flying")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")


class Eagle(Bird):
    def fly(self):
        print("Eagle soaring")


# Usage
def make_bird_fly(bird: Bird):
    bird.fly()


make_bird_fly(Sparrow())
make_bird_fly(Eagle())


#ISP

from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        pass


class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self, document):
        print(f"Scanning: {document}")


class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


# Usage
printer = SimplePrinter()
printer.print_document("Report.pdf")'''

#DIP

from abc import ABC, abstractmethod

class IMessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailSender(IMessageSender):
    def send(self, message):
        print(f"Sending Email: {message}")


class Notification:
    def __init__(self, sender: IMessageSender):
        self.sender = sender

    def alert(self, message):
        self.sender.send(message)


# Usage
email_sender = EmailSender()
notification = Notification(email_sender)
notification.alert("Your order has been shipped.")
