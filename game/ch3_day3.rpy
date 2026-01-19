# ================================================
# CHAPTER 3: DIANOIA (LÝ TRÍ)
# Brother Thang Philosophy Club
# ================================================

label ch3_day3:
    $ current_day = 10
    $ current_chapter = 3
    
    # ========================================
    # CẢNH MỞ ĐẦU - NGÀY 10 (KTX - SÁNG)
    # ========================================
    stop music fadeout 2.0
    scene bg bedroom with dissolve_scene_full
    play music daily_life fadein 1.0

    "Điện thoại rung."
    play sound "sfx/fall.ogg" # Placeholder for phone vibration

    # Bố sends message
    dad "<Đóng gói hành lý đi. Chiều về trại quân sự để làm thủ tục đi lính.>"

    mc "\"..?\""
    mc "\"Đang yên đang lành sao tự nhiên bố lại bảo đi lính?\""
    mc "\"Thôi thì đến hỏi cho ra lẽ vậy.\""

    # ========================================
    # TRẠI - SÁNG
    # ========================================
    scene bg military_camp with wipeleft_scene

    show yuri 3f at t11 # Placeholder for Dad sprite if needed, or just show nothing/Dad defined as character

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

    dad "\"MỚI LÊN ĐẠI HỌC CÓ VÀI NGÀY MÀ CÁI MỒM ĐÃ LEM LẺM, PHÉP TẮC GIA ĐÌNH Ở ĐÂU HẢ?\""
    dad "\"MÀY MÀ KHÔNG NGHE LỜI TAO THÌ MỌI CHUYỆN SAU NÀY TỰ THÂN MÀ LO NẤY, TAO KHÔNG CHU CẤP CHO NỮA.\""

    menu:
        "Dạ… Vâng ạ….":
             # Ending Phat Xit
             mc "\"Dạ… Vâng ạ….\""
             scene black with dissolve_scene_full
             "ENDING: PHÁT XÍT"
             return

        "Con có thể tự lo cho bản thân mình rồi, không cần bố bao bọc nữa!":
             mc "\"Con có thể tự lo cho bản thân mình rồi, không cần bố bao bọc nữa!\""

    hide yuri with dissolve

    # ========================================
    # KTX - TỐI
    # ========================================
    scene bg bedroom with wipeleft_scene
    
    mc "\"Không còn tiền chu cấp, áp lực tài chính của mình tăng lên rồi, từ ngày main phải tiết kiệm lại thôi.\""


    # ========================================
    # CẢNH 1 - NGÀY 14 (KTX - SÁNG)
    # ========================================
    $ current_day = 14
    scene bg bedroom with dissolve

    "Điện thoại rung."
    play sound "sfx/fall.ogg"

    huong "<Nay có lễ hội trường đấy, anh có muốn đi cùng em không?>"

    mc "\"Lễ hội trường sao, nghe có vẻ vui. Cơ mà mình đang hơi kẹt tiền…\""

    menu:
        "OK, chờ anh xíu!":
            mc "<OK, chờ anh xíu!>"
            $ stats.modify_relationship("huong", 5)

        "Nay anh lại đang hơi túng thiếu, để khi khác anh em mình đi chơi sau nha.":
            mc "<Nay anh lại đang hơi túng thiếu, để khi khác anh em mình đi chơi sau nha.>"
            jump ch3_day18 # Skip event

    # ========================================
    # School Festival (Generic BG or School limit)
    # ========================================
    scene bg class_day with wipeleft_scene

    "Vừa bước ra ngoài ký túc xá đã thấy Hương đợi sẵn"
    
    show sayori 1a at t11

    mc "\"Em tới sớm vậy, chờ anh có lâu không?\""

    huong "\"Em cũng mới tới à, thôi ta đi thôi.\""

    scene bg club_day with wipeleft_scene # Reusing club/class as festival temporarily? Or corridor.
    # User mentioned "School Festival" but likely outside. Using class_day for now.
    
    show sayori 1a at t11

    mc "\"Cơ mà lễ hội trường à? Tưởng chỉ có trong anime thôi chứ.\""

    show sayori 1r
    huong "\"Anh lại chẳng thích quá à? Máy tính ảnh có cả một thư mục lưu hình gái anime mà\""

    mc "\"Cái… Sao em biết? Nó… Nó chỉ là tài liệu tham khảo thôi.\""

    "Trường hôm nay mở hội chợ quốc tế, khá là lớn, chắc năm nay lùa được nhiều con vịt vào chuồng."

    show sayori 1m
    huong "\"Wow, lễ hội trường lớn thế nhở, thật xứng danh trường đại học công nghệ hàng đầu Việt Nam.\""

    mc "\"Quả đúng là ngạo nghễ FPT!\""

    huong "\"Sáng giờ chưa có gì bỏ vào mồm cả, đói quá !\""
    huong "\"Vừa hay ở kia có mỳ cay tứ xuyên kìa, hay chúng ta lại đấy ăn đi?\""

    menu:
        "OK luôn!":
            mc "\"OK luôn!\""
            mc "\"Ưm, Mỳ cay Ngon thật đấy!\""
            $ stats.modify_relationship("huong", 5)
        
        "Thôi ta đi xem thứ khác đi…":
            mc "\"Thôi ta đi xem thứ khác đi…\""

    huong "\"Ở đây có chú chó bông này.\""
    huong "\"Nhỏ nhỏ con con chỉ cao bằng bộ PC. Dễ thương quá\""

    menu:
        "Em thích thì để anh mua!":
            mc "\"Em thích thì để anh mua!\""
            mc "\"Mềm mềm ôm thích thật!\""
            $ stats.modify_relationship("huong", 5)

        "Thôi ta đi xem thứ khác đi…":
             mc "\"Thôi ta đi xem thứ khác đi…\""

    huong "\"Chỗ kia trông vui vậy, có anh quay tay dẻo như Khá Bảnh luôn!\""
    huong "\"Lại đấy xem không anh?\""

    menu:
        "Em muốn đi đâu anh đưa đến đấy.":
            mc "\"Em muốn đi đâu anh đưa đến đấy.\""
            huong "\"Hôm nay còn biết tán tỉnh à? Đoán vội vừa đọc bí kíp tán gái nào đó phải không?!\""
            $ stats.modify_relationship("huong", 5)

        "Thôi ta đi xem thứ khác đi…":
            mc "\"Thôi ta đi xem thứ khác đi…\""

    "Chơi vui quá, thấm thoát đã sang buổi chiều…"
    
    # Conditional Check
    if stats.get_relationship("huong") > 80:
        huong "\"Hôm nay… Cảm ơn anh nhá…. Đi chơi với anh vui lắm.\""
        
        mc "\"Không. Câu đó phải anh nói mới đúng.\""
        mc "\"Em biết chuyện anh với bố cãi nhau nên mới rủ anh đi chơi cho khuây khoả hả.\""
        mc "\"Từ trước tới giờ, mỗi lần anh bị bố đánh đều là nhờ có em an ủi.\""
        mc "\"Thật sự anh lúc nào cũng cảm thấy biết ơn em.\""
        
        show sayori 4s
        huong "\"Không phải đâu… Từ nhỏ, em đã chỉ là một con nhóc nhát cáy không dám nói chuyện với ai.\""
        huong "\"Nhờ có anh mà em mới có thể mở lòng được với mọi người xung quanh.\""
        huong "\"Những chuyện vui buồn trong đời em, lúc nào cũng có anh ở bên.\""
        huong "\"Từ lúc nào mà… Em đã thích anh rồi…\""

        mc "\"…\""
        mc "\"Anh rất vui khi nhận được tình cảm của em.\""
        mc "\"Nhưng bây giờ còn nhiều chuyện phải giải quyết, anh chưa thể yêu đương được.\""
        mc "\"Chờ khi mọi chuyện lắng xuống, anh sẽ trả lời em nhá.\""

        huong "\"Dạ vâng… Em sẽ đợi…\""
    
    hide sayori with dissolve

    # ========================================
    # CẢNH 2 - NGÀY 18 (KTX - SÁNG)
    # ========================================
    label ch3_day18:
    $ current_day = 18
    scene bg bedroom with wipeleft_scene

    "Điện thoại rung."
    play sound "sfx/fall.ogg"

    xiu "<Đi uống không cu? Nay chị bao!>"

    mc "\"Của rẻ là của công an… Có khi nào chị ấy bị bắt nên khai ra mình không nhỉ?\""

    menu:
        "Nổ cho em cái địa chỉ nào!":
             mc "<Nổ cho em cái địa chỉ nào!>"
             
        "Tiếc quá, nay em lại có việc bận rồi…":
             mc "<Tiếc quá, nay em lại có việc bận rồi…>"
             jump ch3_day22

    # ========================================
    # PUB - DAY 18
    # ========================================
    scene bg pub with wipeleft_scene

    "Đến quán nhậu Xỉu gửi, thấy đàn chị đang say khướt."

    show monika 1l at t11

    xiu "\"Cu em đến rồi à? Lại đây uống với chị nào!\""

    mc "\"Chị ổn chứ, trông chị say lắm rồi đấy.\""

    xiu "\"Chị mày vẫn uống được, bà chủ, dâng tửu.\""

    mc "\"Nay có chuyện gì buồn sao?\""

    "Xỉu im lặng không nói gì."

    mc "\"Em thấy nay chị uống hơi nhiều rồi đấy. Nếu có gì buồn phiền, cứ nói em.\""
    mc "\"Chẳng giúp được gì chị đâu, cơ mà đỡ hơn là giữ trong lòng.\""

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
    xiu "\"Thậm chí trước chị còn đóng vai công an để doạ ông chú kia phát khóc.\""
    xiu "\"Làm quần quật cả ngày, cơ mà mỗi lần không mời được khách thì lại bị tụi xã hội đen dùng dùi cui điện quật túi bụi.\""

    mc "\"!!?\""
    mc "\"Chị làm việc ở đâu mà nghe nguy hiểm quá vậy?\""

    xiu "\"Ở khu tam thái tử bên Campuchia đấy.\""
    xiu "\"Chị từ lúc sinh ra đã ở đấy rồi.\""
    xiu "\"May sao được các vú em bao che cho nên mới trốn sang được Việt Nam.\""
    xiu "\"Nhưng mà khu tự trị đó gần đây đã bị triết phá, mái nhà xưa nơi chị lớn lên giờ đã chả còn.\""
    xiu "\"Chỉ mong sao các vú em vẫn bình an.\""

    mc "\"Vậy sao….\""
    mc "\"Chị an tâm. Em tin rằng mọi người sẽ ổn thôi.\""

    xiu "\"….\""
    xiu "\"Cảm ơn em.\""

    "Không khí cả buổi đi chơi bỗng rơi vào trầm tư, nhưng rất thích hợp để tịnh tâm suy nghĩ."

    if stats.get_relationship("xiu") > 80:
        xiu "\"Này, muốn làm một ván cá cược với chị không?\""
        xiu "\"Đoán xem…. Chị có đang phải lòng em không?\""

        mc "\"Chị ấy có tình cảm với mình sao? Có lẽ mình nên suy nghĩ một chút.\""
        
        menu:
            "Có":
                mc "\"Có\""
                xiu "\"Lần này…. Em thắng rồi….\""
            
            "Không":
                mc "\"Không\""
                xiu "\"… Tiếc quá….\""
            
            "Những lúc say thế này, con người thường rất dễ mềm lòng…":
                mc "\"Những lúc say thế này, con người thường rất dễ mềm lòng…\""
                # Logic not specified for this option result, assuming generic response or fallthrough
                xiu "\"…\""
    
    xiu "\"Thôi vậy chị về trước đây.\""
    xiu "\"Nay cảm ơn cu em nhiều nha!\""

    hide monika with dissolve

    # ========================================
    # CẢNH 3 - NGÀY 22 (KTX - SÁNG)
    # ========================================
    label ch3_day22:
    $ current_day = 22
    scene bg bedroom with wipeleft_scene

    "Điện thoại rung."
    play sound "sfx/fall.ogg"

    hainu "<Hôm nay tôi đang có hứng, cho phép em rủ tôi đi chơi.>"

    mc "\"Cô tiểu thư này lại bày trò gì nữa vậy? Không nghe lời thì có ảnh hưởng đến tiền lương của mình không ta?\""

    menu:
        "Nhân ngày đẹp trời, quý cô đây có muốn đi chơi với tôi không?":
             mc "<Nhân ngày đẹp trời, quý cô đây có muốn đi chơi với tôi không?>"
        
        "Xin lỗi chị, nay em lại không có hứng lắm…":
             mc "<Xin lỗi chị, nay em lại không có hứng lắm…>"
             jump ch3_day26

    # ========================================
    # MALL - DAY 22
    # ========================================
    scene bg residential with wipeleft_scene # Outside KTX

    "Vừa xuống dưới sân đã thấy một chiếc limousine 32 chỗ đang đợi trước cổng. Từ trong đó, Hải Nữ bước xuống."

    show natsuki 1a at t11

    hainu "\"Đứng ngây ra đó làm gì, còn không mau lên xe.\""

    mc "\"Đây là xe của chị sao? Lần đầu em thấy con xe dài thế này đấy.\""

    hainu "\"Có gì đâu, nhà chị dùng con này để dạo quanh vườn suốt.\""
    
    "Mải mê ngắm nhìn nôi thất, xe đã tới một trung tâm thương mại sầm uất lúc nào không hay."

    scene bg mall with wipeleft_scene

    mc "\"Chỗ này… Toàn là hàng hiệu… Ví tiền của em đang bị bạo lực...\""

    show natsuki 4y
    hainu "(liếc nhìn) \"Vậy sao.\""
    hainu "\"Cầm lấy chút tiền lẻ mà tiêu sài.\""

    "Hải Nữ ném thẳng cục tiền 1 tỷ vào tôi."

    mc "\"Tuân lệnh. Hôm nay chị nói gì em cũng nghe lời hết.\""

    show natsuki 4z
    hainu "\"Được, vậy hôm nay cậu là của tôi.\""
    hainu "\"Dùng số tiền kia để phục vụ cho tôi.\""
    hainu "\"Còn bao nhiêu, cứ giữ lấy.\""

    hainu "\"Được rồi, vậy thì trước tiên ta đi mua đồ.\""
    hainu "\"Cậu thấy bộ đồ này thế nào?\""

    menu:
        "Rất là đẹp ạ!":
             mc "\"Rất là đẹp ạ!\""
             
             hainu "\"Vậy sao.... Thế tôi lấy cái này….\""
        
        "Trông hơi không được thoải mái…":
             mc "\"Trông hơi không được thoải mái…\""
             hainu "(Không say mê trước vẻ đẹp của mình sao, chàng trai này thật thú vị!)"

        "[[Suy luận] Váy ôm sát quá, có lẽ sẽ làm chị ấy đau…":
             mc "\"Váy ôm sát quá, có lẽ sẽ làm chị ấy đau…\""
             hainu "(Không say mê trước vẻ đẹp của mình sao, chàng trai này thật thú vị!)"
             $ stats.modify_relationship("hainu", 5)

    hainu "\"Tiếp theo, đến quầy này đi.\""

    menu:
        "Được thôi, chị muốn mua gì nào?":
             mc "\"Được thôi, chị muốn mua gì nào?\""
             hainu "(Tiểu tử này cũng dẻo mồm đấy chứ!)"

        "Trông chán lắm, đi quầy khác đi.":
             mc "\"Trông chán lắm, đi quầy khác đi.\""
             hainu "\"Tôi không có hỏi ý kiến của cậu.\""
             $ stats.modify_relationship("hainu", -5)

        "[[Suy luận] Đây hình như là một tiệm mỹ phẩm nổi tiếng…":
             mc "\"Đây hình như là một tiệm mỹ phẩm nổi tiếng…\""
             hainu "(Tiểu tử này cũng dẻo mồm đấy chứ!)"
             $ stats.modify_relationship("hainu", 5)


    hainu "\"Tôi đói rồi. Chúng ta tìm chỗ nào ăn đi.\""
    hainu "\"Quán này có danh tiếng khá tốt, có lẽ đồ ăn sẽ rất ngon.\""

    menu:
        "Ưm… Quả thực là rất ngon.":
             mc "\"Ưm… Quả thực là rất ngon.\""
             hainu "(Tốt! Có vẻ cậu ta cũng thích món này.)"

        "Cũng ngon, cơ mà hơi ít.":
             mc "\"Cũng ngon, cơ mà hơi ít.\""
             hainu "\"Câu dám chê quán tôi chọn sao?\""

        "[[Suy luận] Có vẻ chị ấy rất thích món này…":
             mc "\"Có vẻ chị ấy rất thích món này…\""
             hainu "(Tốt! Có vẻ cậu ta cũng thích món này.)"
             $ stats.modify_relationship("hainu", 5)

    hainu "\"Tôi chán rồi. Cậu biết chỗ nào vui không đưa tôi đi.\""

    menu:
        "Hay chúng ta cùng vào đọc sách đi.":
             mc "\"Hay chúng ta cùng vào đọc sách đi.\""
             hainu "(Đọc sách sao, cũng thanh lịch đó chứ!)"

        "Chị có muốn đi dạo cùng em chứ.":
             mc "\"Chị có muốn đi dạo cùng em chứ.\""
             hainu "\"Cả toà nhà to thế này cậu bắt tôi đi bộ suốt sao?\""

        "[[Suy luận] Nên tìm chỗ nào đó mà cả hai có thể vui…":
             mc "\"Nên tìm chỗ nào đó mà cả hai có thể vui…\""
             hainu "(Đọc sách sao, cũng thanh lịch đó chứ!)"
             $ stats.modify_relationship("hainu", 5)

    "Đi khắp cái trung tâm thương mại này hết cả buổi sáng, có lẽ mình nên về rồi."

    if stats.get_relationship("hainu") > 80:
        scene bg residential with wipeleft_scene
        "Trên đường về nhà."
        
        show natsuki 1a at t11

        hainu "\"Hôm nay cảm ơn cậu đã đi cùng tôi.\""
        
        mc "\"Dạ vâng. Có gì đâu ạ.\""
        
        show natsuki 12b
        hainu "\"…\""
        hainu "\"Tôi… Là một người con gái phiền phức đúng không?\""
        hainu "\"Từ trước tới giờ sống trong nhung lụa, được bao người xu nịnh, tôi đã quên mất cách nhìn nhận người khác.\""
        hainu "\"Vào câu lạc bộ này để có thể mở rộng thế giới quan của bản thân, nhưng tôi vẫn chứng nào tật nấy….\""

        mc "\"Không phải vậy đâu.\""
        mc "\"Đúng là có những lúc chị khá phiền, nhưng chị luôn hào phóng với mọi người xung quanh.\""
        mc "\"Nếu không nhờ có chị thì có lẽ sẽ không thể tiếp tục con đường học hành rồi….\""

        show natsuki 12e
        hainu "\"…\""
        hainu "\"Vậy sao…\""

        show natsuki 12f
        hainu "(bật cười) \"Cậu đã thành công thu hút được sự chú ý của tôi rồi đấy.\""
        hainu "\"Sao nào? Trở thành bạn trai của tôi đủ để thoả mãn cậu chứ?\""

        mc "\"Chuyện đó… Bây giờ em đang còn vướng bận nhiều điều, nên vẫn chưa sẵn sàng để bắt đầu mối quan hệ.\""
        mc "\"Đợi sau khi em giải quyết xong mọi chuyện sẽ trả lời chị.\""

        hainu "\"…. Được!\""
        hainu "\"Cậu không thoát được khỏi tay tôi đâu, nhất định cậu sẽ thành của tôi.\""

    hide natsuki with dissolve

    # ========================================
    # CẢNH 4 - NGÀY 26 (KTX - SÁNG)
    # ========================================
    label ch3_day26:
    $ current_day = 26
    scene bg bedroom with wipeleft_scene

    "Điện thoại rung."
    play sound "sfx/fall.ogg"

    ischyros "<Đang có một bộ phim khá hay mà chị muốn xem, cơ mà đi một mình thì lại hơi ngại, em có muốn đi xem cùng chị không?>"

    mc "\"Lâu rồi mình chưa đi xem phim, nhưng mà giá vé lại đắt quá…. Nên làm gì đây?\""

    menu:
        "Chị xem rạp nào vậy em tới đây":
             mc "<Chị xem rạp nào vậy em tới đây>"
             # Go to cinema
             scene bg cinema with wipeleft_scene
             "Đến rạp chiếu phim cùng Hội Trưởng để xem phim “The Truman Show”."
             "Phim khá ấn tượng, làm mình cũng phải nghi ngờ rằng liệu mình có đang ở trong một con game tình cảm nào đó không…."

        "Em cũng muốn đi lắm… Cơ mà tài khoản em lại không cho phép….":
             mc "<Em cũng muốn đi lắm… Cơ mà tài khoản em lại không cho phép….>"

    "Kết thúc Chương 3: DIANOIA."
    return
