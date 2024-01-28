# The script of the game goes in this file.

define skatein = MoveTransition(6.0, enter=offscreenright, enter_time_warp=_warper.easein)
define skateout = MoveTransition(6.0, leave=offscreenleft, enter_time_warp=_warper.easeout)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character("You")
define narrator = Character(what_italic=True)
define bo = Character("Bo")
define melon = Character("Melondy", color="#000000")

# The game starts here.

label start:

    scene bg dark

    "Dark. Everything is dark."

    "Then, a light."

    scene bg light

    me "What? Where am I?"

    "A sign reads, \"Welcome to wizard purgatory!\""

    me "Wizard purgatory? Huh. Well, I am a wizard, and I did just die, so I guess that makes sense!"

    me "What else does the sign say?"

    "\"To escape wizard purgatory, you must best the NUMBER OF WIZARDS Slippery Sorcerers!\""

    me "What the heck is a Slippery Sorcerer?"

    me "I think I see something in the distance over there. It looks like... a skate park?"

    menu:

        "Head towards the run down skate park":
            jump skater_wiz



label skater_wiz:

    scene bg skatepark

    "You make your way across the baren field of purgatory until you find yourself at an old skate park."

    "It looks like it hasn't been touched since the 90's. There's graffiti everywhere."

    show bo neutral
    with skatein

    bo "What's groovy, man?{w} What's your name?"

    me "[name], nice to meet you."

    return


label goth_cafe:

    "You make your way across a baren field to a small, cozy cafe made of black brick. The aroma of strong coffee and bitter chocolate emenates from the little building."

    me "A coffee shop in purgatory? Huh, maybe this place isn't so bad--"

    "A tired looking goth lady walks up to the counter in front of you."

    melon "...hi."

    melon "..."

    melon "......."

    melon "...What can I get you?"

    return
