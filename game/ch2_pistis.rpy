# ================================================
# CHAPTER 2: PISTIS (NIỀM TIN) - DAY 4 TO 9
# Brother Thang Philosophy Club
# ================================================

label ch2_day3:
    
    show screen stats_display
    $ current_chapter = 2
    
    # ========================================
    # NGÀY 4
    # ========================================
    $ current_day = 4
    call ch2_day_start from ch2_day4_start
    
    # Text Scenes: 251-256 (Salary)
    "Chuông báo thức reo."
    mc "(ngáp) \"Buồn ngủ quá… Qua thức xem stream anh Độ hơi khuya rồi…\""
    mc "\"Tài khoản tự nhiên được cộng thêm tiền này! Hội trưởng bảo trả lương theo ngày là thật sao?\""
    "Ting! Bạn nhận được 50.000đ."
    $ stats.modify_tien(50000)
    $ show_stat_change("tien", 50000)
    
    play music t2 fadein 1.0 # Ohayou Sayori (Happy)
    
    mc "\"Chà… Người đâu mà đã xinh đẹp, giàu có lại tốt tính. Có phú bà bao nuôi thế này, cuộc sống đại học mình bắt đầu từ đây!\""

    "Ngày thứ 4 tại FPT đã bắt đầu."
    "Sau những sự kiện dồn dập của những ngày đầu, hôm nay tôi muốn tìm một nhịp điệu riêng cho mình."
    
    # Force CLB Event (Cave Allegory) instead of generic choice
    call ch2_day4_clb_event
    
    call ch2_evening_activity from ch2_day4_eve
    
    call ch2_day_end from ch2_day4_end

    # ========================================
    # NGÀY 5
    # ========================================
    $ current_day = 5
    call ch2_day_start from ch2_day5_start
    
    "Ngày thứ 5."
    "Việc học trên lớp bắt đầu nặng dần, nhưng tôi vẫn muốn dành thời gian buổi chiều cho bản thân."
    
    call ch2_afternoon_activity from ch2_day5_act
    call ch2_evening_activity from ch2_day5_eve
    
    call ch2_day_end from ch2_day5_end

    # ========================================
    # NGÀY 6: SỰ KIỆN TRANH BIỆN (CỐ ĐỊNH)
    # ========================================
    $ current_day = 6
    
    scene black with dissolve_scene_full
    centered "{size=40}Ngày 6{/size}"
    $ renpy.pause(1.5, hard=True)

    scene bg club_day with wipeleft_scene
    play music t6 fadein 1.0

    "Chiều ngày thứ 6, tôi đến CLB như thường lệ."
    "Nhưng hôm nay không khí có vẻ căng thẳng lạ thường."

    show hainu thinking at t21
    show xiu angry at t22

    xiu "\"Tiền là phương tiện để tự do! Có tiền mới có lựa chọn! Bà cứ lý thuyết suông mãi thế không chán à?\""
    
    hainu "\"Nhưng nếu dùng tiền để mua vui nhất thời, cô chỉ đang nô lệ cho dục vọng thôi. Tự do đích thực phải đến từ nhận thức!\""

    mc "(Lại cãi nhau rồi...)"

    show xiu happy at t22

    xiu "\"Á à, cu em đến rồi!\""
    xiu "\"Phân xử đi! Theo em, Hạnh phúc là gì?\""
    xiu "\"Là có tiền tiêu xả láng, sống sướng thân...\""
    xiu "\"Hay là ngồi gặm nhấm mấy cuốn sách triết học dày cộp này?\""

    menu:
        "Theo bạn, hạnh phúc là..."

        "Thỏa mãn bản thân (Ủng hộ Xỉu)":
            mc "\"Em nghĩ... Sống là phải vui. Cứ thoải mái, sảng khoái như chị Xỉu là sướng nhất.\""
            mc "\"Đời người ngắn ngủi, tội gì phải khổ hạnh?\""

            show xiu happy at t22
            show hainu tired at t21

            xiu "\"Chuẩn! 10 điểm! Thằng bé này khá lắm!\""
            hainu "\"Hừmm... Cậu cũng thiển cận như cô ta vậy.\""

            $ gained = stats.modify_relationship("xiu", 10)
            $ show_stat_change("rel_xiu", gained)
            $ gained = stats.modify_relationship("hainu", -2)
            $ show_stat_change("rel_hainu", gained)

        "Đi tìm ý nghĩa (Ủng hộ Hải Nữ)":
            mc "\"Em nghĩ hạnh phúc là khi mình tìm thấy ý nghĩa sống, hoặc làm được gì đó có ích.\""
            mc "\"Như chị Nữ nói, vui thú nhất thời rồi cũng sẽ qua, cái đọng lại mới quan trọng.\""

            show hainu neutral at t21
            show xiu angry at t22

            hainu "\"Nghe chưa? Cậu ấy hiểu chuyện hơn cô tưởng đấy.\""
            xiu "\"Hứ! Đồ ẻo lả. Chả thú vị gì cả.\""

            $ gained = stats.modify_relationship("hainu", 10)
            $ show_stat_change("rel_hainu", gained)
            $ gained = stats.modify_relationship("xiu", -2)
            $ show_stat_change("rel_xiu", gained)

    show hainu neutral at t21
    show xiu neutral at t22

    "Cuộc tranh luận kết thúc, nhưng dường như nó đã định hình một cái gì đó trong tôi."

    hide hainu with dissolve
    hide xiu with dissolve
    
    call ch2_evening_activity from ch2_day6_eve
    
    call ch2_day_end from ch2_day6_end

    # ========================================
    # NGÀY 7
    # ========================================
    $ current_day = 7
    call ch2_day_start from ch2_day7_start
    
    "Ngày thứ 7."
    "Dư âm của cuộc tranh luận hôm qua vẫn còn đâu đó trong đầu tôi."
    
    call ch2_afternoon_activity from ch2_day7_act
    call ch2_evening_activity from ch2_day7_eve
    
    call ch2_day_end from ch2_day7_end

    # ========================================
    # NGÀY 8
    # ========================================
    $ current_day = 8
    call ch2_day_start from ch2_day8_start
    
    "Ngày thứ 8."
    "Một tuần học đã trôi qua. Tôi cảm thấy mình đang dần hòa nhập vào nơi này."
    
    call ch2_afternoon_activity from ch2_day8_act
    call ch2_evening_activity from ch2_day8_eve
    
    call ch2_day_end from ch2_day8_end
    
    # ========================================
    # NGÀY 9: TRƯỚC BÃO
    # ========================================
    $ current_day = 9
    call ch2_day_start from ch2_day9_start
    
    "Ngày thứ 9."
    
    stop music fadeout 2.0
    
    "Hôm nay... tôi có một dự cảm lạ lùng."
    "Mọi thứ dường như quá bình yên."
    
    call ch2_afternoon_activity from ch2_day9_act
    call ch2_evening_activity from ch2_day9_eve
    
    # Lương về
    "Ding!"
    "Thông báo tin nhắn ngân hàng."
    "Là lương làm thêm từ Hải Nữ chuyển khoản."
    
    $ stats.modify_tien(100000)
    $ show_stat_change("tien", 100000)

    mc "\"Có tiền rồi...\""
    mc "\"Mình suýt nữa đã quên mất áp lực ở nhà...\""
    
    call ch2_day_end from ch2_day9_end

    # Transition to Chapter 3
    call ch3_dianoia

    return

# ========================================
# HELPER LABELS
# ========================================

label ch2_day_start:
    scene black with dissolve_scene_full
    centered "{size=40}Ngày [current_day]{/size}"
    $ renpy.pause(1.5, hard=True)

    scene bg ktx_day with dissolve_scene_full
    play music daily_life fadein 1.0
    
    # Daily logic: regen stats
    $ daily_changes = stats.update_daily()

    if daily_changes != 0:
        $ show_stat_change("tien", daily_changes)
    
    return

label ch2_day_end:
    scene black with dissolve
    "Một ngày nữa lại kết thúc."
    $ renpy.pause(1.0)
    return

label ch2_day4_clb_event:
    # Text Scenes: 258-301 (Cave Allegory)
    scene bg club_day with wipeleft_scene
    play music t7 fadein 1.0

    "Tôi quyết định đến CLB sớm."
    
    show hainu neutral at t11

    hainu "\"Cậu… Có vẻ đã thoát khỏi cái hang của mình rồi nhỉ?\""
    
    mc "(bối rối) \"Ơ… Dạ?\""
    mc "\"…\""
    mc "\"Chuyện lần trước… Cảm ơn chị đã nhắc em về trò lừa bịp của chị Xỉu.\""
    
    hainu "\"Không có gì.\""
    
    mc "\"…\""
    mc "\"Mạn phép cho em hỏi, cái từ mà lần trước chị nói khi mới gặp em ấy. Eika… gì ấy nhở?\""
    
    hainu "\"Eikasia.\""
    
    mc "\"Nó là gì vậy ạ?\""
    
    show hainu thinking
    
    hainu "\"…\""
    hainu "\"Cậu biết ngụ ngôn về cái hang của Plato chứ?\""
    
    mc "\"Dạ không.\""
    
    hainu "\"Ngày xửa ngày xưa, có vài người cổ đại sống ở dưới đáy của một cái hang động.\""
    hainu "\"Cái hang đấy có một cái lỗ nhỏ, nơi một ít ánh sáng lọt vào.\""
    hainu "\"Từ cái lỗ đó, có những cái bóng lấp ló hắt lên trên bức tường của cái hang.\""
    hainu "\"Những người cổ đại nhìn thấy nó và đặt tên cho những ảo ảnh này và tin rằng vạn vật chỉ là những cái bóng.\""
    
    show hainu explaining
    
    hainu "\"Một ngày nọ, một người cổ đại tìm được cách thoát ra khỏi cái hang.\""
    hainu "\"Lần đầu tiên trong đời, anh ta thấy được hình dạng thực của những cái bóng.\""
    hainu "\"Anh ta vui mừng quay lại hang động và kể cho những người bạn nghe.\""
    
    show hainu smile
    
    hainu "\"Tuy nhiên, những người bạn lại nghĩ anh ta bị điên… Và thế là họ... Cô lập anh ta đến chết.\""
    
    mc "\"Thật là một câu chuyện bi thảm.\""
    
    show hainu thinking
    
    hainu "\"…\""
    hainu "\"Những người cổ đại, họ chỉ thấy những cái bóng.\""
    hainu "\"Họ bị kẹt trong cái gọi là Eikasia. Họ chỉ nhìn thấy những thứ được cho nhìn thấy.\""
    hainu "\"Vậy theo cậu, người đàn ông tìm được đường ra khỏi hang liệu đã thấy được hình dạng thật của những chiếc bóng?\""
    
    stop music fadeout 2.0 # Silence for thought
    
    menu:
        "Ý kiến của bạn?"
        
        "Nhìn thấy được rồi thì tức là thật!":
            mc "\"Nhìn thấy được rồi thì tức là thật!\""
        
        "Có lẽ là chưa….":
            mc "\"Có lẽ là chưa….\""
            
    show hainu smile
    
    hainu "(cười mỉm) \"Thật ra thì, cái hang của nằm trong một khu bảo tồn người cổ đại!\""
    hainu "\"Những thứ mà người đàn ông đó thấy chỉ là những đồ giả mà thôi.\""
    hainu "\"Vì vậy, anh ta vẫn chưa thoát khỏi ý niệm của bản thân, vẫn bị kẹt trong Pistis…\""
    
    "Chúng tôi bàn luận về triết học cùng Hội Trưởng tới hết buổi."
    
    $ gained = stats.modify_relationship("hainu", 10)
    $ show_stat_change("rel_hainu", gained)
    $ stats.modify_hoc_tap(10)
    $ show_stat_change("hoc_tap", 10)
    
    return

# -------------------------------------------------------------------------
# SYSTEM: ACTIVITY PROGRESSION (COUNT-BASED)
# -------------------------------------------------------------------------

label ch2_afternoon_activity:
    menu:
        "Chiều nay bạn sẽ làm gì?"
        
        "Đến Phòng Gym (Sức khỏe)":
            call ch2_gym_event
        
        "Đến Thư Viện (Học tập)":
            call ch2_library_event
            
        "Làm việc tại CLB (Kiếm tiền)":
            scene bg club_day with wipeleft_scene
            "Tôi ghé qua CLB phụ giúp một chút việc vặt."
            "Tuy hơi chán nhưng có thêm chút tiền tiêu vặt cũng tốt."
            $ stats.modify_tien(50000)
            $ show_stat_change("tien", 50000)
            
    return

label ch2_gym_event:
    scene bg gym with wipeleft_scene
    play music t2 fadein 1.0

    # Increment count
    $ stats.gym_count += 1
    
    if stats.gym_count == 1:
        # Text 315
        mc "\"Mệt quá… Chịu rồi...\""
        
        show xiu angry at t11
        xiu "\"Yếu nhớt! Cầm cái tạ như cầm ly trà sữa thế kia bao giờ mới có người yêu?\""
        
        $ stats.modify_doi_song(5)
        $ show_stat_change("doi_song", 5)
        
    elif stats.gym_count <= 3:
        # Text 317
        mc "\"Cố thêm… Một xíu nữa thôi…\""
        
        show xiu happy at t11
        xiu "\"Khá đấy cu. Nay đẩy ngực được 20kg rồi à? Cố lên, sắp đủ trình làm bao cát cho chị rồi.\""
        
        $ stats.modify_doi_song(10)
        $ show_stat_change("doi_song", 10)
        $ gained = stats.modify_relationship("xiu", 2)
        $ show_stat_change("rel_xiu", gained)
        
    else:
        # Text 318
        mc "\"Chà, tập xong nhìn mình có vẻ đẹp trai hơn rồi đấy.\""
        
        show xiu happy at t11
        xiu "\"Uầy, nhìn 'mlem' phết rồi đấy. Tối nay đi làm bát phở gầu bò nạm thưởng cho cái body này không?\""
        
        $ stats.modify_doi_song(15)
        $ show_stat_change("doi_song", 15)
        $ gained = stats.modify_relationship("xiu", 5)
        $ show_stat_change("rel_xiu", gained)
        
    return

label ch2_library_event:
    scene bg library with wipeleft_scene
    play music t3 fadein 1.0
    
    # Increment count
    $ stats.lib_count += 1
    
    if stats.lib_count == 1:
        # Text 306
        mc "\"Ra là thế… Chả hiểu gì cả.\""
        mc "\"Mở cuốn 'Phê phán lý tính thuần túy' ra đọc được 2 dòng thì mắt díp lại.\""
        
        show hainu tired at t11
        hainu "\"Thư viện là nơi nuôi dưỡng tâm hồn, không phải chỗ ngủ trọ. Ngồi thẳng lưng lên.\""
        
        $ stats.modify_hoc_tap(5)
        $ show_stat_change("hoc_tap", 5)
        
    elif stats.lib_count <= 3:
        # Text 309
        mc "\"Ồ, kiến thức mới đã được tiếp thu.\""
        mc "\"Hoá ra triết học không khô khan như mình tưởng, nó giống như giải một bài toán về cuộc đời vậy.\""
        
        show hainu neutral at t11
        hainu "\"Cậu đang đọc Kant sao? Một lựa chọn không tồi. Nếu có chỗ nào không hiểu, tôi có thể... gợi ý một chút.\""
        
        $ stats.modify_hoc_tap(10)
        $ show_stat_change("hoc_tap", 10)
        $ gained = stats.modify_relationship("hainu", 2)
        $ show_stat_change("rel_hainu", gained)
        
    else:
        # Text 310
        mc "\"Mấy bài này dễ quá, có lẽ mình nên tìm thứ khác khó hơn.\""
        mc "\"Mình tìm thấy sự liên kết giữa Hội hoạ và Triết học. Cả hai đều là cách con người mô tả thế giới.\""
        
        show hainu smile at t11
        hainu "\"Cậu đã bắt đầu chạm vào được Noesis rồi đấy. Ánh mắt cậu nhìn trang sách... đã khác xưa nhiều.\""
        
        $ stats.modify_hoc_tap(15)
        $ show_stat_change("hoc_tap", 15)
        $ gained = stats.modify_relationship("hainu", 5)
        $ show_stat_change("rel_hainu", gained)
        
        # Unlock condition
        $ stats.unlocked_dialectics = True
        $ renpy.notify("Đã mở khóa: Tư duy Biện chứng")
        
    return

# -------------------------------------------------------------------------
# SYSTEM: EVENING ACTIVITY (SOCIAL)
# -------------------------------------------------------------------------

label ch2_evening_activity:
    scene bg ktx with fade
    "Về phòng rồi. Tối nay làm gì nhỉ?"

    menu:
        # Text 322-329 (Xiu KTX logic)
        "Sang phòng Xỉu chơi (Tăng thiện cảm)" if current_day % 2 == 0:
            scene bg ktx_xiu_room with wipeleft
            
            stop music fadeout 1.0
            play music t5 fadein 1.0 # Playful
            
            show xiu neutral at t11
            xiu "\"Chào mừng đến với dịch vụ Campuchia gì cũng tôn của Xỉu. Cu em cần gì nào?\""
            
            menu:
                "Dịch vụ gia sư học tập":
                    xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                    "Tuy nhiên, 'gia sư' kiểu Xỉu lại là dạy cách đối nhân xử thế."
                    $ stats.modify_doi_song(3)
                    $ stats.modify_hoc_tap(2)
                
                "Dịch vụ bồi bổ đời sống":
                    xiu "\"OK luôn. Cứ giao cho chị. Tối nay chị sẽ chăm sóc cu em nhiệt tình.\""
                    "Chúng tôi chơi game và ăn vặt tới khuya."
                    $ stats.modify_doi_song(5)
            
            hide xiu
            
            $ gained = stats.modify_relationship("xiu", 3)
            $ show_stat_change("rel_xiu", gained)
             
        "Nhắn tin hỏi bài Nữ (Tăng thiện cảm)" if current_day % 2 != 0:
            "Tôi nhắn tin hỏi chị Nữ về vài thuật ngữ chưa hiểu."
            "Chị ấy rep khá nhanh và giải thích rất cặn kẽ."
            $ stats.modify_hoc_tap(5)
            $ gained = stats.modify_relationship("hainu", 3)
            $ show_stat_change("rel_hainu", gained)
             
        "Ngủ sớm (Hồi phục)":
            "Tôi quyết định ngủ sớm để giữ gìn sức khỏe."
            $ stats.modify_doi_song(10)
            $ show_stat_change("doi_song", 10)

    return
