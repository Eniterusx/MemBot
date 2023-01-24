# pylint: disable=line-too-long,import-error

"""
Module regarding managing database records.
"""

from typing import Optional, Any

from DatabasePackage.src.connection_module.maintain_connection_to_database import Connection

PICTURE_REMOVE = -4
PICTURE_SUCCESS = 2


class ManageDatabase(Connection):
    """
    Class used to write, change, delete, find and manipulate records in a database.

------------------------------------------------------------------------------------------------------------------------

    !IMPORTANT!
        -   No individual attributes in ManageDatabase class. Only those from witch this class inherits.

        -   It is advised to be VERY careful, while using any methods from this class, because any correct
            action (syntax-wise) is automatically committed to the server and is irreversible in an easy way.

        -   Because this class inherits from Connection it contains more methods than shown here.

------------------------------------------------------------------------------------------------------------------------

    Songs, with which this class was made:
        -   BLACK SABBATH, "Paranoid".
        -   WORKERS & RESOURCES: SOVIET REPUBLIC GAME SOUNDTRACK
        -   DEFTONES, "My Own Summer"
        -   Taco Hemingway, "Polskie Tango"
    """

    def __init__(self):
        """
        **Default constructor**, that takes parameters needed to start connection to a MYSQL server using
        :class:`mysql.connector`.
        """
        super().__init__()

    def __repr__(self):
        """
        ManageDatabase class representation method.

        :return:    Class representation, formatted in a specific way.
        :rtype:     str
        """
        return f'{self.__class__.__name__}(_host={self._host}, _port={self._port}, _dbname={self._dbname}, ' \
               f'_user={self._user}, _password={self._password}, _is_connected={self._is_connected})'

    def __enter__(self):
        """
        Method used to enter with "with" statement. It serves a purpose, because you do not have to think, about
        starting a connection to a database. Program enables connection automatically, when you start a "with"
        statement.

        :return:    Object created with "with" command, that is automatically connected to a database.
        :rtype:     ManageDatabase

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Method used to exit the "with" statement. It serves a purpose, because you do not have to think, about closing
        a connection to a database. Program disables connection automatically, when you end a "with" statement.

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except TooMuchConnections:     Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """
        self.disconnect()

    def add_user(self, discord_id: int, nickname: str) -> int:
        """
        Method used to add user to a database.

        In order to fully understand its arguments, see the latest ER Diagram made by Dominik Breksa which is in
        database_info_schema folder (erd.PNG).

        :param discord_id:  Value for "discord_id" colum in Users table.
        :type discord_id:   int

        :param nickname:    Discord nickname of an account that you want to add to a database.
        :type nickname:     str

        :return:    Returns user_id of an existing user.
        :rtype:     int

        :except mysql.connector.Error:          Any of the exception from "mysql.connector" libreary.
        :except NoConnection:                   Exception from "connection_exceptions.py" file, created by
                                                Dominik Breksa. See its description to understand its occurrence.
        """
        sql = """SELECT * FROM users WHERE discord_id = %s;"""
        data = (str(discord_id),)
        records: list[tuple[Any, ...]] = self._ask(sql, data)
        if len(records) == 0:
            sql = """INSERT INTO users (discord_id, nickname) VALUES (%s, %s);"""
            data = (str(discord_id), str(nickname))
            self._ask(sql, data, False)

            sql = """SELECT user_id FROM users WHERE discord_id = %s;"""
            data = (str(discord_id),)
            records: list[tuple[Any, ...]] = self._ask(sql, data, True)

        return records[0][0]

    def add_picture(self, nickname: str, discord_id: int, file_name: str, file_type: str, url: str, image_hash: str,
                    delete_hash: str, image_category: str = "Empty") -> Optional[int]:
        """
        Method used to add picture url to a database.

        In order to fully understand its arguments, see the latest ER Diagram made by Dominik Breksa which is in
        database_info_schema folder (erd.PNG).

        :param nickname:        Discord nickname of an account that putted this image to a database.
        :type nickname:         str

        :param discord_id:      Value for "discord_id" colum in Pictures table.
        :type discord_id:       int

        :param file_name:       Value for "file_name" colum in Pictures table.
        :type file_name:        str

        :param file_type:       Value for "file_type" colum in Pictures table.
        :type file_type:        str

        :param url:             Value for "url" colum in Pictures table.
        :type url:              str

        :param image_hash:      Value for "image_hash" colum in Pictures table.
        :type image_hash:       str

        :param delete_hash:     Value for "delete_hash" colum in Pictures table.
        :type delete_hash:      str

        :param image_category:   Value for "image_category" colum in Pictures table.
        :type image_category:    str

        :return:    Returns picture_id of an existing picture if insertion was not successful.
        :rtype:     Optional[int]

        :except mysql.connector.Error:          Any of the exception from "mysql.connector" libreary.
        :except NoConnection:                   Exception from "connection_exceptions.py" file, created by
                                                Dominik Breksa. See its description to understand its occurrence.
        """
        user_id = self.add_user(discord_id, nickname)
        sql = """SELECT * FROM pictures WHERE url = %s OR image_hash = %s OR delete_hash = %s;"""
        data = (url, image_hash, delete_hash)
        records: list[tuple[Any, ...]] = self._ask(sql, data)

        if len(records) == 0:
            sql = """   INSERT INTO pictures 
                        (user_id, file_name, file_type, url, image_hash, delete_hash, image_category) 
                        VALUES 
                        (%s, %s, %s, %s, %s, %s, %s);
                  """
            data = (str(user_id), file_name, file_type, url, image_hash, delete_hash, image_category)
            self._ask(sql, data, False)
            return None
        return records[0][0]

    def add_vote(self, discord_id: int, nickname: str, picture_id: int, vote_value: int) -> Optional[int]:
        """
        Method used to add vote to the specific image by a given user.

        In order to fully understand its arguments, see the latest ER Diagram made by Dominik Breksa which is in
        database_info_schema folder (erd.PNG).

        :param discord_id:  Value for "discord_id" of a person that have voted.
        :type discord_id:   int

        :param nickname:    Discord nickname of an account that you want to add to a database.
        :type nickname:     str

        :param picture_id:  Value for "picture_id" colum in Votes table.
        :type picture_id:   int

        :param vote_value:  Value vote: 1 or -1 (Only options).
        :type vote_value:   int

        :return:    Returns vote_value of an existing vote record if insertion was not successful.
        :rtype:     Optional[int]

        :except mysql.connector.Error:          Any of the exception from "mysql.connector" libreary.
        :except NoConnection:                   Exception from "connection_exceptions.py" file, created by
                                                Dominik Breksa. See its description to understand its occurrence.
        """

        user_id = self.add_user(discord_id, nickname)

        sql = """SELECT * FROM votes WHERE user_id = %s AND picture_id = %s;"""
        data = (str(user_id), str(picture_id))
        records: list[tuple[Any, ...]] = self._ask(sql, data)

        if len(records) == 0:
            sql = """REPLACE INTO votes (user_id, picture_id, vote_value) VALUES (%s, %s, %s);"""
            data = (str(user_id), str(picture_id), str(vote_value))
            self._ask(sql, data, False)
            return None
        return records[0][2]


    def add_report(self, discord_id: int, nickname: str, picture_id: int, reason_of_report: str) -> Optional[int]:
        """
        Method used to add vote to the specific image by a given user.

        In order to fully understand its arguments, see the latest ER Diagram made by Dominik Breksa which is in
        database_info_schema folder (erd.PNG).

        :param discord_id:  Value for "discord_id" of a person that have reported other image.
        :type discord_id:   int

        :param nickname:    Discord nickname of an account that you want to add to a database.
        :type nickname:     str

        :param picture_id:  Value for "picture_id" colum in Report table.
        :type picture_id:   int

        :param reason_of_report:  String of explanation, why this image was reported.
        :type reason_of_report:   str

        :return:    Returns report_id of an existing report record if insertion was not successful.
        :rtype:     Optional[int]

        :except mysql.connector.Error:          Any of the exception from "mysql.connector" libreary.
        :except NoConnection:                   Exception from "connection_exceptions.py" file, created by
                                                Dominik Breksa. See its description to understand its occurrence.
        """
        user_id = self.add_user(discord_id, nickname)

        sql = """SELECT * FROM pictures WHERE picture_id = %s;"""
        data = (str(picture_id),)
        records: list[tuple[Any, ...]] = self._ask(sql, data)
        if records:
            sql = """SELECT * FROM reports WHERE user_id = %s AND picture_id = %s;"""
            data = (str(user_id), str(picture_id))
            records: list[tuple[Any, ...]] = self._ask(sql, data)
        else:
            return -1

        if len(records) == 0:
            sql = """INSERT INTO reports (user_id, picture_id, reason_of_report) VALUES (%s, %s, %s);"""
            data = (str(user_id), str(picture_id), reason_of_report)
            self._ask(sql, data, False)
            return None
        return records[0][0]

    def update_picture(self):
        """
        ...
        """

    def update_report(self):
        """
        ...
        """

    def delete_user(self, user_id: int):
        """
        ...
        """

    def delete_picture(self, picture_id: int):
        """
        ...
        """

    def delete_under_performing_picture(self):
        """
        Method used to delete all the images that have a score value less than PICTURE_REMOVE.

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """

        sql = """   DELETE FROM pictures WHERE picture_id IN (
                        SELECT v.picture_id FROM votes AS v INNER JOIN (
                            SELECT picture_id, SUM(vote_value) AS suma FROM votes GROUP BY picture_id
                        ) AS s USING(picture_id)
                        WHERE s.suma < %s
                        GROUP BY picture_id
                    );
              """
        data = (str(PICTURE_REMOVE),)
        self._ask(sql, data, False)

    def remove_reaction(self, statistic_id: int):
        """
        ...
        """

    def ban(self, report_id: int, days_of_ban: int, reason_of_ban: str) -> Optional[int]:
        """
        ...
        """
        sql = """SELECT * FROM banned WHERE report_id = %s;"""
        data = (str(report_id),)
        records: list[tuple[Any, ...]] = self._ask(sql, data)

        if len(records) == 0:
            sql = """
    REPLACE INTO banned (report_id, date_of_unban, reason_of_ban) VALUES  (%s, DATE_ADD(NOW(), INTERVAL %s DAY), %s);
                  """
            data = (str(report_id), str(days_of_ban), reason_of_ban)
            self._ask(sql, data, False)
            return None
        return records[0][0]

    def unban(self, discord_id: int):
        """
        ...
        """
        sql = """SELECT user_id FROM users WHERE discord_id = %s"""
        data = (str(discord_id),)
        record: list[tuple[Any, ...]] = self._ask(sql, data, True)

        if len(record) != 0:
            sql = """   
                        UPDATE banned AS b
                        SET b.date_of_unban = CURRENT_TIMESTAMP()
                        WHERE b.report_id IN(
                            SELECT report_id FROM banned AS ba
                                INNER JOIN reports AS r USING(report_id)
                                INNER JOIN pictures AS p USING(picture_id)
                            WHERE p.user_id = %s
                        );
                  """
            data = (str(record[0][0]),)
            self._ask(sql, data, False)

    def is_user_banned(self, discord_id: int) -> bool:
        """
        ...
        """
        sql = """SELECT user_id FROM users WHERE discord_id = %s"""
        data = (str(discord_id),)
        record: list[tuple[Any, ...]] = self._ask(sql, data, True)
        if len(record) != 0:
            sql = """   SELECT p.user_id FROM pictures AS p
                            INNER JOIN reports AS r USING(picture_id)
                            INNER JOIN banned AS b USING(report_id)
                        WHERE CURRENT_TIMESTAMP() < b.date_of_unban AND p.user_id = %s;
                  """
            data = (str(record[0][0]),)
            record: list[tuple[Any, ...]] = self._ask(sql, data, True)
        return len(record) != 0

    # ------------------------------------------------------------------------------------------------------------------

    def find_user(self, unique_identifier: tuple[str, int]) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to find specific user record using special identifier.

        Possible first tuple slot (zeroed index):
            -   "user_id"
            -   "discord_id"

        :param unique_identifier:   Two slot tuple, where the first element is always one of the columns of Users table
                                    that have unique constraint. And the second is the value that you want to look for.
        :type unique_identifier:    tuple[str, int]

        :return:    If the record was found, then it will return it.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """

        def find_user_user_id(user_id: int) -> tuple[str, tuple[str]]:
            return "SELECT * FROM users WHERE user_id = %s;", tuple([str(user_id)])

        def find_user_discord_id(discord_id: int) -> tuple[str, tuple[str]]:
            return "SELECT * FROM users WHERE discord_id = %s;", tuple([str(discord_id)])

        mode_selector = {
            "user_id": find_user_user_id,
            "discord_id": find_user_discord_id
        }

        mode = mode_selector.get(unique_identifier[0])(unique_identifier[1])

        record: list[tuple[Any, ...]] = self._ask(mode[0], mode[1])

        if len(record) != 0:
            return record

    def find_picture(self, unique_identifier: tuple[str, Any]) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to find specific picture record using special identifier.

        Possible first tuple slot (zeroed index):
            -   "picture_id"
            -   "url"
            -   "image_hash"
            -   "delete_hash"

        :param unique_identifier:   Two slot tuple, where the first element is always one of the columns of Pictures
                                    table that have unique constraint. And the second is the value that you want to look
                                    for.
        :type unique_identifier:    tuple[str, Any]

        :return:    If the record was found, then it will return it.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """

        def find_picture_picture_id(picture_id: int) -> tuple[str, tuple[str]]:
            return """   SELECT * FROM pictures AS p 
                        INNER JOIN (
                            SELECT p.picture_id, COALESCE(SUM(v.vote_value), 0) AS suma FROM pictures AS p
                                LEFT JOIN votes AS v USING(picture_id)
                            GROUP BY p.picture_id
                        ) AS s USING(picture_id)
                    WHERE picture_id = %s AND picture_id NOT IN (
                        SELECT pa.picture_id FROM pictures AS pa
                            INNER JOIN reports AS ra USING(picture_id)
                            INNER JOIN banned AS ba USING(report_id)
                    )
                    GROUP BY picture_id
                    ORDER BY RAND() 
                    LIMIT 1;
              """, tuple([str(picture_id)])

        def find_picture_url(url: str) -> tuple[str, tuple[str]]:
            return "SELECT * FROM pictures WHERE url = %s;", tuple(url, )

        def find_picture_image_hash(image_hash: str) -> tuple[str, tuple[str]]:
            return "SELECT * FROM pictures WHERE image_hash = %s;", tuple(image_hash, )

        def find_picture_delete_hash(delete_hash: str) -> tuple[str, tuple[str]]:
            return "SELECT * FROM pictures WHERE delete_hash = %s;", tuple(delete_hash, )

        mode_selector = {
            "picture_id": find_picture_picture_id,
            "url": find_picture_url,
            "image_hash": find_picture_image_hash,
            "delete_hash": find_picture_delete_hash
        }

        mode = mode_selector.get(unique_identifier[0])(unique_identifier[1])

        record: list[tuple[Any, ...]] = self._ask(mode[0], mode[1])

        if len(record) != 0:
            return record

    def find_report(self, unique_identifier: tuple[str, int, ...]) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to find specific report record using special identifier.

        Possible first tuple slot (zeroed index) can be one of:
            -   "report_id"
            -   "picture_id_&_discord_id"

        :param unique_identifier:   Two slot tuple, where the first element is always one of the columns of Users table
                                    that have unique constraint. And the second is the value that you want to look for.
        :type unique_identifier:    tuple[str, int]

        :return:    If the record was found, then it will return it.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """

        def find_report_report_id(report_id: int, extra) -> tuple[str, tuple[str]]:
            return "SELECT * FROM reports WHERE report_id = %s;", tuple([str(report_id)])

        def find_report_picture_id_discord_id(picture_id: int, discord_id: int) -> tuple[str, tuple[str, str]]:
            return """SELECT * FROM reports WHERE user_id IN (SELECT user_id FROM users WHERE discord_id = %s) AND 
                      picture_id = %s;""", (str(discord_id), str(picture_id))

        mode_selector = {
            "report_id": find_report_report_id,
            "picture_id_&_discord_id": find_report_picture_id_discord_id
        }

        mode = mode_selector.get(unique_identifier[0])(unique_identifier[1], unique_identifier[2])

        record: list[tuple[Any, ...]] = self._ask(mode[0], mode[1])

        if len(record) != 0:
            return record
        return None

    def random_picture(self) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to get a random picture record that has a score value grater than PICTURE_SUCCESS.

        :return:    If the record was found, then it will return it.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """
        sql = """   SELECT * FROM pictures AS p 
                        INNER JOIN (
                            SELECT p.picture_id, COALESCE(SUM(v.vote_value), 0) AS suma FROM pictures AS p
                                LEFT JOIN votes AS v USING(picture_id)
                            GROUP BY p.picture_id
                        ) AS s USING(picture_id)
                    WHERE s.suma >= %s AND picture_id NOT IN (
                        SELECT pa.picture_id FROM pictures AS pa
                            INNER JOIN reports AS ra USING(picture_id)
                            INNER JOIN banned AS ba USING(report_id)
                    )
                    GROUP BY picture_id
                    ORDER BY RAND() 
                    LIMIT 1;
              """
        data: tuple = (str(PICTURE_SUCCESS),)
        record: list[tuple[Any, ...]] = self._ask(sql, data)

        if len(record):
            return record
        return None

    def random_picture_wait_room(self) -> Optional[list[tuple[Any, ...]]]:
        """
        Method used to get a random picture record from waiting room (score value less than PICTURE_SUCCESS).

        :return:    If the record was found, then it will be returned.
        :rtype:     Optional[list[tuple[Any, ...]]]

        :except mysql.connector.Error:  Any of the exception from "mysql.connector" libreary.
        :except NoConnection:           Exception from "connection_exceptions.py" file, created by Dominik Breksa. See
                                        its description to understand its occurrence.
        """
        sql = """   SELECT * FROM pictures AS p 
                        INNER JOIN (
                            SELECT p.picture_id, COALESCE(SUM(v.vote_value), 0) AS suma FROM pictures AS p
                                LEFT JOIN votes AS v USING(picture_id)
                            GROUP BY p.picture_id
                        ) AS s USING(picture_id)
                    WHERE s.suma < %s AND picture_id NOT IN (
                        SELECT pa.picture_id FROM pictures AS pa
                            INNER JOIN reports AS ra USING(picture_id)
                            INNER JOIN banned AS ba USING(report_id)
                    )
                    GROUP BY picture_id
                    ORDER BY RAND() 
                    LIMIT 1;
              """
        data: tuple = (str(PICTURE_SUCCESS),)
        record: list[tuple[Any, ...]] = self._ask(sql, data)

        if len(record):
            return record
        return None
