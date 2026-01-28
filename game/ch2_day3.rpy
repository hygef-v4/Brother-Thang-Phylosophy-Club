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
    
    "Ngày thứ 4 tại FPT đã bắt đầu."
    "Sau những sự kiện dồn dập của những ngày đầu, hôm nay tôi muốn tìm một nhịp điệu riêng cho mình."
    
    call ch2_afternoon_activity from ch2_day4_act
    call ch2_evening_activity from ch2_day4_eve
    
    call ch2_day_end from ch2_day4_end

    # ========================================
    # NGÀY 5
    # ========================================
    $ current_day = 5
    call ch2_day_start from ch2_day5_start
    
    "Ngày thứ 5."
    "Việc học trên lớp bắt đầu nặng dần, nhưng tôi vẫn muốn dành thời gian buổi chiều cho bản thân."
    
    # Logic cũ: Sự kiện Tranh biện ở Ngày 6. Nhưng user suggest Ngày 5 cũng có thể có sự kiện cố định.
    # User request: "Ngày 5 (Sự kiện bắt buộc): Dù người chơi chọn đi đâu, Xỉu và Nữ đều sẽ xuất hiện cùng lúc để cãi nhau". 
    # Tuy nhiên, theo timeline cũ thì Debate là Ngày 6. Để tránh conflict timeline lớn, mình setup Debate ở Ngày 6 như cũ, 
    # Ngày 5 vẫn progression bình thường như user suggest ở phần "TÓM TẮT CÁCH SỬA".
    
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
    play music argument fadein 1.0

    "Chiều ngày thứ 6, tôi đến CLB như thường lệ."
    "Nhưng hôm nay không khí có vẻ căng thẳng lạ thường."

    show yuri 1f at t21
    show monika 2p at t22

    xiu "\"Tiền là phương tiện để tự do! Có tiền mới có lựa chọn! Bà cứ lý thuyết suông mãi thế không chán à?\""
    
    hainu "\"Nhưng nếu dùng tiền để mua vui nhất thời, cô chỉ đang nô lệ cho dục vọng thôi. Tự do đích thực phải đến từ nhận thức!\""

    mc "(Lại cãi nhau rồi...)"

    show monika 1k at t22

    xiu "\"Á à, cu em đến rồi!\""
    xiu "\"Phân xử đi! Theo em, Hạnh phúc là gì?\""
    xiu "\"Là có tiền tiêu xả láng, sống sướng thân...\""
    xiu "\"Hay là ngồi gặm nhấm mấy cuốn sách triết học dày cộp này?\""

    menu:
        "Theo bạn, hạnh phúc là..."

        "Thỏa mãn bản thân (Ủng hộ Xỉu)":
            mc "\"Em nghĩ... Sống là phải vui. Cứ thoải mái, sảng khoái như chị Xỉu là sướng nhất.\""
            mc "\"Đời người ngắn ngủi, tội gì phải khổ hạnh?\""

            show monika 1l at t22
            show yuri 2h at t21

            xiu "\"Chuẩn! 10 điểm! Thằng bé này khá lắm!\""
            hainu "\"Hừmm... Cậu cũng thiển cận như cô ta vậy.\""

            $ gained = stats.modify_relationship("xiu", 10)
            $ show_stat_change("rel_xiu", gained)
            $ gained = stats.modify_relationship("hainu", -2)
            $ show_stat_change("rel_hainu", gained)

        "Đi tìm ý nghĩa (Ủng hộ Hải Nữ)":
            mc "\"Em nghĩ hạnh phúc là khi mình tìm thấy ý nghĩa sống, hoặc làm được gì đó có ích.\""
            mc "\"Như chị Nữ nói, vui thú nhất thời rồi cũng sẽ qua, cái đọng lại mới quan trọng.\""

            show yuri 1a at t21
            show monika 2p at t22

            hainu "\"Nghe chưa? Cậu ấy hiểu chuyện hơn cô tưởng đấy.\""
            xiu "\"Hứ! Đồ ẻo lả. Chả thú vị gì cả.\""

            $ gained = stats.modify_relationship("hainu", 10)
            $ show_stat_change("rel_hainu", gained)
            $ gained = stats.modify_relationship("xiu", -2)
            $ show_stat_change("rel_xiu", gained)

    show yuri 1a at t21
    show monika 1a at t22

    "Cuộc tranh luận kết thúc, nhưng dường như nó đã định hình một cái gì đó trong tôi."

    hide yuri with dissolve
    hide monika with dissolve
    
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

    scene bg mc_room with dissolve_scene_full
    play music daily_life fadein 1.0
    
    # Daily logic: regen stats
    $ daily_changes = stats.update_daily()
    
    return

label ch2_day_end:
    scene black with dissolve
    "Một ngày nữa lại kết thúc."
    $ renpy.pause(1.0)
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
    play music gym_theme fadein 1.0

    # Increment count

    $ stats.gym_count += 1
    
    if stats.gym_count == 1:
        # Lần 1: Gà mờ
        mc "\"Mùi mồ hôi, tiếng tạ va vào nhau 'keng keng'... Đây đích thị là thánh địa của mấy gã to xác.\""
        mc "\"Mình thử nâng quả tạ 5kg xem sao... Ái da! Trẹo cả tay.\""
        
        show monika 2l at t11
        xiu "\"Yếu nhớt! Cầm cái tạ như cầm ly trà sữa thế kia bao giờ mới có người yêu?\""
        
        $ stats.modify_doi_song(5)
        $ show_stat_change("doi_song", 5)
        
    elif stats.gym_count <= 3:
        # Lần 2-3: Bắt đầu quen
        mc "\"Hôm nay mình đã biết cách thở đúng nhịp. Hít vào, thở ra...\""
        mc "\"Cảm giác cơ bắp bắt đầu đau nhức, nhưng là cái đau của sự phát triển.\""
        
        show monika 1k at t11
        xiu "\"Khá đấy cu. Nay đẩy ngực được 20kg rồi à? Cố lên, sắp đủ trình làm bao cát cho chị rồi.\""
        
        $ stats.modify_doi_song(10)
        $ show_stat_change("doi_song", 10)
        $ gained = stats.modify_relationship("xiu", 2)
        $ show_stat_change("rel_xiu", gained)
        
    else:
        # Lần 4+: Thành thạo
        mc "\"Nhìn vào gương, mình thấy cơ ngực đã bắt đầu lộ rõ.\""
        mc "\"Giờ mình có thể nâng mức tạ mà tuần trước mình còn không nhấc nổi.\""
        
        show monika 3b at t11
        xiu "\"Uầy, nhìn 'mlem' phết rồi đấy. Tối nay đi làm bát phở gầu bò nạm thưởng cho cái body này không?\""
        
        $ stats.modify_doi_song(15)
        $ show_stat_change("doi_song", 15)
        $ gained = stats.modify_relationship("xiu", 5)
        $ show_stat_change("rel_xiu", gained)
        
    return

label ch2_library_event:
    scene bg library with wipeleft_scene
    play music library_theme fadein 1.0
    
    # Increment count
    $ stats.lib_count += 1
    
    if stats.lib_count == 1:
        # Lần 1: Buồn ngủ
        mc "\"Thư viện yên tĩnh quá... Mùi sách cũ làm mình muốn... khò khò...\""
        mc "\"Mở cuốn 'Phê phán lý tính thuần túy' ra đọc được 2 dòng thì mắt díp lại.\""
        
        show yuri 2h at t11
        hainu "\"Thư viện là nơi nuôi dưỡng tâm hồn, không phải chỗ ngủ trọ. Ngồi thẳng lưng lên.\""
        
        $ stats.modify_hoc_tap(5)
        $ show_stat_change("hoc_tap", 5)
        
    elif stats.lib_count <= 3:
        # Lần 2-3: Tập trung
        mc "\"Mình bắt đầu hiểu được sơ sơ khái niệm 'Vật tự nó' rồi.\""
        mc "\"Hoá ra triết học không khô khan như mình tưởng, nó giống như giải một bài toán về cuộc đời vậy.\""
        
        show yuri 1a at t11
        hainu "\"Cậu đang đọc Kant sao? Một lựa chọn không tồi. Nếu có chỗ nào không hiểu, tôi có thể... gợi ý một chút.\""
        
        $ stats.modify_hoc_tap(10)
        $ show_stat_change("hoc_tap", 10)
        $ gained = stats.modify_relationship("hainu", 2)
        $ show_stat_change("rel_hainu", gained)
        
    else:
        # Lần 4+: Giác ngộ -> Unlock True Ending condition
        mc "\"Mình tìm thấy sự liên kết giữa Hội hoạ và Triết học.\""
        mc "\"Cả hai đều là cách con người mô tả thế giới. Một bên dùng màu sắc, một bên dùng tư duy.\""
        
        show yuri 1s at t11
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
        "Sang phòng Xỉu chơi (Tăng thiện cảm)" if current_day % 2 == 0: # Available on even days
            scene bg ktx with wipeleft
            "Tôi sang phòng bà chị Xỉu chơi game."
            "Tuy thua liểng xiểng nhưng cũng xả được stress."
            $ stats.modify_doi_song(5)
            $ gained = stats.modify_relationship("xiu", 3)
            $ show_stat_change("rel_xiu", gained)
             
        "Nhắn tin hỏi bài Nữ (Tăng thiện cảm)" if current_day % 2 != 0: # Available on odd days
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
