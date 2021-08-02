from .TelegramBot import TelegramBot
import threading as th
import time


class TelegramBotManager(TelegramBot):
    def __init__(self, token, chatID, updateTime):
        """
        Initalisiert den TelegramBot und den TelegramManager
        :param token: API Token
        :param chatID: zugehörige ChatID
        :param updateTime: zeit, wie oft die Update Funktion Updaten soll
        """
        super().__init__(token, chatID)
        self.lastMessageDate = 0
        self.commands = []
        updateThread = th.Thread(target=self.updater, args=(updateTime,))
        updateThread.start()

    def updater(self, updateTime):
        """
        Führt alle Funktionen aus, die in ihr enthalte sind in einem bestimmten Zeitintervall
        :param updateTime: Zeit, wie oft Upgedatet wird
        :return: None
        """
        while True:
            try:
                self.commandHandler()
                time.sleep(updateTime)
            except Exception as exc:
                print("Der Telegram Updater wurde abgebrochen, da: " + str(exc))
                exit()

    def commandHandler(self):
        data = self.getUpdate()
        if self.checkIfMessageIsNew(data):
            command = self.getLatestMessage()
            answer = self.findAnswerToCommand(command)
            if not answer:
                responce = self.sendMessage("Diesen Command gibt es leider nicht!")
            else:
                responce = self.sendMessage(answer)

    def checkIfMessageIsNew(self, message):
        date = message["result"][-1]["message"]["date"]
        if self.lastMessageDate == 0:
            self.lastMessageDate = date
        elif date > self.lastMessageDate:
            self.lastMessageDate = date
            return True
        return False

    def setCommands(self, commands):
        """
        Setzt das CommandArray auf das vorgegebene Command Array

        Richtige Schreibweise von commands: [{"command" : "...", "answer" : "..."}, ...]

        :param commands: Command und Answer Array
        :return: boolean ob erfolgreich
        """
        if self.checkCommands(commands):
            self.commands = commands
            return True
        return False

    def addCommand(self, command):
        """
        Fügt einen weiteren Command in richtiger Schreibweise zu dem CommandArray hinzu

        Richtige Schreibweise von commands: {"command" : "...", "answer" : "..."}

        :param command: Command und Answer
        :return: boolean ob erfolgreich
        """
        if self.checkCommands([command]):
            self.commands.append(command)
            return True
        return False

    def findAnswerToCommand(self, command):
        """
        Findet die korrekte Antwort zu einem Command
        :param command: Command String
        :return: Answer String
        """
        for i in self.commands:
            if i["command"] == command:
                return i["answer"]
        return False

    @staticmethod
    def checkCommands(commands):
        """
        Prüft, ob die Commands korreckt gebildet wurden
        :param commands: Commnad und Answer Array
        :return: boolean
        """
        for i in commands:
            try:
                test = i["command"]
                test = i["answer"]
            except:
                print("Die Commands konnten nicht hinzugefügt werden, da sie nicht den Richtlinien entsprechen!")
                return False
            return True