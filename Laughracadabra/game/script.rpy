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

label scene_select:
    menu:
        "Where should I go next?"

        "The Skatepark":
            jump skater_wiz

        "The Coffee Shop":
            jump goth_cafe
        
        "The Desert":
            jump gun_wiz


# The game starts here.
label start:

    scene bg dark

    "Dark. Everything is dark." (window_background="gui/boring_textbox.png")

    "Then, a light." (window_background="gui/boring_textbox.png")

    scene bg light with dissolve

    me "What? Where am I?"  (window_background="gui/boring_textbox.png")

    scene bg giftshop with dissolve

    "A gift shop." (window_background="gui/boring_textbox.png")

    me "Oh, the gift shop! Look at all these mugs! They've all got cool names on them." (window_background="gui/boring_textbox.png")

    "What does that sign say?" (window_background="gui/boring_textbox.png")

    "{size=+10}\"TAKE A MUG ON YOUR WAY OUT\"{/size}" (window_background="gui/boring_textbox.png")

    me "They're all so good! Which one should I choose?" (window_background="gui/boring_textbox.png")

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

    "You pick up the mug with \"[name]\" inscribed on it." (window_background="gui/boring_textbox.png")

    "Another sign on the wall: {size=+5}\"SKATEPARK THATAWAY\"{/size} with an arrow pointing out the door." (window_background="gui/boring_textbox.png")

    "You step outside, and see a run-down skatepark nearby.{nw}" (window_background="gui/boring_textbox.png")

    menu:

        extend ""
        
        "Head to the skatepark.":
            jump skater_wiz
        
        # "Fuck that. Let's go to the cafe.":
        #     jump goth_cafe


label skater_wiz:

    scene bg skatepark
    with fade

    "It looks like it hasn't been touched since the 90's. There's graffiti everywhere." (window_background="gui/boring_textbox.png")

    show bo neutral
    with skatein

    skater_wizard "What's groovy, man?{w=1.0} What's your name?" (window_background="gui/boring_textbox.png")

    show hp 3:
        zoom 0.5
        xalign 0.05
        yalign 0.05

    me "I'm {w=1.5}{nw}" (name="You", window_background="gui/boring_textbox.png")

    with vpunch

    me "I'm {fast}[name], nice to meet you."

    skater_wizard "Well hey there, [name], and what an odd name that is. My name's Bo!{p=1.0}That's short for Skateboard Radical."

    bo "What brings you here?"

    jump scene_select


label goth_cafe:

    scene bg cafe
    with fade

    "You make your way across a baren field to a small, cozy cafe made of black brick. The aroma of strong coffee and bitter chocolate emenates from the little building."

    me "A coffee shop? Huh, maybe this place isn't so bad-"

    "A tired looking goth lady walks up to the counter in front of you."

    show melon neutral
    show hp 3:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    
    melon "...Hi."

    melon "..."

    melon "......"

    melon "...What can I get you?"

    menu:
        extend ""
        "Bad choice. Take damage. (Replace this with dialogue.)":
            $ gothHealth -= 1

            if gothHealth == 2:
                show hp 2
            if gothHealth == 1:
                show hp 1
            if gothHealth <= 0:
                show hp 0

            play sound "audio/sfx clownhonk.mp3"

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
            
            play sound "audio/sfx clownhonk.mp3"

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
            
            play sound "audio/sfx clownhonk.mp3"


            "Ouch."

        "Mid choice. No damage. (Replace this with dialogue.)":
            "..."
    
    melon "Get out."
    if gothHealth <= 0:
        jump clown_town
    else:
        jump gun_wiz

    jump scene_select


label gun_wiz:

    scene bg desert
    with fade

    me "Add dialogue."

    show hp 3:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    
    jump scene_select


label clown_town:
    scene bg clowntown
    play music "audio/bgm clowntown.mp3"
    
    me "Damn."

    return

