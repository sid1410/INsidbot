from datetime import datetime
from bot import TelegramBot

from Utils.utilityMethods import (register,
                                  show_creator,
                                  show_remaining_sol_count,
                                  show_pack_details,
                                  make_reply,
                                  recharge, increase
                                  )

bot_functions = {
    '/register': register,
    '/creator': show_creator,
    '/count': show_remaining_sol_count,
    '/start': show_pack_details,
}
bot = TelegramBot()
update_id = 23752398

while True:
    updates = bot.get_updates(offset=update_id)
    print("New message")
    updates = updates['result']
    if updates:
        for update in updates:
            update_id = update['update_id']
            try:
                msg = update['message']['text']
                time_msg_sent = datetime.fromtimestamp(update['message']['date'])
                _from = update['message']['from']['id']
                reply_to_msg = update['message']['message_id']

                func = bot_functions.get(msg, None)

                if msg.startswith('/recharge'):
                    recharge(bot=bot, chat_id=_from, msg=msg)
                elif msg.startswith('/increase'):
                    increase(bot=bot, chat_id=_from, msg=msg)
                elif func:
                    func(bot=bot, chat_id=_from)
                else:
                    reply = make_reply(
                        bot=bot, _from=_from
                        , reply_to_msg=reply_to_msg, link=msg, msg_timing=time_msg_sent)
            except Exception as err:
                msg = None
                time_msg_sent = None