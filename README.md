# xkcdpwd
xkcd password generator

I wrote this because I didn't want to use the bloated xkcd password generators on github. 

# Usage

genpw.py takes 0 or 1 arguments. 

Running genpw.py without any arguments will default to generating a 10 word long password. 

Running genpw.py with 1 integer argument will cause it to generate a n-word-long password where n is the argument supplied. 

Example:

	python3 genpw.py 15

This will generate a 15-word-long password. 

To allow running the script without explicitly invoking python:

	chmod +x genpw.py 

# Notes

The random number is generated using os.urandom(), which means it is OS dependent. Make sure os.urandom() generates truly random numbers on your system. 

# Background

In 2012, an attacker with a few thousand dollars of equipment can guess hundreds of billions of passwords per second. 

That means more than a quadrillion passwords per hour (10^15). 

Having millions of such rigs allows guessing a quintillion (10^18) passwords per second. 

Global hashes per second in 2018 surpassed 20 exahashes per second (10^19) and will probably surpass 100 exahashes (10^20) by the end of the decade. 

There are about 10^9 seconds in 50 years. 

Assuming compute power doubles every year, and that currently we are at 2^67 passwords per second, in 50 years we will be at 10^35 passwords per second. 

This means that in a few decades, 128 bits of entropy will no longer be safe. To be "future-proof" you will need at least 160 bits of entropy.  

To be secure from an adversary capable of cracking 10^35 passwords per second for 50 years, we want to draw our passwords from a potential password pool of at least 10^44 or about 2^148 passwords. 

In the xkcd example, 4 words are drawn from a pool of 2^11 words for a total of 2^44 bits of entropy, or approximately 10^13. This can be cracked in less than 1 second by a machine in 2012. It is not secure. 

If you are drawing from a pool of 2^11 words then you will need about 14 words to be safe. 

If you are drawing from a pool of 2^16 words then you will need about 10 words to be safe. 

If you are drawing from a pool of 2^6 chars then you will need about 25 characters to be safe. 

**UPDATE:** A CMU study has found that using words instead of random characters does not increase memorability, making this entire exercise pointless. You might as well just remember 25 random characters instead. See: [Correct horse battery staple:
Exploring the usability of system-assigned passphrases][http://cups.cs.cmu.edu/soups/2012/proceedings/a7_Shay.pdf]

The words should be separated by spaces because otherwise your long passwords may be guessed by shorter password guessers e.g a 4 word strength password like "book case the rapist" can potentially be guessed by a 2-word guessing algorithm. 


Note: If the words are not completely randomly chosen and randomly arranged then you no longer have any security guarantees. You can re-roll, but you must not modify the password to make it "easier to remember" (nor for any other reason).  

