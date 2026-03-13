# Project 1

**Author:** Gagana Bengaluru Ramesh  
**Course:** CS 4348

---

## logger.py

**Usage:** `python logger.py filename.txt`

**Notes:**
- This program is what writes all commands to the log file
- Input is formatted: `ACTION string`
- Use `quit` to stop execution

---

## encrypter.py

**Usage:** `python encrypter.py`

**Notes:**
- This program handles the password for encryption and decryption and the actual encryption and decryption of a string
- Input is formatted: `COMMAND string`
- Command list:
  1. `passkey` — sets passkey to given string
  2. `encrypt` — encrypt given string
  3. `decrypt` — decrypt given string
  4. `quit` — stops execution

---

## driver.py

**Usage:** `python driver.py filename.txt`

**Notes:**
- This program is a wrapper for both the encrypter and logger programs and allows for strings to be encrypted, decrypted, and set as a password
- This program also keeps a history that keeps all given strings to be reused
- Follow Menu and Prompts for input
