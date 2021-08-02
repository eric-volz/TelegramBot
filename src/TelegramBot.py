import requests
import json


class TelegramBot:
    def __init__(self, token, chatID):
        """
        Initalisiert den Telegram Chatbot
        :param token: API Token
        :param chatID: zugehörige ChatID
        """

        self.token = token
        self.url = "https://api.telegram.org/bot" + self.token + "/"
        self.chatID = chatID

    @staticmethod
    def getChatID(token):
        """
        Statische Methonde zum Erhalten der Chat ID
        :param token: API Token
        :return: Chat ID
        """
        url = "https://api.telegram.org/bot" + str(token) + "/"
        data = requests.get(url + "getUpdates")
        j = json.loads(data.text)
        return j["result"][-1]["message"]["chat"]["id"]

    def getUpdate(self):
        """
        Fragt nach einem Update JSON mit den neusten Nachrichten
        :return: Update JSON
        """
        data = requests.get(self.url + "getUpdates")
        j = json.loads(data.text)
        return j

    def getLatestMessage(self):
        """
        :return: Gibt die letzte Geschriebene Nachricht vom Client zurück
        """
        return self.getUpdate()["result"][-1]["message"]["text"]

    def sendMessage(self, text):
        """
        Sendet einen Nachricht an den Client
        :param text: gesendete Nachricht
        :return: responce, ob erfolgreich: 200 == erfolgreich
        """
        params = {"chat_id": self.chatID, "text": text}
        responce = requests.post(self.url + "sendMessage", params=params)
        return responce