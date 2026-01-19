# ================================================
# CHAPTER 2: PISTIS (NIỀM TIN)
# Brother Thang Philosophy Club
# ================================================

label ch2_day2:
    $ current_day = 2
    $ current_chapter = 2
    $ current_time_slot = "morning"

    # ========================================
    # CẢNH ĐẦU: KTX - SÁNG
    # ========================================
    stop music fadeout 2.0
    scene bg bedroom with dissolve_scene_full
    play music daily_life fadein 1.0

    play sound "sfx/fall.ogg" # Placeholder for alarm

    mc "(ngáp) \"Buồn ngủ quá… Qua thức xem stream anh Độ hơi khuya rồi…\""
    mc "\"Tài khoản tự nhiên được cộng thêm tiền này! Là từ chị thủ quỹ tối qua sao?\""
    mc "\"Chà… Người đâu mà đã xinh đẹp, giàu có lại tốt tính. Phú bà của cuộc đời ta đây rồi!\""

    # ========================================
    # CẢNH: SÂN - SÁNG
    # ========================================
    scene bg class_day with wipeleft_scene

    mc "\"Buổi đầu tiên có lẽ mình nên đến CLB xem thử…\""

    # ========================================
    # CẢNH 1: CLB - SÁNG
    # ========================================
    scene bg club_day with wipeleft_scene

    "Vừa bước vào phòng CLB, tình cờ thế nào lại gặp lại chị gái tối qua."

    show monika 1d at t11

    xiu "\"Ô! Xem ai đây kìa! Cu em là thành viên mới của cái CLB tẻ nhạt này à?\""
    xiu "\"Trùng hợp ghê, chị cũng là thành viên đó!\""
    xiu "\"Hữu duyên thế này thì tối này chị em ta lại phải làm ván cá độ rồi!\""

    menu:
        "Dạ vâng…":
            mc "\"Dạ vâng…\""

    show yuri 3h at t11
    show monika 1a at t21
    show yuri 3h at t22

    ischyros "\"XỈU!!!\""
    
    "Hội trưởng bước vào."

    ischyros "\"BÀ LẠI ĐỊNH ĐI LỪA THÀNH VIÊN MỚI NỮA ĐẤY HẢ? CÓ BIẾT BAO NHIÊU NGƯỜI CHẠY KHỎI CLB MÌNH VÌ BỊ BÀ LỪA CHO HẾT TIỀN RỒI KHÔNG HẢ?\""

    show monika 1k
    xiu "(lủi mất) \"Đùa tí, làm gì căng.\""
    hide monika with dissolve

    show yuri 2f at t11

    ischyros "\"Còn cả cậu nữa, ai rủ gì cậu cũng làm à? Chính kiến của cậu đâu hả?\""

    mc "\"Dạ…. Dạ…. Tại em nghĩ chỉ chơi cho vui thôi chứ đâu có biết là lừa đảo….\""

    show yuri 3f

    ischyros "\"…. Thật là một niềm tin mù quáng….\""
    ischyros "\"Sống trên đời phải biết nghi ngờ, nếu không thì chả khác nào mấy thằng nghe lời người ta cầm 2 tỷ đầu tư vào HDPE để rồi tán gia bại sản\""
    
    show yuri 1a
    ischyros "\"Thôi được rồi… nay cậu về đì.\""

    hide yuri with dissolve

    # ========================================
    # HÀNH LANG - SÁNG
    # ========================================
    scene bg corridor with wipeleft_scene

    show monika 1d at t11

    xiu "\"Cu em chịu khó ngồi nghe cái bà hội trưởng đấy lảm nhảm thế nhỉ?\""
    xiu "\"Phải chị chị làm vội ba giấc rồi!\""
    xiu "\"Thế kèo của chị em mình tối nay chú tính thế nào? Chơi hay không chơi nói một lời nào.\""

    mc "(Thắng ăn cả mà thua thì ăn ***, có lẽ mình nên suy nghĩ cẩn thận một chút…)"

    menu:
        "Chơi thì chơi, sợ gì?":
            $ stats.modify_relationship("xiu", 5)
            mc "\"Chơi thì chơi, sợ gì?\""
            show monika 1k
            xiu "\"Ngon, thắng rồi! Tiền cu em chị xin nhá!\""

        "Thôi, nay em xin kiếu!":
            mc "\"Thôi, nay em xin kiếu!\""
            show monika 1a
            xiu "\"Chậc... Tuỳ cu.\""

    hide monika with dissolve

    # ========================================
    # CLB - SÁNG TRƯA CHIỀU (Free Time)
    # ========================================
    
    # [Nói chuyện với Hội Trưởng]
    scene bg club_day with wipeleft_scene
    show yuri 1a at t11

    ischyros "\"Cậu… Có vẻ đã thoát khỏi cái hang của mình rồi nhỉ?\""

    mc "(bối rối) \"Ơ… Dạ?\""
    mc "\"…\""
    mc "\"Chuyện lần trước… Cảm ơn chị đã nhắc em về trò lừa bịp của chị Xỉu.\""

    ischyros "\"Không có gì.\""

    mc "\"…\""
    mc "\"Mạn phép cho em hỏi, cái từ mà lần trước chị nói khi mới gặp em ấy. Eika… gì ấy nhở?\""

    ischyros "\"Eikasia.\""

    mc "\"Nó là gì vậy ạ?\""

    show yuri 1f
    ischyros "\"…\""
    ischyros "\"Cậu biết ngụ ngôn về cái hang của Plato chứ?\""

    mc "\"Dạ không.\""

    show yuri 2f
    ischyros "\"Ngày xửa ngày xưa, có vài người cổ đại sống ở dưới đáy của một cái hang động.\""
    ischyros "\"Cái hang đấy có một cái lỗ nhỏ, nơi một ít ánh sáng lọt vào.\""
    ischyros "\"Từ cái lỗ đó, có những cái bóng lấp ló hắt lên trên bức tường của cái hang.\""
    ischyros "\"Những người cổ đại nhìn thấy nó và đặt tên cho những ảo ảnh này và tin rằng vạn vật chỉ là những cái bóng.\""
    
    show yuri 2e
    ischyros "\"Một ngày nọ, một người cổ đại tìm được cách thoát ra khỏi cái hang.\""
    ischyros "\"Lần đầu tiên trong đời, anh ta thấy được hình dạng thực của những cái bóng.\""
    ischyros "\"Anh ta vui mừng quay lại hang động và kể cho những người bạn nghe.\""
    ischyros "\"Tuy nhiên, những người bạn lại nghĩ anh ta bị điên… Và thế là họ... Cô lập anh ta đến chết.\""

    mc "\"Thật là một câu chuyện bi thảm.\""

    show yuri 1f
    ischyros "\"…\""
    ischyros "\"Những người cổ đại, họ chỉ thấy những cái bóng.\""
    ischyros "\"Họ bị kẹt trong cái gọi là Eikasia. Họ chỉ nhìn thấy những thứ được cho nhìn thấy.\""
    
    show yuri 3f
    ischyros "\"Vậy theo cậu, người đàn ông tìm được đường ra khỏi hang liệu đã thấy được hình dạng thật của những chiếc bóng?\""

    menu:
        "Nhìn thấy được rồi thì tức là thật!":
            mc "\"Nhìn thấy được rồi thì tức là thật!\""

        "Có lẽ là chưa….":
            mc "\"Có lẽ là chưa….\""
            $ stats.modify_relationship("ischyros", 5)

    show yuri 1a
    ischyros "(cười mỉm) \"Thật ra thì, cái hang của nằm trong một khu bảo tồn người cổ đại!\""
    ischyros "\"Những thứ mà người đàn ông đó thấy chỉ là những đồ giả mà thôi.\""
    ischyros "\"Vì vậy, anh ta vẫn chưa thoát khỏi ý niệm của bản thân, vẫn bị kẹt trong Pistis…\""

    "Bàn luận về triết học cùng Hội Trưởng tới hết buổi..."
    hide yuri with dissolve

    # [Nói chuyện với Hải Nữ]
    show natsuki 1c at t11

    hainu "\"Cậu tới đúng lúc lắm, hội trưởng vừa bảo tôi kiểm toán lại chi tiêu tháng vừa rồi.\""
    hainu "\"Tôi để sổ sách đằng kia, cậu ra làm đi.\""

    menu:
        "Dạ vâng, em làm ngay!":
            mc "\"Dạ vâng, em làm ngay!\""
            "Cả một núi sổ sách phải giải quyết, đến lúc xong thì đã sang buổi..."
            $ stats.modify_relationship("hainu", 5)

        "Xin lỗi, nay em hơi bận xíu….":
            mc "\"Xin lỗi, nay em hơi bận xíu….\""
            show natsuki 4x
            hainu "\"Hừ! Vậy thôi!\""

    hide natsuki with dissolve

    # ========================================
    # THƯ VIỆN & GYM - SÁNG TRƯA CHIỀU
    # ========================================
    scene bg library with wipeleft_scene

    # [Nói chuyện với Hương]
    
    mc "\"Em đang làm gì vậy Hương?\""
    
    "Hương vội che đi màn hình máy tính."
    
    show sayori 1b at t11

    huong "\"Không có gì đâu anh, em chỉ đang làm bùa… À không, hỗ trợ các bạn học sinh trong trường học tập thôi.\""

    mc "\"Vậy sao, em giỏi thật đấy. Nghe bảo một kỳ em học tận 20 lớp mà vẫn có thời gian giúp bạn bè vậy hả?\""

    show sayori 1a
    huong "\"Dạ vâng, em được các bạn nhờ thôi. Vậy dạo này anh học hành có ổn không, cần em giúp gì không nào?\""

    mc "\"Anh cũng ổn. Cơ mà nhiều môn phải học quá, học trên lớp rồi lại còn học coursera online nữa. Anh còn chưa có thời gian ngồi làm coursera đây này.\""

    show sayori 4r
    huong "\"Coursera á? Thế ảnh hỏi đúng người rồi đấy. Em có mẹo này có thể giúp anh này. Anh có muốn biết không?\""

    mc "\"Mẹo gì cơ?\""

    "Ngồi trò chuyện vui vẻ với Hương cả buổi..."
    $ stats.modify_relationship("huong", 5)
    
    hide sayori with dissolve

    # [Học bài]
    "Giở sách ra ôn lại bài cũ."
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

    $ stats.modify_hoc_tap(5)

    # [GYM]
    scene bg gym with wipeleft_scene

    menu:
        "Nâng tạ rèn luyện cơ tay":
             "Nâng tạ rèn luyện cơ tay."
        "Chạy bộ rèn luyện cơ chân":
             "Chạy bộ rèn luyện cơ chân."
    
    if stats.doi_song < 20:
        mc "\"Mệt quá… Chịu rồi...\""
    elif stats.doi_song < 50:
        mc "\"Phù… Nay đến đây thôi vậy\""
    elif stats.doi_song < 80:
        mc "\"Cố thêm… Một xíu nữa thôi…\""
    elif stats.doi_song < 100:
        mc "\"Chà, tập xong nhìn mình có vẻ đẹp trai hơn rồi đấy.\""
    else:
        mc "\"Mấy cái này nhẹ quá, hết cái nặng hơn rồi à?\""

    $ stats.modify_doi_song(5)

    # ========================================
    # KTX - TỐI
    # ========================================
    scene bg bedroom with wipeleft_scene
    
    # [Nói chuyện với Xỉu]
    show monika 1a at t11

    xiu "\"Chào mừng đến với dịch vụ Campuchia gì cũng tôn của Xỉu. Cu em cần gì nào?\""

    menu:
        "Dịch vụ gia sư học tập":
             $ stats.modify_hoc_tap(5)
             "Gia sư học tập..."
        "Dịch vụ bồi bổ đời sống":
             $ stats.modify_doi_song(5)
             "Bồi bổ đời sống..."

    show monika 1k
    xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
    
    hide monika with dissolve

    "[[Về phòng] Đi ngủ."
    scene black with dissolve_scene_full

    "Kết thúc Ngày 2."
    jump ch3_day3
