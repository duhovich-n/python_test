# -*- coding: utf-8 -*-
from model.group import Group


def test_create_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Имя группы", header="Заголовок", footer="Футер"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_empty_create_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
