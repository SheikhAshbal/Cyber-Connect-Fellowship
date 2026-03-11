# DISKO 1 – PicoCTF Forensics Writeup

## Challenge Information

* **Challenge Name:** DISKO 1
* **Category:** Forensics
* **Author:** Darkraicg492
* **Description:**

  > Can you find the flag in this disk image?

The challenge provides a disk image file:

```
disko-1.dd
```

`.dd` files are raw disk images that may contain files, filesystem data, or hidden information.

---

# Approach

Since the challenge provides a disk image, the first step is to check whether the flag is directly stored inside the image as readable text.

In many CTF challenges, flags follow a known format. For PicoCTF, the format is:

```
picoCTF{...}
```

Therefore, we can search the disk image for any strings matching this format.

---

# Step 1 – Extract Readable Strings

We use the `strings` command to extract human-readable text from the disk image.

```
strings disko-1.dd
```

This prints all readable ASCII strings from the binary file.

---

# Step 2 – Filter for the Flag

Since we know the flag format starts with `picoCTF{`, we can filter the output using `grep`.

```
strings disko-1.dd | grep "picoCTF{"
```

---

# Step 3 – Identify the Flag

Running the command returns:

<img width="409" height="111" alt="image" src="https://github.com/user-attachments/assets/bfe72cc7-a036-4b6e-bc5b-e44bde808584" />

```
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```

This means the flag was stored as a plain string inside the disk image.

---

# Flag

```
picoCTF{1t5_ju5t_4_5tr1n9_c63b02ef}
```



✔ **Challenge Solved**
