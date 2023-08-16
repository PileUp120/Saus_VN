# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    play music "audio/Bocchi_Screams.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Ivan" "GACHA"

    "Ivan" "GACHAGACHAGACHAGACHA"

    "Ivan" "ivan.exe is not working"


    # This ends the game.
label sprite:
    "Ayana" "Have you noticed something's wrong with Ivan"
    show cursed
    "Ayana" "Boo"
    return
