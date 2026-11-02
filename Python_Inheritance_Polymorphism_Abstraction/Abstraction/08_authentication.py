from abc import ABC, abstractmethod


class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def __init__(self, saved_password, entered_password):
        self.saved_password = saved_password
        self.entered_password = entered_password

    def authenticate(self):
        return self.saved_password == self.entered_password


class OTPAuthentication(Authentication):
    def __init__(self, saved_otp, entered_otp):
        self.saved_otp = str(saved_otp)
        self.entered_otp = str(entered_otp)

    def authenticate(self):
        return self.saved_otp == self.entered_otp


class BiometricAuthentication(Authentication):
    def __init__(self, biometric_matched):
        self.biometric_matched = biometric_matched

    def authenticate(self):
        return self.biometric_matched


methods = [
    PasswordAuthentication("pass123", "pass123"),
    OTPAuthentication(123456, 123456),
    BiometricAuthentication(True)
]

for method in methods:
    print(method.__class__.__name__, "Success" if method.authenticate() else "Failed")
