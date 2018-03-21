# Stegano
Information Security using Steganography over Cryptography

The Stegano Project aims to implement a pure form of Steganography.
Its final goal is to take any form of medium(Source Data)and hide User Data in it
by implementing a technique called Steganography.

Steganography is an alternate method to hide data as compared to encryption which
incorporates default methods of scrambling or messing with user data. Steganography
on the other hand simply hides User Data in an inconspicuous way within a medium
so that the final data looks like any regular non important form of data.
Hiding encrypted data within a medium takes it a step further and maximizes Security

Stegano aims to provide a complete solution for secure data encapsulation within a medium
and showcasing various different methods available to do that.

## Dependencies
pip3 install -r requirements.txt

## Road Map
* Read the data
* Apply encryption algorithm on the data
* Use image as an interface and perform minor changes on image using the encrypted data
* Read the image and extract those changes
* Collect all the changes in proper order
* Decrypt the ordered encrypted data to extract original data
* Result can be split into different mediums

## Possible Upgradation
* Input data can be of any form be it audio, video, image, text etc.
* Can use audio, video, image as possible interface
* <s>Result can be split into different mediums</s>
