# ================================================
# BROTHER THANG PHILOSOPHY CLUB - MAIN ENTRY POINT
# ================================================

label start:
    # Entry point của game
    # Reset characters and styles to ensure clean state for New Game
    $ quick_menu = True
    $ restore_all_characters()
    $ style.say_dialogue = style.normal
    $ config.allow_skipping = True
    $ _dismiss_pause = config.developer

    # Call Chapter 1 Day 1+2
    call day0
    
    # Sau khi ch1 kết thúc, return về main menu
    return
