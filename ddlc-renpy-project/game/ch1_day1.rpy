# ================================================
# CHAPTER 1: EIKASIA (ẢO ẢNH) - DAY 1
# Brother Thang Philosophy Club
# ================================================

label ch1_day1:
    
    # Show stats UI
    show screen stats_display
    
    $ current_day = 1
    $ current_chapter = 1
    
    stop music fadeout 2.0
    scene bg mc_room with dissolve_scene_full
    
    play music daily_life fadein 1.0
    
    # ========================================
    # SCENE 1: NHÀ - ĐÊM
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
    
    # ========================================
    # SCENE 2: SÂN TRƯỜNG - SÁNG
    # ========================================
    
    scene bg class_day with wipeleft_scene
    
    play music daily_life fadein 1.0
    
    "Tại sân trường FPT."
    "Sân trường đông nghịt."
    "Ai cũng trông như nhân vật chính của cuộc đời mình."
    "Còn mình thì như một thằng NPC vừa spawn vậy."
    
    mc "(Đông quá!)"
    mc "(Đông thế này chắc không ai để ý mình đâu nhỉ.)"
    
    # Gặp Hương lần đầu
    show sayori 1b at t11
    
    huong "\"Alo Thắng à, anh có phải là Thắng không?\""
    
    "Tôi quay đầu lại, bất chợt thấy một bóng dáng quen thuộc."
    
    mc "\"Ủa Hương? Sao em ở đây?\""
    
    show sayori 4r
    
    huong "\"Em thi vượt cấp để được vào đây cùng anh đó.\""
    
    mc "\"Vậy sao…\""
    
    # Set flag đã gặp Hương
    $ stats.met_huong = True
    
    "Đây là Khuất Quang Hương, bạn thuở nhỏ của tôi."
    "Một hacker thần đồng nghìn năm có một."
    "Cơ mà tính cách ẻm có hơi dị dị…."
    
    show sayori 2l
    
    huong "\"Anh Thắng à, anh tính bỏ em đi mà trốn lên tận cái trường này sao?\""
    
    mc "\"Không anh đâu có...\""
    
    show sayori 2m
    
    huong "\"Ui, thôi anh đừng có chối, thông tin về chiều cao, cân nặng, sở thích, địa chỉ nhà trọ, lịch sinh hoạt của anh,… em có cả rồi ở đây rồi.\""
    huong "\"Anh có cần em đọc cho nghe một số thông tin không?\""
    
    mc "\"Hả? Thôi thôi xin em…\""
    
    show sayori 1a
    
    huong "\"Nếu muốn em tha cho thì… Đăng ký vào CLB Triết của trường này đi.\""
    
    show sayori 1k
    
    huong "(thì thầm) \"Đăng ký vào rồi anh đừng có hòng mà thoát khỏi tay em.\""
    
    mc "(Mình không muốn vào đó đâu, nghe chán lắm!)"
    mc "(Nhưng nếu Hương đã bảo vậy thì… Thử vào xem sao…)"
    
    # CHOICE 1: Vào CLB (forced cho MVP)
    menu:
        huong "\"Vậy anh nghĩ sao?\""
        
        "Ừ… được rồi":
            mc "\"Ừ… được rồi.\""
            
            # Relationship tăng
            $ multiplier = stats.get_stat_multiplier_huong()
            $ gained = stats.modify_relationship("huong", 5, multiplier)
            $ show_stat_change("rel_huong", gained)
            
            show sayori 4r
            
            huong "\"Ngoan~ Học xong nhớ lên đăng ký đi nhé. Em đi trước đây.\""
    
    hide sayori with dissolve
    
    # ========================================
    # SCENE 3: PHÒNG CLB - TRƯA
    # ========================================
    
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Mở cửa ra, trước mặt là một người con gái đứng nhìn xuống dưới sân trường."
    "Đó có lẽ là hội trưởng CLB Triết học Plato – Đào Chí Ischyros."
    
    show yuri 1a at t11
    
    ischyros "\"Eikasia.\""
    
    mc "\"..?\""
    mc "(Nghe giống như tên một món vũ khí trong game RPG nào đó vậy.)"
    
    show yuri 1f
    
    ischyros "\"Là cấp độ thấp nhất của nhận thức.\""
    
    "Hội Trưởng quay lại, nhìn thẳng vào tôi."
    
    show yuri 2f at t11
    
    ischyros "\"Cậu kia. Cậu thấy bầu trời màu gì?\""
    
    mc "(bối rối) \"Ờ… màu xanh ạ.\""
    
    show yuri 3h
    
    ischyros "\"Thiển cận!\""
    ischyros "\"Mặt trời không chỉ phát ra một màu, mà là cả một phổ ánh sáng.\""
    ischyros "\"Nếu tôi nói… Bầu trời thực chất chỉ là khoảng đen của vũ trụ.\""
    
    mc "\"…Hả?\""
    
    show yuri 2f
    
    ischyros "\"Bầu trời vốn không hề xanh.\""
    ischyros "\"Màu xanh cậu thấy… Là ánh sáng bị tán xạ… Chỉ là ảo ảnh mà cậu tạo ra để diễn giải về thế giới.\""
    
    "Một khoảng im lặng…"
    
    $ stats.met_ischyros = True
    
    show yuri 1a
    
    ischyros "\"Vậy cậu đến đây làm gì?\""
    
    mc "(Gượng cười) \"Dạ em muốn gia nhập CLB ạ!\""
    
    show yuri 1f
    
    ischyros "\"…\""
    
    show yuri 1a
    
    ischyros "\"Được thôi… Cậu được nhận.\""
    
    # Tăng relationship với Ischyros
    $ multiplier = stats.get_stat_multiplier_ischyros()
    $ gained = stats.modify_relationship("ischyros", 3, multiplier)
    $ show_stat_change("rel_ischyros", gained)
    
    hide yuri with dissolve
    
    # ========================================
    # SCENE 4: PHÒNG CLB - CHIỀU
    # ========================================
    
    scene bg club_day with dissolve
    
    "Tan học rồi…"
    
    mc "\"Tan học rồi, về thôi.\""
    mc "\"Thôi chết, chìa khoá đâu rồi?\""
    mc "\"Hình như mình để quên trên phòng CLB rồi.\""
    
    scene bg club_day with fade
    
    "Vừa bước vào phòng đã thấy một đàn chị nằm trên ghế sofa."
    
    show natsuki 1c at t11
    
    hainu "\"Này.\""
    
    mc "\"Dạ?\""
    
    show natsuki 2c
    
    hainu "\"Giúp tôi mấy việc.\""
    
    $ stats.met_hainu = True
    
    # CHOICE 2: Giúp Hải Nữ
    menu:
        hainu "\"Cậu có rảnh không?\""
        
        "Dạ vâng ạ…":
            mc "\"Dạ vâng ạ…\""
            
            "Sắp xếp tài liệu."
            "Dọn dẹp nhà cửa."
            "Mấy việc lặt vặt nhưng làm rất mệt."
            
            # Stats giảm
            $ stats.modify_doi_song(-5)
            $ show_stat_change("doi_song", -5)
            
            "Trong khi đó đàn chị vẫn cứ ung dung ngồi nghỉ trên sofa."
            
            show natsuki 1a
            
            hainu "\"Tôi là Vũ Hải Nữ, thủ quỹ của CLB này.\""
            hainu "\"Cậu là thành viên mới hả, rảnh chứ?\""
            
            mc "\"Dạ… rảnh ạ…\""
            
            show natsuki 1k
            
            hainu "\"Được! Vậy làm việc cho tôi.\""
            hainu "\"Chỉ cần làm những việc mà hội trưởng giao cho tôi là được!\""
            hainu "\"Tất nhiên tôi sẽ trả tiền.\""
            
            mc "\"Tiền… thật chứ?\""
            
            show natsuki 1a
            
            hainu "\"Tôi không rảnh để đùa.\""
            
            menu:
                hainu "\"Vậy cậu có nhận không?\""
                
                "Việc tốt thế này tất nhiên em nhận rồi!":
                    mc "\"Việc tốt thế này tất nhiên em nhận rồi!\""
                    
                    # Relationship tăng với Hải Nữ
                    $ multiplier = stats.get_stat_multiplier_hainu()
                    $ gained = stats.modify_relationship("hainu", 5, multiplier)
                    $ show_stat_change("rel_hainu", gained)
                    
                    show natsuki 1k
                    
                    hainu "\"Tốt. Ngày mai đến sớm nhé.\""
    
    hide natsuki with dissolve
    
    # ========================================
    # SCENE 5: KÝ TÚC XÁ - TỐI
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
    
    # CHOICE 3: Cá cược với Xỉu
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
            
            xiu "\"Chị là Võ Minh Xỉu, phòng ở bên cạnh, nếu cần gì cứ sang gọi chị nhá!\""
    
    hide monika with dissolve
    
    # ========================================
    # SCENE KẾT - ĐÊM
    # ========================================
    
    scene bg bedroom with fade
    play music sad fadein 1.0
    
    "..."
    
    mc "(ngáp) \"Ôi mệt quá…\""
    mc "\"Hôm nay quả thật là một ngày dài…\""
    mc "\"Ngày mai… Mong mọi chuyện vẫn ổn…\""
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    # Hide stats UI
    hide screen stats_display
    
    # ========================================
    # END OF DAY 1 - COMING SOON
    # ========================================
    
    $ renpy.pause(1.0)
    
    call screen coming_soon
    
    # Return to main menu
    return

