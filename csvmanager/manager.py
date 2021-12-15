"""csv"""
# pylint: disable=(no-member)
from pathlib import Path
import pandas as pd


class CSVManager:
    """csv"""

    @staticmethod
    def get_path():
        """csv"""
        return str(Path(__file__).parent.absolute()) + "/result/data.csv"

    @staticmethod
    def write(num1, num2, operation, result):
        """csv"""
        df_result = pd.read_csv(CSVManager.get_path())
        df_result.loc[len(df_result.index)] = [num1, num2, operation, result]
        df_result = df_result.drop_duplicates()
        df_result.to_csv(CSVManager.get_path(), index=False)

    @staticmethod
    def read():
        """csv"""
        df_result = pd.read_csv(CSVManager.get_path())
        return list(df_result.values.tolist())

    @staticmethod
    def column_values():
        """csv"""
        df_result = pd.read_csv(CSVManager.get_path())
        return df_result.columns.values
