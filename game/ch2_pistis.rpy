# ================================================
# CHAPTER 2: PISTIS (NIỀM TIN) - DAY 4 TO 9
# Brother Thang Philosophy Club
# ================================================

label day3:
    scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0

    $ current_chapter = 2
    
    # ========================================
    # NGÀY 4
    # ========================================
    # Text Scenes: 251-256 (Salary)
    "Chuông báo thức reo."
    mc "(ngáp) \"Buồn ngủ quá… Qua thức xem stream anh Độ hơi khuya rồi…\""
    "Ting"
    mc "\"Bố gửi tiền tiêu vặt hàng ngày à?\""
    mc "\"Ngon luôn, cuộc sống đại học của mình bắt đầu từ đây!\""

    menu:
        "Đi ngủ":
            # End of day summary
            scene black with fade
            
            $ renpy.pause(2.0)
            
            stop music fadeout 2.0
            if current_time_slot == 1:
                jump daily_routine_noon

        "Ra ngoài" if current_time_slot != 3:
            jump daily_activity
    
    return

# ========================================
# HELPER LABELS
# ========================================

label plato_cave:
    # Text Scenes: 258-301 (Cave Allegory)
    play music deep_thought fadein 1.0

    show hainu 1a at t11

    hainu "\"Cậu… Có vẻ đã thoát khỏi cái hang của mình rồi nhỉ?\""
    
    mc "(bối rối) \"Ơ… Dạ?\""
    mc "\"…\""
    mc "\"Chuyện lần trước… Cảm ơn chị đã nhắc em về trò lừa bịp của chị Xỉu.\""
    
    hainu "\"Không có gì.\""
    
    mc "\"…\""
    mc "\"Mạn phép cho em hỏi, cái từ mà lần trước chị nói khi mới gặp em ấy. Eika… gì ấy nhở?\""
    
    hainu "\"Eikasia.\""
    
    mc "\"Nó là gì vậy ạ?\""
    
    show hainu 1b
    
    hainu "\"…\""
    hainu "\"Cậu biết ngụ ngôn về cái hang của Plato chứ?\""
    
    mc "\"Dạ không.\""
    
    hainu "\"Ngày xửa ngày xưa, có vài người cổ đại sống ở dưới đáy của một cái hang động.\""
    hainu "\"Cái hang đấy có một cái lỗ nhỏ, nơi một ít ánh sáng lọt vào.\""
    hainu "\"Từ cái lỗ đó, có những cái bóng lấp ló hắt lên trên bức tường của cái hang.\""
    hainu "\"Những người cổ đại nhìn thấy nó và đặt tên cho những ảo ảnh này và tin rằng vạn vật chỉ là những cái bóng.\""
    
    show hainu 1c
    
    hainu "\"Một ngày nọ, một người cổ đại tìm được cách thoát ra khỏi cái hang.\""
    hainu "\"Lần đầu tiên trong đời, anh ta thấy được hình dạng thực của những cái bóng.\""
    hainu "\"Anh ta vui mừng quay lại hang động và kể cho những người bạn nghe.\""
    
    show hainu 1e
    
    hainu "\"Tuy nhiên, những người bạn lại nghĩ anh ta bị điên… Và thế là họ... Cô lập anh ta đến chết.\""
    
    mc "\"Thật là một câu chuyện bi thảm.\""
    
    show hainu 1b
    
    hainu "\"…\""
    hainu "\"Những người cổ đại, họ chỉ thấy những cái bóng.\""
    hainu "\"Họ bị kẹt trong cái gọi là Eikasia. Họ chỉ nhìn thấy những thứ được cho nhìn thấy.\""
    hainu "\"Vậy theo cậu, người đàn ông tìm được đường ra khỏi hang liệu đã thấy được hình dạng thật của những chiếc bóng?\""
    
    menu:
        "Có lẽ là rồi….":
            pass
        
        "Có lẽ là chưa….":
            $ gained = stats.modify_relationship("hainu", 6)
            $ show_stat_change("rel_hainu", gained)
            
    show hainu 1e
    
    hainu "(cười mỉm) \"Thật ra thì, cái hang nằm trong một khu bảo tồn người cổ đại!\""
    hainu "\"Những thứ mà người đàn ông đó thấy chỉ là những đồ giả mà thôi.\""
    hainu "\"Vì vậy, anh ta vẫn chưa thoát khỏi ý niệm của bản thân, vẫn bị kẹt trong Pistis…\""
    hainu "\"Đó chính là cái lồng của niềm tin vào trí tuệ của bản thân, nó giam giữ và ngăn cách anh ta chạm tới chân lý…\""
    
    $ gained = stats.modify_relationship("hainu", 6)
    $ show_stat_change("rel_hainu", gained)

    $ first_talk = True
    
    return