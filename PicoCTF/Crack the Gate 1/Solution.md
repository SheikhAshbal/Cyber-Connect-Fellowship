# picoCTF – Crack the Gate 1 Walkthrough

> Web Exploitation | Login Bypass | Hidden Developer Backdoor  

---

# Challenge Overview

We are given a login portal and the email of the target:
ctf-player@picoctf.org

<img width="1044" height="806" alt="image" src="https://github.com/user-attachments/assets/eed6c442-a1de-4df0-9452-39f276950c75" />


The password is unknown, and brute force attempts fail.

The description hints that *“something feels off… like the developer left a secret way in.”*

That means this is probably not about guessing the password — it’s about finding a logic flaw.

# Step 1 – Inspect the Page Source

The first thing I did was inspect the page source.

Right at the top of the HTML, I noticed this comment:

<!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->

<img width="836" height="96" alt="image" src="https://github.com/user-attachments/assets/6c8b5b50-7290-4596-a858-bb218d486a52" />
That clearly doesn’t look random.

It’s actually ROT13 encoded.

After decoding: NOTE: Jack - temporary bypass: use header "X-Dev-Access: yes"
<img width="1444" height="642" alt="image" src="https://github.com/user-attachments/assets/a27cbe1c-bb52-4cdc-ac9a-bc658b46d7d6" />

That’s the backdoor.
The developer left a temporary header-based bypass and forgot to remove it.

# Step 2 – Understand the Login Request
Looking at the JavaScript:
<img width="628" height="132" alt="image" src="https://github.com/user-attachments/assets/f7f7c5a0-8187-4d29-961e-76069ed89cc4" />

The login request is sent to: /login
So instead of using the form normally, we can manually craft the request and include the special header.

# Step 3 – Exploiting the Header
Using curl:
<img width="577" height="98" alt="image" src="https://github.com/user-attachments/assets/be68a840-bc75-4113-8b53-fa95936b089d" />
Notice:
Password can be anything
The server trusts the X-Dev-Access header

# Step 4 – Getting the Flag
Server response:
<img width="1097" height="206" alt="image" src="https://github.com/user-attachments/assets/3dd528ac-fa77-4a6a-b10d-b17d189a97f3" />

Flag : picoCTF{brut4_f0rc4_3e21b3a3}

