# ================================================
# CHAPTER 1: EIKASIA (ẢO ẢNH) - DAY 1 & 2
# Brother Thang Philosophy Club
# ================================================

label ch1_day1_day2:
    
    # Show stats UI
    show screen stats_display
    
    $ current_day = 1
    $ current_chapter = 1
    
    stop music fadeout 2.0
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢ NH 1{/color}{/size}\n{size=24}NHÀ - ĐÊM{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    scene bg mc_room with dissolve_scene_full
    
    play music daily_life fadein 1.0
    
    # ========================================
    # CẢNH 1: NHÀ - ĐÊM
    # ========================================
    
    "Đêm khuya."
    
    mc "(lo lắng) \"Ok… check điểm nào…\""
    
    "Click."
    
    "Danh sách trúng tuyển dài đằng đẵng hiện ra."
    
    "Nhưng lại… không có tên mình."
    
    mc "(thở dài)"
    mc "\"…Hầy.\""
    
    "Không buồn."
    "Không sốc."
    "Chỉ là cảm giác quen quen… Như mấy lần mở ví ra dù biết trước nó trống trơn."
    
    mc "(Chắc do hội đồng không đủ trình để hiểu nghệ thuật của mình…)"
    
    play sound "sfx/closet-open.ogg"
    
    "Cánh cửa mở."
    
    "Bố tôi, Võ Quang Hưng, một Đại Tá quân đội, bước vào."
    
    show dad at t11
    
    dad "\"Trượt rồi à?\""
    
    mc "\"Vâng… con thấy mình làm bài cũng ổn áp mà nhỉ.\""
    
    dad "\"Ừ. Ổn cái đầu mày ý!\""
    
    mc "\"…?\""
    
    dad "\"Thôi. Trượt rồi thì vào FPT mà học đi.\""
    dad "\"Ít nhất cũng phải lấy được cái bằng Đại học.\""
    
    mc "\"Nhưng…\""
    
    dad "\"Nhưng nhị cái gì!\""
    dad "\"Mày có nghe lời tao không thì bảo hả?\""
    
    mc "\"….\""
    mc "\"Dạ vâng ạ...\""
    
    hide dad with dissolve
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢNH 2{/color}{/size}\n{size=24}SÂN TRƯỜNG FPT - SÁNG{/size}\n{size=18}Ngày 1{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 2: NGÀY 1 (SÂN - SÁNG)
    # ========================================
    
    scene bg class_day with wipeleft_scene
    
    play music daily_life fadein 1.0
    
    "Tại sân trường FPT."
    "Sân trường đông nghịt."
    "Ai cũng trông như nhân vật chính của cuộc đời mình."
    "Còn mình thì như một thằng NPC vừa spawn vậy."
    
    mc "(Đông quá!)"
    mc "(Đông thế này chắc không ai để ý mình đâu nhỉ.)"
    
    # NEW: Phone call from Xỉu
    play sound "sfx/pageflip.ogg"  # Phone ring sound
    
    "Bỗng nhiên, điện thoại bất ngờ nhận một cuộc gọi từ số lạ."
    
    mc "\"???\""
    mc "\"Ai đây nhở?\""
    
    # Accept call
    "Click."
    
    show monika 1d at t11
    
    xiu "\"Alo Thắng à, em có phải là Thắng không?\""
    
    mc "(???) \"Dạ vâng. Cho hỏi ai đấy ạ?\""
    
    show monika 1j
    
    xiu "\"Chị là Võ Minh Xỉu, thành viên câu lạc bộ Triết học Plato.\""
    xiu "\"Nghe bảo cu em là sinh viên mới, không biết có rảnh không nhỉ?\""
    
    show monika 5a
    
    xiu "\"Nếu rảnh thì tham gia CLB của bọn chị đi. Khi tham gia sẽ có cơ hội nhận được rất nhiều ưu đãi hấp dẫn…\""
    
    mc "\"Dạ thôi chị ơi, em hơi bận xíu...\""
    
    show monika 1j
    
    xiu "\"Ui, thôi em đừng có chối, thông tin về chiều cao, cân nặng, sở thích, địa chỉ nhà trọ, lịch sinh hoạt của em,… chị có cả rồi ở đây rồi.\""
    xiu "\"Cu em có cần chị đọc cho nghe một số thông tin không?\""
    
    mc "\"Hả? Thôi thôi cho em xin…\""
    
    show monika 1k
    
    xiu "\"Nếu vậy thì hãy tham gia ngay cùng bọn chị nào!\""
    xiu "\"Vậy nhá, chị rất mong chờ được gặp lại em tại CLB Triết học Plato, tầng 2, phòng 217, toà Beta, Trường Đại học FPT!\""
    
    mc "(Mình không muốn vào đó đâu, nghe chán lắm!)"
    mc "(Nhưng nếu người ta đã mời như vậy thì từ chối có vẻ cũng hơi ngại…)"
    
    menu:
        xiu "\"Vậy em có tham gia không?\""
        
        "Dạ vâng, em sẽ tham gia ạ":
            mc "\"Dạ vâng, em sẽ tham gia ạ.\""
            
            # Relationship tăng với Xỉu
            $ multiplier = stats.get_stat_multiplier_xiu()
            $ gained = stats.modify_relationship("xiu", 5, multiplier)
            $ show_stat_change("rel_xiu", gained)
            
            show monika 1k
            
            xiu "\"Ngon~ Học xong nhớ lên đăng ký em nhé. Bái bai!\""
    
    hide monika with dissolve
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢNH 3{/color}{/size}\n{size=24}PHÒNG CLB TRIẾT HỌC PLATO - CHIỀU{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 3: CLB - CHIỀU
    # ========================================
    
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Mở cửa ra, trước mặt là một người con gái đứng nhìn xuống dưới sân trường."
    "Đó có lẽ là hội trưởng CLB Triết học Plato – Vũ Hải Nữ."
    
    # Hải Nữ now uses Yuri sprite (as president)
    show yuri 1a at t11
    
    hainu "\"Eikasia.\""
    
    mc "\"..?\""
    mc "(Nghe giống như tên một món vũ khí trong game RPG nào đó vậy.)"
    
    show yuri 1f
    
    hainu "\"Là cấp độ thấp nhất của nhận thức.\""
    
    "Hội Trưởng quay lại, nhìn thẳng vào tôi."
    
    show yuri 2f at t11
    
    hainu "\"Cậu kia. Cậu thấy bầu trời màu gì?\""
    
    mc "(bối rối) \"Ờ… màu xanh ạ.\""
    
    show yuri 3h
    
    hainu "\"Thiển cận!\""
    hainu "\"Mặt trời không chỉ phát ra một màu, mà là cả một phổ ánh sáng.\""
    hainu "\"Nếu tôi nói… Bầu trời thực chất chỉ là khoảng đen của vũ trụ.\""
    
    mc "\"…Hả?\""
    
    show yuri 2f
    
    hainu "\"Bầu trời vốn không hề xanh.\""
    hainu "\"Màu xanh cậu thấy… Là ánh sáng bị tán xạ… Chỉ là ảo ảnh mà cậu tạo ra để diễn giải về thế giới.\""
    
    "Một khoảng im lặng…"
    
    $ stats.met_hainu = True
    
    show yuri 1a
    
    hainu "\"Vậy cậu đến đây làm gì?\""
    
    mc "(Gượng cười) \"Dạ em muốn gia nhập CLB ạ!\""
    
    show yuri 1f
    
    hainu "\"…\""
    
    show yuri 1a
    
    hainu "\"Được thôi… Cậu được nhận.\""
    
    # Tăng relationship với Hải Nữ
    $ multiplier = stats.get_stat_multiplier_hainu()
    $ gained = stats.modify_relationship("hainu", 3, multiplier)
    $ show_stat_change("rel_hainu", gained)
    
    hide yuri with dissolve
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢNH 3{/color}{/size}\n{size=24}KÝ TÚC XÁ - TỐI{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 3B: KTX - TỐI (Cá cược lần 1)
    # ========================================
    
    scene bg bedroom with wipeleft_scene
    play music tense fadein 1.0
    
    "Về đến ký túc xá..."
    
    show monika 1d at t11
    
    xiu "\"Ê cu.\""
    
    mc "\"Dạ?\""
    
    $ stats.met_xiu = True
    
    show monika 1j
    
    xiu "(cười đểu) \"Tân sinh viên hả?\""
    xiu "\"Muốn chơi một trò chơi đêm muộn khiến bao con người thổn thức chứ?\""
    
    mc "(Đỏ mặt) \"Dạ?\""
    
    show monika 5a
    
    xiu "\"Đùa xíu thôi! Tối nay đang có trận MU đá với MC, cu em có muốn vào xem cùng chị không nào?\""
    xiu "\"Cơ mà chỉ xem thôi thì chán phèo, hay là chị em mình làm trận cá cược đi nhỉ?\""
    xiu "\"Nhóc thấy thế nào?\""
    
    mc "(Nghe có vẻ nguy hiểm. Cơ mà có tận 50%% cơ hội thắng mà, hay thử xíu nhỉ?)"
    
    menu:
        xiu "\"Vậy chơi không?\""
        
        "Chơi thì chơi, sợ gì?":
            mc "\"Chơi thì chơi, sợ gì?\""
            
            show monika 1k
            
            xiu "\"Có chí khí đấy, vậy cu em theo đội nào?\""
            
            menu:
                "Chọn đội?"
                
                "ALL IN MU!!!":
                    mc "\"Dạo này MU đang mạnh, theo MU vậy!\""
                    $ xiu_bet_choice = "MU"
                
                "ALL IN MC!!!":
                    mc "\"Dạo này MU đá đần lắm… Thôi thì theo MC vậy!\""
                    $ xiu_bet_choice = "MC"
            
            show monika 2a
            
            xiu "\"OK! OK! Vậy thì chị theo đội còn lại.\""
            
            "..."
            "Xem trận đấu..."
            "..."
            
            # Random kết quả (50/50)
            $ match_result = renpy.random.choice(["MU", "MC"])
            
            if xiu_bet_choice == match_result:
                # Thắng!
                show monika 2h
                
                xiu "\"Ây da! Thua mất rồi! Lần này coi như em gặp may.\""
                xiu "\"Cu em được đấy! Lần sau lại chơi tiếp nhá.\""
                
                # Nhận tiền
                $ stats.modify_tien(50000)
                $ show_stat_change("tien", 50000)
                
                # Relationship tăng
                $ gained = stats.modify_relationship("xiu", 10)
                $ show_stat_change("rel_xiu", gained)
                
            else:
                # Thua
                show monika 1k
                
                xiu "\"Hehe! Chị thắng rồi! Tiền cu em chị xin nhá!\""
                
                # Mất tiền
                $ stats.modify_tien(-50000)
                $ show_stat_change("tien", -50000)
                
                # Relationship giảm
                $ gained = stats.modify_relationship("xiu", -5)
                $ show_stat_change("rel_xiu", gained)
            
            show monika 1a
            
            xiu "\"Chị ở phòng bên cạnh, nếu cần gì cứ sang gọi chị nhá!\""
        
        "Không, em không chơi cá cược.":
            mc "\"Dạ thôi chị, em không muốn chơi cá cược ạ.\""
            mc "\"Em sợ mất tiền lắm.\""
            
            show monika 5a
            
            xiu "\"Ừ thì thôi. Nhát thế thì đành chịu vậy.\""
            xiu "\"Chị ở phòng bên cạnh, nếu cần gì cứ sang gọi chị nhá!\""
    
    hide monika with dissolve
    
    # ========================================
    # DAY 1 → DAY 2 TRANSITION
    # ========================================
    
    # Scene label
    scene black
    with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}{color=#ffdd00}CẢNH 4{/color}{/size}\n{size=24}PHÒNG CLB - SÁNG{/size}\n{size=18}Ngày 2{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 4: CLB - SÁNG (Ngày 2)
    # ========================================
    
    # DAY 2 INITIALIZATION
    $ current_day = 2
    $ stats.update_daily()
    
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Vừa bước vào phòng CLB, tình cờ thế nào lại gặp lại chị gái tối qua."
    
    show monika 1d at t11
    
    xiu "\"Ô! Xem ai đây kìa! Cu em là thành viên mới của cái CLB tẻ nhạt này à?\""
    xiu "\"Trùng hợp ghê, chị cũng là thành viên đó!\""
    
    show monika 1k
    
    xiu "\"Hữu duyên thế này thì tối này chị em ta lại phải làm ván cá độ rồi!\""
    
    mc "\"Dạ… Dạ vâng…\""
    
    # Hải Nữ xuất hiện
    show monika 1d at t21
    show yuri 3y at t22
    
    hainu "\"XỈU!!!\""
    
    "Hội trưởng bước vào."
    
    show yuri 4y at t22
    
    hainu "\"BÀ LẠI ĐI GỌI ĐIỆN CHÈO KÉO THÀNH VIÊN VÀO CLB ĐỂ TIỆN TAY LỪA ĐẢO NỮA HẢ?\""
    hainu "\"HÔM QUA CÓ MỘT NGƯỜI MỚI GIA NHẬP, CÓ PHẢI LÀ DO BÀ DỤ DỖ KHÔNG HẢ?\""
    hainu "\"ĐÂY LÀ CLB TRIẾT CHỨ KHÔNG PHẢI Ổ LỪA ĐẢO CỦA BÀ ĐÂU NHÁ!\""
    
    show monika 2p at t21
    
    xiu "(lủi mất) \"Đùa tí, làm gì căng.\""
    
    show yuri 2f at t22
    
    hainu "\"Còn cả cậu nữa, ai rủ gì cậu cũng làm à? Chính kiến của cậu đâu hả?\""
    
    mc "\"Dạ…. Dạ…. Tại em nghĩ chỉ chơi cho vui thôi chứ đâu có biết là lừa đảo….\""
    
    show yuri 1h
    
    hainu "\"…. Thật là một niềm tin mù quáng….\""
    hainu "\"Sống trên đời phải biết nghi ngờ, nếu không thì chả khác nào mấy thằng nghe lời người ta cầm 2 tỷ đầu tư vào HDPE để rồi tán gia bại sản.\""
    
    show yuri 1g
    
    hainu "\"Thôi được rồi… nay cậu về đi.\""
    
    hide yuri with dissolve
    hide monika with dissolve
    
    # ========================================
    # HÀNH LANG - SÁNG (Betting choice 2)
    # ========================================
    
    scene bg corridor with wipeleft_scene
    
    "Vừa ra khỏi phòng CLB đã thấy Xỉu đuổi theo."
    
    show monika 2a at t11
    
    xiu "\"Cu em chịu khó ngồi nghe cái bà hội trưởng đấy lảm nhảm thế nhỉ?\""
    xiu "\"Phải chị chị làm vội ba giấc rồi!\""
    
    show monika 1j
    
    xiu "\"Thế kèo của chị em mình tối nay chú tính thế nào? Chơi hay không chơi nói một lời nào.\""
    
    mc "(Thắng ăn cả mà thua thì ăn ***, có lẽ mình nên suy nghĩ cẩn thận một chút…)"
    
    menu:
        xiu "\"Vậy chơi không?\""
        
        "Chơi thì chơi, sợ gì?":
            mc "\"Chơi thì chơi, sợ gì?\""
            
            show monika 1k
            
            xiu "\"Ngon, thắng rồi! Tiền cu em chị xin nhá!\""
            
            # Tự động thua (theo story)
            $ stats.modify_tien(-50000)
            $ show_stat_change("tien", -50000)
            
            $ gained = stats.modify_relationship("xiu", -3)
            $ show_stat_change("rel_xiu", gained)
            
        "Thôi, nay em xin kiếu!":
            mc "\"Thôi, nay em xin kiếu!\""
            mc "\"Em đang hơi cần tiền lắm, không dám liều nữa.\""
            
            show monika 5a
            
            xiu "\"Chậc... Tuỳ cu.\""
            xiu "\"Vậy thì chị đi kiếm con mồi khác vậy.\""
    
    hide monika with dissolve
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢNH 5{/color}{/size}\n{size=24}TOUR TRƯỜNG - CHIỀU{/size}\n{size=18}Thư viện → Gym → Canteen{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 5: TOUR TRƯỜNG VỚI XỈU (NEW SCENE)
    # ========================================
    
    scene bg corridor with wipeleft_scene
    play music daily_life fadein 1.0
    
    "Vừa ra khỏi phòng CLB đã thấy Xỉu đuổi theo."
    
    show monika 2a at t11
    
    xiu "\"Ây cu.\""
    xiu "\"Đừng giận chị nha.\""
    xiu "\"Dù sao thì chị em mình cũng cùng CLB, phòng lại còn cạnh nhau nữa…\""
    xiu "\"Hay là, để tạ lỗi, chị dắt em đi xem trường nha.\""
    
    mc "(Không sao, em cũng không giận gì đâu.)"
    
    menu:
        xiu "\"Vậy có đồng ý không?\""
        
        "Không sao, em cũng không giận gì đâu":
            mc "\"Không sao, em cũng không giận gì đâu.\""
            
            show monika 1k
            
            xiu "\"Ngon. Chị em mình cứ thế thôi, hẹ hẹ hẹ.\""
            xiu "\"Được rồi, để chị dẫn đoàn nhà mình đi tham quan trường nào!\""
            
            # Relationship tăng
            $ gained = stats.modify_relationship("xiu", 5)
            $ show_stat_change("rel_xiu", gained)
        
        "Em cũng tham quan vòng rồi, không cần phiền chị đâu ạ":
            mc "\"Em cũng tham quan vòng rồi, không cần phiền chị đâu ạ.\""
            
            show monika 5a
            
            xiu "\"Thế thôi vậy. Em về nha, chị đi trước đây.\""
            
            hide monika with dissolve
            
            # Skip tour, jump to CẢNH 6
            jump ch1_scene6
    
    # Tour 1: Thư viện
    scene bg corridor with fade
    
    show monika 1a at t11
    
    xiu "\"Đầu tiên là thư viện, là một nơi vô cùng lý tưởng để ngồi ôn lại bài cũ…, hoặc là ngủ.\""
    
    show monika 1j
    
    xiu "\"Nghe bảo Hội Trưởng thích mấy anh zai học bá đó, nếu em định tán chị ấy thì tốt nhất thử thông thạo bảy mấy món triết học Mác Leenin hay Tư tưởng Hồ Chí Minh đi.\""
    
    mc "\"Ghê vậy sao? Học xong đống đấy thì chắc tu vi đắc đạo lúc nào chả biết.\""
    
    # Tăng học tập vì có hint
    $ stats.modify_hoc_tap(3)
    $ show_stat_change("hoc_tap", 3)
    
    # Tour 2: Gym
    scene bg class_day with fade
    
    show monika 5a at t11
    
    xiu "\"Kế đến là phòng Gym, nơi các anh giai sáu múi flex đống cơ của mình.\""
    xiu "\"Gu chị là mấy anh chàng cao to đen hôi thể hình lực lưỡng, thi thoảng ra ngó mấy anh giai chống đẩy mà them chảy nước giãi.\""
    
    mc "\"Tém tém thôi chị ơi, liêm xỉ trôi theo hàng nước của chị rồi kìa.\""
    
    show monika 1k
    
    # Tour 3: Canteen & Robot T31
    scene bg class_day with fade
    
    show monika 1a at t11
    
    xiu "\"Cuối cùng là căng tin, nơi sinh hoạt văn hoá của hội những người không biết xấu hổ.\""
    
    mc "\"A! Con lợn này.\""
    
    show monika 1d at t11
    
    xiu "\"Đây là robot bán hàng số hiệu T31 tên là DaoChiCuong do tập đoàn FPT sản xuất.\""
    xiu "\"Phế lắm, chị chửi nó suốt. Mong sau này robot xâm chiếm thế giới nó không nhớ mặt chị.\""
    
    # T31 interaction
    mc "\"Uhm... Chào bạn T31?\""
    
    "Robot T31 quay lại nhìn tôi với đôi mắt LED đỏ."
    
    "T31" "\"Hasta la vista, baby.\""
    
    mc "(Ủa... Sao lại tiếng Tây???)"
    
    show monika 2p
    
    xiu "\"Thấy chưa! Nó bị lỗi phần mềm rồi đấy. Bảo sửa mãi không chịu.\""
    
    "T31" "\"I'll be back.\""
    
    "Robot T31 lăn đi về phía kho."
    
    mc "\"Có vẻ nó thích phim Terminator nhỉ...\""
    
    show monika 1k
    
    xiu "\"Ai mà biết được. Chắc là ai đó cài đặt lỗi cho vui.\""
    
    "..."
    
    show monika 2a
    
    xiu "\"Thôi muộn rồi, chị té trước đây nha.\""
    
    # Relationship và đời sống tăng
    $ gained = stats.modify_relationship("xiu", 5)
    $ show_stat_change("rel_xiu", gained)
    $ stats.modify_doi_song(5)
    $ show_stat_change("doi_song", 5)
    
    hide monika with dissolve
    
    # Scene label
    scene black
    with dissolve
    
    centered "{size=40}{color=#ffdd00}CẢNH 6{/color}{/size}\n{size=24}PHÒNG CLB - TỐI{/size}\n{size=18}Giúp Hội Trưởng xử lý sổ sách{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH 6: CLB - TỐI (Giúp Hải Nữ)
    # ========================================
    
    label ch1_scene6:
    
    scene bg class_day with wipeleft_scene
    
    "Tan học rồi…"
    
    mc "\"Tan học rồi, về thôi.\""
    mc "\"Thôi chết, chìa khoá đâu rồi?\""
    mc "\"Hình như mình để quên trên phòng CLB rồi.\""
    
    scene bg club_day with fade
    play music club_theme fadein 1.0
    
    "Phòng CLB vẫn sáng đèn."
    "Hội Trưởng ở trong phòng, trước mặt là một chồng sổ sách cao chạm trần!!?"
    
    show yuri 1a at t11
    
    hainu "\"Cậu là thành viên mới. Muộn rồi còn tới đây làm gì?\""
    
    mc "\"Em để quên chìa khoá ạ.\""
    
    show yuri 1f
    
    hainu "\"Chìa khoá hả? Tôi thấy nó nên đặt ở kia kìa.\""
    
    "Đã tìm thấy chìa khoá, đang định đi về…."
    
    show yuri 2f
    
    hainu "\"Này.\""
    
    mc "\"Dạ?\""
    
    hainu "\"Giúp tôi xử lý đống sổ sách này với được chứ.\""
    hainu "\"Tất nhiên tôi sẽ trả lương theo ngày.\""
    
    mc "(Sổ sách nhiều vượt mức pickleball rồi, cơ mà vừa hay, tiền mình có hơi vô gia cư…)"
    
    menu:
        hainu "\"Vậy cậu có giúp không?\""
        
        "Dạ vâng ạ…":
            mc "\"Dạ vâng ạ…\""
            
            "Tài liệu chất đống như núi, xử lý xong thì cũng đã muộn."
            
            # Stats giảm đời sống vì làm việc muộn
            $ stats.modify_doi_song(-5)
            $ show_stat_change("doi_song", -5)
            
            show yuri 1a
            
            hainu "\"Nay cảm ơn cậu. Không có cậu chắc tôi bị đống giấy tờ này bán hành đến chết mất!\""
            hainu "\"…\""
            hainu "\"Chiều nay… Tôi có hơi nặng lời.\""
            
            show yuri 2f
            
            hainu "\"Nhưng mà… Con người khác với mọi sinh vật ở khả năng suy nghĩ và phản biện.\""
            hainu "\"Suy nghĩ và phản biện là nền móng của triết học.\""
            hainu "\"Nếu cậu thật sự muốn tham gia CLB này, thì mong cậu hãy học cách tư duy…\""
            
            # Relationship tăng mạnh
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 10, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            # Học tập tăng
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
        
        "Nay em lại hơi bận…":
            mc "\"Nay em lại hơi bận…\""
            
            "Định đi nhưng thấy vẻ mặt tiều tuỵ của Hội Trưởng, thôi đành giúp vậy…"
            
            mc "\"…Thôi được rồi, em sẽ giúp chị.\""
            
            show yuri 1a
            
            "Tài liệu chất đống như núi, xử lý xong thì cũng đã muộn."
            
            # Stats giảm đời sống vì làm việc muộn
            $ stats.modify_doi_song(-5)
            $ show_stat_change("doi_song", -5)
            
            hainu "\"Nay cảm ơn cậu. Không có cậu chắc tôi bị đống giấy tờ này bán hành đến chết mất!\""
            hainu "\"…\""
            hainu "\"Chiều nay… Tôi có hơi nặng lời.\""
            
            show yuri 2f
            
            hainu "\"Nhưng mà… Con người khác với mọi sinh vật ở khả năng suy nghĩ và phản biện.\""
            hainu "\"Suy nghĩ và phản biện là nền móng của triết học.\""
            hainu "\"Nếu cậu thật sự muốn tham gia CLB này, thì mong cậu hãy học cách tư duy…\""
            
            # Relationship tăng mạnh
            $ multiplier = stats.get_stat_multiplier_hainu()
            $ gained = stats.modify_relationship("hainu", 10, multiplier)
            $ show_stat_change("rel_hainu", gained)
            
            # Học tập tăng
            $ stats.modify_hoc_tap(5)
            $ show_stat_change("hoc_tap", 5)
    
    hide yuri with dissolve
    
    # ========================================
    # SCENE KẾT - ĐÊM
    # ========================================
    
    scene bg bedroom with fade
    play music sad fadein 1.0
    
    "Về đến phòng..."
    
    mc "(ngáp) \"Ôi mệt quá…\""
    mc "\"Hôm nay quả thật là một ngày dài…\""
    mc "\"Gặp được Hội Trưởng, chị Xỉu… Cuộc sống đại học bắt đầu từ đây!\""
    mc "\"Ngày mai… Mong mọi chuyện vẫn ổn…\""
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    # ========================================
    # END OF CHAPTER 1 (Day 1-2)
    # ========================================
    
    $ renpy.pause(2.0)
    
    # Transition to Chapter 2 (Day 3)
    # Note: Stats UI remains visible for continuity
    call ch2_day3
    
    return
