import requests


class TelegramBotAnswerFunctions:

    @staticmethod
    def checkIfServerIsOnline(url):
        try:
            return requests.get(url)
        except Exception as e:
            return e

    @staticmethod
    def serverOnline():
        urls = ["https://volz.link", "https://cloud.volz.link", "https://it.volz.link", "https://musik.volz.link",
                "https://travelknuffis.de"]
        notWorking = []
        for u in urls:
            data = TelegramBotAnswerFunctions.checkIfServerIsOnline(u)
            try:
                if data.status_code != 200:
                    notWorking.append(u + ": " + str(data))
            except:
                notWorking.append(u + ": " + str("Webseite ist nicht Existent!"))

        if len(notWorking) == 0:
            return "Alle Server sind Online!"
        else:
            string = ""
            for u in notWorking:
                string = string + u + "\n"

            return "Diese Server sind nicht Online: \n" + string
