from Resources.documentApiData import DocumentApiData
from DatabseHelpers.db_helpers import (create_new_user_data,
                                       check_existing_user,
                                       get_remaining_solutions,
                                       decrease_remaining_solutions,
                                       user_details,
                                       dorecharge, doincrease
                                       )
from datetime import datetime, timedelta
from Resources.constants import *
from WebScrapping.fetchSolution import fetch_answer
from config import key


def is_eligible_to_get_solution(chat_id):
    user = user_details(telegram_id=chat_id)
    if user:
        sol = get_remaining_solutions(telegram_id=chat_id)
        return True if sol > 0 else False


def required_registration(bot, chat_id):
    bot.send_text_message(
        chat_id,
        text="You need to register first. You don't not exist in our system\nUse /register command".format(
            chat_id)
    )


def register(bot, chat_id):
    existing = check_existing_user(telegram_id=chat_id)
    if not existing:
        create_new_user_data(telegram_id=chat_id)
        bot.send_text_message(
            chat_id,
            text="You have successfully registered\nRegistration Id: {}".format(chat_id)
        )
    else:
        bot.send_text_message(
            chat_id,
            text="I detected that you are already there in our system with ID: {}\nNo need to register again !!!".format(
                chat_id)
        )


def show_remaining_sol_count(bot, chat_id):
    existing = check_existing_user(telegram_id=chat_id)

    if existing:
        sols = get_remaining_solutions(telegram_id=chat_id)
        bot.send_text_message(
            chat_id,
            text=solution_count_msg+str(sols)
        )
    else:
        required_registration(bot=bot, chat_id=chat_id)


def show_creator(bot, chat_id):
    bot.send_text_message(
        chat_id,
        text="SK owns this bot".format(
            chat_id)
    )


def make_reply(bot, _from, reply_to_msg, link, msg_timing):
    is_eligible = is_eligible_to_get_solution(chat_id=_from)
    if not is_eligible:
        bot.send_error_message(chat_id=_from, reply_to_msg=reply_to_msg, text=pack_expiry_message)
        return False

    try:
        answer_file = fetch_answer(link)
        if answer_file == "Do not decrease":
            bot.send_error_message(chat_id=_from, reply_to_msg=reply_to_msg, text=unable_to_fetch)
            return
    except Exception as e:
        bot.send_error_message(chat_id=_from, reply_to_msg=reply_to_msg, text=error_text)
        print(e)
        return
    try:
        with open("solution.html", 'wb') as tmp:
            # do stuff with temp file
            tmp.write(answer_file.encode('utf-8'))
        with open("solution.html", 'rb') as sol:
            new_solution_document = DocumentApiData(_from, reply_to_msg, sol)
            response = bot.send_document(new_solution_document)
            if response.status_code == 200:
                if datetime.now() - msg_timing <= timedelta(minutes=15):
                    decrease_remaining_solutions(telegram_id=_from)
                else:
                    bot.send_text_message(chat_id=_from, text=late_message)
                show_remaining_sol_count(bot, chat_id=_from)
    except Exception as e:
        print(e)
        bot.send_error_message(chat_id=_from, reply_to_msg=reply_to_msg, text=bot_error)

    finally:
        # os.remove(str(os.getcwd())+"/solution.html")
        pass

    return True


def show_pack_details(bot, chat_id):
    bot.send_text_message(
        chat_id,
        text=pack_details
    )


def recharge(bot, chat_id, msg):
    try:
        _, pin, telegram_id, packprice = msg.split()
        msg = "Wrong security Key"
        if pin == key:
            success = dorecharge(telegram_id=telegram_id, pack_rate=packprice)
            if success:
                msg = "Recharge Done"
            else:
                msg = "Chat_id or pack price is wrong"
    except Exception:
        msg = "Wrong Command"
    bot.send_text_message(
        chat_id,
        text=msg
    )


def increase(bot, chat_id, msg):
    try:
        _, pin, telegram_id = msg.split()
        msg = "Wrong security Key"
        if key == pin:
            success = doincrease(telegram_id=telegram_id)
            if success:
                msg = "Increase Done"
            else:
                msg = "Chat_id is wrong"
    except Exception:
        msg = "Wrong Command"
    bot.send_text_message(
        chat_id,
        text=msg
    )
