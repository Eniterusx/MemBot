# pylint: disable=line-too-long

"""
Module including all the reading form database exceptions.
"""


class DataWasNotFound(Exception):
    """
    Class that indicates DataWasNotFound error. It is thrown when record / records, that we are trying to find in a
    database, was not found (SQL returned empty table).
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
               f'Data that is tried to be received from a database, using provided arguments, was not found.\n' \
               f'To be more specific \" {self._message} \" function is sending the error.\n' \
               f'Keep in mind that the verification process was passed, meaning your data is correct format.\n' \
               f'So only the database doesnt have any records for following arguments.'
