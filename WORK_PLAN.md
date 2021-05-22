request
1) type
1.1) text
1.2) image
1.3) video
1.4) sound
2) ts
3) content
3.1) text
3.1.1) message
3.2) image, video, sound
3.2.1) name

Text:
1) Date
1.1) Weekend - print emoji 6 or 7
(https://coderoad.ru/25707222/%D0%BF%D0%B5%D1%87%D0%B0%D1%82%D1%8C-python-emoji-%D0%B2-%D0%B2%D0%B8%D0%B4%D0%B5-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-unicode)
1.2) Otherwise - print number of words in content, without counting the same word twice

Image:
1) extension is JPG - print name without extension
2) Otherwise - print (ts - 24 hours)(86400 sec)

Video:
1) Date:
1.1) Weekend:
1.1.1) If if file extension contains 4 characters - print OK
1.1.2) Otherwise - print REJECT
1.2) Otherwise 
1.2.1) If if file extension contains 3 characters - print OK
1.2.2) Otherwise - print REJECT

Sound:
1)Print the first unique character in content
2) if it does not exist - print None
