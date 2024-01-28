# The script of the game goes in this file.

define skatein = MoveTransition(6.0, enter=offscreenright, enter_time_warp=_warper.easein)
define skateout = MoveTransition(6.0, leave=offscreenleft, enter_time_warp=_warper.easeout)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define name = "You"
define me = Character("[name]")
define narrator = Character(what_italic=True)
define skater_wizard = Character("Skater Wizard")
define bo = Character("Bo Rad")
define melon = Character("Melondy", color="#000000")

# Wizard health variables
default skaterHealth = 3
default gothHealth = 3
default gunHealth = 3

# The game starts here.
label start:

    scene bg dark

    "Dark. Everything is dark."

    "Then, a light."

    scene bg light with dissolve

    me "What? Where am I?"

    scene bg giftshop with dissolve

    "A gift shop."

    me "Oh, the gift shop! Look at all these mugs! They've all got cool names on them."

    "What does that sign say?"

    "{size=+10}\"TAKE A MUG ON YOUR WAY OUT\"{/size}"
    
    me "They're all so good! Which one should I choose?"

    menu:

        "Gorgonzola":
            $ name = "Gorgonzola"

        "Carbon Tetrafluoride":
            $ name = "Carbon Tetrafluoride"

        "Sasquatch":
            $ name = "Sasquatch"

        "Tepid":
            $ name = "Tepid"

        "Quintessential":
            $ name = "Quintessential"

        "Milk Steak":
            $ name = "Milk Steak"

        "Canned Frosting":
            $ name = "Canned Frosting"

        "Blackberry like the phone":
            $ name = "Blackberry like the phone"

        "Mug":
            $ name = "Mug"

        "Fried Milk":
            $ name = "Fried Milk"

    "You pick up the mug with \"[name]\" inscribed on it."

    "Another sign on the wall: {size=+5}\"SKATEPARK THATAWAY\"{/size} with an arrow pointing out the door."

    "You step outside, and see a run-down skatepark nearby."

    menu:
        "Head to the skatepark":
            jump skater_wiz
        
        "Fuck that. Let's go to the cafe.":
            jump goth_cafe


label skater_wiz:

    scene bg skatepark
    with fade

    "It looks like it hasn't been touched since the 90's. There's graffiti everywhere."

    show bo neutral
    with skatein

    skater_wizard "What's groovy, man?{w=1.0} What's your name?"

    show hp 3:
        xalign 0.0
        yalign 0.0

    pause 2.0

    me "[name], nice to meet you."

    skater_wizard "Well hey there, [name], and what an odd name that is. My name's Bo!{p=1.0}That's short for Skateboard Radical."

    bo "What brings your here?"

    return


label goth_cafe:

    # scene bg cafe

    "You make your way across a baren field to a small, cozy cafe made of black brick. The aroma of strong coffee and bitter chocolate emenates from the little building."

    me "A coffee shop in purgatory? Huh, maybe this place isn't so bad--"

    "A tired looking goth lady walks up to the counter in front of you."

    show hp 3:
        xalign 0.0
        yalign 0.0
    
    melon "...hi."

    melon "..."

    melon "......."

    melon "...What can I get you?"

    menu:
        "Bad choice. Take damage. (Replace this with dialogue.)":
            $ gothHealth -= 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 1:
                show hp 1
            if gothHealth <= 0:
                show hp 0

            "Ouch."

        "Mid choice. No damage. (Replace this with dialogue.)":
            "Boring."
        
    menu:
        "Bad choice 2. Take damage. (Replace this with dialogue.)":
            $ gothHealth -= 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 1:
                show hp 1
            if gothHealth <= 0:
                show hp 0
            
            "Ouch."

        "Mid choice. No damage. (Replace this with dialogue.)":
            "Zzz."
    
    menu:
        "Bad choice 3. Take damage. (Replace this with dialogue.)":
            $ gothHealth -= 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 1:
                show hp 1
            if gothHealth <= 0:
                show hp 0

            "Ouch."

        "Mid choice. No damage. (Replace this with dialogue.)":
            "..."
    
    melon "Get out."
    if gothHealth <= 0:
        jump clown_town
    else:
        jump gun_wiz

    return


label gun_wiz:
    scene bg desert

    me "Add dialogue."

    show hp 3:
        xalign 0.0
        yalign 0.0
    
    return


label clown_town:
    scene bg clowntown
    
    me "Damn."

    return
