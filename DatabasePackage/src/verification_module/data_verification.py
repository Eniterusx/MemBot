# pylint: disable=line-too-long,import-error

"""
Module including the verifying method.
"""

from typing import Any, Optional

from DatabasePackage.src.verification_module.bounds import Bound


class Verification:
    """
    Class used to verify the data send to a database.

------------------------------------------------------------------------------------------------------------------------

    Songs, with which this class was made:
        -   WORKERS & RESOURCES: SOVIET REPUBLIC OFFICIAL GAME SOUNDTRACK
        -   50 Cent, "In Da Club"
    """

    def __init__(self, _b: Bound = Bound()):
        """
        **Constructor** that lets you select bounds on witch verification process will rely on.

        :param _b:  Specific bounds that can be used as verifier.
        :type _b:   Bound

        """
        self._b: Bound = _b
        self.__error_data: list[tuple[str, Any]] = []

    def __repr__(self):
        """
        Verification class representation method.

        :return:    Class representation, formatted in a specific way.
        :rtype:     str
        """
        return f'{self.__class__.__name__}(_b={self._b})'

    @property
    def error_data(self) -> list[tuple[str, Any]]:
        """
        Getter for self.__error_data. Makes this variable immutable.

        :return:    List of all the data, that was not correct. Inside each 2 slot tuple there is information type of
                    argument provided and in the second the value of argument given.
        :rtype:     list[tuple[str, Any]]
        """
        return self.__error_data

    @property
    def b(self) -> Bound:
        """
        Getter for self._b. Makes this variable immutable.

        :return:    Bound used in verification process.
        :rtype:     Bound
        """
        return self._b

    def verify_data(self, data: list[tuple[str, Any], ...]) -> Optional[list[tuple[str, Any], ...]]:
        """
        This method is used to verify specific data, that you want to put in a database.

        The use of this method is very simple:
            1.  Create a list in a following way: l = [(<%>, <%%>), ...], where:

                -   "%" - Here you put a string, that informs what type of data you sent to verify. In other words what
                    colum your argument refers to. Then a specific function will be used to verify your second argument.

                        Type of data -- What data type put in "%%":
                            'file_name' - str
                            'file_type' - str
                            'image_category' - str
                            'size'- file
                            'reason_of_report' - str
                            'reason_of_ban' - str

                -   "%%" - The actual peace of data in one of a types: string, int or file.

            2.  Put your list that you want to check in to a function above.

            3.  See if this function returns None.

            4.  If all hope is lost and correct data is marked as wrong, please keep in mind, that there might be a
                bug or two, so it is advised to report it to Dominik.

        Examples of use:
            1.  We want to check the following data in a pictures table:

                    file_name, file_type, url and delete_hash
                        l = [
                            ('file_name', "Best_file_in_the_world")
                        ]
                    V.verify_data(l) -- Will not throw any exceptions and .error_data() method will return:
                        t = []
                    Which means that everything went smoothly and without problems.

            2.  We want to check the following data in a reports and statistics table:

                    reason_of_report, file_type
                        l = [
                            ('reason_of_report', "I will not tell you :)"),
                            ('file_type', "Trolololo...")
                        ]
                    V.verify_data(l) -- Will throw exception VerificationProcessNotPassed and .error_data() method will
                    return:
                        t = [('file_type_must_be_in_allowed_types', "Trolololo...")]

        :param data:    It is a list of parameters that you want to check. Each parameter needs to have one of
                        badges listed above, as a first element of a tuple and a parameter provided as a second.
        :type data:     list[tuple[str, Any], ...]

        :return:        List of test with provided values that have not passed certain tests.
        :rtype:         list[tuple[str, Any], ...]
        """
        self.__error_data = []

        for variable in data:
            check = self._b.check(variable[0], variable[1])
            if check is not None:
                self.__error_data.append(check)

        if len(self.__error_data) != 0:
            return self.__error_data
        return None
