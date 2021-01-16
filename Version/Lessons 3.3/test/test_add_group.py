# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    app.group.create(Group(name="Имя группы", header="Заголовок", footer="Футер"))


def test_empty_create_group(app):
    app.group.create(Group(name="", header="", footer=""))
