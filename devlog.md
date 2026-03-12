# Project 1 Write Up

**Author:** Gagana Ramesh (gxb210015)  
**Professor:** Salazar  
**Date:** 12 March 2026
**Time:** 1:47 PM

**Thoughts so far:**
I realized the Vigenère cipher only works on letters, so I need to make sure
the input going to encrypt/decrypt is only alphabetic characters.
I also need to handle the case where no passkey is set yet.

**Plan for this session:**
Finish the encrypter with proper error output format (ERROR, not [ERROR]).
Make sure it handles uppercase input correctly since the spec says I can assume one case.

**Session notes:**
Got the encrypter working. It reads commands from stdin, parses the command
from the argument, and performs encrypt/decrypt using the Vigenère cipher.
Fixed the error output to use "ERROR" instead of "[ERROR]" to match the spec.
The PASSKEY command now correctly outputs "RESULT" with no argument.