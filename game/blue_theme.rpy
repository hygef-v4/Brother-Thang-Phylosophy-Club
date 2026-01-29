init -1:
    # Define Blue Theme Assets using modern MatrixColor (Hue shift ~220deg for Pink -> Blue)
    image textbox_blue = Transform("gui/textbox.png", matrixcolor=HueMatrix(240)) # Pink to Blue shift
    image namebox_blue = Transform("gui/namebox.png", matrixcolor=HueMatrix(240))
    # Animated Blue Backgrounds
    image menu_bg_blue:
        topleft
        Transform("gui/menu_bg.png", matrixcolor=HueMatrix(240))
        menu_bg_loop

    image game_menu_blue:
        topleft
        Transform("gui/menu_bg.png", matrixcolor=HueMatrix(240))
        menu_bg_loop

    image main_menu_blue = Transform("gui/main_menu.png", matrixcolor=HueMatrix(240))
    
    # Overlays
    image overlay_game_menu_blue = Transform("gui/overlay/game_menu.png", matrixcolor=HueMatrix(240))
    image overlay_main_menu_blue = Transform("gui/overlay/main_menu.png", matrixcolor=HueMatrix(240))
    image menu_nav_blue:
        Transform("gui/overlay/main_menu.png", matrixcolor=HueMatrix(240))
        menu_nav_move

    # Choice button backgrounds
    image choice_hover_blue = Transform("gui/button/choice_hover_background.png", matrixcolor=HueMatrix(240))

    # Slot button backgrounds
    image slot_idle_blue = Transform("gui/button/slot_idle_background.png", matrixcolor=HueMatrix(240))
    image slot_hover_blue = Transform("gui/button/slot_hover_background.png", matrixcolor=HueMatrix(240))

    # Menu Particles
    image menu_particles:
        SnowBlossom("gui/menu_particle.png", count=10, border=50, xspeed=(20, 50), yspeed=(20, 50), start=0, fast=True, horizontal=True)
