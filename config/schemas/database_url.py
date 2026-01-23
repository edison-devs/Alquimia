
class ConnectionData:
    def __init__(self, DATABASE, DIALECT, USER=None, PASSWORD=None, HOST=None, PORT=None, DRIVER=None):
        self.user = USER
        self.password = PASSWORD
        self.host = HOST
        self.port = PORT
        self.database = DATABASE
        self.dialect = DIALECT
        self.driver = DRIVER
        
    @property
    def url_embedded(self):
        return f"{self.dialect}:///{self.database}"

    @property
    def url_server(self):
        return (
            f"{self.dialect}+{self.driver}://"
            f"{self.user}:{self.password}@"
            f"{self.host}:{self.port}/"
            f"{self.database}"
        )