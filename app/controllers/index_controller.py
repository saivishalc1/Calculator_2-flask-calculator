"""R"""
# pylint: disable=(too-few-public-methods)
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import render_template
from app.controllers.controller import ControllerBase


class IndexController(ControllerBase):
    """R"""
    @staticmethod
    def get():
        """R"""
        return render_template('index.html')
