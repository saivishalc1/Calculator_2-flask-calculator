"""A simple flask web app"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from csvmanager.manager import CSVManager

class CalculatorController(ControllerBase):
    """A simple flask web app"""
    @staticmethod
    def post():
        """A simple flask web app"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            value1 = int(request.form['value1'])
            value2 = int(request.form['value2'])
            operation = request.form['operation']
            my_tuple = (value1, value2)
            check = getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            if check:
                CSVManager.write(value1, value2, operation, result)
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation, result=result)
        return render_template('calculator2.html', error=error)
    @staticmethod
    def get():
        """R"""
        return render_template('calculator.html')
