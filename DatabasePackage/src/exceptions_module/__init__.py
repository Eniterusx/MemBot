# pylint: disable=line-too-long

"""
Module that contains exceptions thrown by all classes in other modules.

Modules covered by these exceptions inside:

o.n.|   Name of module      |   Referencing file including exceptions
----|-----------------------|-------------------------------------------------------------------------------------------
1.  |   connection_module   |   connection_exceptions.py
2.  |   verification_module |   verification_exceptions.py
3.  |   manage_module       |   writing_exceptions.py, reading_exceptions.py

!IMPORTANT!

-   Please note that, because there is present inheritance, between modules classes, sometimes you need to import more
    files, than shown here. For more information, on what exceptions are thrown, by what method it is advised to see
    full description of the previously considered method in its class. There will be a list of all of them.

-   No tests are being developed dor this module, because it only contains exception classes.

In "database_not_working_pictures" directory are located some pictures, that are shown when discord user is trying to
execute a Meme-bot command, while the connection with a database was not established.
"""
