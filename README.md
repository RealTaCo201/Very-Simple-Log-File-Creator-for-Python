# Very-Simple-Log-File-Creator-for-Python
As simple as... Import logger, create a logger object with output folder, then object.log("whatever you want")

All you need to do is add "import logger" to the beggining of your program,
create a logger object like this: mylogger = logger.Logger("output folder goes here"),
and finally log whatever you want with: mylogger.log("whatever you want to add to your log file")

It will be saved in a file called logmonth-day-year.txt like this: log8-18-2022.txt

Everytime the log function is called it will add a new line to the log file like this:
mm-dd-yy@h:m:s:  whatever you logged
