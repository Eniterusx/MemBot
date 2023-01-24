# pylint: disable=line-too-long

"""
Module including all the writing to a database exceptions.
"""

from typing import Any


class UserAlreadyExistsInDataBase(Exception):
    """
    Class that indicates UserAlreadyExistsInDataBase error. It is thrown when developer tries to add the same user
    (identical discord_id) twice to a database (No duplicates allowed).
    """

    def __init__(self, _message: tuple[Any, tuple[str, ...]], *args):
        """
        Constructor to an exception.

        :param _message:        Tuple of function, that thrown this exception and second tuple containing its arguments.
                                That have triggered this error.
        :type _message:         tuple[Any, tuple[str, ...]]

        :param args:            All the other arguments used, by :class:`Exception`.
        """
        super().__init__(args)
        self._message: tuple[Any, tuple[str, ...]] = _message
        self._information: str = f'Problem accrued with: {self._message[0].__name__}{self._message[1]}'

    def __str__(self):
        """
        Converter of the exception to str type, to help print this error and therefore making it easier to gather
        information about the problem.

        :return:    Full explanation of an error.
        :rtype:     str
        """
        return f'Exception!!!!! {__class__.__name__} exception was thrown.\n' \
               f'You cannot add the same user twice.\n' \
               f'{self._information}\n' \
               f'By the same user we understand, that he has identical discord_id as some other user in a database.\n' \
               f'If you want to modify this user use .update_user() method from WritingToDatabase class object.'


class PictureAlreadyExistsInDataBase(Exception):
    """
    Class that indicates PictureAlreadyExistsInDataBase error. It is thrown when developer tries to add the same picture
    (identical url or image_hash or delete_hash) twice to a database (No duplicates allowed).
    """

    def __init__(self, _message: tuple[Any, tuple[str, ...]], *args):
        """
        Constructor to an exception.

        :param _message:        Tuple of function, that thrown this exception and second tuple containing its arguments.
                                That have triggered this error.
        :type _message:         tuple[Any, tuple[str, ...]]

        :param args:            All the other arguments used, by :class:`Exception`.
        """
        super().__init__(args)
        self._message: tuple[Any, tuple[str, ...]] = _message
        self._information: str = f'Problem accrued with: {self._message[0].__name__}{self._message[1]}'

    def __str__(self):
        """
        Converter of the exception to str type, to help print this error and therefore making it easier to gather
        information about the problem.

        :return:    Full explanation of an error.
        :rtype:     str
        """
        return f'Exception!!!!! {__class__.__name__} exception was thrown.\n' \
               f'You cannot add the same picture twice.\n' \
               f'{self._information}\n' \
               f'By the same picture we understand, that it has identical url or image_hash or delete_hash as some ' \
               f'other picture in a database.\n' \
               f'If you want to modify this picture use .update_picture() method from WritingToDatabase class object.'
