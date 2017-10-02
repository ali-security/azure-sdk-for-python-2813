# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ChainerSettings(Model):
    """Specifies the settings for Chainer job.

    :param python_script_file_path: The path and file name of the python
     script to execute the job.
    :type python_script_file_path: str
    :param python_interpreter_path: The path to python interpreter.
    :type python_interpreter_path: str
    :param command_line_args: Command line arguments that needs to be passed
     to the python script.
    :type command_line_args: str
    :param process_count: Number of processes parameter that is passed to MPI
     runtime. The default value for this property is equal to nodeCount
     property
    :type process_count: int
    """

    _validation = {
        'python_script_file_path': {'required': True},
    }

    _attribute_map = {
        'python_script_file_path': {'key': 'pythonScriptFilePath', 'type': 'str'},
        'python_interpreter_path': {'key': 'pythonInterpreterPath', 'type': 'str'},
        'command_line_args': {'key': 'commandLineArgs', 'type': 'str'},
        'process_count': {'key': 'processCount', 'type': 'int'},
    }

    def __init__(self, python_script_file_path, python_interpreter_path=None, command_line_args=None, process_count=None):
        self.python_script_file_path = python_script_file_path
        self.python_interpreter_path = python_interpreter_path
        self.command_line_args = command_line_args
        self.process_count = process_count
