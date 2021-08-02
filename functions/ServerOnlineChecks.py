import requests


class ServerOnlineChecks:
    """
    Klasse mit statischen Funktionen
    """

    @staticmethod
    def getServerStatus(url):
        """
        Gibt den Server Status, der übergebenen URL zurück
        :param url: Adresse einer Webseite
        :return: Server Status oder Error
        """
        try:
            return requests.get(url)
        except Exception as e:
            return e

    @staticmethod
    def checkIfMultipleServerAreOnline(urls):
        """
        Überprüft, ob alle URLs den Statuscode 200 enthalten
        :param urls: Array mit URLs
        :return: String mit Infos über die Server
        """
        notWorking = []
        for u in urls:
            data = ServerOnlineChecks.getServerStatus(u)
            try:
                if data.status_code != 200:
                    notWorking.append(u + ": " + str(data))
            except Exception as e:
                notWorking.append(u + ": " + str("Webseite ist nicht Existent!"))

        if len(notWorking) == 0:
            return "Alle Server sind Online!"
        else:
            string = ""
            for u in notWorking:
                string = string + u + "\n"

            return "Diese Server sind nicht Online: \n" + string
