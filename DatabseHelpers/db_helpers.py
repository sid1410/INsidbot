from datetime import datetime
from db_connect import session
from .Dao import Chat, Pack


def dorecharge(telegram_id, pack_rate):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    prev = customer.availedsolutions
    pack = session.query(Pack).filter(Pack.packprice == pack_rate).first()
    if pack and customer:
        customer.packid = pack.packid
        customer.availedsolutions = pack.solutions + prev
        customer.packpurchasedate = datetime.today()
        session.add(customer)
        session.commit()
        return True
    return False


def doincrease(telegram_id):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    if customer:
        customer.availedsolutions += 1
        session.add(customer)
        session.commit()
        return True
    return False


def create_new_user_data(telegram_id):
    customer = Chat(telegramid=telegram_id)
    session.add(customer)
    session.commit()


def check_existing_user(telegram_id):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    if customer:
        return True
    return False


def get_remaining_solutions(telegram_id):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    return customer.availedsolutions


def decrease_remaining_solutions(telegram_id):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    customer.availedsolutions -= 1
    session.add(customer)
    session.commit()


def user_details(telegram_id):
    customer = session.query(Chat).filter(Chat.telegramid == telegram_id).first()
    return customer
