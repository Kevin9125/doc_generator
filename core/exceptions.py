
class MauvaisFormatFichierException(Exception):
    def __init__(self, message):
        super().__init__(message)#appelle le constructeur de la classe exception

