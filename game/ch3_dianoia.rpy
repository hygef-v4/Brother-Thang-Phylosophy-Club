# ================================================
# CHAPTER 3: DIANOIA (SUY NGẪM) - DAY 10 TO 13
# Brother Thang Philosophy Club
# ================================================

label ch3_dianoia:
    
    # Show stats UI
    show screen stats_display
    
    $ current_chapter = 3
    $ current_day = 10
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}Ngày 10{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # NGÀY 10: BIẾN CỐ (BỐ GỌI & TRẠI QUÂN SỰ)
    # ========================================
    
    scene bg ktx_day with dissolve_scene_full
    play music t2 fadein 1.0
    
    "Sáng ngày thứ 10."
    "Điện thoại rung."
    
    # Text 336
    dad "\<Đóng gói hành lý đi. Chiều về trại quân sự để làm thủ tục đi lính.\>"
    
    mc "\"..?\""
    mc "\"Đang yên đang lành sao tự nhiên bố lại bảo đi lính?\""
    mc "\"Thôi thì đến hỏi cho ra lẽ vậy.\""
    
    scene bg sota with wipeleft_scene # Trại quân sự
    stop music fadeout 2.0
    play music t10 fadein 2.0 # Ominous/Strict
    
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
    play music t6 fadein 0.5 # Poem Panic (Argument)
    
    dad "\"MỚI LÊN ĐẠI HỌC CÓ VÀI NGÀY MÀ CÁI MỒM ĐÃ LEM LẺM, PHÉP TẮC GIA ĐÌNH Ở ĐÂU HẢ?\""
    dad "\"MÀY MÀ KHÔNG NGHE LỜI TAO THÌ MỌI CHUYỆN SAU NÀY TỰ THÂN MÀ LO LẤY, TAO KHÔNG CHU CẤP CHO NỮA.\""
    
    menu:
        dad "\"Mày chọn đi!\""
        
        "Dạ… Vâng ạ….":
            mc "\"Dạ… Vâng ạ….\""
            jump ending_fascist
             
        "Con có thể tự lo cho bản thân mình rồi!":
            mc "\"Con có thể tự lo cho bản thân mình rồi, không cần bố bao bọc nữa!\""
            
            dad "\"Mày... Mày được lắm!\""
            dad "\"Cút cho khuất mắt tao!\""
            
            jump ch3_day10_night

label ch3_day10_night:

    scene bg ktx with fade
    play music t9 fadein 1.0 # Sayo-nara (Sad/Tense)
    
    # Text 375
    mc "\"Không còn tiền chu cấp, áp lực tài chính của mình tăng lên rồi, từ ngày mai phải tiết kiệm lại thôi.\""
    
    scene black with dissolve_scene_full
    
    # ========================================
    # NGÀY 11: TRỐN CHẠY (ESCAPISM)
    # ========================================
    
    centered "{size=40}Ngày 11{/size}"
    $ renpy.pause(1.5, hard=True)
    $ current_day = 11

    scene bg ktx_day with dissolve_scene_full
    
    "Điện thoại rung."
    
    # CHECK AFFINITY TO DECIDE EVENT
    if stats.rel_xiu > stats.rel_hainu:
        jump ch3_day11_xiu_drunk
    else:
        jump ch3_day11_hainu_movie

label ch3_day11_xiu_drunk:
    # Text 393
    xiu "\<Đi uống không cu? Nay chị bao!\>"
    
    mc "\"Của rẻ là của công an… Có khi nào chị ấy bị bắt nên khai ra mình không nhỉ?\""
    
    menu:
        "\<Nổ cho em cái địa chỉ nào!\>":
            pass
        "\<Tiếc quá, nay em lại có việc bận rồi…\>":
            # Force go anyway due to script logic simplicity? Or skip?
            # Text implies scene happens. Let's assume he goes.
            mc "\"Mà thôi... Chị ấy mời nhiệt tình thế mà.\""
            pass

    scene bg bar with wipeleft_scene # Quán bar/nhậu
    play music t3 fadein 1.0
    
    "Đến quán nhậu Xỉu gửi, thấy đàn chị đang say khướt."
    
    show xiu neutral at t11
    
    xiu "\"Cu em đến rồi à? Lại đây uống với chị nào!\""
    mc "\"Chị ổn chứ, trông chị say lắm rồi đấy.\""
    xiu "\"Chị mày vẫn uống được, bà chủ, dâng tửu.\""
    mc "\"Nay có chuyện gì buồn sao?\""
    
    "Xỉu im lặng không nói gì."
    
    mc "\"Em thấy nay chị uống hơi nhiều rồi đấy. Nếu có gì buồn phiền, cứ nói em.\""
    mc "\"Chẳng giúp được gì chị đâu, cơ mà đỡ hơn là giữ trong lòng.\""
    
    show xiu sad
    play music t9 fadein 1.0 # Sad backstory
    
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
    
    # Text 453 Tình cảm > 80 check (Assuming high enough here for the scene)
    
    show xiu smirk
    
    xiu "\"Này, muốn làm một ván cá cược với chị không?\""
    xiu "\"Đoán xem…. Chị có đang phải lòng em không?\""
    
    mc "\"Chị ấy có tình cảm với mình sao? Có lẽ mình nên suy nghĩ một chút.\""
    
    menu:
        "Có":
            mc "\"Có.\""
            # If romance logic needed, set flags here
            
        "Không":
            mc "\"Không.\""
            
        "Suy nghĩ":
            mc "\"Những lúc say thế này, con người thường rất dễ mềm lòng…\""

    # Text 464 (Assuming 'Có' or positive outcome for drama)
    
    show xiu sad
    
    xiu "\"Lần này…. Em thắng rồi….\""
    
    "..."
    
    xiu "\"Thôi vậy chị về trước đây.\""
    xiu "\"Nay cảm ơn cu em nhiều nha!\""
    
    jump ch3_reflection

label ch3_day11_hainu_movie:
    # Text 473
    hainu "\<Đang có một bộ phim khá cuốn mà chị muốn xem, cơ mà đi một mình thì lại hơi ngại, em có muốn đi xem cùng chị không?\>"
    
    mc "\"Lâu rồi mình chưa đi xem phim, nhưng mà giá vé lại đắt quá…. Nên làm gì đây?\""
    
    menu:
        "\<Chị xem rạp nào vậy em tới đây\>":
            $ ticket_price = 100000
            if stats.tien >= ticket_price:
                mc "\"Được rồi, mình vẫn đủ tiền. Đi thôi!\""
                $ stats.modify_tien(-ticket_price)
                $ show_stat_change("tien", -ticket_price)
            else:
                mc "\"Chết dở, mình không đủ tiền vé rồi...\""
                mc "\"Thành thật với chị ấy vậy.\""
                mc "Nhưng rồi Hải Nữ nhắn lại: <Tôi bao.>"
        
        "\<Em cũng muốn đi lắm… Cơ mà tài khoản em lại không cho phép…\>":
            mc "Nhưng rồi Hải Nữ nhắn lại: <Tôi bao.>"
    
    scene bg cinema with wipeleft_scene # Rạp phim
    play music t7 fadein 1.0 # Yuri theme (Intellectual/Romance)
    
    "Đến rạp chiếu phim cùng Hội Trưởng để xem phim “The Truman Show”."
    "Phim khá ấn tượng, làm mình cũng phải nghi ngờ rằng liệu mình có đang ở trong một con game tình cảm nào đó không…."
    
    show hainu neutral at t11
    
    hainu "\"Bộ phim hay thật đấy nhỉ?\""
    mc "\"Ừ! Cảnh kết lúc Truman cúi chào khán giả lần cuối quả thật là Absolutely Cinema.\""
    
    show hainu thinking
    
    hainu "\"…\""
    hainu "\"Cảnh đó… Cậu có nghĩ rằng, quyết định bước ra khỏi trường quay là đúng đắn chứ?\""
    mc "\"Chắc chắn rồi, sao lại không chứ?\""
    
    "VŨ HẢI NỮ: \"Theo tôi thì, nếu lơ những điều kỳ lạ xung quanh đi, có lẽ cuộc sống của cậu ấy sẽ hạnh phúc hơn.\""
    "VŨ HẢI NỮ: \"Nhưng nó chỉ là một hạnh phúc giả tạo, theo kịch bản chứ không thực sự là điều cậu ta muốn.\""
    
    show hainu explaining
    
    hainu "\"…\""
    hainu "\"Cậu còn nhớ ngụ ngôn về cái hang chứ?\""
    hainu "\"Tình cảnh của Truman giống như những người cổ đại vậy.\""
    hainu "\"Đều bị mắc kẹt trong những quan niệm, những điều thân thuộc với bản thân.\""
    hainu "\"Tuy nhiên, Truman đã phá bỏ những tưởng chừng như là chân lý để mà đến với thực tiễn.\""
    hainu "\"Theo cậu, tại sao lại có sự khác nhau vậy?\""
    
    menu:
        "Là do mong muốn của cậu ta sao?":
            pass
        "Ờ… Cậu ta may mắn hơn sao?":
            pass
        "Có lẽ là do điều làm nên sự khác biệt giữa hai nhân vật…":
            pass
            
    hainu "\"Nó là nhờ khát khao tìm ra chân lý, là nhờ sự tư duy và nhận thức của bản thân cậu ta, là nhờ Dianoia.\""
    hainu "\"…\""
    
    show hainu smile
    
    hainu "\"Ông tôi là một nhà triết gia…. Cả đời ông đi giao giảng về tầm quan trọng của triết học cho mọi người…\""
    hainu "\"Nhưng họ lại nghĩ ông chỉ là một lão già lắm lời, cho rằng ông bị điên…. Họ cho rằng ông chỉ làm những điều vô nghĩa….\""
    
    mc "\"…\""
    mc "\"Em không nghĩ thế đâu!\""
    mc "\"Có thể không phải tất cả, nhưng chắc chắn có nhiều người đã tìm được sự hứng thú với triết học nhờ ông….\""
    mc "\"…Trong đó có cả chị nữa…\""
    mc "\"…Và nhờ chị, em cũng đã yêu thích môn này rồi…\""
    mc "\"Vì vậy, hành động của ông không hề là vô ích.\""
    
    show hainu smile
    
    hainu "\"…\""
    hainu "\"Cảm ơn em.\""
    hainu "\"Em đã từng nghe đến hiện tượng vướng víu lượng tử chưa?\""
    hainu "\"Có những hạt liên kết với nhau dù ở cách xa bao nhiêu, khi tính chất một hạt thay đổi thì cái kia cũng đổi theo.\""
    hainu "\"Tôi từng không tin một vật có thể tác động đến vật khác ở khoảng cách xa vậy.\""
    hainu "\"Cho đến khi, em tác động vào cuộc đời tôi….\""
    
    mc "\"…\""
    
    hainu "\"Thôi muộn rồi…. Tôi về trước đây.\""
    
    mc "(Vừa nãy, có phải ý chị ấy là….)"
    
    jump ch3_reflection

label ch3_reflection:
    
    # ========================================
    # NGÀY 12 & 13: TỰ VẤN
    # ========================================
    
    hide xiu
    hide hainu
    with dissolve
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}Ngày 12 & 13{/size}"
    $ renpy.pause(2.0, hard=True)
    
    scene bg ktx_day with dissolve_scene_full
    play music t4 fadein 1.0 # Monika theme (Piano/Thinking)
    
    $ current_day = 13
    
    mc "Hai ngày trôi qua, tôi nhốt mình trong phòng."
    mc "\"Lời chị Xỉu nói... Lời Hội Trưởng nói...\""
    mc "\"Và cả mệnh lệnh của Bố.\""
    
    mc "\"Ngày mai là sinh nhật mình...\""
    mc "\"Cũng là hạn chót phải trả lời bố.\""
    mc "\"Mình phải quyết định thôi.\""
    
    # Transition to Chapter 4
    call ch4_noesis
    
    return

# ========================================
# ENDING: PHÁT XÍT (FASCIST ENDING)
# ========================================

label ending_fascist:
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}Nhiều năm sau...{/size}"
    $ renpy.pause(2.0, hard=True)
    
    scene bg sota with fade # Trại quân sự
    play music t10 fadein 1.0
    
    "Mấy chục năm sau, thế giới bước qua cuộc Chiến tranh Thế Giới thứ 3."
    "Cuộc chiến kết thúc với sự thống trị của một tên độc tài."
    "Khi ấy, tên độc tài ấy đang trong một bong ke chuẩn bị cho buổi tử hình tập thể các nhà triết gia."
    
    # show mc_dictator at t11 # Nếu có sprite MC độc tài
    
    mc "\"Khi đứng đây thì tôi muốn nói chuyện với bố tôi!\""
    mc "\"Bố ơi, bố ơi, bố thấy đúng khi cho con nghỉ học chưa.\""
    mc "\"Năm xưa các người chê nghệ thuật của tôi không nhìn xa trông rộng, nay tôi vẽ lại cả bản đồ thế giới, các người thấy đã đủ rộng rồi chứ?\""
    
    "Hắn chỉ tay vào đám tù nhân."
    
    mc "\"Còn những tên triết gia này, chỉ giỏi kích động mõm.\""
    mc "\"Thế giới mới do ta xây dựng không cần tranh luận, không cần biện chứng, không cần triết học.\""
    mc "\"Chỉ cần một chân lý duy nhất, chính là ta.\""
    
    scene black with dissolve_scene_full
    # Philosophical Recap
    call ending_explanation("fascist")
    
    return
