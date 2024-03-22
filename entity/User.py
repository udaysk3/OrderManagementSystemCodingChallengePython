class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    # Getters and setters
    def getUserId(self):
        return self.userId

    def setUserId(self, userId):
        self.userId = userId

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password

    def getRole(self):
        return self.role

    def setRole(self, role):
        self.role = role