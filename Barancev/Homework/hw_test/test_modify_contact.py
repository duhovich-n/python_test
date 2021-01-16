from hw_model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="firstname"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="lastname"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))


def test_modify_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(company="company"))
    app.contact.modify_first_contact(Contact(company="New company"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(address="address"))
    app.contact.modify_first_contact(Contact(address="New address"))

