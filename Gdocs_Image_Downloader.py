# Google drive mass image downloader - ElijahC

import wget

defaultLink = "https://drive.usercontent.google.com/download?id={0}&export=download" # Default link to download a file from gdocs instead of view, script will break if google change this

f = open("Gdoc_Links.yaml", "r") # You can use a different text file if you want, if you are having issues here paste in the whole path
count = 0
for x in f:
    if x[0] == '<' or x[0:8] == 'https://':
        count = count + 1
        wget.download(defaultLink.format((x.split('/'))[5]), './{0}.JPG'.format(count)) #Outputs to current directory, change '' for different output location
