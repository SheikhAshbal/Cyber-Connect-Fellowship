# 🔍 Riddle Registry — Finding the Hidden Flag in PDF Metadata
Link : https://play.picoctf.org/practice/challenge/530?difficulty=1&page=1

Sometimes in CTFs, the biggest clue is not in what you see… but in what you don’t see.

Recently, I solved a challenge called “Riddle Registry”, and at first glance, it looked like a simple PDF with random text. But as always in CTFs, if something looks ordinary, it probably isn’t.

Let’s break down how I solved it.

# 📄 The Challenge
The description hinted that the PDF looked like nonsense, but something was hidden inside. That immediately made me think:

If it’s not in the visible content… maybe it’s in the metadata.

That’s a very common trick in file-based challenges.

# Step 1: Opening the PDF
After downloading the file confidential.pdf, I opened it normally.

It contained random text, some blacked-out sections, and nothing that looked like a flag.

At this point, many people might waste time trying to analyze the visible text. But I decided to check something deeper.
<img width="1053" height="1075" alt="image" src="https://github.com/user-attachments/assets/882843a2-5ddc-41df-9421-8441f998b534" />

# Step 2: Checking the Metadata
Instead of using command-line tools, I decided to quickly inspect the metadata using an online tool: https://metadataview.com/

After uploading the PDF, I carefully reviewed the metadata fields:

Title

Producer

File type

Author

And that’s when I noticed something strange.

In the Author field, instead of a normal name, there was this string: cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9mOTQzMDBjNH0=
That definitely didn’t look like a person’s name.
<img width="1230" height="1062" alt="image" src="https://github.com/user-attachments/assets/7082ac4b-0fa3-4b06-a719-f70d1fdbb699" />

# Step 3: Recognizing Base64
The string ended with = — a classic sign of Base64 encoding.

Base64 strings typically:

Use letters and numbers

Include + or /

End with = or ==

So my next move was obvious: decode it.

# Step 4: Decoding with CyberChef
To decode the string, I used one of my favorite tools: https://gchq.github.io/CyberChef/

I selected the From Base64 operation and pasted the suspicious string into the input panel.

And just like that…

The flag appeared: picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}
<img width="1505" height="801" alt="image" src="https://github.com/user-attachments/assets/1c24963c-2df5-4df1-bfc4-b574b1bd40b8" />
