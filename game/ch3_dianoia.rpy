# ================================================
# CHAPTER 3: DIANOIA (LÝ TRÍ)
# Brother Thang Philosophy Club
# ================================================

label ch3_dianoia:
    
    # Show stats UI just in case
    show screen stats_display
    
    $ current_chapter = 3
    $ current_day = 10
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}{color=#ff0000}CHƯƠNG 3{/color}{/size}\n{size=30}DIANOIA (LÝ TRÍ){/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # CẢNH MỞ ĐẦU - NGÀY 10 (KTX – SÁNG)
    # ========================================
    
    scene bg bedroom with wipeleft_scene
    play music tense fadein 1.0
    
    "Điện thoại rung."
    
    play sound "sfx/pageflip.ogg"
    
    "Bố: <Đóng gói hành lý đi. Chiều về trại quân sự để làm thủ tục đi lính.>"
    
    mc "\"..?\""
    mc "\"Đang yên đang lành sao tự nhiên bố lại bảo đi lính?\""
    mc "\"Thôi thì đến hỏi cho ra lẽ vậy.\""
    
    # ========================================
    # TRẠI QUÂN SỰ - SÁNG
    # ========================================
    
    scene bg club_day with fade # Placeholder for Military Camp if not avail, using generic or club for now
    # Note: Using club_day as placeholder, ideally need a military bg
    
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
    
    # Scene shake effect
    with hpunch
    
    dad "\"MỚI LÊN ĐẠI HỌC CÓ VÀI NGÀY MÀ CÁI MỒM ĐÃ LEM LẺM, PHÉP TẮC GIA ĐÌNH Ở ĐÂU HẢ?\""
    dad "\"MÀY MÀ KHÔNG NGHE LỜI TAO THÌ MỌI CHUYỆN SAU NÀY TỰ THÂN MÀ LO LẤY, TAO KHÔNG CHU CẤP CHO NỮA.\""
    
    menu:
        dad "\"QUYẾT ĐỊNH MAU!\""
        
        "Dạ… Vâng ạ….":
             # ENDING PHÁT XÍT
             mc "\"Dạ… Vâng ạ….\""
             jump ending_fascist
        
        "Con có thể tự lo cho bản thân mình rồi, không cần bố bao bọc nữa!":
             mc "\"Con có thể tự lo cho bản thân mình rồi, không cần bố bao bọc nữa!\""
             
             dad "\"GIỎI! ĐƯỢC LẮM!\""
             dad "\"ĐỂ TAO XEM MÀY SỐNG ĐƯỢC BAO LÂU!\""
             
             $ stats.dad_cutoff = True
             $ show_stat_change("tien", 0) # Trigger update check, maybe not needed here specifically
             
             hide dad with dissolve
             
             scene bg bedroom with fade
             
             mc "\"Không còn tiền chu cấp, áp lực tài chính của mình tăng lên rồi, từ ngày mai phải tiết kiệm lại thôi.\""
             
             jump ch3_time_skip

label ending_fascist:
    
    # Text already spoken in choice block
    
    scene black with dissolve_scene_full
    
    centered "{size=30}{color=#ff0000}ENDING: PHÁT XÍT{/color}{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    scene bg club_day with fade # Placeholder for bunker
    
    "Mấy chục năm sau, thế giới bước qua cuộc Chiến tranh Thế Giới thứ 3."
    "Cuộc chiến kết thúc với sự thống trị của một tên độc tài."
    "Khi ấy, tên độc tài ấy đang trong một bong ke chuẩn bị cho buổi tử hình tập thể các nhà triết gia."
    
    show dad at t11
    
    mc "\"Khi đứng đây thì tôi muốn nói chuyện với bố tôi!\""
    mc "\"Bố ơi, bố ơi, bố thấy đúng khi cho con nghỉ học chưa.\""
    mc "\"Năm xưa các người chê nghệ thuật của tôi không nhìn xa trông rộng, nay tôi vẽ lại cả bản đồ thế giới, các người thấy đã đủ rộng rồi chứ?\""
    mc "\"Còn những tên triết gia này, chỉ giỏi kích động mõm.\""
    mc "\"Thế giới mới do ta xây dựng không cần tranh luận, không cần biện chứng, không cần triết học.\""
    mc "\"Chỉ cần một chân lý duy nhất, chính là ta.\""
    
    "GAME OVER."
    
    return

# ========================================
# TIME SKIP TO DAY 14
# ========================================

label ch3_time_skip:
    
    scene black with dissolve
    
    "Nhiều ngày trôi qua..."
    "Tôi cố gắng cân bằng giữa việc học, làm thêm và sinh hoạt CLB."
    "Tiền nong trở nên eo hẹp hơn khi không còn trợ cấp từ bố."
    
    $ current_day = 14
    
    centered "{size=30}{color=#ffdd00}NGÀY 14{/color}{/size}\n{size=20}Đi nhậu với Xỉu{/size}"
    
    jump ch3_day14

# ========================================
# CẢNH 1 – NGÀY 14 (KTX – SÁNG)
# ========================================

label ch3_day14:
    
    scene bg bedroom with wipeleft_scene
    play music daily_life fadein 1.0
    
    "Điện thoại rung."
    
    "VÕ MINH XỈU: <Đi uống không cu? Nay chị bao!>"
    
    mc "\"Của rẻ là của công an… Có khi nào chị ấy bị bắt nên khai ra mình không nhỉ?\""
    
    menu:
        # xiu variable might be object or string, better use "VÕ MINH XỈU" or narrator if xiu object not shown yet
        xiu "\"Đi không?\""
        
        "Nổ cho em cái địa chỉ nào!":
             mc "<Nổ cho em cái địa chỉ nào!>"
             jump ch3_day14_drinking
        
        "Tiếc quá, nay em lại có việc bận rồi…":
             mc "<Tiếc quá, nay em lại có việc bận rồi…>"
             "Tôi từ chối khéo. Bỏ lỡ một dịp hiểu thêm về Xỉu."
             jump ch3_day18_pre


label ch3_day14_drinking:
    
    scene bg club_day with fade # Placeholder for bar/pub
    play music sad fadein 1.0
    
    "Đến quán nhậu Xỉu gửi, thấy đàn chị đang say khướt."
    
    show monika "1d" at t11
    
    xiu "\"Cu em đến rồi à? Lại đây uống với chị nào!\""
    
    mc "\"Chị ổn chứ, trông chị say lắm rồi đấy.\""
    
    xiu "\"Chị mày vẫn uống được, bà chủ, dâng tửu.\""
    
    mc "\"Nay có chuyện gì buồn sao?\""
    
    "Xỉu im lặng không nói gì."
    
    mc "\"Em thấy nay chị uống hơi nhiều rồi đấy. Nếu có gì buồn phiền, cứ nói em.\""
    mc "\"Chẳng giúp được gì chị đâu, cơ mà đỡ hơn là giữ trong lòng.\""
    
    show monika "1f"
    
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
    mc "\"Chị an tâm. Em tin rằng mọi người sẽ ổn thôi.\""
    
    show monika "1a"
    
    xiu "\"….\""
    xiu "\"Cảm ơn em.\""
    
    "Không khí cả buổi đi chơi bỗng rơi vào trầm tư, nhưng rất thích hợp để tịnh tâm suy nghĩ."
    
    if stats.rel_xiu > 80:
        
        show monika "1k"
        
        xiu "\"Này, muốn làm một ván cá cược với chị không?\""
        xiu "\"Đoán xem…. Chị có đang phải lòng em không?\""
        
        mc "(Chị ấy có tình cảm với mình sao? Có lẽ mình nên suy nghĩ một chút.)"
        
        menu:
            "Trả lời Xỉu:"
            
            "Có":
                 mc "\"Có.\""
                 
                 show monika "1l"
                 
                 xiu "\"Lần này…. Em thắng rồi….\""
                 
                 $ stats.modify_relationship("xiu", 10)
                 
            "Không":
                 mc "\"Không.\""
                 
                 show monika "1f"
                 
                 xiu "\"… Tiếc quá….\""
            
            "Suy nghĩ":
                 mc "\"Những lúc say thế này, con người thường rất dễ mềm lòng…\""
                 mc "\"Em nghĩ là do rượu nói thôi.\""
                 
                 xiu "\"Hmm... Chắc vậy.\""

    show monika "1a"
    
    xiu "\"Thôi vậy chị về trước đây.\""
    xiu "\"Nay cảm ơn cu em nhiều nha!\""
    
    hide monika with dissolve
    
    jump ch3_day18_pre

# ========================================
# CẢNH 4 – NGÀY 18 (KTX – SÁNG)
# ========================================

label ch3_day18_pre:
    
    scene black with dissolve
    
    $ current_day = 18
    
    centered "{size=30}{color=#ffdd00}NGÀY 18{/color}{/size}\n{size=20}Xem phim cùng Hội Trưởng{/size}"
    
    jump ch3_day18_new

label ch3_day18_new:
    
    scene bg bedroom with wipeleft_scene
    play music daily_life fadein 1.0
    
    "Điện thoại rung."
    
    "VŨ HẢI NỮ: <Đang có một bộ phim khá cuốn mà chị muốn xem, cơ mà đi một mình thì lại hơi ngại, em có muốn đi xem cùng chị không?>"
    
    mc "\"Lâu rồi mình chưa đi xem phim, nhưng mà giá vé lại đắt quá…. Nên làm gì đây?\""
    
    menu:
        hainu "<Đi xem phim không?>"
        
        "Đi luôn!":
             mc "Chị xem rạp nào vậy em tới đây!"
             jump ch3_day18_movie
        
        "Từ chối":
             mc "Em cũng muốn đi lắm… Cơ mà tài khoản em lại không cho phép…."
             "Tôi đành ở nhà."
             jump ch3_end

label ch3_day18_movie:
    
    scene bg club_day with fade # Placeholder for Cinema
    play music heart fadein 1.0
    
    "Đến rạp chiếu phim cùng Hội Trưởng để xem phim \"The Truman Show\"."
    "Phim khá ấn tượng, làm mình cũng phải nghi ngờ rằng liệu mình có đang ở trong một con game tình cảm nào đó không…."
    
    show yuri "1a" at t11
    
    "VŨ HẢI NỮ: \"Bộ phim hay thật đấy nhỉ?\""
    
    mc "\"Ừ! Cảnh kết lúc Truman cúi chào khán giả lần cuối quả thật là Absolutely Cinema.\""
    
    show yuri "2f"
    
    "VŨ HẢI NỮ: \"…\""
    "VŨ HẢI NỮ: \"Cảnh đó… Cậu có nghĩ rằng, quyết định bước ra khỏi trường quay là đúng đắn chứ?\""
    
    mc "\"Chắc chắn rồi, sao lại không chứ?\""
    
    "VŨ HẢI NỮ: \"Theo tôi thì, nếu lơ những điều kỳ lạ xung quanh đi, có lẽ cuộc sống của cậu ấy sẽ hạnh phúc hơn.\""
    "VŨ HẢI NỮ: \"Nhưng nó chỉ là một hạnh phúc giả tạo, theo kịch bản chứ không thực sự là điều cậu ta muốn.\""
    
    if stats.rel_hainu > 80:
        
        show yuri "3a"
        
        "VŨ HẢI NỮ: \"…\""
        "VŨ HẢI NỮ: \"Cậu còn nhớ ngụ ngôn về cái hang chứ?\""
        "VŨ HẢI NỮ: \"Tình cảnh của Truman giống như những người cổ đại vậy.\""
        "VŨ HẢI NỮ: \"Đều bị mắc kẹt trong những quan niệm, những điều thân thuộc với bản thân.\""
        "VŨ HẢI NỮ: \"Tuy nhiên, Truman đã phá bỏ những tưởng chừng như là chân lý để mà đến với thực tiễn.\""
        "VŨ HẢI NỮ: \"Theo cậu, tại sao lại có sự khác nhau vậy?\""
        
        menu:
            "Tại sao khác nhau?"
            
            "Là do mong muốn của cậu ta sao?":
                 mc "\"Là do mong muốn của cậu ta sao?\""
            
            "Ờ… Cậu ta may mắn hơn sao?":
                 mc "\"Ờ… Cậu ta may mắn hơn sao?\""
            
            "Có lẽ là do điều làm nên sự khác biệt giữa hai nhân vật…":
                 mc "\"Có lẽ là do điều làm nên sự khác biệt giữa hai nhân vật…\""
                 mc "\"Nó là nhờ khát khao tìm ra chân lý, là nhờ sự tư duy và nhận thức của bản thân cậu ta, là nhờ Dianoia.\""
                 
                 $ stats.modify_relationship("hainu", 10)
        
        show yuri "2f"
        
        "VŨ HẢI NỮ: \"…\""
        "VŨ HẢI NỮ: \"Ông tôi là một nhà triết gia…. Cả đời ông đi giao giảng về tầm quan trọng của triết học cho mọi người…\""
        "VŨ HẢI NỮ: \"Nhưng họ lại nghĩ ông chỉ là một lão già lắm lời, cho rằng ông bị điên…. Họ cho rằng ông chỉ làm những điều vô nghĩa….\""
        
        mc "\"…\""
        mc "\"Em không nghĩ thế đâu!\""
        mc "\"Có thể không phải tất cả, nhưng chắc chắn có nhiều người đã tìm được sự hứng thú với triết học nhờ ông….\""
        mc "\"…Trong đó có cả chị nữa…\""
        mc "\"…Và nhờ chị, em cũng đã yêu thích môn này rồi…\""
        mc "\"Vì vậy, hành động của ông không hề là vô ích.\""
        
        show yuri "3y"
        
        "VŨ HẢI NỮ: \"…\""
        "VŨ HẢI NỮ: \"Cảm ơn em.\""
        "VŨ HẢI NỮ: \"Em đã từng nghe đến hiện tượng vướng víu lượng tử chưa?\""
        "VŨ HẢI NỮ: \"Có những hạt liên kết với nhau dù ở cách xa bao nhiêu, khi tính chất một hạt thay đổi thì cái kia cũng đổi theo.\""
        "VŨ HẢI NỮ: \"Tôi từng không tin một vật có thể tác động đến vật khác ở khoảng cách xa vậy.\""
        "VŨ HẢI NỮ: \"Cho đến khi, em tác động vào cuộc đời tôi….\""
        
        mc "\"…\""
        
        "VŨ HẢI NỮ: \"Thôi muộn rồi…. Tôi về trước đây.\""
        
        mc "(Vừa nãy, có phải ý chị ấy là….)"
    
    hide yuri with dissolve
    
    mc "(Chà… Buổi xem phim này làm mình phải suy nghĩ nhiều quá…)"
    mc "(Liệu ngồi im theo sự sắp đặt của người khác hay tự lực bằng mong muốn của mình…. Quả là một lựa chọn khó khăn….)"
    
    jump ch3_end

label ch3_end:
    
    scene black with dissolve_scene_full
    
    $ renpy.pause(2.0, hard=True)
    
    call ch4_noesis
    
    return
