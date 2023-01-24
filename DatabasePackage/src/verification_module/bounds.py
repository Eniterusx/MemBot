# pylint: disable=line-too-long,import-error

"""
Module inclining's the bound to data sent to a database.
"""

import re
from typing import Any, Optional

ALLOWED_EXTENSIONS = ['mp4', 'png', 'gif', 'jpg', 'jpeg', 'apng']


class Bound:
    """
    Class used as pattern of bounds to verify data send to a database.

    List of bounds for all the methods are located in method description.

------------------------------------------------------------------------------------------------------------------------

    !IMPORTANT!
        -   All methods, beside check(...) and _tes(...) in this class are serving a supportive role, are
            self-explanatory and rather simple.

        -   If you find yourself not knowing which colum certain bound checks fell free to look on the erd.PNG image
            located: "docs/database_info_schema" or just see the description the specific table located in the same
            folder. At the end you can ask Dominik Breksa what it does.

------------------------------------------------------------------------------------------------------------------------

    For any bug reports please contact: Dominik Breksa.

------------------------------------------------------------------------------------------------------------------------

    Songs, with which this class was made:
        -   Malik Montana, "7 5 0".
        -   Malik Montana x Diho, "Naaajak".
        -   Malik Montana, "Robie YEAH".
        -   Malik Montana, "Mówili".
    """

    def __init__(self):
        """
        Default constructor that sets starting bounds.

        If you have desire to change some of its parameters use .update_bounds(...) method from this class.
        """
        self.__dispatch: dict[str, Any] = {
            'file_name': self._verify_file_name,
            'file_type': self._verify_file_type,
            'file_size': self._verify_file_size,
            'image_category': self._verify_image_category,

            'reason_of_report': self._verify_reason_of_report,

            'reason_of_ban': self._verify_reason_of_ban
        }

    def __repr__(self):
        """
        Bound class representation method.

        :return:    Class representation, formatted in a specific way.
        :rtype:     str
        """
        return f'{self.__class__.__name__}()'

    def __str__(self):
        """
        Bound class to string method.

        :return:        Returns the string representation of an object.
        :rtype:         str
        """
        return f'{self.__class__.__name__}()'

    def check(self, type_of_argument: str, argument: Any) -> Optional[tuple[str, Any]]:
        """
        Method that calls adequate method that goes through a validation process.

        :param type_of_argument:    Colum your argument refers to. See the description of Verification.verify_data(...)
                                    method, because the type_of_argument is complementary.
        :type type_of_argument:     str

        :param argument:            the actual peace of data that you want to check correctness.

        :return:    Tuple that have two slots; in the first type of data that was checked and in a second the argument
                    that you try to validate.
        :rtype:     Optional[tuple[str, Any]]
        """
        return self.__dispatch.get(type_of_argument)(argument)

    @staticmethod
    def _test(test_selector: list[Any, ...]) -> Optional[str]:
        """
        Method that is used to run a tests given in an arguments.

        :param test_selector:   List of all the test to run (as a functions).
        :type:                  list[Any, ...]

        :return:    The outcome of a test if it was not passed.
        :rtype:     str
        """
        for test in test_selector:
            output = test()
            if output is not None:
                return output
        return None

    # Pictures----------------------------------------------------------------------------------------------------------

    def _verify_file_name(self, file_name: str) -> Optional[tuple[str, str]]:
        """
        Bound method:   Provided file_name must be between 1 and 511 characters and can only contain characters from
                        this regex [A-Za-z0-9_ ąćęłńóśźżł].

        :param file_name:  File name that you want to check.
        :type file_name:   str

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_file_name_must_contain_specific_characters() -> Optional[str]:
            pattern = "^[A-Za-z0-9_ ąćęłńóśźżł]+$"
            if re.search(pattern, file_name) is None:
                return "file_name_must_contain_specific_characters"
            return None

        def _verify_file_name_must_be_specific_length() -> Optional[str]:
            if not 2 <= len(file_name) <= 70:
                return "file_name_must_be_specific_length"
            return None

        test_selector = [
            _verify_file_name_must_contain_specific_characters,
            _verify_file_name_must_be_specific_length
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), file_name
        return None

    def _verify_file_type(self, file_type: str) -> Optional[tuple[str, str]]:
        """
        Bound method:   Provided file_type must be one of ALLOWED_EXTENSIONS.

        :param file_type:  File type that you want to check.
        :type file_type:   str

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_file_type_must_be_in_allowed_types() -> Optional[str]:
            if file_type not in ALLOWED_EXTENSIONS:
                return "file_type_must_be_in_allowed_types"
            return None

        test_selector = [
            _verify_file_type_must_be_in_allowed_types
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), file_type
        return None

    def _verify_image_category(self, image_category: str) -> Optional[tuple[str, str]]:
        """
        Bound method:   Provided image_category must be longer that a single character. And must match this regex:
                        ^[A-z0-9_ ąćęłńóśźżł]+$ .

        :param image_category:  Category of image that you want to check.
        :type image_category:   str

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_image_category_must_contain_specific_characters() -> Optional[str]:
            pattern = "^[A-z0-9_ ąćęłńóśźżł]+$"
            if not re.search(pattern, image_category):
                return "image_category_must_contain_specific_characters"
            return None

        test_selector = [
            _verify_image_category_must_contain_specific_characters
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), image_category
        return None

    def _verify_file_size(self, attachment) -> Optional[tuple[str, Any]]:
        """
        Bound method:   File size cannot be larger than 25MiB.

        :param attachment:  File that you want to check.
        :type attachment:   file

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_file_size_too_big() -> Optional[str]:
            if attachment.size / (1024 * 1024) > 25:
                return "_verify_file_size_too_big"
            return None

        test_selector = [
            _verify_file_size_too_big
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), attachment
        return None

    # Reports-----------------------------------------------------------------------------------------------------------

    def _verify_reason_of_report(self, reason_of_report: str) -> Optional[tuple[str, str]]:
        """
        Bound method:   Provided reason_of_report must be longer that a single character.  And must match this regex:
                        ^[A-z0-9_ ąćęłńóśźżł]+$ .

        :param reason_of_report:  Reason of report that you want to check.
        :type reason_of_report:   str

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_reason_of_report_must_contain_specific_characters() -> Optional[str]:
            pattern = "^[A-z0-9_ ąćęłńóśźżł]+$"
            if re.search(pattern, reason_of_report) is None:
                return "reason_of_report_must_contain_specific_characters"
            return None

        test_selector = [
            _verify_reason_of_report_must_contain_specific_characters
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), reason_of_report
        return None

    # Banned------------------------------------------------------------------------------------------------------------

    def _verify_reason_of_ban(self, reason_of_ban: str) -> Optional[tuple[str, str]]:
        """
        Bound method:   Provided reason_of_ban must be longer that a single character.  And must match this regex:
                        ^[A-z0-9_ ąćęłńóśźżł]+$ .

        :param reason_of_ban:  Reason of ban that you want to check.
        :type reason_of_ban:   str

        :return:    If check was not passed it will return the data to verification.
        :rtype:     Optional[tuple[str, str]]
        """
        def _verify_reason_of_ban_must_contain_specific_characters() -> Optional[str]:
            pattern = "^[A-z0-9_ ąćęłńóśźżł]+$"
            if re.search(pattern, reason_of_ban) is None:
                return "reason_of_ban_must_contain_specific_characters"
            return None

        test_selector = [
            _verify_reason_of_ban_must_contain_specific_characters
        ]

        out = self._test(test_selector)
        if out is not None:
            return self._test(test_selector), reason_of_ban
        return None
