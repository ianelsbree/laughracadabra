# The script of the game goes in this file.

define skatein = MoveTransition(6.0, enter=offscreenright, enter_time_warp=_warper.easein)
define skateout = MoveTransition(6.0, leave=offscreenleft, enter_time_warp=_warper.easeout)

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define name = "You"
define me = Character("[name]")
define narrator = Character(what_italic=True)
define skater_wizard = Character("Skater Wizard", image="bo")
define bo = Character("Bo Rad", color="#ff47cc", image="bo")
define marble = Character("Marble", color="#000000", image="marble")
define beef = Character("Beef", color="#000062", image="beef")
define slip = Character("Slip", color="#1e2900", image="slip")
define slay = Character("Slay", color="#61012d", image="slay")
define gun = Character("Gun", color="#6b1414", image="gun")
define judge = Character("", what_font="Jokerman-Regular.ttf", what_size=40)
define shrimp = Character("The High Prawn Wizard", image="shrimp")
define frog = Character("Frogbert", color="#3a703aff", image="frog")

# Wizard health variables
default skaterHealth = 0
default gothHealth = 0
default gunHealth = 0
default frogHealth = 0
default beefHealth = 0
default devilHealth = 0
default bugHealth = 0
default shrimpHealth = 0

define judgement = 0
image spinner_clown = Movie(play="spin_for_clowntown.mpeg", loop=False, keep_last_frame=True)
image spinner_down = Movie(play="spin_for_downtown.mpeg", loop=False, keep_last_frame=True)

label scene_select:
    menu:
        "Where should I go next?"

        "The Skatepark":
            jump skatepark_scene

        "The Coffee Shop":
            jump cafe_scene

        "The Desert":
            jump desert_scene
        
        "The Tropics":
            jump tropics_scene

        "Beef's House":
            jump beef_scene
        
        "The Town Square":
            jump town_scene

        "The Ocean Floor":
            jump ocean_floor

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
            jump skatepark_scene

        # "Fuck that. Let's go to the cafe.":
        #     jump cafe_scene

label skatepark_scene:

    scene bg skatepark
    with fade

    "It looks like it hasn't been touched since the 90's. There's graffiti everywhere." (window_background="gui/boring_textbox.png")

    show bo neutral
    with skatein

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    with easeinleft

    skater_wizard "What's groovy, man?{w=1.0} What's your name?" (window_background="gui/boring_textbox.png")

    me "I'm {w=1.5}{nw}" (name="You", window_background="gui/boring_textbox.png")

    with vpunch

    me "I'm {fast}[name], nice to meet you."

    skater_wizard "Well hey there, [name], and what an odd name that is. My name's Bo!{p=1.0}That's short for Skateboard Radical."
    
    show bo explain

    bo "Well, you must be new here! You're gonna meet a lot of interesting folks today."

    bo "It's in your best interest to use the spells in your spell book to make them all laugh!"

    menu:
        "Why?":

            bo "You'll see!"

        "Okay":

            bo "Alright, let's see..."

    bo "Everyone you meet will be weak to a certain type of humor."

    bo "Let's see what spells you've got!"

    narrator "\"Propose\""

    bo "Woah! That's a powerful spell! You won't make it through this with just one spell though. Let me lend you a hand and teach you some of mine."

    bo "I put an enchantment on your spell book as well, to help you choose spells, so you don't have to look through the whole thing every time."

    bo "How about you try to make me laugh? I'll give you a hint, my favorite kind of joke is a knock knock joke!"

    menu:

        "Knock knock?":

            bo "Who's there?"

            me "Ice cream."

            bo "Ice cream who?"

            me "ICE CREAM SO YOU CAN HEAR ME!"
            play sound "audio/sfx clownhonk.mp3"

            $ skaterHealth += 1

            if skaterHealth == 1:
                show hp 1
            if skaterHealth == 2:
                show hp 2
            if skaterHealth == 3:
                show hp 3

            bo "Heh... That was pretty groovy. Why don't you try another one?"

        "How does a penguin guild its house?":

            bo "How?"

            me "Igloos it together!"

            bo "... {p}Well, not terrible, but it's not my kind of joke."

            bo "Why don't you try again?"

    menu:

        "Knock knock!":

            bo "Who's there?"

            me "Interupting cow."

            bo "Interupting cow wh--?"

            me "MOOOOO!"
            play sound "audio/sfx clownhonk.mp3"

            $ skaterHealth += 1

            if skaterHealth == 1:
                show hp 1
            if skaterHealth == 2:
                show hp 2
            if skaterHealth == 3:
                show hp 3

            bo "You've got some totally tubular jokes! Gimme one more!"

        "What do you call a fly without wings?":

            bo "What?"

            me "A walk!"

            bo "...{p}I'm sure thta joke would work for someone else, but remember, I like {bold}knock knock jokes{/bold}."

            bo "Try again."

    menu:

        "What's the difference between a piano and a fish?":

            bo "What?"

            me "You can tune a piano, but you can't tuna fish!"

            bo "...{p}If you'd been funnier, I would have laughed. Like this!"

            show bo thumb

        "Knock, knock!":

            bo "Who's there?"

            me "Cash."

            bo "Cash who?"

            me "No thanks, but I'd love some peanuts!"

            show bo thumb
            play sound "audio/sfx clownhonk.mp3"

            $ skaterHealth += 1

            if skaterHealth == 1:
                show hp 1
            if skaterHealth == 2:
                show hp 2
            if skaterHealth == 3:
                show hp 3

            bo "RADICAL! I think you're ready to go!"

    bo "I'll send word of your arrival to the others.{p}Good luck, [name]!"


    menu:
        "Explore the field":
            jump cafe_scene

label cafe_scene:

    scene bg cafe
    with fade

    play music "audio/bgm cafe.mp3"

    "You make your way across a baren field to a small, cozy cafe made of black brick. The aroma of strong coffee and bitter chocolate emenates from the little building."

    me "A coffee shop? Huh, maybe this place isn't so bad-"

    "A tired looking goth lady walks up to the counter in front of you."

    show marble neutral
    with easeinright

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    with easeinleft
    
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
        extend ""
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
        extend ""
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

    menu:
        "Go adventuring in the desert.":
            jump desert_scene

    if gothHealth >= 3:
        jump clown_town
    if gothHealth <= 0:
        jump down_town


label desert_scene:

    scene bg gundesert
    with fade

    show gun neutral

    me "Add dialogue."

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    with easeinleft

    menu:
        "Enter the apartment.":
            jump beef_scene

label beef_scene:
    define boob_flag = False
    
    scene bg beefhouse
    with fade

    play music "audio/bgm beefhouse.mp3"

    show beef hag

    "This decrepit old man welcomes you."

    beef "Oh... welcome, sonny, to my humble dwelling."

    beef grab "Here, let me get a little more comfortable..."

    show beef neutral
    with hpunch
    
    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    with easeinleft

    beef "That's better."

    beef "So go on. Make me laugh!"

    me "Uhh... Let's see..." 

    menu:
        "What's the difference between an old bus stop and a lobster with big breasts?":

            beef "Hmm?"

            me "One's a crusty bus station, and the other's a busty crustacean!"

            $ boob_flag = True
            beef boob @ laugh "Aha! That's a good one!"
            play sound "audio/sfx clownhonk.mp3"

            $ beefHealth += 1

            if beefHealth == 1:
                show hp 1
            if beefHealth == 2:
                show hp 2
            if beefHealth == 3:
                show hp 3

        "Why was six afraid of seven?":

            beef "Why?"

            me "Because seven ate nine!"

            beef @ irritated "A numbers joke? Laaaaame."

    beef "Let's see what else you've got!"

    menu:
        "Want to hear a poop joke?":

            beef "Yes! Tell me."

            me "Ah never mind, they all stink!"
            
            $ boob_flag = True
            beef boob @ laugh "Ha! I like that. You're real funny."
            play sound "audio/sfx clownhonk.mp3"

            $ beefHealth += 1

            if beefHealth == 1:
                show hp 1
            if beefHealth == 2:
                show hp 2
            if beefHealth == 3:
                show hp 3

        "What did the triangle say to the square?":

            beef "What?"

            me "You're pointless!"

            if boob_flag:
                beef boob @ irritated "Dude, shapes? Really? Not cool."
            else:
                beef @ irritated "Dude, shapes? Really? Not cool."

    beef "Alright, last try. Give me everything you've got!"

    menu:

        "Are monsters good at math?":

            beef "I don't know, are they?"

            me "Not unless you Count Dracula!"

            beef @ irritated "That joke sucks, man. Two thumbs down."

        "What do you call a cow with no legs?":

            beef "I don't know, what?"

            me "Ground beef!"

            $ boob_flag = True

            beef boob @ laugh "Ground beef! Because he's on the ground! Ahahaha."
            play sound "audio/sfx clownhonk.mp3"

            $ beefHealth += 1

            if beefHealth == 1:
                show hp 1
            if beefHealth == 2:
                show hp 2
            if beefHealth == 3:
                show hp 3

    if boob_flag:
        beef boob "Now get outta here, kid."
    else:
        beef "Now get outta here, kid."


    menu:
        "Take a trip to the tropics.":
            jump tropics_scene

label tropics_scene:

    scene bg frogroom
    with fade

    play music "audio/bgm tropics.mp3"

    show hp 0:
        zoom 0.5
        xalign 0.05
        yalign 0.05
    
    show frogfrog speak
    frog "Ribbit."

    show frogfrog neutral

    menu:
        "What the fuck.":
            show frogfrog speak
            frog "Have you never seen excellence before?"
            me "My apologies. I didn't mean to offend."
        
        "Oh, I love frogs!":
            show frogfrog laugh
            frog "Finally, a person with taste in this hellscape."

        "Kiss the frog.":
            show frogfrog disgust
            frog "Stay away from me."
            me "Shut it and listen to this."

    show frogfrog neutral

    menu:
        "Bad joke.":
            show frogfrog disgust

            frog "Don't strain yourself."

        "Good joke.":
            show frogfrog laugh
            $ frogHealth += 1

            frog "Ribbit, ribbit! I'll have to tell my colleagues at the lab that one."

    if frogHealth == 1:
        show hp 1
    if frogHealth == 2:
        show hp 2
    if frogHealth == 3:
        show hp 3

    jump scene_select


label ocean_floor:
    scene bg oceanfloor
    with fade

    me "Am I underwater???"

    show shrimp neutral
    shrimp "BEHOLD, mere mortal!"

    me "..."

    shrimp "You DARE approach me? 'Tis I, the HIGH PRAWN WIZARD!"

    shrimp "Tell me a witty jest, at your peril!!!"
    show hp 0:
            zoom 0.5
            xalign 0.05
            yalign 0.05

    me "Alright, let's give it a shot..."

    menu:
        "What do you call a prawn who will not share his plant material, decaying organic matter, micro-organisms, small shellfish and worms?":
            shrimp "Hmm?"
            me "Shelfish!"
            show shrimp mad
            shrimp "Not funny!"

        "What did one prawn say to his special prawn friend?":

            shrimp "Do tell me!"

            me "You're one in a krillion!!!"
            play sound "audio/sfx clownhonk.mp3"

            $ shrimpHealth += 1

            if shrimpHealth == 1:
                show hp 1
            if shrimpHealth == 2:
                show hp 2
            if shrimpHealth == 3:
                show hp 3

            show shrimp laugh
            shrimp "Ah! Ah ha ha!"

    show shrimp neutral
    shrimp "Tell me another, you fool!"

    menu:
        "What happened to the prawn who's business took off?":

            shrimp "Tell me! I must know!"

            me "They became a krillionaire!"
            play sound "audio/sfx clownhonk.mp3"

            $ shrimpHealth += 1

            if shrimpHealth == 1:
                show hp 1
            if shrimpHealth == 2:
                show hp 2
            if shrimpHealth == 3:
                show hp 3

            show shrimp laugh
            shrimp "Wow! You are a very amusing mortal!"

        "How did the prawn perish?":

            shrimp "How did they indeed?"

            me "They contracted a deadly krillness!"

            show shrimp mad
            shrimp "That is not a funny topic! I do not laugh! No no!"

    show shrimp neutral
    shrimp "One last chance at a joke for you!"

    menu:
        "What did the prawn say when discussing options for urban housing?":

            shrimp "Hmm?"

            me "Apartment complex? I find it quite SHRIMPLE!"

            shrimp "..."

            shrimp "......"

            show shrimp laugh
            play sound "audio/sfx clownhonk.mp3"
            shrimp "OH, I understand! Because I am a shrimp! Hahahahahahaha!!!"

            $ shrimpHealth += 1

            if shrimpHealth == 1:
                show hp 1
            if shrimpHealth == 2:
                show hp 2
            if shrimpHealth == 3:
                show hp 3

        "What do opposing prawns do in warfare?":

            shrimp "Do tell?"

            me "They Krill each other!"

            shrimp "..."

            shrimp "......"

            show shrimp mad
            shrimp "Not amusing enough. Begone!"

    show shrimp neutral
    shrimp "Perhaps we shall meet again, mere mortal. Now begone from my throne of the High Prawn Wizard!"



label town_scene:
    
    scene bg townsquare
    with fade

    show slay talk_closed
    show slip talk_closed

    slip "Howdy!"

    slay "Meowdy."

    jump scene_select

label judgement_scene:

    scene bg spinner
    with fade

    judge "Welcome to your judgement!"

    judge "Let's see where you're headed!"

    $ judgement = renpy.random.randint(0, 1)
    # $ judgement = 1

    if judgement == 0:
        jump judgement_clown
    else:
        jump judgement_down
        
    label judgement_clown:
        $ renpy.movie_cutscene("spin_for_clowntown.mpeg")
        play sound "audio/bgm harpup.mp3"
        scene landed_on_clowntown
        judge "Looks like you're headed to Clowntown!"
        jump clown_town
        
    label judgement_down:
        $ renpy.movie_cutscene("spin_for_downtown.mpeg")
        play sound "audio/bgm harpdown.mp3"
        scene landed_on_downtown
        judge "Looks like you're headed Downtown!"
        jump down_town

label clown_town:
    
    scene bg clowntown
    with fade

    play music "audio/bgm clowntown.mp3"

    me "Hehehehehe."

    menu:
        extend ""
        "Accept your fate.":
            return

    return

label down_town:
    scene bg downtown
    with fade

    play music "audio/bgm downtown.mp3"

    me "Damn."

    menu:
        extend ""
        "Accept your fate.":
            return

    return
