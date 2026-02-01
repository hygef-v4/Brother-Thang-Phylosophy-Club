# ================================================
# DAILY ROUTINE SYSTEM (Day 4-9)
# Brother Thang Philosophy Club
# ================================================

label daily_routine_morning:
    # ========================================
    # MORNING ACTIVITY (SÁNG)
    # ========================================
    
    $ current_day += 1
    scene black with dissolve_scene_full
    
    # Dynamic background selection (Day 4-13)
    if current_day == 4:
        scene bg fpt_7 with fade
    elif current_day == 5:
        scene bg fpt_8 with fade
    elif current_day == 6:
        scene bg fpt_9 with fade
    elif current_day == 7:
        scene bg fpt_10 with fade
    elif current_day == 8:
        scene bg fpt_14 with fade
    elif current_day == 9:
        scene bg fpt_15 with fade
    elif current_day == 10:
        scene bg fpt_16 with fade
    elif current_day == 11:
        scene bg fpt_20 with fade
    elif current_day == 12:
        scene bg fpt_21 with fade
    elif current_day == 13:
        scene bg fpt_22 with fade
    else:
        scene bg fpt_23 with fade
    
    centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5)
    $ current_time_slot = 1
    
    # Daily stats update
    $ daily_changes = stats.update_daily()
    $ show_stat_change("tien", daily_changes)

    if current_day == 3 and script_m:
        scene bg club_day with wipeleft_scene
        play music club_theme fadein 1.0

        call plato_cave

        return
    elif current_day == 7:
        call day7
    elif current_day == 9:
        call day9
    elif current_day == 11:
        call day11
    else:
        call daily_activity

    return

label daily_routine_afternoon:
    # ========================================
    # AFTERNOON ACTIVITY (CHIỀU)
    # ========================================
    if script_m:
        return
    scene black
    
    # Dynamic background selection (Day 4-13)
    if current_day == 4:
        scene bg fpt_24 with fade
    elif current_day == 5:
        scene bg fpt_25 with fade
    elif current_day == 6:
        scene bg fpt_26 with fade
    elif current_day == 7:
        scene bg fpt_27 with fade
    elif current_day == 8:
        scene bg fpt_29 with fade
    elif current_day == 9:
        scene bg fpt_30 with fade
    elif current_day == 10:
        scene bg fpt_31 with fade
    elif current_day == 11:
        scene bg fpt_37 with fade
    elif current_day == 12:
        scene bg fpt_38 with fade
    elif current_day == 13:
        scene bg fpt_39 with fade
    else:
        scene bg fpt_40 with fade
    
    centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5)
    $ current_time_slot = 2
    
    call daily_activity

    return

label daily_routine_evening:
    # ========================================
    # EVENING DORM (TỐI)
    # ========================================
    if script_m and current_day != 13:
        return
    scene black
    
    # Dynamic background selection (Day 4-13)
    if current_day == 4:
        scene bg fpt_12 with fade
    elif current_day == 5:
        scene bg fpt_13 with fade
    elif current_day == 6:
        scene bg fpt_17 with fade
    elif current_day == 7:
        scene bg fpt_18 with fade
    elif current_day == 8:
        scene bg fpt_19 with fade
    elif current_day == 9:
        scene bg fpt_28 with fade
    elif current_day == 10:
        scene bg fpt_32 with fade
    elif current_day == 11:
        scene bg fpt_33 with fade
    elif current_day == 12:
        scene bg fpt_34 with fade
    elif current_day == 13:
        scene bg fpt_35 with fade
    else:
        scene bg fpt_36 with fade
    
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5)
    $current_time_slot = 3
    
    if current_day == 13:
        call day13_evening
    else:
        "Về phòng, kết thúc một ngày dài..."
        call daily_dorm

    # ========================================
    # END OF DAY - INCREMENT DAY COUNTER
    # ========================================
        
    # Loop back for next day (Day 4→9)
    jump daily_routine_loop

label daily_routine_loop:
    call daily_routine_morning
    if script_m:
        return

    call daily_routine_afternoon

    call daily_routine_evening

# ========================================
# MORNING ACTIVITY
# ========================================

label daily_activity:
    scene bg class_day with fade
    play music daily_life fadein 1.0
    
    show screen stats_display
    show screen konami_listener

    menu:
        "Về KTX ngủ":
            # End of day summary
            scene black with fade
            
            $ renpy.pause(2.0)
            
            stop music fadeout 2.0

            return

        "Đến Thư viện ngồi học":
            jump daily_library
        
        "Đến Gym luyện tập":
            jump daily_gym

        "Đến CLB gặp Hội Trưởng":
            jump daily_clb
    
# ========================================
# EVENING DORM ACTIVITIES
# ========================================

label daily_dorm:
    if current_time_slot == 3:
        scene bg ktx with wipeleft_scene  # Custom: Ký túc xá FPT
    else:
        scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0

    show screen stats_display
    show screen konami_listener

    menu:
        "Đi ngủ":
            if current_day == 7:
                call day7_evening

            # End of day summary
            scene black with fade
            
            $ renpy.pause(2.0)
            
            stop music fadeout 2.0

        "Nói chuyện với Xỉu":
            show xiu 1a at t11
            
            xiu "\"Chào mừng đến với dịch vụ Campuchia gì cũng tôn của Xỉu. Cu em cần gì nào?\""
            
            menu:
                "Dịch vụ gia sư học tập (100,000 VNĐ)":
                    if stats.tien >= 100000:
                        $ stats.modify_tien(-100000)
                        $ show_stat_change("tien", -100000)
                        
                        $ stats.modify_hoc_tap(10)
                        $ show_stat_change("hoc_tap", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show xiu happy
                        xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                    else:
                        show xiu angry
                        xiu "\"Không có tiền thì nghỉ!\""
                
                "Dịch vụ bồi bổ sức khỏe (100,000 VNĐ)":
                    if stats.tien >= 100000:
                        $ stats.modify_tien(-100000)
                        $ show_stat_change("tien", -100000)
                        
                        $ stats.modify_doi_song(10)
                        $ show_stat_change("doi_song", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show xiu happy
                        xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                    else:
                        show xiu angry
                        xiu "\"Không có tiền thì nghỉ!\""
                
                "Không cần":
                    show xiu neutral
                    xiu "\"Thế thôi...\""
            
            hide xiu with dissolve
    
    return

# ========================================
# REUSABLE ACTIVITIES
# ========================================

label daily_clb:
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    show screen stats_display
    show screen konami_listener

    if first_talk:
        show hainu neutral at t11
        hainu "\"Cậu tới rồi à? Giúp tôi một số việc được không?\""
        mc "\"Dạ, vâng ạ.\""
        
        $ stats.modify_tien(50000)
        $ show_stat_change("tien", 50000)

        # Good relationship gains
        $ gained = stats.modify_relationship("hainu", 6)
        $ show_stat_change("rel_hainu", gained)
        
        hide hainu with dissolve
    else:
        call plato_cave
    
    return

label daily_library:
    scene bg library with wipeleft_scene  # Custom: Thư viện FPT
    play music library_theme fadein 1.0
    
    show screen stats_display
    show screen konami_listener

    "Giở sách vở ra, ôn lại bài cũ..."
    
    # Stat-dependent dialogue (học tập)
    if stats.hoc_tap < 20:
        mc "\"Ra là thế… Chả hiểu gì cả.\""
    elif stats.hoc_tap < 50:
        mc "\"Hừm…. Bài này khó hiểu quá…\""
    elif stats.hoc_tap < 80:
        mc "\"Có một số chỗ chưa hiểu lắm, lần sau lên lớp hỏi lại cô vậy.\""
    elif stats.hoc_tap < 100:
        mc "\"Ồ, kiến thức mới đã được tiếp thu.\""
    else:
        mc "\"Mấy bài này dễ quá, có lẽ mình nên tìm thứ khác khó hơn.\""
    
    # Balanced afternoon study
    $ stats.modify_hoc_tap(10)
    $ show_stat_change("hoc_tap", 10)
    
    return

label daily_gym:
    scene bg gym with wipeleft_scene  # Custom: Phòng gym FPT
    play music gym_theme fadein 1.0
    
    show screen stats_display
    show screen konami_listener

    "Rèn luyện cơ thể, giải toả tinh thần..."
    
    # Stat-dependent dialogue (sức khoẻ = đời sống)
    if stats.doi_song < 20:
        mc "\"Mệt quá… Chịu rồi...\""
    elif stats.doi_song < 50:
        mc "\"Phù… Nay đến đây thôi vậy.\""
    elif stats.doi_song < 80:
        mc "\"Cố thêm… Một xíu nữa thôi…\""
    elif stats.doi_song < 100:
        mc "\"Chà, tập xong nhìn mình có vẻ đẹp trai hơn rồi đấy.\""
    else:
        mc "\"Mấy cái này nhẹ quá, hết cái nặng hơn rồi à?\""
    
    # Good health gains
    $ stats.modify_doi_song(10)
    $ show_stat_change("doi_song", 10)

    return
