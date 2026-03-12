# Project 1 Write Up

**Author:** Gagana Ramesh (gxb210015)  
**Professor:** Salazar  
**Date:** 12 March 2026
**Time:** 2:35 PM

**Thoughts so far:**
The logger is straightforward — it just reads log messages from stdin and
writes them to a file with a timestamp. One thing I need to be careful about
is making sure the timestamp is fresh for each log entry, not just captured once at startup.

**Plan for this session:**
Implement the logger. Make sure the argument check works properly
(need at least 2 args since argv[0] is the script name).

**Session notes:**
Logger is done. It reads from stdin, parses the action from the message,
and writes it in the format YYYY-MM-DD HH:MM [ACTION] MESSAGE.
I made sure datetime.now() is called inside the loop so each entry
gets the actual current time.