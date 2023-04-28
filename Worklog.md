03/28/2023
- Set up aws account
- Set up github repo and am able to push info to it

04/17/2023
- Got python running on laptop and ran a hello world function
- Installed requests pacakge locally (using pip) and then was able to download a pdf file from url (in bytes)
- Did some searching and found a pdf reader for python to install 
- Tried to directly convert response object to Pdf reader but ran into issues and had to pause

04/18/2023
- Saved PDF to OS and then was able to pass the PDF into the reader 
- Reader isn't able to cleanly extract text yet. Need to play around with that (or possibly consider other ways of extracting text)

04/28/2023
- Switched to using PDF plumber and was able to extract text.
- Started moving things to own functions to not have a monolith
- Time to start actually doing something with the text :D 