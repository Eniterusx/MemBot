# pylint: disable=line-too-long

"""
Module including all the verification process exceptions.
"""

from typing import Any


class VerificationProcessNotPassed(Exception):
    """
    Class that indicates VerificationProcessNotPassed error. It is thrown when the data that developer is trying to
    supply query i.e. url / user password / user_id does not meet a specific bound for type of data.
    """

    def __init__(self, _message: list[tuple[str, Any], ...], *args):
        """
        **Constructor** to an exception.

        :param _message:        List of tuples of types_of_data, that serve as an information to a function telling it
                                which bound to check with provided arguments. It contains only the data, that did not
                                meet as desired requirement.
        :type _message:         list[tuple[str, Any], ...]

        :param args:            All the other arguments used, by :class:`Exception`.
        """
        super().__init__(args)
        self._message: list[tuple[str, Any], ...] = _message

        self._information: str = ""
        for err in self._message:
            self._information += f'-  Problem accrued with: \" {err[0]}: {err[1]} \". See the bound description for ' \
                                 f'this type_of_argument in Bound class.\n'

    def __str__(self):
        """
        Converter of the exception to str type, to help print this error and therefore making it easier to gather
        information about the problem.

        :return:    Full explanation of an error.
        :rtype:     str
        """
        return f'Exception!!!!! {__class__.__name__} exception was thrown.\n' \
               f'Data sent to a database is not correct format and was not committed.\n' \
               f'To be more specific:\n' \
               f'{self._information}'
