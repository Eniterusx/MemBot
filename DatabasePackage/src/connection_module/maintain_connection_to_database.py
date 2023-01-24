# pylint: disable=line-too-long,import-error

"""
Module related to connecting to a database.
"""

from typing import Optional, Any

import mysql.connector

from DatabasePackage.src.connection_module.env_live import HOST, PORT, DATABASE_NAME, USERNAME, PASSWORD, CHARACTER_SET


class Connection:
    """
    Class used to maintain connection with a database and help with optimization.

------------------------------------------------------------------------------------------------------------------------

    !IMPORTANT!
        -   Keep in mind that despite the previous note methods used in this class will not throw more exceptions than
            listed in method description.

------------------------------------------------------------------------------------------------------------------------

    For any bug reports please contact: Dominik Breksa.

------------------------------------------------------------------------------------------------------------------------

    Songs, with which this class was made:
        -   BLACK SABBATH, "Paranoid".
        -   WORKERS & RESOURCES: SOVIET REPUBLIC GAME SOUNDTRACK
        -   DEFTONES, "My Own Summer"
    """

    def __init__(self):
        """
        **Default constructor**, that takes parameters needed to start connection to a MYSQL server using
        :class:`mysql.connector`.
        """
        self._conn = None
        self._cur = None
        self._host: str = HOST
        self._port: str = PORT
        self._dbname: str = DATABASE_NAME
        self._user: str = USERNAME
        self._password: str = PASSWORD
        self._charset = CHARACTER_SET
        self._is_connected: bool = False

    @property
    def is_connected(self) -> bool:
        """
        Getter for self._is_connected. Makes this variable immutable.

        :return:    True if you have earlier used .connect() method False otherwise.
        :rtype:     bool
        """
        return self._is_connected

    def __repr__(self) -> str:
        """
        Connection class representation method.

        :return:    Class representation, formatted in a specific way.
        :rtype:     str
        """
        return f'{self.__class__.__name__}(_host={self._host}, _port={self._port}, _dbname={self._dbname}, ' \
               f'_user={self._user}, _password={self._password}, _is_connected={self._is_connected})'

    def connect(self):
        """
        Used to initiate a connection. Must be used first before any further methods are called
        (apart from default constructor). Otherwise, other class methods will raise error: NoConnection meaning that no
        connection is started.

        !IMPORTANT!
            -   This method is deprecated. It is advised to use "with" command while managing connection, while
                using ManageDatabase class.

        For connection details it uses the arguments provided in a constructor.

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        """
        if not self._is_connected:
            self._conn = mysql.connector.connect(host=self._host, port=self._port, database=self._dbname,
                                                 user=self._user, password=self._password, raise_on_warnings=True,
                                                 charset=self._charset)
            self._cur = self._conn.cursor()
            self._is_connected = True
        else:
            return

    def disconnect(self):
        """
        Method used to disconnect from a MYSQL server. It must be used, before exiting the program in order to free a
        port on your device and kill a specific process in a database.

        !IMPORTANT!
            -   This method is deprecated. It is advised to use "with" command while managing connection, while
                using ManageDatabase class.

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        """
        if self._conn is not None and self._is_connected:
            self._is_connected = False
            self._cur.close()
            self._conn.close()
            self._cur = None
            self._conn = None
        else:
            return

    def _ask(self, sql: str, data: tuple[Any, ...] = tuple(), mode: bool = True) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to proceed an SQL query. It is resistant to SQL injection attacks.

        :param sql:     Parameter, that is used, as a query to a database.
        :type sql:      str

        :param data:    Argument, that is used to fill SQL queries with arguments. Must be tuple of strings. Default to
                        Empty tuple.
        :type data:     tuple[Any, ...]

        :param mode:    Variable telling the function what type of query it must proceed. If False means that it will
                        commit a data, True it will return the result of a query.
        :type mode:     bool

        :return:    It is optional to return a list of tuple. In other words the list is where all the record are
                    located, but the record itself is a specific tuple in that list.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """
        if self._is_connected:
            self._cur.execute(sql, data)  # Query execution
            if mode:
                return self._cur.fetchall()  # Returning answer to a proces
            self._conn.commit()  # Possible commit to a database
        return None
