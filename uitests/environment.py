# -*- coding: utf-8 -*-
"""
    ui-tests.environment
    ~~~~~~~~~~~~~~~~~~~~

    Behave framework initial script with environment.
"""

from uitests.lib.selenium import setup_browser, flush_browser
from uitests.lib.session import Session


def before_scenario(context, scenario):
    """
    Function called before behave scenario.
    Parses provided arguments and creates selenium browser.

    :param context: behave context
    :param scenario: behave scenario
    """

    browser = context.config.userdata.get("browser", "firefox")
    headless = str2bool(context.config.userdata.get("headless", "y"))
    remote = context.config.userdata.get("remote", "")
    url = context.config.userdata.get("url", "www.facebook.com")
    username = context.config.userdata.get("username", "admin@gmail.com")
    password = context.config.userdata.get("password", "Admin@123")

    setup_browser(context, browser, remote, headless)
    context.url = "https://{url}".format(url=url)
    context.session = Session(username, password)


def after_scenario(context, scenario):
    """
    Function called after behave scenario.
    Saves screenshot and closes the selenium browser.

    :param context: behave context
    :param scenario: behave scenario
    """

    success = scenario.status != "failed"
    flush_browser(context, scenario.name, success)


def str2bool(string):
    """
    Converts string to boolean

    :param string: input string
    :returns: string converted to boolean
    """

    return string.lower() in ("yes", "y", "true", "t", "1")
