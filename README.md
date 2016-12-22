# Project GymLocker

A student / lock / locker recordkeeping system

I made this for my high school, but I believe it was dropped. The code here should be better than Project Exchange's, but I can't make any guarantees that it's *good*. Most of the code is hook-ins to the database anyhow. All of this project except for this file is original code from ~3 years ago except for parts where I've sensitive information was held.

## Overview

I may go back and edit this, but a thorough overview is already given on my personal website [here](http://mattrasto.me/project/gymlocker/).

## Technologies

I used the following tools:

* Python
* Django
* MySQL

## Main Model

The main model goes (somewhat) like this:

1. User does things on website
2. Django takes requests and fires appropriate functions in DatabaseScripts folder (in Utilities folder)
3. DatabaseScripts hooks into database and does any necessary retrieving / updating of records

## Using the Code

If you want to use the code, feel free. The "gym_locker1.mwb" file contains the MySQL database schema which should have just one model inside called "gym_locker". Then you just need to install the Python packages necessary (I think just Django, though there might be more) and it should work. I've put "\***" in place of any info that needs to be filled in.
