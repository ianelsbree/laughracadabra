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
define marble = Character("Marble", color="#000000")
define beef = Character("Beef")

# Wizard health variables
default skaterHealth = 0
default gothHealth = 0
default gunHealth = 0

label scene_select:
    menu:
        "Where should I go next?"

        "The Skatepark":
            jump skater_wiz

        "The Coffee Shop":
            jump goth_cafe

        "The Desert":
            jump gun_wiz
        
        "The Tropics":
            jump frog_wiz

        "Beef's House":
            jump beef_house

# The game starts here.
label start:
    scene bg dark
    
    play music "audio/bgm intro.mp3"

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

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05

    skater_wizard "What's groovy, man?{w=1.0} What's your name?" (window_background="gui/boring_textbox.png")

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

    show marble neutral

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    
    marble "...Hi."

    marble "..."

    marble "......"

    marble "...What can I get you?"

    menu:
        extend ""
        "Bad joke. (Replace this with dialogue.)":
            marble "Zzz."

        "Good joke. Made her laugh. (Replace this with dialogue.)":
            play sound "audio/sfx clownhonk.mp3"

            $ gothHealth += 1

            if gothHealth == 1:
                show hp 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 3:
                show hp 3

    menu:
        "Bad joke 2. (Replace this with dialogue.)":
            marble "You're not funny."

        "Good joke. Made her laugh. (Replace this with dialogue.)":
            play sound "audio/sfx clownhonk.mp3"

            $ gothHealth += 1

            if gothHealth == 1:
                show hp 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 3:
                show hp 3

    menu:
        "Bad joke 3. (Replace this with dialogue.)":
            marble "You suck."

        "Good joke. Made her laugh. (Replace this with dialogue.)":
            play sound "audio/sfx clownhonk.mp3"

            $ gothHealth += 1

            if gothHealth == 1:
                show hp 1
            if gothHealth == 2:
                show hp 2
            if gothHealth == 3:
                show hp 3
    
    marble "Get out."

    if gothHealth >= 3:
        jump clown_town
    if gothHealth <= 0:
        jump down_town
    else:
        jump scene_select


label gun_wiz:

    scene bg gundesert
    with fade

    me "Add dialogue."

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05

    jump scene_select

label beef_house:
    scene bg beefhouse
    with fade

    show beef hag

    "This decrepit old man welcomes you."

    beef "Oh... welcome, sonny, to my humble dwelling."

    show beef hag_grab

    beef "Here, let me get a little more comfortable..."

    show beef neutral
    show hp 0:
            zoom 0.5
            xalign 0.05
            yalign 0.05

    beef "That's better."

    me "Haha what if joke."

    show beef neutral_boob
    with hpunch

    beef "AHAHAHAHAAA what a jester you are!"

label frog_wiz:
    scene bg frogroom
    with fade

    jump scene_select

label clown_town:
    scene bg clowntown
    play music "audio/bgm clowntown.mp3"

    me "Hehehehehe."

    menu:
        extend ""
        "Accept your fate.":
            return

    return

label down_town:
    scene bg downtown

    me "Damn."

    return
