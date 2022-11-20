# File-Hasher

Creating a simlpe method to hash a file with Python.

<h3>Modules Used:</h3><br>
1. hashlib
<br>
<h3>The Process:</h3>
1. The script is pretty straight forward. First we import the hashlib module followed by creating a variable to store the sha256 hash function. We then create a with open statement to read the file being hashed and then ensuring that as long as the file size is greater than 0 we will go ahead and hash that file.<br>
<br>
<br>
<a href="https://imgur.com/36YZQEh"><img src="https://i.imgur.com/36YZQEh.jpg" title="source: imgur.com" /></a>
<br>
<br>
2. The product of the hash script.
<br>
<br>
<a href="https://imgur.com/puVqPJo"><img src="https://i.imgur.com/puVqPJo.jpg" title="source: imgur.com" /></a>
<br>
<br>
<h3>Lessons Learned:</h3>
1. One problem I did run into was an error when the script was trying to locate the file location. <br>
<br>
"SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape"
<br>
<br>
I had to add an "r" to convert the string to a raw string when establishing the file path in the file variable.
