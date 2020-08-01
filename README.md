# Password-Manager
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![pm](https://user-images.githubusercontent.com/68439180/89103017-7b5d0a80-d3c3-11ea-8a86-a4309d1c3fa8.gif)


## About 
An easy to understand and implement password manager that efficiently stores account details of various websites. The passwords, before storing, are encrypted using the ROT cipher. When a user retrieves a password, it is decrypted back into its original form.
To use the password manager, the user is first required to create a master account<br>
Programming Language: **Python** <br>
**Learn more about ROT here:** [ROT Cipher](https://www.dcode.fr/rot-cipher)
## Requirements 
To install a requirement, you can download from the link mentioned.
- **Python**            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Download Python](https://www.python.org/downloads/)

## Implementation 
- Open CMD, navigate to the working directory. Type in:  ```python Password_Manager.py``` or double click the code file to execute the program.
- If the user is using the manager for the first time, he/she will be required to create a master account. Thereafter, the user can just login using these master credentials.
- After logging in, the user has the options to store, retrieve, delete the account details of a specific site or exit the manager.
- When the user enters his/her account details, the password is encrypted before storing. The encryption is done using ROT cipher.
- If the user chooses to view his account details, the password is decrypted and the details are displayed.

## Notes 
- Only **ONE** account's details (the most recent one) will be stored.

