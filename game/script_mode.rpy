label script_mode:
    $ script_m = True
    $ quick_menu = True
    $ restore_all_characters()
    $ style.say_dialogue = style.normal
    $ config.allow_skipping = True
    $ _dismiss_pause = config.developer

    $ stats.modify_doi_song(100)
    $ stats.modify_hoc_tap(100)
    $ stats.modify_relationship("xiu", 100)
    $ stats.modify_relationship("hainu", 100)

    call day0

    $ current_day = 2
    call daily_routine_loop
    
    $ current_day = 6
    call daily_routine_loop

    $ current_day = 8
    call daily_routine_loop

    if not xiu_script:
        $ stats.modify_relationship("xiu", -100)

    $ current_day = 10
    call daily_routine_loop

    if not hainu_script:
        $ stats.modify_relationship("hainu", -100)

    $ current_day = 13
    call daily_routine_evening