# Project 1 Write Up

**Author:** Gagana Ramesh (gxb210015)  
**Professor:** Salazar  
**Date:** 12 March 2026
**Time:** 3:22 PM

**Thoughts so far:**
The driver is the most complex part. It needs to spawn the logger and encrypter
as subprocesses, communicate through pipes, and handle user input with a menu.
I need to be careful about the order of reads/writes to avoid pipe deadlocks.

**Plan for this session:**
Build the driver with the menu system, subprocess spawning, and basic
encrypt/decrypt/password/history/quit commands.

**Session notes:**
Got the driver working with the menu loop. It spawns logger and encrypter
using Popen and communicates through stdin/stdout pipes.
Had an issue where the passkey command was "clogging" the pipe because
I was trying to read stdout from the encrypter even though PASSKEY
only outputs "RESULT" with no extra data. Fixed it by still reading
the RESULT line but not displaying it.
History is working — stores all input strings for reuse.