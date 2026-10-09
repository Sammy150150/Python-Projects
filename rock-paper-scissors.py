import urllib
import requests

while True:
    randomURL = "https://www.random.org/integers/?num=1&min=1&max=3&col=1&base=10&format=plain&rnd=new"
    response = requests.get(randomURL)
    randomNum = response.text.strip()

    if randomNum == "1":
        computerChoice = "Rock"
    elif randomNum == "2":
        computerChoice = "Paper"
    elif randomNum == "3":
        computerChoice = "Scissors"

    playerChoice = input("Rock Paper Scissors: ")

    playerChoiceLowercase = playerChoice.casefold()
    computerChoiceLowercase = computerChoice.casefold()

    print(computerChoice)

    if playerChoiceLowercase == computerChoiceLowercase:
        print("Tie")
    elif (
        (playerChoiceLowercase == 'rock' and computerChoiceLowercase == 'paper') or
        (playerChoiceLowercase == 'paper' and computerChoiceLowercase == 'scissors') or
        (playerChoiceLowercase == 'scissors' and computerChoiceLowercase == 'rock')
    ):
        print("You Lose")

    elif (
        (playerChoiceLowercase == 'rock' and computerChoiceLowercase == 'scissors') or
        (playerChoiceLowercase == 'paper' and computerChoiceLowercase == 'rock') or
        (playerChoiceLowercase == 'scissors' and computerChoiceLowercase == 'paper')
    ):
        print("You Win")
    else:
        print("Invadid")
