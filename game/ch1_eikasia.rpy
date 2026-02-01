# ================================================
# CHAPTER 1: EIKASIA & PISTIS (NGÀY 1 - 3)
# Brother Thang Philosophy Club
# ================================================

init python:
    import random

label day0:
    
    # Show stats UI
    
    $ current_chapter = 1
    
    stop music fadeout 2.0
    scene black with dissolve_scene_full

    scene bg yenlang with fade
    $ renpy.pause(2.0)
    
    scene bg mc_room with wipeleft_scene
    play music club_theme fadein 1.0
    
    # ========================================
    # CẢNH 1: NHÀ - ĐÊM (NGÀY 1)
    # ========================================
    
    "Đêm khuya."
    
    mc "(lo lắng) \"Ok… check điểm nào…\""
    
    "Click."
    
    "Danh sách trúng tuyển dài đằng đẵng hiện ra."
    
    "Nhưng lại… không có tên mình."
    
    mc "(thở dài) \"…Hầy.\""
    
    "Không buồn."
    "Không sốc."
    "Chỉ là cảm giác quen quen… Như mấy lần mở ví ra dù biết trước nó trống trơn."
    
    mc "(Chắc do hội đồng không đủ trình để hiểu nghệ thuật của mình…)"
    
    play sound "sfx/closet-open.ogg"
    
    "Cánh cửa mở."
    
    "Bố tôi, Võ Quang Hưng, một Đại Tá quân đội, bước vào."
    
    show dad sitting at t11
    
    dad "\"Trượt rồi à?\""
    
    play music gym_theme fadein 1.0 # Ominous
    
    mc "\"Vâng… con thấy mình làm bài cũng ổn áp mà nhỉ.\""
    
    show dad 1h

    dad "\"Ừ. Ổn cái đầu mày ý!\""
    
    mc "\"…?\""
    
    play sound anhchoemcohoi
    dad "\"Thôi. Trượt rồi thì vào FPT mà học đi.\""
    dad "\"Ít nhất cũng phải lấy được cái bằng Đại học.\""
    
    mc "\"Nhưng…\""
    
    show dad 1e
    
    dad "\"Nhưng nhị cái gì!\""
    dad "\"Mày có nghe lời tao không thì bảo hả?\""
    
    mc "\"….\""
    mc "\"Dạ vâng ạ...\""
    
    hide dad with dissolve
    jump day1_morning

    
label day1_morning:
    # CHUYỂN CẢNH: NHẬP HỌC (Vẫn là Ngày 1)
    
    $ current_day = 1

    stop music fadeout 2.0
    scene black with dissolve_scene_full

    scene bg fpt_1 with fade
    centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(2.0)
    
    # ========================================
    # CẢNH 2: SÂN TRƯỜNG - SÁNG (NGÀY 1)
    # ========================================
    
    scene bg fpt_yard with wipeleft_scene  # Custom: Sân trường FPT
    play music main_theme fadein 1.0
    
    "Tại sân trường FPT."
    "Hôm nay là ngày nhập học đầu tiên."
    "Sân trường đông nghịt."
    "Ai cũng trông như nhân vật chính của cuộc đời mình."
    "Còn tôi thì như một thằng NPC vừa spawn vậy."
    
    mc "(Đông quá!)"
    mc "(Đông thế này chắc không ai để ý mình đâu nhỉ.)"
    
    # Phone call from Xỉu
    play sound "sfx/pageflip.ogg"  # Phone ring sound
    
    "Bỗng nhiên, điện thoại bất ngờ nhận một cuộc gọi từ số lạ."
    
    mc "\"???\""
    mc "\"Ai đây nhở?\""
    
    # Accept call
    "Click."
    
    unknown "\"Alo Thắng à, em có phải là Thắng không?\""
    
    play music library_theme fadein 1.0 # Natsuki/Xiu playful theme
    
    mc "???" 
    mc "\"Dạ vâng. Cho hỏi ai đấy ạ?\""
    
    unknown "\"Chị là chuyên viên Marketing của câu lạc bộ Triết học Plato.\""
    unknown "\"Nghe bảo cu em là sinh viên mới, không biết có rảnh không nhỉ?\""
    unknown "\"Nếu rảnh thì tham gia CLB của bọn chị đi. Khi tham gia sẽ có cơ hội nhận được rất nhiều ưu đãi hấp dẫn…\""
    
    mc "\"Dạ thôi chị ơi, em hơi bận xíu...\""
    
    unknown "\"Ui, thôi em đừng có chối, thông tin về chiều cao, cân nặng, sở thích, địa chỉ nhà trọ, lịch sinh hoạt của em,… chị có cả rồi ở đây rồi.\""
    unknown "\"Cu em có cần chị đọc cho nghe một số thông tin không?\""
    
    mc "\"Hả? Thôi thôi cho em xin…\""
    
    unknown "\"Nếu vậy thì hãy tham gia ngay cùng bọn chị nào!\""
    unknown "\"Vậy nhá, chị rất mong chờ được gặp lại em tại CLB Triết học Plato, tầng 2, phòng 217, toà Beta, Trường Đại học FPT!\""
    
    mc "(Mình không muốn vào đó đâu, nghe chán lắm!)"
    mc "(Nhưng nếu người ta đã mời như vậy thì từ chối có vẻ cũng hơi ngại…)"
    
    menu:
        "Dạ vâng, em sẽ tham gia ạ":
            unknown "\"Ngon~ Học xong nhớ lên đăng ký em nhé. Bái bai!\""

    jump day1_afternoon
    
label day1_afternoon:
    # Scene label
    scene bg fpt_2 with fade
    centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.0)
    
    # ========================================
    # CẢNH 3: CLB - CHIỀU (NGÀY 1)
    # ========================================
    
    scene bg club_day with wipeleft_scene
    play music deep_thought fadein 1.0
    
    "Mở cửa ra, trước mặt là một người con gái đứng nhìn xuống dưới sân trường."
    "Đó có lẽ là hội trưởng CLB Triết học Plato – Vũ Hải Nữ."
    
    show hainu 1a at t11
    
    hainu "\"Eikasia.\""
    
    mc "\"..?\""
    mc "(Nghe giống như tên một món vũ khí trong game RPG nào đó vậy.)"
    
    show hainu 1b
    
    hainu "\"Là cấp độ thấp nhất của nhận thức.\""
    
    "Hội Trưởng quay lại, nhìn thẳng vào tôi."
    
    show hainu 1c at t11
    
    hainu "\"Cậu kia. Cậu thấy bầu trời màu gì?\""
    
    mc "(bối rối) \"Ờ… màu xanh ạ.\""
    
    show hainu 1d
    
    hainu "\"Thiển cận!\""
    hainu "\"Mặt trời không chỉ phát ra một màu, mà là cả một phổ ánh sáng.\""
    hainu "\"Nếu tôi nói… Bầu trời thực chất chỉ là khoảng đen của vũ trụ.\""
    
    mc "\"…Hả?\""
    
    show hainu 1c
    
    hainu "\"Bầu trời vốn không hề xanh.\""
    hainu "\"Màu xanh cậu thấy… Là ánh sáng bị tán xạ… Chỉ là ảo ảnh mà cậu tạo ra để diễn giải về thế giới.\""
    
    "Một khoảng im lặng…"
    
    $ stats.met_hainu = True
    
    show hainu 1a
    
    hainu "\"Vậy cậu đến đây làm gì?\""
    
    mc "(Gượng cười) \"Dạ em muốn gia nhập CLB ạ!\""
    
    show hainu 1b
    
    hainu "\"…\""
    
    show hainu 1a
    
    hainu "\"Được thôi… Cậu được nhận.\""
    
    # Tăng relationship với Hải Nữ
    $ gained = stats.modify_relationship("hainu", 5)
    $ show_stat_change("rel_hainu", gained)
    
    hide hainu with dissolve

    jump day1_evening
    
label day1_evening:
    # ========================================
    # CẢNH 4: KTX - TỐI (NGÀY 1)
    # ========================================
    scene bg fpt_3 with fade
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.0)
    
    scene bg ktx with wipeleft_scene  # Custom: Ký túc xá FPT
    play music dorm_theme fadein 1.0
    
    "Ngày nhập học đầu tiên kết thúc."
    "Về đến ký túc xá, tôi định ngả lưng nghỉ ngơi chút thì..."
    
    show xiu 1a at t11
    
    xiu "\"Ê cu.\""
    
    mc "\"Dạ?\""
    
    $ stats.met_xiu = True
    
    show xiu 1g
    
    xiu "(cười đểu) \"Tân sinh viên hả?\""
    xiu "\"Muốn chơi một trò chơi đêm muộn khiến bao con người thổn thức chứ?\""
    
    mc "(Đỏ mặt) \"Dạ?\""
    
    show xiu 1g
    
    xiu "\"Đùa xíu thôi! Tối nay đang có trận T1 với GENG, cu em có muốn vào xem cùng chị không nào?\""
    xiu "\"Cơ mà chỉ xem thôi thì chán phèo, hay là chị em mình làm trận cá cược đi nhỉ?\""
    xiu "\"Nhóc thấy thế nào?\""
    
    mc "(Nghe có vẻ nguy hiểm. Cơ mà có tận 50%% cơ hội thắng mà, hay thử xíu nhỉ?)"
    
    menu:
        "Chơi thì chơi, sợ gì?":
            # Relationship tăng
            $ gained = stats.modify_relationship("xiu", 15)
            $ show_stat_change("rel_xiu", gained)

            show xiu 1b
            
            xiu "\"Có chí khí đấy, vậy cu em theo đội nào?\""
            
            menu:
                "ALL IN T1!!!":
                    $ xiu_bet_choice = "T1"
                
                "ALL IN GENG!!!":
                    $ xiu_bet_choice = "GENG"
            
            show xiu 1a
            
            xiu "\"OK! OK! Vậy thì chị theo đội còn lại.\""
            
            "..."
            "Xem trận đấu..."
            "..."
            
            # Thắng!
            show xiu 1c
            
            xiu "\"Ây da! Thua mất rồi! Lần này coi như em gặp may.\""

            show xiu 1b

            xiu "\"Cu em được đấy! Lần sau lại chơi tiếp nhá.\""
            xiu "\"Chị ở phòng bên cạnh, nếu cần gì cứ sang gọi chị nhá!\""
            
            # Nhận tiền
            $ amount = stats.modify_tien(stats.tien)
            $ show_stat_change("tien", amount)
    
    hide xiu with dissolve

    jump day2_morning
    
# ========================================
# NGÀY 2: BỊ MẮNG VÀ TOUR TRƯỜNG
# ========================================
    
label day2_morning:
    $ current_day = 2
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    scene bg fpt_4 with fade
    centered "{size=30}{color=#ffdd00}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(2.0)

    scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    "\"Hôm qua vừa gia nhập CLB, nay đến xem thử xem sao\"."
    
    # CẢNH 5 CŨ: CLB - SÁNG (Bị mắng)
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Vừa bước vào phòng, tình cờ thế nào lại gặp lại chị gái tối qua."
    
    show xiu 1a at t11
    
    xiu "\"Ô! Xem ai đây kìa! Cu em là thành viên mới của cái CLB tẻ nhạt này à?\""
    xiu "\"Trùng hợp ghê, chị cũng là thành viên đó!\""
    
    show xiu 1b
    
    xiu "\"Hữu duyên thế này thì tối này chị em ta lại phải làm kèo cá độ rồi! Vừa hay nay lại có kèo MU với Chealsea\""
    
    mc "\"Dạ vâng…\""
    
    # Hải Nữ xuất hiện
    show xiu 1a at t21
    show hainu 1b at t22
    
    hainu "\"XỈU!!!\""
    
    stop music fadeout 0.5
    play sound "sfx/slap.ogg" # Just for shock effect, or maybe just music stop.
    play music love_theme fadein 0.5 # Poem Panic
    
    "Hội trưởng bước vào."
    
    show hainu 1d at t22
    
    hainu "\"BÀ LẠI ĐI GỌI ĐIỆN CHÈO KÉO THÀNH VIÊN VÀO CLB ĐỂ TIỆN TAY LỪA ĐẢO NỮA HẢ?\""
    hainu "\"HÔM QUA CÓ MỘT NGƯỜI MỚI GIA NHẬP, CÓ PHẢI LÀ DO BÀ DỤ DỖ KHÔNG HẢ?\""
    hainu "\"ĐÂY LÀ CLB TRIẾT CHỨ KHÔNG PHẢI Ổ LỪA ĐẢO CỦA BÀ ĐÂU NHÁ!\""
    
    show xiu 1d at t21
    
    xiu "(lủi mất) \"Đùa tí, làm gì căng.\""

    hide xiu with dissolve
    
    show hainu 1c at t22
    
    hainu "\"Còn cả cậu nữa, ai rủ gì cậu cũng làm à? Chính kiến của cậu đâu hả?\""
    
    mc "\"Dạ…. Dạ…. Tại em nghĩ chỉ chơi cho vui thôi chứ đâu có biết là lừa đảo….\""
    
    show hainu 1d
    
    hainu "\"…. Thật là một niềm tin mù quáng….\""
    hainu "\"Sống trên đời phải biết nghi ngờ, nếu không thì chả khác nào mấy thằng nghe lời người ta cầm 2 tỷ đầu tư vào HDPE để rồi tán gia bại sản.\""
    
    show hainu 1e
    
    hainu "\"Thôi được rồi… nay cậu về đi.\""
    
    hide hainu with dissolve
    hide xiu with dissolve
    
    # CẢNH 6 CŨ: TOUR TRƯỜNG (Chiều Ngày 2)
    
    scene bg hallway with wipeleft_scene  # Custom: Hành lang FPT
    play music canteen_theme
    
    show xiu 1a at t11
    
    xiu "\"Cu em chịu khó ngồi nghe cái bà hội trưởng đấy lảm nhảm thế nhỉ?\""
    xiu "\"Phải chị chị làm vội ba giấc rồi!\""

    mc "\"Vậy ra chị là người mời em vào CLB sao?\""

    show xiu 1g

    xiu "\"Thấy cu em có vẻ thông minh sáng sủa, chị cũng chỉ muốn mời chú em vào cùng chơi thôi mà.\""
    xiu "\"Thế kèo của chị em mình chú tính thế nào? Chơi hay không chơi nói một lời nào.\""

    menu:
        "Chơi thì chơi, sợ gì?":
            show xiu 1b
            
            xiu "\"Có chí khí đấy, vậy cu em theo đội nào?\""
            # Relationship tăng
            $ gained = stats.modify_relationship("xiu", 15)
            $ show_stat_change("rel_xiu", gained)
            
            menu:
                "ALL IN MU!!!":
                    $ xiu_bet_choice = "MU" 
                    play sound siuuu
                
                "ALL IN Chealsea!!!":
                    $ xiu_bet_choice = "Chealsea"
            
            show xiu 1a
            
            xiu "\"OK! OK! Vậy thì chị theo đội còn lại.\""
            
            "..."
            "Xem trận đấu..."
            "..."
            
            # Thắng!
            show xiu 1g
            
            xiu "\"Ngon, thắng rồi! Tiền cu em chị xin nhá!\""
            
            # Nhận tiền
            $ amount = stats.modify_tien(-stats.tien)
            $ show_stat_change("tien", amount)
        
        "Thôi, nay em xin kiếu!":
            xiu "Thế thôi vậy."

    jump day2_afternoon

label day2_afternoon:
    scene bg fpt_6 with fade
    centered "{size=30}{color=#ffaa00}CHIỀU{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.0)

    scene bg fpt_5 with wipeleft_scene
    play music sota_theme fadein 1.0

    show xiu 1b at t11

    xiu "\"Ây cu.\""
    xiu "\"Đừng giận chị nha.\""
    xiu "\"Dù sao thì chị em mình cũng cùng CLB, phòng lại còn cạnh nhau nữa…\""
    xiu "\"Hay là, để tạ lỗi, chị dắt em đi xem trường nha.\""
    
    menu:
        "Không sao, em cũng không giận gì đâu":
            xiu "\"Ngon. Chị em mình cứ thế thôi, hẹ hẹ hẹ.\""
            xiu "\"Được rồi, để chị dẫn đoàn nhà mình đi tham quan trường nào!\""
            
            # Relationship tăng
            $ gained = stats.modify_relationship("xiu", 5)
            $ show_stat_change("rel_xiu", gained)
        
        "Em cũng tham quan vòng rồi, không cần phiền chị đâu ạ":
            show xiu 1g
            
            xiu "\"Thế thôi vậy. Em về nha, chị đi trước đây.\""
            
            hide xiu with dissolve
            
            # Skip tour
            jump day2_evening
    
    # Tour 1: Thư viện
    scene bg library with fade  # Custom: Thư viện FPT
    play music library_theme fadein 1.0 # Reset to happy music
    
    show xiu 1a at t11
    
    xiu "\"Đầu tiên là thư viện, là một nơi vô cùng lý tưởng để ngồi ôn lại bài cũ…, hoặc là ngủ.\""
    
    show xiu 1b
    
    xiu "\"Nghe bảo Hội Trưởng thích mấy anh trai học bá đó, nếu em định tán chị ấy thì tốt nhất thử thông thạo bảy mấy món triết học Mác Leenin hay Tư tưởng Hồ Chí Minh đi.\""
    
    mc "\"Ghê vậy sao? Học xong đống đấy thì chắc tu vi đắc đạo lúc nào chả biết.\""
    
    # Tour 2: Gym
    scene bg gym with fade  # Custom: Phòng gym FPT
    play music gym_theme fadein 1.0 # Reset to happy music
    
    show xiu 1g at t11
    
    xiu "\"Kế đến là phòng Gym, nơi các anh zai sáu múi flex đống cơ của mình.\""
    xiu "\"Gu chị là mấy anh chàng cao to đen hôi thể hình lực lưỡng, thi thoảng ra ngó mấy anh giai chống đẩy mà thèm rỉ nước giãi.\""
    
    mc "\"Tém tém thôi chị ơi, liêm xỉ trôi theo hàng nước của chị rồi kìa.\""
    
    show xiu 1b
    
    # Tour 3: Canteen & Robot T31
    scene bg canteen with fade  # Custom: Canteen FPT
    play music canteen_theme fadein 1.0 
    
    show xiu 1a at t11
    
    xiu "\"Cuối cùng là căng tin, nơi sinh hoạt văn hoá của hội những người không biết xấu hổ.\""
    
    show xiu 1a at t21
    show pig at t22 with dissolve
    
    mc "\"A! Con lợn này.\""
    
    show xiu 1a at t21
    
    xiu "\"Đây là robot bán hàng số hiệu T31 tên đầy đủ là DaoChiCuong do tập đoàn FPT sản xuất.\""
    xiu "\"Phế lắm, chị chửi nó suốt. Mong sau này robot xâm chiếm thế giới nó không nhớ mặt chị.\""
    
    $ t31_voice = random.choice(["\"I'll be back.\"", "\"Hasta la vista, baby.\""])
    
    play sound "sfx/glitch1.ogg"
    
    pig "[t31_voice]"
    
    hide pig with dissolve
    
    show xiu 1a
    
    xiu "\"Thôi muộn rồi, chị té trước đây nha.\""
    
    # ========================================
    # NGÀY 3: QUÊN CHÌA KHÓA & TRẢ NỢ
    # ========================================
    
label day2_evening:
    scene bg fpt_11 with fade
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    $ renpy.pause(1.0)
    
    # CẢNH 7
    
    scene bg class_day with fade
    play music daily_life fadein 1.0
    
    mc "\"Tan học rồi, về thôi.\""
    mc "\"Thôi chết, chìa khoá đâu rồi?\""
    mc "\"Hình như mình để quên trên phòng CLB rồi.\""
    
    scene bg club_messy with wipeleft_scene  # CLB lộn xộn giấy tờ
    play music club_theme fadein 1.0 # Yuri theme
    
    "Phòng CLB vẫn sáng đèn."
    "Hội Trưởng ở trong phòng, trước mặt là một chồng sổ sách cao chạm trần!!?"
    
    show hainu 1a at t11
    
    hainu "\"Cậu là thành viên mới. Muộn rồi còn tới đây làm gì?\""
    
    mc "\"Em để quên chìa khoá ạ.\""
    
    show hainu 1b
    
    hainu "\"Chìa khoá hả? Tôi thấy nó nên đặt ở kia kìa.\""
    
    "Đã tìm thấy chìa khoá, đang định đi về…."
    
    show hainu 1c
    
    hainu "\"Này.\""
    
    mc "\"Dạ?\""
    
    hainu "\"Giúp tôi xử lý đống sổ sách này với được chứ.\""
    hainu "\"Tất nhiên tôi sẽ trả lương.\""
    
    mc "(Sổ sách nhiều vượt mức pickleball rồi, cơ mà vừa hay, tiền mình có hơi vô gia cư…)"
    
    menu:
        hainu "\"Vậy cậu có giúp không?\""
        
        "Dạ vâng ạ…":
            pass
        
        "Nay em lại hơi bận…":
            "Định đi nhưng thấy vẻ mặt tiều tuỵ của Hội Trưởng, thôi đành giúp vậy…"
            
            mc "\"…Thôi được rồi, em sẽ giúp chị.\""
            
    "Tài liệu chất đống như núi, xử lý xong thì cũng đã muộn."

    $ gained = stats.modify_tien(50000)
    $ show_stat_change("tien", gained)

    show hainu 1a
    
    hainu "\"Nay cảm ơn cậu. Không có cậu chắc tôi bị đống giấy tờ này bán hành đến chết mất!\""
    hainu "\"…\""
    hainu "\"Chiều nay… Tôi có hơi nặng lời.\""
    
    show hainu 1c
    
    hainu "\"Nhưng mà… Con người khác với mọi sinh vật ở khả năng suy nghĩ và phản biện.\""
    hainu "\"Suy nghĩ và phản biện là nền móng của triết học.\""
    hainu "\"Nếu cậu thật sự muốn tham gia CLB này, thì mong cậu hãy học cách tư duy…\""
    
    # Relationship tăng mạnh
    $ gained = stats.modify_relationship("hainu", 5)
    $ show_stat_change("rel_hainu", gained)
    
    hide hainu with dissolve
    
    if not script_m:
        jump daily_routine_evening
    else:
        return
