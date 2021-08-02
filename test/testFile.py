
def test(tb):
    token = "1869353284:AAGmgbwOaGr3CWYitRG1ULsNG0DiI4SBewQ"

    bot = tb.TelegramBotManager(token, tb.TelegramBotManager.getChatID(token), 1)

    bot.addCommand(
        {"command": "update", "answer": tb.ServerOnlineChecks.checkIfMultipleServerAreOnline(["https://volz.link"])})
