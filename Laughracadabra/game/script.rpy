# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("You")
define world = Character("")
define bo = Character("Bo")
define melon = Character("Melondy", color="#000000")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    me "*Dark. Everything is dark.*"

    me "*Then, a light.*"

    me "What? Where am I?"

    world "*A sign reads, \"Welcome to wizard purgatory!\"*"

    me "Wizard purgatory? Huh. Well, I am a wizard, and I did just die, so I guess that makes sense!"

    me "What else does the sign say?"

    world "*\"To escape wizard purgatory, you must best the NUMBER OF WIZARDS Slippery Sorcerers!\"*"

    me "What the heck is a Slippery Sorcerer?"

    me "I think I see something in the distance over there. It looks like... a skate park?"

    menu:
      
        "Head towards the run down skate park":
            jump skater_wiz



label skater_wiz:

    world "You make your way across the baren field of purgatory until you find yourself at an old skate park."

    world "It looks like it hasn't been touched since the 90's. There's graffiti everywhere."

    world "A really cool looking teenager approaches you on a super rad skateboard."



    return


label goth_cafe:

    world "You make your way across a baren field to a small, cozy cafe made of black brick. The aroma of strong coffee and bitter chocolate emenates from the little building."

    me "A coffee shop in purgatory? Huh, maybe this place isn't so bad--"

    world "A tired looking goth lady walks up to the counter in front of you."

    melon "...hi."

    melon "..."

    melon "......."

    melon "...What can I get you?"

    # This ends the game.
    return
