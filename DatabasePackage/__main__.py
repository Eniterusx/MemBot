from DatabasePackage.src.manage_module.manage_database import ManageDatabase as Manage
from DatabasePackage.src.verification_module.data_verification import Verification as Verify

"""
Run this main to test to check if you have connection to a database. (it will print one record from a database).
"""

if __name__ == "__main__":
    with Manage() as M:
        print(M.random_picture())  # If nothing prints out than you do not have connection to a database :( .

        # Tests
