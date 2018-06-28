from os import getenv
import re
import time
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import phonenumbers
from models import Order as order_table

CONNECT_TIMEOUT = int(getenv('CONNECT_TIMEOUT'))
REQUEST_TIMEOUT = int(getenv('REQUEST_TIMEOUT'))
ENGINE = create_engine(getenv('DB_URI'))
SESSION = Session(ENGINE)


def get_table():
    base = automap_base()
    base.prepare(ENGINE, reflect=True)
    return base.classes.orders


def get_orders_with_non_edited_phones(orders):
    db_query = SESSION.query(orders).filter(
        orders.edited_contact_phone.is_(None))
    return db_query


def correct_contact_phone(db_query):
    for order in db_query:
        contact_phone = order.contact_phone
        if not re.match(r'^\+7', contact_phone):
            contact_phone = '+7' + contact_phone
        phone_number = phonenumbers.parse(contact_phone)
        edited_contact_phone = phone_number.national_number
        order.edited_contact_phone = edited_contact_phone
    SESSION.commit()


def normalize_phones():
    while True:
        try:
            orders = order_table
        except sqlalchemy.exc.OperationalError:
            time.sleep(CONNECT_TIMEOUT)
        else:
            db_query = get_orders_with_non_edited_phones(orders)
            correct_contact_phone(db_query)
            time.sleep(REQUEST_TIMEOUT)


if __name__ == '__main__':
    normalize_phones()
