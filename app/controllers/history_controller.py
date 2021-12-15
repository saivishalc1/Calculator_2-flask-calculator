"""csv"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
# pylint: disable=(too-few-public-methods)
from flask import render_template
from app.controllers.controller import ControllerBase
from csvmanager.manager import CSVManager


class HistoryController(ControllerBase):
    """csv"""
    @staticmethod
    def get():
        """csv"""
        return render_template("history.html", titles=CSVManager.column_values(),
                               row_data=CSVManager.read(), zip=zip)
