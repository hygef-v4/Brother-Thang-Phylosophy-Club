# ================================================
# CHAPTER 2: PISTIS (NIỀM TIN) - DAY 3
# Brother Thang Philosophy Club
# ================================================

label ch2_day3:
    
    # Show stats UI
    show screen stats_display
    
    $ current_day = 3  # FIX: This is Day 3 (Chapter 1 = Day 1+2)
    $ current_chapter = 2
    
    # Daily stats update
    $ daily_changes = stats.update_daily()
    
    # Show daily stat changes
    $ show_stat_change("hoc_tap", daily_changes["hoc_tap"])
    $ show_stat_change("doi_song", daily_changes["doi_song"])
    $ show_stat_change("rel_xiu", daily_changes["rel_xiu"])
    $ show_stat_change("tien", daily_changes["tien"])
    
    stop music fadeout 2.0
    scene bg bedroom with dissolve_scene_full
    
    play music daily_life fadein 1.0
    
    # ========================================
    # SCENE MỞ ĐẦU: KÝ TÚC XÁ - SÁNG
    # ========================================
    
    "Chuông báo thức reo."
    
    mc "(ngáp) \"Buồn ngủ quá… Qua thức xem stream anh Độ hơi khuya rồi…\""
    
    "Tôi mở điện thoại kiểm tra."
    
    mc "\"Tài khoản tự nhiên được cộng thêm tiền này! Là từ chị thủ quỹ tối qua sao?\""
    mc "\"Chà… Người đâu mà đã xinh đẹp, giàu có lại tốt tính. Phú bà của cuộc đời ta đây rồi!\""
    
    "Nhìn lại stats, tiền đã tăng lên khá nhiều nhờ bonus từ Hải Nữ."
    
    # ========================================
    # CLB - SÁNG CHIỀU (Philosophy Discussion)
    # ========================================
    
    scene bg fpt_yard with wipeleft_scene  # Đi qua sân FPT đến CLB
    
    mc "Buổi đầu tiên có lẽ mình nên đến CLB xem thử…"
    
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    # Direct to philosophy conversation with Hải Nữ
    "Tôi đến phòng CLB, thấy Hải Nữ đang ngồi đọc sách."
    
    show yuri 1a at t11
    
    hainu "\"Cậu… Có vẻ đã thoát khỏi cái hang của mình rồi nhỉ?\""
    
    mc "(bối rối) \"Ơ… Dạ?\""
    
    "…"
    
    mc "\"Chuyện lần trước… Cảm ơn chị đã nhắc em về trò lừa bịp của chị Xỉu.\""
    
    show yuri 1f
    
    hainu "\"Không có gì.\""
    
    mc "\"…\""
    mc "\"Mạn phép cho em hỏi, cái từ mà lần trước chị nói khi mới gặp em ấy. Eika… gì ấy nhở?\""
    
    show yuri 2a
    
    hainu "\"Eikasia.\""
    
    mc "\"Nó là gì vậy ạ?\""
    
    show yuri 2f
    
    hainu "\"…\""
    hainu "\"Cậu biết ngụ ngôn về cái hang của Plato chứ?\""
    
    mc "\"Dạ không.\""
    
    show yuri 1a
    
    # ========================================
    # PLATO'S CAVE ALLEGORY
    # ========================================
    
    hainu "\"Ngày xửa ngày xưa, có vài người cổ đại sống ở dưới đáy của một cái hang động.\""
    
    show yuri 1f
    
    hainu "\"Cái hang đấy có một cái lỗ nhỏ, nơi một ít ánh sáng lọt vào.\""
    hainu "\"Từ cái lỗ đó, có những cái bóng lấp ló hắt lên trên bức tường của cái hang.\""
    
    show yuri 2f
    
    hainu "\"Những người cổ đại nhìn thấy nó và đặt tên cho những ảo ảnh này và tin rằng vạn vật chỉ là những cái bóng.\""
    
    show yuri 1a
    
    hainu "\"Một ngày nọ, một người cổ đại tìm được cách thoát ra khỏi cái hang.\""
    hainu "\"Lần đầu tiên trong đời, anh ta thấy được hình dạng thực của những cái bóng.\""
    
    show yuri 2g
    
    hainu "\"Anh ta vui mừng quay lại hang động và kể cho những người bạn nghe.\""
    
    show yuri 2w
    
    hainu "\"Tuy nhiên, những người bạn lại nghĩ anh ta bị điên… Và thế là họ... Cô lập anh ta đến chết.\""
    
    mc "\"Thật là một câu chuyện bi thảm.\""
    
    show yuri 1f
    
    hainu "\"…\""
    hainu "\"Những người cổ đại, họ chỉ thấy những cái bóng.\""
    hainu "\"Họ bị kẹt trong cái gọi là Eikasia. Họ chỉ nhìn thấy những thứ được cho nhìn thấy.\""
    
    show yuri 2f
    
    hainu "\"Vậy theo cậu, người đàn ông tìm được đường ra khỏi hang liệu đã thấy được hình dạng thật của những chiếc bóng?\""
    
    # CHOICE: Philosophy question
    menu:
        hainu "\"Cậu nghĩ sao?\""
        
        "Nhìn thấy được rồi thì tức là thật!":
            mc "\"Nhìn thấy được rồi thì tức là thật!\""
            mc "\"Anh ta đã thoát ra ngoài, đương nhiên là thấy được sự thật rồi.\""
            
            show yuri 1h
            
            hainu "\"Sai rồi.\""
            
            # Không tăng stats
        
        "Có lẽ là chưa….":
            mc "\"Có lẽ là chưa….\""
            mc "\"Làm sao chúng ta biết được thứ bên ngoài hang là thật?\""
            
            show yuri 3a
            
            hainu "\"Chính xác!\""
            
            # Tăng học tập
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 5, multiplier)
            $ show_stat_change("rel_hainu", gained)
    
    show yuri 2k
    
    hainu "(cười mỉm) \"Thật ra thì, cái hang của họ nằm trong một khu bảo tồn người cổ đại!\""
    hainu "\"Những thứ mà người đàn ông đó thấy chỉ là những đồ giả mà thôi.\""
    
    show yuri 2f
    
    hainu "\"Vì vậy, anh ta vẫn chưa thoát khỏi ý niệm của bản thân, vẫn bị kẹt trong Pistis…\""
    hainu "\"Niềm tin dựa trên những gì anh ta nhìn thấy, nhưng chưa phải là chân lý.\""
    
    mc "\"Vậy… Làm sao để thoát khỏi Pistis?\""
    
    show yuri 1f
    
    hainu "\"Đó là con đường dài. Từ Eikasia đến Pistis, rồi Dianoia, và cuối cùng là Noesis.\""
    hainu "\"Nhưng đó là chuyện của những ngày sau. Hôm nay cậu đã hiểu được bước đầu tiên.\""
    
    hide yuri with dissolve
    
    "Bàn luận về triết học cùng Hội Trưởng khiến tôi cảm thấy học được nhiều thứ."
    
    # ========================================
    # TIME SLOT ACTIVITY SYSTEM
    # Buổi SÁNG đã dùng cho Philosophy → Còn CHIỀU + TỐI
    # ========================================
    
    # Initialize time slot variables
    # Buổi sáng đã hết (Philosophy discussion), bắt đầu từ slot 1 (Chiều)
    $ time_slots_used = 1
    $ max_time_slots = 2  # Sáng (đã dùng) + Chiều (còn lại)
    
label ch2_activity_loop:
    
    # Check if all time slots used (both morning and afternoon)
    if time_slots_used >= max_time_slots:
        # Auto transition to evening (dorm)
        jump ch2_evening_transition
    
    # Time period indicator
    if time_slots_used == 0:
        scene black
        centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Chọn hoạt động buổi sáng{/size}"
        $ renpy.pause(1.5, hard=True)
    elif time_slots_used == 1:
        scene black
        centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Chọn hoạt động buổi chiều{/size}"
        $ renpy.pause(1.5, hard=True)
    
    scene bg class_day with fade
    
    # Activity selection menu
    menu:
        "Chọn hoạt động:"
        
        "Đến CLB" if time_slots_used < max_time_slots:
            jump ch2_club_activities
        
        "Đến Thư viện" if time_slots_used < max_time_slots:
            jump ch2_library_activities
        
        "Đến Gym" if time_slots_used < max_time_slots:
            jump ch2_gym_activities
        
        "Bỏ qua (về phòng sớm)":
            jump ch2_evening_transition

# ========================================
# CLB ACTIVITIES
# ========================================

label ch2_club_activities:
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    menu:
        "Làm gì tại CLB?"
        
        "Nói chuyện với Hội Trưởng":
            show yuri 1a at t11
            
            hainu "\"Cậu muốn tìm hiểu thêm về triết học sao?\""
            
            mc "\"Dạ vâng, em thấy những gì chị nói rất thú vị.\""
            
            show yuri 2f
            
            hainu "\"Triết học không chỉ là kiến thức, mà là cách sống.\""
            hainu "\"Mỗi ngày đặt câu hỏi về những gì ta tin là chân lý.\""
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 5, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            # Tăng học tập
            $ stats.modify_hoc_tap(3)
            $ show_stat_change("hoc_tap", 3)
            
            hide yuri with dissolve
            
            # Activity completed - consume time slot
            $ time_slots_used += 1
            jump ch2_activity_loop
        
        "Giúp Hải Nữ kế toán":
            show yuri 1a at t11
            
            hainu "\"Cậu tới đúng lúc lắm, hội trưởng vừa bảo tôi kiểm toán lại chi tiêu tháng vừa rồi.\""
            hainu "\"Tôi để sổ sách đằng kia, cậu ra làm đi.\""
            
            mc "\"Dạ vâng, em làm ngay!\""
            
            show yuri 2f
            
            "Sắp xếp tài liệu..."
            "Kiểm tra số liệu..."
            "Nhập dữ liệu vào máy tính..."
            
            "Cả một núi sổ sách phải giải quyết!"
            
            # Mất thêm 1 time slot vì công việc nhiều
            $ time_slots_used += 1
            
            if time_slots_used > max_time_slots:
                $ time_slots_used = max_time_slots
                
                "Làm việc đến tận chiều muộn mới xong..."
            
            show yuri 1a
            
            hainu "\"Xong rồi à? Cậu làm việc khá nhanh đấy.\""
            hainu "\"Tiền công ngày hôm nay đây.\""
            
            # Nhận tiền bonus
            $ bonus = int(stats.rel_hainu * 500)
            $ stats.modify_tien(bonus)
            $ show_stat_change("tien", bonus)
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 8, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            # Tăng học tập nhưng giảm đời sống
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
            $ stats.modify_doi_song(-5)
            $ show_stat_change("doi_song", -5)
            
            hide yuri with dissolve
            
            jump ch2_activity_loop
        
        "Quay lại":
            jump ch2_activity_loop

# ========================================
# EVENING TRANSITION
# ========================================

label ch2_evening_transition:
    # Transition to evening
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Về ký túc xá{/size}"
    $ renpy.pause(2.0, hard=True)
    
    # Go to dorm activities
    jump ch2_dorm_activities
 
# ========================================
# LIBRARY ACTIVITIES
# ========================================

label ch2_library_activities:
    scene bg corridor with wipeleft_scene
    play music daily_life fadein 1.0
    
    menu:
        "Làm gì tại Thư viện?"
        
        "Học bài":
            "Giở sách ra ôn lại bài cũ..."
            
            # Stat-dependent dialogue
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
            
            # Tăng học tập, giảm sức khỏe nhẹ
            $ stats.modify_hoc_tap(10)
            $ show_stat_change("hoc_tap", 10)
            $ stats.modify_doi_song(-5)
            $ show_stat_change("doi_song", -5)
            
            # Activity completed - consume time slot
            $ time_slots_used += 1
            jump ch2_activity_loop
        
        "Quay lại":
            jump ch2_activity_loop

# ========================================
# GYM ACTIVITIES
# ========================================

label ch2_gym_activities:
    scene bg class_day with wipeleft_scene
    
    menu:
        "Làm gì tại Gym?"
        
        "Nâng tạ":
            "Nâng tạ rèn luyện cơ tay..."
            
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
            
            # Tăng sức khỏe
            $ stats.modify_doi_song(12)
            $ show_stat_change("doi_song", 12)
            
            # Activity completed - consume time slot
            $ time_slots_used += 1
            jump ch2_activity_loop
        
        "Chạy bộ":
            "Chạy bộ rèn luyện cơ chân..."
            
            # Stat-dependent dialogue
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
            
            # Tăng sức khỏe
            $ stats.modify_doi_song(12)
            $ show_stat_change("doi_song", 12)
            
            # FIX: Activity completed - consume time slot
            $ time_slots_used += 1
            jump ch2_activity_loop
        
        "Quay lại":
            jump ch2_activity_loop

# ========================================
# DORM ACTIVITIES
# ========================================

label ch2_dorm_activities:
    scene bg bedroom with wipeleft_scene
    play music tense fadein 1.0
    
    menu:
        "Làm gì tại KTX?"
        
        "Nói chuyện với Xỉu":
            show monika 1d at t11
            
            xiu "\"Chào mừng đến với dịch vụ Campuchia gì cũng tôn của Xỉu. Cu em cần gì nào?\""
            
            menu:
                "Cần gì từ Xỉu?"
                
                "Dịch vụ gia sư học tập":
                    show monika 1a
                    
                    xiu "\"OK luôn. Cứ giao cho chị. Giá 20,000 VNĐ nha!\""
                    
                    if stats.tien >= 20000:
                        mc "\"Được, anh nhờ chị!\""
                        
                        $ stats.modify_tien(-20000)
                        $ show_stat_change("tien", -20000)
                        
                        "Xỉu dạy kèm một lúc..."
                        
                        $ stats.modify_hoc_tap(10)
                        $ show_stat_change("hoc_tap", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 3)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show monika 1k
                        
                        xiu "\"Xong rồi đó! Cu em thông minh lắm, học nhanh!\""
                    else:
                        mc "\"Ủa, anh không đủ tiền…\""
                        
                        show monika 2p
                        
                        xiu "\"Thế thì đi kiếm tiền rồi quay lại!\""
                
                "Dịch vụ bồi bổ đời sống":
                    show monika 5a
                    
                    xiu "\"Oho~ Thú vị đấy! Giá cũng 20,000 VNĐ thôi!\""
                    
                    if stats.tien >= 20000:
                        mc "\"OK, deal!\""
                        
                        $ stats.modify_tien(-20000)
                        $ show_stat_change("tien", -20000)
                        
                        "Xỉu dẫn đi ăn uống thư giãn..."
                        
                        $ stats.modify_doi_song(10)
                        $ show_stat_change("doi_song", 10)
                        
                        $ gained = stats.modify_relationship("xiu", 3)
                        $ show_stat_change("rel_xiu", gained)
                        
                        show monika 1k
                        
                        xiu "\"Thế nào, sảng khoái chưa?\""
                    else:
                        mc "\"Anh hết tiền rồi…\""
                        
                        show monika 2p
                        
                        xiu "\"Nghèo thế mà còn đòi hưởng thụ!\""
                
                "Không cần gì":
                    mc "\"Không, cảm ơn chị.\""
                    
                    show monika 2a
                    
                    xiu "\"Vậy sao, cần gì cứ tìm chị!\""
            
            hide monika with dissolve
            
            # End day after talking to Xỉu
            jump ch2_end_of_day
        
        "Đi ngủ (kết thúc ngày)":
            jump ch2_end_of_day

# ========================================
# END OF DAY 3 (CHAPTER 2)
# ========================================

label ch2_end_of_day:
    
    scene bg bedroom with fade
    play music sad fadein 1.0
    
    "Về đến phòng..."
    
    mc "(ngáp) \"Hôm nay học được khá nhiều thứ…\""
    mc "\"Eikasia, Pistis… Nghe có vẻ sâu sắc nhưng cũng hơi khó hiểu.\""
    
    # Stats summary
    "Nhìn lại stats của ngày hôm nay..."
    
    if stats.hoc_tap >= 70:
        mc "\"Học tập tiến bộ khá tốt!\""
    elif stats.hoc_tap <= 30:
        mc "\"Học hành có vẻ đang sa sút… Phải cố gắng hơn.\""
    
    if stats.doi_song >= 70:
        mc "\"Sức khỏe thì đang ổn.\""
    elif stats.doi_song <= 30:
        mc "\"Mệt mỏi quá… Cần chăm sóc bản thân hơn.\""
    
    mc "\"Ngày mai lại là một ngày mới…\""
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    $ renpy.pause(2.0)
    
    # ========================================
    # TRANSITION TO DAILY ROUTINE (Day 4-9)
    # ========================================
    
    # Set day to 4 and start daily routine loop
    $ current_day = 4
    
    # Call daily routine system
    call daily_routine_loop
    
    # Return to main menu
    return


