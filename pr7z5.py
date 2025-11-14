from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, message):
        pass
class EmailService(NotificationService):
    def send(self, message):
        print(f"Email: {message}")
class SMSService(NotificationService):
    def send(self, message):
        print(f"SMS: {message}")
class UserNotifier:
    def __init__(self, service: NotificationService):
        self.service = service
    def notify(self, message):
        self.service.send(message)
email_service = EmailService()
sms_service = SMSService()
notifier1 = UserNotifier(email_service)
notifier1.notify("Привіт по Email")
notifier2 = UserNotifier(sms_service)
notifier2.notify("Привіт по SMS")
