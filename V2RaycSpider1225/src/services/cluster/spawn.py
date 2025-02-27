# -*- coding: utf-8 -*-
# Time       : 2021/12/22 9:00
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description: 催化剂

from services.settings import PATH_CHROMEDRIVER
from .exceptions import UnknownNestException
from .nest import LionCubOfCintra, LaraDorren


def devil_king_armed(atomic: dict, silence=True, mirror=False):
    """
    Production line for running instances

    :param atomic:
    :param silence:
    :param mirror:
    :return:
    """
    _blood = atomic.get("nest", "")
    if _blood == "sspanel":
        cirilla = LionCubOfCintra(
            atomic=atomic,
            silence=silence,
            chromedriver_path=PATH_CHROMEDRIVER
        )
        return cirilla if mirror is False else cirilla.assault
    elif _blood == "v2board":
        cirilla = LaraDorren(
            atomic=atomic,
            silence=silence,
            chromedriver_path=PATH_CHROMEDRIVER
        )
        return cirilla if mirror is False else cirilla.assault

    raise UnknownNestException
