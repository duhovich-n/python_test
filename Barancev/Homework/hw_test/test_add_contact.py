# -*- coding: utf-8 -*-
from hw_model.contact import Contact


def test_create_contact(app):
    app.contact.create(Contact(firstname="Никита", lastname="Духович", company="Компания", address="Улица"))


def test_empty_create_contact(app):
    app.contact.create(Contact(firstname="", lastname="", company="", address=""))
