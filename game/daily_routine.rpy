# ================================================
# DAILY ROUTINE SYSTEM (Day 4-9)
# Brother Thang Philosophy Club
# ================================================

label daily_routine_loop:
    # Daily routine cho Day 4-9: Farm stats period
    
    # Check if reached Day 10 (Chapter 3)
    if current_day >= 10:
        # Transition to Chapter 3
        jump ch3_dianoia
    
    # Show stats UI
    show screen stats_display
    
    # Daily stats update
    $ daily_changes = stats.update_daily()
    
    # Show daily stat changes
    if daily_changes != 0:
        $ show_stat_change("tien", daily_changes)
    
    # ========================================
    # MORNING ACTIVITY (SÁNG)
    # ========================================
    
    scene black
    centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5, hard=True)
    
    call daily_activity
    
    # ========================================
    # AFTERNOON ACTIVITY (CHIỀU)
    # ========================================
    
    scene black
    centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.5, hard=True)
    
    call daily_activity
    
    # ========================================
    # EVENING DORM (TỐI)
    # ========================================
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(2.0, hard=True)
    
    call daily_dorm
    
    # ========================================
    # END OF DAY - INCREMENT DAY COUNTER
    # ========================================
    
    $ current_day += 1
    
    # Loop back for next day (Day 4→9)
    jump daily_routine_loop


# ========================================
# MORNING ACTIVITY
# ========================================

label daily_activity:
    scene bg class_day with fade
    play music daily_life fadein 1.0
    
    menu:
        "Đến CLB":
            jump daily_clb
        
        "Đến Thư viện":
            jump daily_library
        
        "Đến Gym":
            jump daily_gym
    
    return

# ========================================
# EVENING DORM ACTIVITIES
# ========================================

label daily_dorm:
    scene bg ktx with wipeleft_scene  # Custom: Ký túc xá FPT
    play music tense fadein 1.0
    
    "Về phòng, kết thúc một ngày dài..."
    
    menu:
        "Nói chuyện với Xỉu":
            show xiu 1a at t11
            
            xiu "\"Chào mừng đến với dịch vụ Campuchia gì cũng tôn của Xỉu. Cu em cần gì nào?\""
            
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
                        xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                        "..."
                    else:
                        show monika 2p
                        xiu "\"Không có tiền thì nghỉ!\""
                
                "Dịch vụ bồi bổ sức khỏe (20,000 VNĐ)":
                    if stats.tien >= 20000:
                        $ stats.modify_tien(-20000)
                        $ show_stat_change("tien", -20000)
                        
                        $ stats.modify_doi_song(10)
                        $ show_stat_change("doi_song", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show monika 1k
                        xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                        "..."
                    else:
                        show monika 2p
                        xiu "\"Không có tiền thì nghỉ!\""
                
                "Không cần":
                    show monika 2a
                    xiu "\"Thế thôi...\""
            
            hide xiu with dissolve
        
        "Đi ngủ":
            mc "\"Mệt quá, ngủ sớm vậy...\""
    
    # End of day summary
    scene black with fade
    play music sad fadein 1.0
    
    mc "(ngáp) \"Ngày mai lại là một ngày mới...\""
    
    $ renpy.pause(1.0)
    
    stop music fadeout 2.0
    
    return

# ========================================
# REUSABLE ACTIVITIES
# ========================================

label daily_clb:
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    menu:
        "Giúp đỡ Hải Nữ":
            show yuri 1a at t11
            hainu "\"Cậu tới rồi à? Giúp tôi một số việc được không?\""
            mc "\"Dạ, vâng ạ.\""
            
            # Good relationship gains
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 6, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            $ stats.modify_tien(50000)
            $ show_stat_change("tien", 50000)
            
            hide yuri with dissolve
        "Quay lại":
            jump daily_activity
    
    return

label daily_library:
    scene bg library with wipeleft_scene  # Custom: Thư viện FPT
    play music daily_life fadein 1.0
    
    menu:
        "Ôn bài":
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
        "Quay lại":
            jump daily_activity
    
    return

label daily_gym:
    scene bg gym with wipeleft_scene  # Custom: Phòng gym FPT
    
    menu:
        "Luyện tập":
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
        "Quay lại":
            jump daily_activity
    
    return
