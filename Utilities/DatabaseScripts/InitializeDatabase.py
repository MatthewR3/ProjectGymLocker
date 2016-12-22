# --------------------------------------------------
# Module Name:		InitializeDatabase
# Purpose:			Opens a connection with the database
# Author:			Matthew Rastovac
# Date Created:		7/18/15
#
# Current Version: 	1.0
# Last Modified:	7/18/15
# Last Change:		Began development
# --------------------------------------------------

import MySQLdb



# Initializes database and opens connection
def initialize():

    db = MySQLdb.connect("localhost", "root", "***", "gym_locker")
    cursor = db.cursor()

    return db, cursor
