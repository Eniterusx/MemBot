# pylint: disable=line-too-long

"""
Module including all the connection exceptions.
"""


class NoConnection(Exception):
    """
    Class that indicates, NoConnection error. It is thrown when developer tries to perform some reading / writing
    activity, but forgot to use .connect() method on a desired class object.
    """

    def __init__(self, _message: str, *args):
        """
        **Constructor** to an exception.

        :param _message:    Name of a method with its arguments, that thrown this exception.
        :type _message:     str

        :param args:        All the other arguments used, by :class:`Exception`.
        """
        super().__init__(args)
        self._message: str = _message

    def __str__(self):
        """
        Converter of the exception to str type, to help print this error and therefore making it easier to gather
        information about the problem.

        :return:    Full explanation of an error.
        :rtype:     str
        """
        return f'Exception!!!!! {__class__.__name__} exception was thrown.\n' \
               f'No database connection was established.\n' \
               f'Before you use this method: \" {self._message} \" try to firstly use .connect() method, but don\'t ' \
               f'forget to close it afterwards with .disconnect() method at the end of a program / function.'
