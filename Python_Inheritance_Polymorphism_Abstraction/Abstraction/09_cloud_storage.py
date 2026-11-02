from abc import ABC, abstractmethod


class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, filename):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded", filename, "to Google Drive.")

    def download_file(self, filename):
        print("Downloaded", filename, "from Google Drive.")

    def delete_file(self, filename):
        print("Deleted", filename, "from Google Drive.")


class OneDrive(CloudStorage):
    def upload_file(self, filename):
        print("Uploaded", filename, "to OneDrive.")

    def download_file(self, filename):
        print("Downloaded", filename, "from OneDrive.")

    def delete_file(self, filename):
        print("Deleted", filename, "from OneDrive.")


for service in [GoogleDrive(), OneDrive()]:
    service.upload_file("notes.pdf")
    service.download_file("notes.pdf")
    service.delete_file("notes.pdf")
