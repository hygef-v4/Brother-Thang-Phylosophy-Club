# ================================================
# CHAPTER 3: DIANOIA (SUY NGẪM) - DAY 10 TO 13
# Brother Thang Philosophy Club
# ================================================

label day7:    
    scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    $ current_chapter = 3

    "Điện thoại rung."
    
    # Text 336
    dad "\Đóng gói hành lý đi. Chiều về trại quân sự để làm thủ tục đi lính.\""
    
    mc "\"..?\""
    mc "\"Đang yên đang lành sao tự nhiên bố lại bảo đi lính?\""
    mc "\"Thôi thì đến hỏi cho ra lẽ vậy.\""
    
    scene bg sota with wipeleft_scene # Trại quân sự
    play music sota_theme fadein 1.0 # Ominous/Strict
    
    show dad at t11
    
    dad "\"Con tới rồi hả?\""
    dad "\"Bố chuẩn bị sẵn thủ tục nghĩa vụ quân sự rồi.\""
    dad "\"Giờ đi theo bố kiểm tra thể lực.\""
    dad "\"Xong về thì nhớ làm cái giấy thôi học.\""
    
    mc "\"Sao tự nhiên lại nghỉ học hả bố?\""
    mc "\"Trên trường việc học của con vẫn ổn mà?\""
    
    dad "\"Thời buổi nào rồi mà còn học Đại học nữa.\""
    dad "\"Mỹ đang lục đục đánh nhau với Cuba rồi.\""
    dad "\"Con phải vào quân đội để lên đường bảo vệ Tổ Quốc.\""
    dad "\"Chứ cứ ru rú ở hậu phương thì làm được gì?\""
    
    mc "\"Ở hậu phương đâu phải là không đóng góp được gì cho Tổ Quốc?\""
    mc "\"Con vẫn có thể góp sức xây dựng Xã hội mà?\""
    mc "\"Đất Nước cũng là một thực thể triết học, nó cần phải vận động để có thể tồn tại, sự vận động đó không chỉ đến từ việc bảo vệ mà còn phải đến từ việc phát triển để tiến bộ.\""
    mc "\"Nó tạo ra cho chúng ta những tri thức, mà tri thức là sức mạnh giúp cho Đất Nước hùng cường hơn.\""
    
    dad "\"Chỉ có những nhà khoa học xuất sắc mới đủ sức tạo ra tri thức, loại hoạ sĩ quèn như mày thì làm ăn được cái gì cho Tổ Quốc?\""
    dad "\"Thôi! Vào quân đội rèn luyện kỷ luật, chứ làm hoạ sĩ ra ngoài lương được mấy đồng?\""
    
    mc "\"Hoạ sĩ nước mình vất vả, nhưng họ dâng hiến tất cả!\""
    mc "\"Con muốn trở thành hoạ sĩ để góp phần làm đẹp cho Đất Nước chứ không phải chỉ vì tiền!\""
    
    show dad at s11 # angry shake
    play music canteen_theme fadein 1.0 # Poem Panic (Argument)
    
    dad "\"MỚI LÊN ĐẠI HỌC CÓ VÀI NGÀY MÀ CÁI MỒM ĐÃ LEM LẺM, PHÉP TẮC GIA ĐÌNH Ở ĐÂU HẢ?\""
    dad "\"MÀY MÀ KHÔNG NGHE LỜI TAO THÌ MỌI CHUYỆN SAU NÀY TỰ THÂN MÀ LO LẤY, TAO KHÔNG CHU CẤP CHO NỮA.\""
    
    menu:
        "Dạ… Vâng ạ…." if stats.doi_song == 0 and stats.hoc_tap == 0:
            jump ending_fascist
        
        "Con có thể tự lo cho bản thân mình rồi!":
            jump daily_routine_evening

label day7_evening:
    # Text 375
    mc "\"Không còn tiền chu cấp, áp lực tài chính của mình tăng lên rồi, từ ngày mai phải tiết kiệm lại thôi.\""
    
    return

label day9:
    scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    # Text 393
    "Điện thoại rung."
    xiu "Đi uống không cu? Nay chị bao!"
    
    mc "\"Của rẻ là của công an… Có khi nào chị ấy bị bắt nên khai ra mình không nhỉ?\""
    
    menu:
        "Nổ cho em cái địa chỉ nào!":
            $ xiu_script = True
            $ gained = stats.modify_relationship("xiu", 6)
            $ show_stat_change("rel_xiu", gained)
        "Tiếc quá, nay em lại có việc bận rồi…":
            return

    scene bg bar with wipeleft_scene # Quán bar/nhậu
    play music dorm_theme fadein 1.0
    
    "Đến quán nhậu Xỉu gửi, thấy đàn chị đang say khướt."
    
    show xiu 1a at t11
    
    xiu "\"Cu em đến rồi à? Nghe bảo dạo này em cãi nhau với bố hả? Thế thì lại đây uống với chị nào!\""
    mc "\"Chị ổn chứ, trông chị say lắm rồi đấy.\""
    xiu "\"Chị mày vẫn uống được, bà chủ, dâng tửu.\""
    mc "\"Nay có chuyện gì buồn sao?\""
    
    "Xỉu im lặng không nói gì."
    
    mc "\"Em thấy nay chị uống hơi nhiều rồi đấy. Nếu có gì buồn phiền, cứ nói em.\""
    mc "\"Chẳng giúp được gì chị đâu, cơ mà đỡ hơn là giữ trong lòng.\""
    
    show xiu 1c
    play music gym_theme fadein 1.0 # Sad backstory
    
    xiu "\"…\""
    xiu "\"Gia đình chị sắp không còn nữa rồi…\""
    
    mc "\"!!?\""
    mc "\"Có chuyện gì xảy ra à? Bố mẹ chị cãi nhau hả?\""
    
    xiu "\"Không phải bố mẹ, chỉ là những người đã nuôi chị lớn mà thôi.\""
    xiu "\"Chị từ nhỏ đã không biết mặt bố mẹ, được các vú em trong cô nhi viện nuôi lớn.\""
    xiu "\"Cuộc sống trong cô nhi viện cũng khá khó khăn, điều kiện ăn uống sinh hoạt thiếu thốn đủ đường, đã thế còn khá là bức bối, đi đâu cũng có người theo quản.\""
    xiu "\"Cơ mà tình cảm của chị với các vú em thì lại khăng khít như ruột thịt vậy.\""
    
    mc "\"Em không biết hồi nhỏ chị lại sống cơ cực như vậy đấy.\""
    
    xiu "\"Thiếu thốn đủ đường như thế nên các vú em phải làm việc cho tụi xã hội đen từ đêm đến sáng.\""
    xiu "\"Chị từ khi còn nhỏ cũng đã phải đi làm rồi.\""
    
    mc "(Làm việc cho xã hội đen sao, nghe nguy hiểm quá vậy.)"
    mc "\"Từ nhỏ luôn sao? Chị bị bắt đi làm gì vậy?\""
    
    xiu "\"Nhiều việc lắm, từ gọi điện quảng cáo đến tư vấn khách hàng.\""
    xiu "\"Thậm chí trước chị còn đóng vai công an để dọa ông chú kia phát khóc.\""
    xiu "\"Làm quần quật cả ngày, cơ mà mỗi lần không mời được khách thì lại bị tụi xã hội đen dùng dùi cui điện quật túi bụi.\""
    
    mc "\"!!?\""
    mc "\"Chị làm việc ở đâu mà nghe nguy hiểm quá vậy?\""
    
    xiu "\"Ở khu tam thái tử bên Campuchia đấy.\""
    xiu "\"Chị từ lúc sinh ra đã ở đấy rồi.\""
    xiu "\"May sao được các vú em bao che cho nên mới trốn sang được Việt Nam.\""
    xiu "\"Nhưng mà khu tự trị đó gần đây đã bị triệt phá, mái nhà xưa nơi chị lớn lên giờ đã chả còn.\""
    xiu "\"Chỉ mong sao các vú em vẫn bình an.\""
    
    mc "\"Vậy sao….\""
    mc "\"Đúng là cuộc sống luôn đầy rẫy bất công. Nhưng mà chị biết không...\""
    mc "\"Chính những trải nghiệm đó đã tạo nên chị của ngày hôm nay. Mạnh mẽ, kiên cường và luôn lạc quan.\""
    mc "\"Em tin rằng dù ở đâu, các vú em vẫn luôn dõi theo và tự hào về chị. Và quan trọng hơn cả...\""
    mc "\"Chị không cô đơn. Chị còn có tụi em, có CLB, và có cả em nữa.\""
    
    xiu "\"….\""
    xiu "\"Cảm ơn em... Thật đấy.\""
    
    "Không khí cả buổi đi chơi bỗng rơi vào trầm tư, nhưng rất thích hợp để tịnh tâm suy nghĩ."
    
    # Text 453 Tình cảm > 80 check
    if stats.get_relationship("xiu") >= 80:
        show xiu 1g
        play music love_theme fadein 1.0
        
        xiu "\"Này, muốn làm một ván cá cược với chị không?\""
        xiu "\"Đoán xem…. Chị có đang phải lòng em không?\""
        
        mc "\"Chị ấy có tình cảm với mình sao?\""
        mc "\"Dạo gần đây mình nhận ra phải nghĩ kỹ trước khi trả lời.\""
        
        menu:
            mc "\"Có lẽ mình nên suy nghĩ một chút.\""

            "Có":
                $ gained = stats.modify_relationship("xiu", 6)
                $ show_stat_change("rel_xiu", gained)
                show xiu 1h
                xiu "\"Lần này…. Em thắng rồi….\""
            "Không":
                show xiu 1a
                xiu "\"Tiếc quá…. Chị thắng rồi…\""
            "Suy nghĩ":
                menu:
                    mc "\"Những lúc say thế này, con người thường rất dễ mềm lòng…\""
                    "Có":
                        $ gained = stats.modify_relationship("xiu", 6)
                        $ show_stat_change("rel_xiu", gained)
                        show xiu 1h
                        xiu "\"Lần này…. Em thắng rồi….\""
                    "Không":
                        show xiu 1c
                        xiu "\"Tiếc quá…. Chị thắng rồi…\""

        mc "…"

    show xiu 1a
    
    xiu "\"Thôi vậy chị về trước đây nha.\""
    
    jump daily_routine_evening

label day11:
    scene bg ktx_day with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    # Text 473
    "Điện thoại rung."
    hainu "Chào buổi sáng. Đang có một bộ phim khá cuốn mà chị muốn xem, cơ mà đi một mình thì lại hơi ngại, em có muốn đi xem cùng chị không?"
    
    mc "\"Lâu rồi mình chưa đi xem phim, nhưng mà giá vé lại đắt quá…. Nên làm gì đây?\""
    
    menu:
        "Chị xem rạp nào vậy em tới đây!":
            $ hainu_script = True
            $ gained = stats.modify_relationship("hainu", 6)
            $ show_stat_change("rel_hainu", gained)
        "Em cũng muốn đi lắm… Cơ mà tài khoản em lại không cho phép…":
            return
    
    scene bg cinema with wipeleft_scene # Rạp phim
    play music club_theme fadein 1.0 # Yuri theme (Intellectual/Romance)

    mc "Em đến rồi đây, chị chờ lâu chưa?"
    show hainu 1e at t11
    hainu "Chị cũng vừa tới thôi."
    mc "Nghe bảo em cãi nhau với bố hả? Có ổn không?"
    mc "Em không sao. Thôi, ta vào xem đi!"
    
    "Vào rạp cùng Hội Trưởng để xem phim “The Truman Show”."
    "Phim khá ấn tượng, làm mình cũng phải nghi ngờ rằng liệu mình có đang ở trong một con game tình cảm nào đó không…."
    
    show hainu 1a
    play music library_theme fadein 1.0
    
    hainu "\"Bộ phim hay thật đấy nhỉ?\""
    mc "\"Ừ! Cảnh kết lúc Truman cúi chào khán giả lần cuối quả thật là Absolutely Cinema.\""
    
    show hainu 1b
    
    hainu "\"…\""
    hainu "\"Cảnh đó… Cậu có nghĩ rằng, quyết định bước ra khỏi trường quay là đúng đắn chứ?\""
    mc "\"Chắc chắn rồi, sao lại không chứ?\""
    
    hainu "\"Theo tôi thì, nếu lơ những điều kỳ lạ xung quanh đi, có lẽ cuộc sống của cậu ấy sẽ hạnh phúc hơn.\""
    hainu "\"Nhưng nó chỉ là một hạnh phúc giả tạo, theo kịch bản chứ không thực sự là điều cậu ta muốn.\""
    
    if stats.get_relationship("hainu") >= 80:
        show hainu 1c
        play music deep_thought fadein 1.0
        
        hainu "\"…\""
        hainu "\"Cậu còn nhớ ngụ ngôn về cái hang chứ?\""
        hainu "\"Tình cảnh của Truman giống như những người cổ đại vậy.\""
        hainu "\"Đều bị mắc kẹt trong những quan niệm, những điều thân thuộc với bản thân.\""
        hainu "\"Tuy nhiên, Truman đã phá bỏ những tưởng chừng như là chân lý để mà đến với thực tiễn.\""
        hainu "\"Theo cậu, tại sao lại có sự khác nhau vậy?\""
        mc "\"Đây là một câu hỏi triết học sao?\""
        
        menu:
            mc "\"Có lẽ mình nên suy nghĩ một chút.\""

            "Là do mong muốn của cậu ta sao?":
                $ gained = stats.modify_relationship("hainu", 6)
                $ show_stat_change("rel_hainu", gained)
            "Ờ… Cậu ta may mắn hơn sao?":
                pass
            "Suy Nghĩ":
                menu:
                    mc "\"Có lẽ là do điều làm nên sự khác biệt giữa hai nhân vật…\""
                    "Là do mong muốn của cậu ta sao?":
                        $ gained = stats.modify_relationship("hainu", 6)
                        $ show_stat_change("rel_hainu", gained)
                    "Ờ… Cậu ta may mắn hơn sao?":
                        pass
                
        hainu "\"Nó là nhờ khát khao tìm ra chân lý, là nhờ sự tư duy và nhận thức của bản thân cậu ta, là nhờ Dianoia.\""
        hainu "\"…\""
        
        show hainu 1e
        
        hainu "\"Ông tôi là một nhà triết gia…. Cả đời ông đi giao giảng về tầm quan trọng của triết học cho mọi người…\""
        hainu "\"Nhưng họ lại nghĩ ông chỉ là một lão già lắm lời, cho rằng ông bị điên…. Họ cho rằng ông chỉ làm những điều vô nghĩa….\""
        
        mc "\"…\""
        mc "\"Em không nghĩ thế đâu!\""
        mc "\"Có thể không phải tất cả, nhưng chắc chắn có nhiều người đã tìm được sự hứng thú với triết học nhờ ông….\""
        mc "\"…Trong đó có cả chị nữa…\""
        mc "\"…Và nhờ chị, em cũng đã yêu thích môn này rồi…\""
        mc "\"Vì vậy, hành động của ông không hề là vô ích.\""
        
        show hainu 1h
        play music love_theme fadein 1.0
        
        hainu "\"…\""
        hainu "\"Cảm ơn em.\""
        hainu "\"…\""
        hainu "\"Em đã từng nghe đến hiện tượng vướng víu lượng tử chưa?\""
        hainu "\"Có những hạt liên kết với nhau dù ở cách xa bao nhiêu, khi tính chất một hạt thay đổi thì cái kia cũng đổi theo.\""
        hainu "\"Tôi từng không tin một vật có thể tác động đến vật khác ở khoảng cách xa vậy.\""
        hainu "\"Cho đến khi, em tác động vào cuộc đời tôi….\""
        
        mc "\"…\""
        mc "(Vừa nãy, có phải ý chị ấy là….)"

    show hainu 1a
    
    hainu "\"Thôi muộn rồi…. Tôi về trước đây.\""
    
    jump daily_routine_evening

label day13_evening:
    # ========================================
    # NGÀY 14: TIỆC SINH NHẬT SỚM & QUYẾT ĐỊNH
    # ========================================
    
    # Check relationships to determine path intro
    $ current_chapter = 4
    if stats.rel_xiu > 80 and stats.rel_hainu > 80:
        jump day13_both
    elif stats.rel_xiu > 80:
        jump day13_xiu
    elif stats.rel_hainu > 80:
        jump day13_hainu
    else:
        jump ending_objective_idealism


