# VeeamSoftwareTestTask
Program to synchronize two folders, writing into a log file every time there's a change.

Features:

Synchronization: The replica folder is modified to match the source folder.
Periodically synchronization, time defined by the user.
Logging: Logs are created every time a change is made after a synchronization.

How to use:
1 Run the command "python sync_folders.py" on the console. 
2 When the program opens it'll ask for 3 prompts:
  The source folder Path
  The replica folder Path
  The interval between synchronizations in minutes.
  
After running it, just leave the program open and every x minutes it will synchronize the folders.

Every time there is a change in the replica folder the program appends to (or creates if it's the first time) a log file called: Replica_Log_File.txt

