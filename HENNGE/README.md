https://challenge.hennge.com/

! Mission 1 and 2
Take input of string of integers and return sum of squares in GO language without using for loop and store it in secret gist --> pretty easy to do!


! Mission 3 --> extremely challenging

successful code file - totp1.py

initial attempt - totp.py

Generate a 10 digit TOTP valid for 30 sec based on rfc 6238 using a secret userid(email) and suffix (HENNGECHALLENGE003)

T0 = 0

timestep = 30 second

POST request your url of secret gist to https://api.challenge.hennge.com/challenges/003  with basic auth having passwd as TOTP

Read - https://datatracker.ietf.org/doc/html/rfc6238 for reference  

CREDITS - https://github.com/yodalee/

