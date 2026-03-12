# Project 1 Write Up

**Author:** Gagana Ramesh (gxb210015)  
**Professor:** Salazar  
**Date:** 12 March 2026
**Time:** 4:18 PM

**Thoughts so far:**
I re-read the spec and realized two things I missed:
1. Input to encrypt, decrypt, and password should only contain letters.
   "Hello World!" should give an error because of the space and exclamation mark.
2. The encrypted/decrypted results should also be saved in the history,
   not just the original input strings.

**Plan for this session:**
Add input validation to reject non-alphabetic input.
Fix history to also append the result after encryption/decryption.
Also want to normalize all input to uppercase before sending to encrypter
since the spec says input should be case insensitive.

**Session notes:**
Added an is_valid_input() function that checks text.isalpha().
Now the driver converts everything to uppercase before sending to the encrypter,
which makes the Vigenère cipher math consistent.
Also fixed history — results are now appended after the RESULT prefix is stripped.
Tested encrypt "HELLO" with passkey "HELLO" and got "OIWWC" which matches the spec example.