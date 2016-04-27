#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pickle

from bottle import (
    route,
    run,
    template,
    debug,
    request,
    redirect,
    default_app,
)

DEFAULT_LIST = [
    [u'Wynieść śmieci', False],
    [u'Zjeść obiad', False],
    [u'Zmyć naczynia', True]
]

DUMP_FILE = "todo.bin"


@route('/', name="main_page")
def todo_list():
    output = template('make_table', rows=enumerate(todo_list_obj))
    return output


@route('/new', method="POST")
def new_item():
    new_task = request.POST.get('task')
    todo_list_obj.append([new_task, False])
    # return "Dodalem {}".format(new_task)
    save_list(todo_list_obj, DUMP_FILE)
    redirect(default_app().get_url("main_page"))


@route('/del/<no:int>', method="GET")
def del_item(no):
    del todo_list_obj[no]
    save_list(todo_list_obj, DUMP_FILE)
    redirect(default_app().get_url("main_page"))


@route('/toggle/<no:int>', method="GET")
def toggle_item(no):
    todo_list_obj[no][1] = not(todo_list_obj[no][1])
    save_list(todo_list_obj, DUMP_FILE)
    redirect(default_app().get_url("main_page"))


def save_list(list_object, filename):
    with open(filename, 'w') as file:
        pickle.dump(list_object, file)
    # mozemy tez napisac tak
    # pickle.dump(list_object, open(filename, 'w'))


def get_saved_list(filename):
    try:  # zlapiemy wyjatek z otwierania pliku lub z od-picklowywania
        unpickled = pickle.load(open(filename))
    except:
        print "Can't unpickle the file. Using default!"
        return DEFAULT_LIST
    return unpickled


todo_list_obj = get_saved_list(DUMP_FILE)

debug(True)  # to nalezy usunac w gotowej aplikacji zeby wlaczyc cache'owanie
run()
