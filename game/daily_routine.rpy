# ================================================
# DAILY ROUTINE SYSTEM (Day 4-9)
# Brother Thang Philosophy Club
# ================================================

label daily_routine_loop:
    # Daily routine cho Day 4-9: Farm stats period
    
    # Check if reached Day 10 (Chapter 3)
    if current_day >= 10:
        # Transition to Chapter 3
        scene black with dissolve_scene_full
        stop music fadeout 2.0
        
        centered "{size=40}{color=#ff0000}CHAPTER 3{/color}{/size}\n{size=24}Day 10{/size}\n{size=18}Coming Soon...{/size}"
        $ renpy.pause(3.0, hard=True)
        
        call screen coming_soon_ch3
        return
    
    # Show stats UI
    show screen stats_display
    
    # Daily stats update
    $ daily_changes = stats.update_daily()
    
    # Show daily stat changes
    $ show_stat_change("hoc_tap", daily_changes["hoc_tap"])
    $ show_stat_change("doi_song", daily_changes["doi_song"])
    $ show_stat_change("rel_xiu", daily_changes["rel_xiu"])
    $ show_stat_change("tien", daily_changes["tien"])
    
    # ========================================
    # MORNING ACTIVITY (SÁNG)
    # ========================================
    
    scene black
    centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5, hard=True)
    
    call daily_morning_activity
    
    # ========================================
    # AFTERNOON ACTIVITY (CHIỀU)
    # ========================================
    
    scene black
    centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5, hard=True)
    
    call daily_afternoon_activity
    
    # ========================================
    # EVENING DORM (TỐI)
    # ========================================
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Về ký túc xá{/size}"
    $ renpy.pause(2.0, hard=True)
    
    call daily_evening_dorm
    
    # ========================================
    # END OF DAY - INCREMENT DAY COUNTER
    # ========================================
    
    $ current_day += 1
    
    # Loop back for next day (Day 4→9)
    jump daily_routine_loop


# ========================================
# MORNING ACTIVITY
# ========================================

label daily_morning_activity:
    scene bg class_day with fade
    play music daily_life fadein 1.0
    
    menu:
        "Chọn hoạt động buổi sáng:"
        
        "Đến CLB":
            jump daily_clb_morning
        
        "Đến Thư viện":
            jump daily_library_morning
        
        "Đến Gym":
            jump daily_gym_morning
    
    return


# ========================================
# AFTERNOON ACTIVITY
# ========================================

label daily_afternoon_activity:
    scene bg class_day with fade
    play music daily_life fadein 1.0
    
    menu:
        "Chọn hoạt động buổi chiều:"
        
        "Đến CLB":
            jump daily_clb_afternoon
        
        "Đến Thư viện":
            jump daily_library_afternoon
        
        "Đến Gym":
            jump daily_gym_afternoon
    
    return


# ========================================
# EVENING DORM ACTIVITIES
# ========================================

label daily_evening_dorm:
    scene bg ktx with wipeleft_scene  # Custom: Ký túc xá FPT
    play music tense fadein 1.0
    
    "Về đến phòng, kết thúc một ngày dài..."
    
    menu:
        "Làm gì trước khi ngủ?"
        
        "Nói chuyện với Xỉu":
            show monika 1d at t11
            
            xiu "\"Ê cu em! Hôm nay thế nào?\""
            
            menu:
                "Dịch vụ gia sư học tập (20,000 VNĐ)":
                    if stats.tien >= 20000:
                        $ stats.modify_tien(-20000)
                        $ show_stat_change("tien", -20000)
                        
                        $ stats.modify_hoc_tap(10)
                        $ show_stat_change("hoc_tap", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show monika 1k
                        xiu "\"OK! Chị dạy cho.\""
                        "..."
                    else:
                        show monika 2p
                        xiu "\"Nghèo thế mà học?\""
                
                "Dịch vụ bồi bổ sức khỏe (20,000 VNĐ)":
                    if stats.tien >= 20000:
                        $ stats.modify_tien(-20000)
                        $ show_stat_change("tien", -20000)
                        
                        $ stats.modify_doi_song(10)
                        $ show_stat_change("doi_song", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show monika 1k
                        xiu "\"Đi đây!\""
                        "..."
                    else:
                        show monika 2p
                        xiu "\"Không tiền thì nghỉ!\""
                
                "Không cần":
                    show monika 2a
                    xiu "\"Vậy sao.\""
            
            hide monika with dissolve
        
        "Đi ngủ luôn":
            mc "\"Mệt quá, ngủ sớm vậy...\""
    
    # End of day summary
    scene black with fade
    play music sad fadein 1.0
    
    mc "(ngáp) \"Ngày mai lại là một ngày mới...\""
    
    $ renpy.pause(1.0)
    
    stop music fadeout 2.0
    
    return


# ========================================
# REUSABLE ACTIVITIES - MORNING
# ========================================

label daily_clb_morning:
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Đến CLB, không gian yên tĩnh..."
    
    show yuri 1a at t11
    
    hainu "\"Chào cậu.\""
    
    mc "\"Chào chị.\""
    
    menu:
        "Nói chuyện với Hải Nữ":
            hainu "\"Hôm nay có gì muốn học không?\""
            mc "\"Dạ, em muốn tìm hiểu thêm về triết học.\""
            
            "Hải Nữ chia sẻ thêm về triết học..."
            
            # Balanced gains for farming
            $ stats.modify_hoc_tap(8)
            $ show_stat_change("hoc_tap", 8)
            
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 7, multiplier)
            $ show_stat_change("rel_hainu", gained)
        
        "Giúp Hải Nữ kế toán (kiếm tiền)":
            "Ngồi đọc sách triết học và giúp chị kế toán..."
            
            # Earn money + study + relationship
            $ bonus = 15000
            $ stats.modify_tien(bonus)
            $ show_stat_change("tien", bonus)
            
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
            
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 5, multiplier)
            $ show_stat_change("rel_hainu", gained)
    
    hide yuri with dissolve
    return

label daily_library_morning:
    scene bg library with wipeleft_scene  # Custom: Thư viện FPT
    play music daily_life fadein 1.0
    
    "Thư viện yên tĩnh, thích hợp để học..."
    
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
    
    # Balanced study gains
    $ stats.modify_hoc_tap(12)
    $ show_stat_change("hoc_tap", 12)
    $ stats.modify_doi_song(-3)
    $ show_stat_change("doi_song", -3)
    
    return

label daily_gym_morning:
    scene bg gym with wipeleft_scene  # Custom: Phòng gym FPT
    
    "Phòng gym, rèn luyện sức khỏe..."
    
    menu:
        "Nâng tạ":
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
            $ stats.modify_doi_song(15)
            $ show_stat_change("doi_song", 15)
        
        "Chạy bộ":
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
            $ stats.modify_doi_song(15)
            $ show_stat_change("doi_song", 15)
    
    return


# ========================================
# REUSABLE ACTIVITIES - AFTERNOON
# ========================================

label daily_clb_afternoon:
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "CLB buổi chiều có nhiều người hơn..."
    
    menu:
        "Học triết":
            # Good study gains
            $ stats.modify_hoc_tap(8)
            $ show_stat_change("hoc_tap", 8)
        
        "Nói chuyện với Hải Nữ":
            show yuri 1a at t11
            hainu "\"Buổi chiều cậu vẫn ở đây à?\""
            mc "\"Dạ, em muốn học thêm với chị.\""
            
            # Good relationship gains
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 6, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            $ stats.modify_hoc_tap(4)
            $ show_stat_change("hoc_tap", 4)
            
            hide yuri with dissolve
    
    return

label daily_library_afternoon:
    scene bg library with wipeleft_scene  # Custom: Thư viện FPT
    play music daily_life fadein 1.0
    
    "Thư viện buổi chiều đông người..."
    
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
    $ stats.modify_doi_song(-2)
    $ show_stat_change("doi_song", -2)
    
    return

label daily_gym_afternoon:
    scene bg gym with wipeleft_scene  # Custom: Phòng gym FPT
    
    "Gym buổi chiều, tập cùng mọi người..."
    
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
    $ stats.modify_doi_song(12)
    $ show_stat_change("doi_song", 12)
    
    return
