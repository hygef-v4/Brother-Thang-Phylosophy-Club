# ================================================
# CHAPTER 2: PISTIS (NIỀM TIN) - DAY 2
# Brother Thang Philosophy Club
# ================================================

label ch2_day2:
    
    # Show stats UI
    show screen stats_display
    
    $ current_day = 2
    $ current_chapter = 2
    
    # Daily stats update
    $ stats.update_daily()
    
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
    # SCENE 1: PHÒNG CLB - SÁNG
    # ========================================
    
    scene bg class_day with wipeleft_scene
    
    mc "\"Buổi đầu tiên có lẽ mình nên đến CLB xem thử…\""
    
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Vừa bước vào phòng CLB, tình cờ thế nào lại gặp lại chị gái tối qua."
    
    show monika 1d at t11
    
    xiu "\"Ô! Xem ai đây kìa! Cu em là thành viên mới của cái CLB tẻ nhạt này à?\""
    xiu "\"Trùng hợp ghê, chị cũng là thành viên đó!\""
    
    show monika 1k
    
    xiu "\"Hữu duyên thế này thì tối này chị em ta lại phải làm ván cá độ rồi!\""
    
    mc "\"Dạ… Dạ vâng…\""
    
    # Ischyros xuất hiện
    show monika 1d at t21
    show yuri 3y at t22
    
    ischyros "\"XỈU!!!\""
    
    "Hội trưởng bước vào."
    
    show yuri 4y at t22
    
    ischyros "\"BÀ LẠI ĐỊNH ĐI LỪA THÀNH VIÊN MỚI NỮA ĐẤY HẢ?\""
    ischyros "\"CÓ BIẾT BAO NHIÊU NGƯỜI CHẠY KHỎI CLB MÌNH VÌ BỊ BÀ LỪA CHO HẾT TIỀN RỒI KHÔNG HẢ?\""
    
    show monika 2p at t21
    
    xiu "(lủi mất) \"Đùa tí, làm gì căng.\""
    
    show yuri 2f at t22
    
    ischyros "\"Còn cả cậu nữa, ai rủ gì cậu cũng làm à? Chính kiến của cậu đâu hả?\""
    
    mc "\"Dạ…. Dạ…. Tại em nghĩ chỉ chơi cho vui thôi chứ đâu có biết là lừa đảo….\""
    
    show yuri 1h
    
    ischyros "\"…. Thật là một niềm tin mù quáng….\""
    ischyros "\"Sống trên đời phải biết nghi ngờ, nếu không thì chả khác nào mấy thằng nghe lời người ta cầm 2 tỷ đầu tư vào HDPE để rồi tán gia bại sản.\""
    
    show yuri 1g
    
    ischyros "\"Thôi được rồi… nay cậu về đì.\""
    
    hide yuri with dissolve
    hide monika with dissolve
    
    # ========================================
    # SCENE 2: HÀNH LANG - SÁNG
    # ========================================
    
    scene bg corridor with wipeleft_scene
    
    "Vừa ra khỏi phòng CLB đã thấy Xỉu đuổi theo."
    
    show monika 2a at t11
    
    xiu "\"Cu em chịu khó ngồi nghe cái bà hội trưởng đấy lảm nhảm thế nhỉ?\""
    xiu "\"Phải chị chị làm vội ba giấc rồi!\""
    
    show monika 1j
    
    xiu "\"Thế kèo của chị em mình tối nay chú tính thế nào? Chơi hay không chơi nói một lời nào.\""
    
    mc "(Thắng ăn cả mà thua thì ăn ***, có lẽ mình nên suy nghĩ cẩn thận một chút…)"
    
    # CHOICE: Cá cược lần 2 với Xỉu
    menu:
        xiu "\"Vậy chơi không?\""
        
        "Chơi thì chơi, sợ gì?":
            mc "\"Chơi thì chơi, sợ gì?\""
            
            $ xiu_day2_bet = True
            
            show monika 1k
            
            xiu "\"Ngon, thắng rồi! Tiền cu em chị xin nhá!\""
            
            # Mất tiền (tối nay sẽ thua)
            $ stats.modify_tien(-50000)
            $ show_stat_change("tien", -50000)
            
            # Relationship giảm
            $ gained = stats.modify_relationship("xiu", -3)
            $ show_stat_change("rel_xiu", gained)
        
        "Thôi, nay em xin kiếu!":
            mc "\"Thôi, nay em xin kiếu!\""
            mc "\"Em đang hơi cần tiền lắm, không dám liều nữa.\""
            
            $ xiu_day2_bet = False
            
            show monika 5a
            
            xiu "\"Chậc... Tuỳ cu.\""
            xiu "\"Vậy thì chị đi kiếm con mồi khác vậy.\""
            
            # Không mất tiền, nhưng cũng không tăng relationship
    
    hide monika with dissolve
    
    # ========================================
    # SCENE 3: PHÒNG CLB - DISCUSSION EIKASIA
    # ========================================
    
    scene bg club_day with wipeleft_scene
    
    "Tôi quay lại phòng CLB, thấy Ischyros đang ngồi đọc sách."
    
    show yuri 1a at t11
    
    ischyros "\"Cậu… Có vẻ đã thoát khỏi cái hang của mình rồi nhỉ?\""
    
    mc "(bối rối) \"Ơ… Dạ?\""
    
    "…"
    
    mc "\"Chuyện lần trước… Cảm ơn chị đã nhắc em về trò lừa bịp của chị Xỉu.\""
    
    show yuri 1f
    
    ischyros "\"Không có gì.\""
    
    mc "\"…\""
    mc "\"Mạn phép cho em hỏi, cái từ mà lần trước chị nói khi mới gặp em ấy. Eika… gì ấy nhở?\""
    
    show yuri 2a
    
    ischyros "\"Eikasia.\""
    
    mc "\"Nó là gì vậy ạ?\""
    
    show yuri 2f
    
    ischyros "\"…\""
    ischyros "\"Cậu biết ngụ ngôn về cái hang của Plato chứ?\""
    
    mc "\"Dạ không.\""
    
    show yuri 1a
    
    # ========================================
    # PLATO'S CAVE ALLEGORY
    # ========================================
    
    ischyros "\"Ngày xửa ngày xưa, có vài người cổ đại sống ở dưới đáy của một cái hang động.\""
    
    show yuri 1f
    
    ischyros "\"Cái hang đấy có một cái lỗ nhỏ, nơi một ít ánh sáng lọt vào.\""
    ischyros "\"Từ cái lỗ đó, có những cái bóng lấp ló hắt lên trên bức tường của cái hang.\""
    
    show yuri 2f
    
    ischyros "\"Những người cổ đại nhìn thấy nó và đặt tên cho những ảo ảnh này và tin rằng vạn vật chỉ là những cái bóng.\""
    
    show yuri 1a
    
    ischyros "\"Một ngày nọ, một người cổ đại tìm được cách thoát ra khỏi cái hang.\""
    ischyros "\"Lần đầu tiên trong đời, anh ta thấy được hình dạng thực của những cái bóng.\""
    
    show yuri 2g
    
    ischyros "\"Anh ta vui mừng quay lại hang động và kể cho những người bạn nghe.\""
    
    show yuri 2w
    
    ischyros "\"Tuy nhiên, những người bạn lại nghĩ anh ta bị điên… Và thế là họ... Cô lập anh ta đến chết.\""
    
    mc "\"Thật là một câu chuyện bi thảm.\""
    
    show yuri 1f
    
    ischyros "\"…\""
    ischyros "\"Những người cổ đại, họ chỉ thấy những cái bóng.\""
    ischyros "\"Họ bị kẹt trong cái gọi là Eikasia. Họ chỉ nhìn thấy những thứ được cho nhìn thấy.\""
    
    show yuri 2f
    
    ischyros "\"Vậy theo cậu, người đàn ông tìm được đường ra khỏi hang liệu đã thấy được hình dạng thật của những chiếc bóng?\""
    
    # CHOICE: Philosophy question
    menu:
        ischyros "\"Cậu nghĩ sao?\""
        
        "Nhìn thấy được rồi thì tức là thật!":
            mc "\"Nhìn thấy được rồi thì tức là thật!\""
            mc "\"Anh ta đã thoát ra ngoài, đương nhiên là thấy được sự thật rồi.\""
            
            show yuri 1h
            
            ischyros "\"Sai rồi.\""
            
            # Không tăng stats
        
        "Có lẽ là chưa….":
            mc "\"Có lẽ là chưa….\""
            mc "\"Làm sao chúng ta biết được thứ bên ngoài hang là thật?\""
            
            show yuri 3a
            
            ischyros "\"Chính xác!\""
            
            # Tăng học tập
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_ischyros()
            $ gained = stats.modify_relationship("ischyros", 5, multiplier)
            $ show_stat_change("rel_ischyros", gained)
    
    show yuri 2k
    
    ischyros "(cười mỉm) \"Thật ra thì, cái hang của họ nằm trong một khu bảo tồn người cổ đại!\""
    ischyros "\"Những thứ mà người đàn ông đó thấy chỉ là những đồ giả mà thôi.\""
    
    show yuri 2f
    
    ischyros "\"Vì vậy, anh ta vẫn chưa thoát khỏi ý niệm của bản thân, vẫn bị kẹt trong Pistis…\""
    ischyros "\"Niềm tin dựa trên những gì anh ta nhìn thấy, nhưng chưa phải là chân lý.\""
    
    mc "\"Vậy… Làm sao để thoát khỏi Pistis?\""
    
    show yuri 1f
    
    ischyros "\"Đó là con đường dài. Từ Eikasia đến Pistis, rồi Dianoia, và cuối cùng là Noesis.\""
    ischyros "\"Nhưng đó là chuyện của những ngày sau. Hôm nay cậu đã hiểu được bước đầu tiên.\""
    
    hide yuri with dissolve
    
    "Bàn luận về triết học cùng Hội Trưởng khiến tôi cảm thấy học được nhiều thứ."
    
    # ========================================
    # TIME SLOT ACTIVITY SYSTEM
    # ========================================
    
    # Initialize time slot variables
    $ time_slots_used = 0
    $ max_time_slots = 3
    
label ch2_activity_loop:
    
    # Check if all time slots used
    if time_slots_used >= max_time_slots:
        jump ch2_end_of_day
    
    scene bg class_day with fade
    
    # Activity selection menu
    menu:
        "Chọn hoạt động:"
        
        "Đến CLB" if time_slots_used < max_time_slots:
            $ time_slots_used += 1
            jump ch2_club_activities
        
        "Đến Thư viện" if time_slots_used < max_time_slots:
            $ time_slots_used += 1
            jump ch2_library_activities
        
        "Đến Gym" if time_slots_used < max_time_slots:
            $ time_slots_used += 1
            jump ch2_gym_activities
        
        "Về phòng nghỉ":
            jump ch2_dorm_activities

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
            
            ischyros "\"Cậu muốn tìm hiểu thêm về triết học sao?\""
            
            mc "\"Dạ vâng, em thấy những gì chị nói rất thú vị.\""
            
            show yuri 2f
            
            ischyros "\"Triết học không chỉ là kiến thức, mà là cách sống.\""
            ischyros "\"Mỗi ngày đặt câu hỏi về những gì ta tin là chân lý.\""
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_ischyros()
            $ gained = stats.modify_relationship("ischyros", 5, multiplier)
            $ show_stat_change("rel_ischyros", gained)
            
            # Tăng học tập
            $ stats.modify_hoc_tap(3)
            $ show_stat_change("hoc_tap", 3)
            
            hide yuri with dissolve
            
            jump ch2_activity_loop
        
        "Giúp Hải Nữ kế toán":
            show natsuki 1c at t11
            
            hainu "\"Cậu tới đúng lúc lắm, hội trưởng vừa bảo tôi kiểm toán lại chi tiêu tháng vừa rồi.\""
            hainu "\"Tôi để sổ sách đằng kia, cậu ra làm đi.\""
            
            mc "\"Dạ vâng, em làm ngay!\""
            
            show natsuki 1a
            
            "Sắp xếp tài liệu..."
            "Kiểm tra số liệu..."
            "Nhập dữ liệu vào máy tính..."
            
            "Cả một núi sổ sách phải giải quyết!"
            
            # Mất thêm 1 time slot vì công việc nhiều
            $ time_slots_used += 1
            
            if time_slots_used > max_time_slots:
                $ time_slots_used = max_time_slots
                
                "Làm việc đến tận chiều muộn mới xong..."
            
            show natsuki 1k
            
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
            
            hide natsuki with dissolve
            
            jump ch2_activity_loop
        
        "Quay lại":
            jump ch2_activity_loop

# ========================================
# LIBRARY ACTIVITIES
# ========================================

label ch2_library_activities:
    scene bg corridor with wipeleft_scene
    play music daily_life fadein 1.0
    
    menu:
        "Làm gì tại Thư viện?"
        
        "Nói chuyện với Hương":
            show sayori 1a at t11
            
            mc "\"Em đang làm gì vậy Hương?\""
            
            "Hương vội che đi màn hình máy tính."
            
            show sayori 1o
            
            huong "\"Không có gì đâu anh, em chỉ đang làm bùa… À không, hỗ trợ các bạn học sinh trong trường học tập thôi.\""
            
            mc "\"Vậy sao, em giỏi thật đấy. Nghe bảo một kỳ em học tận 20 lớp mà vẫn có thời gian giúp bạn bè vậy hả?\""
            
            show sayori 1b
            
            huong "\"Dạ vâng, em được các bạn nhờ thôi. Vậy dạo này anh học hành có ổn không, cần em giúp gì không nào?\""
            
            mc "\"Anh cũng ổn. Cơ mà nhiều môn phải học quá, học trên lớp rồi lại còn học coursera online nữa. Anh còn chưa có thời gian ngồi làm coursera đây này.\""
            
            show sayori 1k
            
            huong "\"Coursera á? Thế anh hỏi đúng người rồi đấy. Em có mẹo này có thể giúp anh này. Anh có muốn biết không?\""
            
            mc "\"Mẹo gì cơ?\""
            
            show sayori 4r
            
            huong "\"Hehe~ Để em chỉ anh!\""
            
            "Ngồi trò chuyện vui vẻ với Hương..."
            
            # Tăng cả học tập và đời sống
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
            $ stats.modify_doi_song(3)
            $ show_stat_change("doi_song", 3)
            
            # Tăng relationship
            $ multiplier = stats.get_stat_multiplier_huong()
            $ gained = stats.modify_relationship("huong", 5, multiplier)
            $ show_stat_change("rel_huong", gained)
            
            hide sayori with dissolve
            
            jump ch2_activity_loop
        
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
            
            # Tăng học tập, giảm đời sống
            $ stats.modify_hoc_tap(15)
            $ show_stat_change("hoc_tap", 15)
            $ stats.modify_doi_song(-10)
            $ show_stat_change("doi_song", -10)
            
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
            
            # Stat-dependent dialogue
            if stats.doi_song < 20:
                mc "\"Mệt quá... Chịu rồi...\""
            elif stats.doi_song < 50:
                mc "\"Phù… Nay đến đây thôi vậy.\""
            elif stats.doi_song < 80:
                mc "\"Cố thêm… Một xíu nữa thôi…\""
            elif stats.doi_song < 100:
                mc "\"Chà, tập xong nhìn mình có vẻ đẹp trai hơn rồi đấy.\""
            else:
                mc "\"Mấy cái này nhẹ quá, hết cái nặng hơn rồi à?\""
            
            # Tăng đời sống, giảm học tập
            $ stats.modify_doi_song(15)
            $ show_stat_change("doi_song", 15)
            $ stats.modify_hoc_tap(-5)
            $ show_stat_change("hoc_tap", -5)
            
            jump ch2_activity_loop
        
        "Chạy bộ":
            "Chạy bộ rèn luyện cơ chân..."
            
            # Stat-dependent dialogue
            if stats.doi_song < 20:
                mc "\"Hổng hển… Không chạy nổi nữa…\""
            elif stats.doi_song < 50:
                mc "\"Mệt rồi, nghỉ thôi.\""
            elif stats.doi_song < 80:
                mc "\"Chạy thêm vài vòng nữa là được.\""
            else:
                mc "\"Dễ dàng quá! Marathon cũng không sợ!\""
            
            # Tăng đời sống, giảm học tập
            $ stats.modify_doi_song(15)
            $ show_stat_change("doi_song", 15)
            $ stats.modify_hoc_tap(-5)
            $ show_stat_change("hoc_tap", -5)
            
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
            
            jump ch2_dorm_activities
        
        "Đi ngủ (kết thúc ngày)":
            jump ch2_end_of_day

# ========================================
# END OF DAY 2
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
    
    # Hide stats UI
    hide screen stats_display
    
    # ========================================
    # END OF CHAPTER 2 - COMING SOON
    # ========================================
    
    $ renpy.pause(1.0)
    
    call screen coming_soon_ch3
    
    # Return to main menu
    return


