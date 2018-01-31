# Pokemon functions!
# Answer key to building the 'catch_pokemon' function

from random import randint

"""
This function will attempt to capture a pokemon. 
Success is random, but better conditions => better chance of capturing the pokemon

Arguments:
pokemon: string corresponding to pokemon name
ball_type: string corresponding to pokeball type
health_color: string corresponding to pokemon health color
ailment: boolean corresponding to whether the pokemon is ailing
legendary: boolean corresponding to whether the pokemon is legendary
"""
def catch_pokemon(pokemon, ball_type, health_color, ailment, legendary):
    chanceOfSuccess = 0
    if ball_type == "normal":
        chanceOfSuccess += 10
    elif ball_type == "great":
        chanceOfSuccess += 20
    elif ball_type == "ultra":
        chanceOfSuccess += 30
    elif ball_type == "master":
        return "Successfully caught " + pokemon

    if health_color == "green":
        chanceOfSuccess += 15
    elif health_color == "yellow":
        chanceOfSuccess += 25
    elif health_color == "red":
        chanceOfSuccess += 35
    
    if ailment:
        chanceOfSuccess += 10
    
    if legendary:
        chanceOfSuccess -= 10
    if not legendary:
        chanceOfSuccess += 10
    
    randNum = randint(0, 100):
    if randNum < chanceOfSuccess:
        return "Successfully caught " + pokemon
    else:
        return "Failed to catch " + pokemon

