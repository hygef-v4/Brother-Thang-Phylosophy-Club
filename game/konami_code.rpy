init python:
    konami = ["K_UP", "K_UP", "K_DOWN", "K_DOWN", "K_LEFT", "K_RIGHT", "K_LEFT", "K_RIGHT", "K_b", "K_a"]
    konami_input = []

    def check_konami(key):
        global konami_input
        konami_input.append(key)

        if len(konami_input) > len(konami):
            konami_input.pop(0)

        if konami_input == konami:
            konami_input = []
            renpy.call_in_new_context("konami_menu")

screen konami_listener():
    key "K_UP" action Function(check_konami, "K_UP")
    key "K_DOWN" action Function(check_konami, "K_DOWN")
    key "K_LEFT" action Function(check_konami, "K_LEFT")
    key "K_RIGHT" action Function(check_konami, "K_RIGHT")
    key "K_a" action Function(check_konami, "K_a")
    key "K_b" action Function(check_konami, "K_b")

label konami_menu:
    menu:
        "Cheat Menu"
        "Jump Chapter 1":
            jump ch1_day1_day2
        "Jump Chapter 2":
            jump ch2_day3
        "Jump Chapter 3":
            jump ch3_dianoia
        "Add money":
            $ stats.modify_tien(1000000)
        "Max live":
            $ stats.modify_doi_song(100)
        "Max study":
            $ stats.modify_hoc_tap(100)
        "Exit":
            return
