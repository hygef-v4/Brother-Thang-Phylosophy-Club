init python:
    import datetime
    menu_trans_time = 1

    splash_message_default = "Trải nghiệm này không nhằm giải trí.\nHãy đọc chậm, và tự suy nghĩ."

    splash_messages = [
        "Ta là ai, nếu không có ký ức?",
        "Ý nghĩa có tồn tại nếu không có người quan sát?",
        "Im lặng cũng là một câu trả lời.",
        "Không phải mọi câu hỏi đều cần đáp án.",
        "Bạn có chắc mình đang lựa chọn?",
        "Tri thức là nhớ lại. — Plato",
        "Tôi tư duy, vậy nên tôi tồn tại. — Descartes",
        "Người ta luôn bị lên án để tự do. — Sartre",
        "Con người là thước đo của vạn vật. — Protagoras",
        "Sống không được kiểm chứng không đáng sống. — Socrates"
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

# Ghost art and glitch removed for philosophy focus

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 180
    zoom 0.25
    menu_logo_move

image menu_particles:
    block:
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=35, particleTime=5.0, particleXSpeed=4, particleYSpeed=3).sm
        alpha 0.6
        5.0
        repeat

image menu_particles_slow:
    block:
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=25, particleTime=7.0, particleXSpeed=2, particleYSpeed=2).sm
        alpha 0.5
        7.0
        repeat

image menu_particles_fast:
    block:
        ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=30, particleTime=3.5, particleXSpeed=6, particleYSpeed=4).sm
        alpha 0.7
        3.5
        repeat

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -400
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

label splashscreen:
    python:
        import datetime
        process_list = []
        currentuser = ""

        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass

            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)

                    if user:
                        currentuser = user
            except:
                pass

    python:
        firstrun = ""

        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass

    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            # Quick menu enabled for ESC access

            scene black

            menu:

                "A previous save file has been found. Would you like to delete your save data and start over?"

                "Yes, delete my existing data.":

                    "Deleting save data...{nw}"

                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()

                "No, continue where I left off.":

                    $ restore_relevant_characters()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.first_run:
        python:
            restore_all_characters()

        # Quick menu enabled for ESC access

        scene white

        pause 0.5

        scene tos
        with Dissolve(1.0)

        pause 1.0

        "Trải nghiệm này chứa các nội dung mang tính triết học và tự vấn."

        "Nó không đưa ra câu trả lời, chỉ đặt ra câu hỏi."

        menu:

            "Bằng cách tiếp tục, bạn đồng ý rằng đây là một trải nghiệm tư duy, không phải giải trí thụ động."

            "Tôi đồng ý.":

                pass

        $ persistent.first_run = True

        scene tos2
        with Dissolve(1.5)

        pause 1.0

        scene white


    # Character file checks removed for philosophy focus

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]

            a = range(1,12)

            for i in range(3):
                b = renpy.random.choice(a)

                persistent.special_poems[i] = b

                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')

    if persistent.autoload:
        jump autoload

    $ config.allow_skipping = True  # Always allow skipping

    # Ghost menu and s_kill_early removed for philosophy focus

    show white

    $ splash_message = renpy.random.choice(splash_messages)  # Always show philosophical message
    $ config.main_menu_music = audio.t1

    $ renpy.music.play(config.main_menu_music)

    $ starttime = datetime.datetime.now()

    show intro with Dissolve(0.5, alpha=True)

    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())

    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())

    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)

    $ config.allow_skipping = True

    return

label after_load:

    if persistent.playthrough == 0:
        $ restore_all_characters()

    $ config.allow_skipping = True  # Always allow skipping
    $ _dismiss_pause = config.developer

    $ style.say_dialogue = style.normal

    # Yuri kill and anticheat removed for philosophy focus
    if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
        $ persistent.first_load = True

        call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())

    return

label autoload:

    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen

            del _old_game_menu_screen

        if "_old_history" in globals():
            _history = _old_history

            del _old_history

        renpy.block_rollback()

        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    # Yuri kill removed for philosophy focus

    if renpy.get_return_stack():
        $ renpy.pop_call()

    jump expression persistent.autoload

# autoload_yurikill removed for philosophy focus

label before_main_menu:

    $ config.main_menu_music = audio.t1

    return

label quit:

    return

label readonly:

    scene black

    "The game cannot be run because you are trying to run it from a read-only location."

    "Please copy the DDLC application to your desktop or other accessible location and try again."

    $ renpy.quit()

    return

