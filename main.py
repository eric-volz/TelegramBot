from secrets import Key
from TelegramBotManager import TelegramBotManager
from TelegramBotAnswerFunctions import TelegramBotAnswerFunctions
import time


print(TelegramBotManager.getChatID(Key.token))
#manager = TelegramBotManager(Key.token, TelegramBotManager.getChatID(Key.token), 0.5)
#manager.setCommands(
    #[{"command" : "update", "answer" : TelegramBotAnswerFunctions.serverOnline()}
    # ]
#)

time.sleep(10)