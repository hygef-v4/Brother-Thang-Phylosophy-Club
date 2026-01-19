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
    # END OF DAY 2
    # ========================================
    
    scene bg bedroom with wipeleft_scene
    play music sad fadein 1.0
    
    "Về đến phòng..."
    
    mc "(ngáp) \"Hôm nay học được khá nhiều thứ…\""
    mc "\"Eikasia, Pistis… Nghe có vẻ sâu sắc nhưng cũng hơi khó hiểu.\""
    mc "\"Ngày mai lại là một ngày mới…\""
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    # Hide stats UI
    hide screen stats_display
    
    # ========================================
    # END OF CHAPTER 2 - COMING SOON
    # ========================================
    
    $ renpy.pause(1.0)
    
    call screen coming_soon
    
    # Return to main menu
    return
