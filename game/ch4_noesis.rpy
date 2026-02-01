# ================================================
# CHAPTER 4: NOESIS (TRI THỨC) - DAY 14 & 15
# Brother Thang Philosophy Club
# ================================================

label day13_both:
    scene bg ktx with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    "Điện thoại rung."
    xiu "\"Ây cu. Tới CLB tí đi. Có việc.\""

    mc "(Giờ này còn gọi gì nữa nhở? Lại ra căng tin hát hò tuyển thành viên à?)"
    mc "(Thôi thì cứ tới xem sao vậy.)"

    scene bg club_party with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Giữa phòng trưng một băng rôn Happy Birthday."
    
    show hainu 1a at t21
    show xiu 1a at t22
    
    hainu "\"snvv nghen.\""
    xiu "\"Em bé tuổi mới hay ăn chóng lớn nhá.\""
    
    mc "\"…\""
    mc "\"Dạ em cảm ơn ạ.\""
    
    xiu "\"Thôi vào phòng đi, để chị bật Happy Birthday to You cho bé này thổi nến nhá.\""
    show xiu 1b
    
    "Đã lâu rồi mới vui như thế này, bạn ăn chơi suýt quên thời gian. Chỉ có điều…"
    
    mc "\"Cơ mà ngày mai mới là sinh nhật em cơ mà, sao nay tổ chức sớm vậy?\""
    play music love_theme fadein 1.0
    "Cả phòng bỗng im bặt."
    
    show hainu 1b
    
    hainu "\"Ngày mai, chị nghĩ em nên về nhà làm hoà với bố.\""
    hainu "\"Dù sao cũng là gia đình, bố em thực sự chỉ lo cho em mà thôi….\""
    
    show xiu 1d
    
    xiu "\"Lo cho hộ lý khi về già thì có đấy!\""
    hainu "\"Xỉu!\""
    xiu "\"Nói gì sai hả. Mấy người có gia đình hạnh phúc làm sao hiểu được nỗi khổ khi phải làm tất cả để hài lòng gia đình chứ?\""
    xiu "\"Chị nghĩ em nên kệ họ đi, cứ làm theo mong muốn của bản thân là được.\""
    
    show hainu 1a
    
    hainu "\"Vậy… Mong muốn của em là gì?\""
    
    menu:
        "Vậy thì… Để em về nói chuyện với bố…":
            jump ending_metaphysical_materialism
            
        "Không cần đâu, em tin thời gian sẽ chữa lành tất cả.":
            jump ending_subjective_idealism
            
        "Suy Nghĩ":
            menu:
                mc "\"Những thứ mà mình học được những ngày qua, có lẽ sẽ giúp bố hiểu mình…\""
                "Em tin rằng, triết học giúp con người ta gắn kết lại với nhau!":
                    jump ending_dialectical_materialism

label day13_xiu:
    scene bg ktx with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    show xiu 1a at t11
    
    xiu "\"Ây cu, về rồi à?\""
    xiu "\"Mai sinh nhật đúng không? »\""
    xiu "\"Chương trình thế nào đây nhỉ?\""
    
    mc "\"…\""
    mc "\"Có lẽ em sẽ về nhà.\""
    mc "\"Từ hồi cãi nhau với bố em vẫn chưa về rồi…\""
    
    xiu "\"Có ông bô như thế mà cậu vẫn chịu được thì đúng là thiếu mỗi cái áo cà sa là thành phật đấy.\""
    xiu "\"Làm người phải biết tự lo cho bản thân, trước tiên cứ chill đi cái đã, những cái khác ắt sẽ tự dưng tốt lên thôi.\""
    xiu "\"Như Nguyễn Du nói ấy: 'Người buồn cảnh có vui đâu bao giờ?'\""
    
    mc "\"Nhưng mà… Như thế có sợ ăn gậy vì vi phạm tiêu chuẩn cộng đồng không?\""
    mc "\"Dù sao thì em thấy, vẫn nên về xin lỗi bố một câu chứ, sợ sau này bố con nhìn mặt nhau cũng khó…\""
    
    xiu "\"Ui giời ơi, em tôi cứ lo xa!\""
    xiu "\"Mấy cái quy tắc đó sau cùng cũng chỉ là do con người tự đặt ra mà thôi.\""
    xiu "\"Sao phải làm khổ mình vậy chứ, cứ sống theo bản thân mong muốn là được mà.\""
    xiu "\"Chị nghĩ em cứ kệ nó đi, rồi thời gian sẽ chữa lành tất cả mà.\""
    
    menu:
        "Dạ vâng, thế thì em nghe lời chị vậy.":
            jump ending_subjective_idealism
            
        "Em nghĩ vẫn nên về thì hơn…":
            jump ending_metaphysical_materialism

label day13_hainu:
    scene bg ktx with wipeleft_scene
    play music dorm_theme fadein 1.0
    
    "Điện thoại rung."
    hainu "\"Em rảnh không. Tới CLB chị nhờ chút với.\""

    mc "(Giờ này còn gọi gì nữa nhở? Lại ra căng tin hát hò tuyển thành viên à?)"
    mc "(Thôi thì cứ tới xem sao vậy.)"
    
    scene bg club_party with wipeleft_scene
    play music club_theme fadein 1.0 # Yuri (Hainu)
    
    "Giữa phòng trưng một băng rôn Happy Birthday."
    
    show hainu 1a at t11
    
    hainu "\"snvv nghen.\""
    
    mc "\"…\""
    mc "\"Dạ em cảm ơn ạ.\""
    
    hainu "\"Thôi, vào ăn đi em, chị có đặt bánh sinh nhật cỡ bự cho em rồi đấy!\""
    
    "Đã lâu rồi mới vui như thế này, bạn ăn chơi suýt quên thời gian. Chỉ có điều…"
    play music deep_thought fadein 1.0
    mc "\"Cơ mà ngày mai mới là sinh nhật em cơ mà, sao nay tổ chức sớm vậy?\""
    
    hainu "\"Ngày mai, chị nghĩ em nên về nhà làm hoà với bố.\""
    hainu "\"Dù sao cũng là gia đình, bố em thực sự chỉ lo cho em mà thôi….\""
    
    mc "\"Chuyện đó… Không phải em không muốn làm hoà với bố, mà là do nguyên nhân xuất phát từ áp lực bố em tạo ra, chỉ làm hoà thôi em nghĩ không ăn thua….\""
    
    hainu "\"Đúng là áp lực từ kỳ vọng của phụ huynh là rất lớn, nhưng nó là một động lực để ta có thể phát triển.\""
    hainu "\"Mọi vật nếu muốn tồn tại, đều phải vận động mà phát triển, không thể cứ mãi trì trệ như thế được!\""
    
    menu:
        "Quyết định (Sáng mai - Ngày 15)?"
        
        "Vậy thì… Để em về nói chuyện với bố…":
            jump ending_metaphysical_materialism
            
        "Không, em đã chịu đựng quá đủ rồi!":
            jump ending_objective_idealism

# ========================================
# ENDINGS (NGÀY 15)
# ========================================

label ending_objective_idealism:
    scene bg ktx with wipeleft_scene
    play music deep_thought fadein 1.0 # Eerie/Space
    
    centered "{size=30}{color=#ff6600}TỐI{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    
    "Đêm khuya, không ngủ được nằm trằn trọc suy nghĩ"
    
    mc "\"Cuộc đời đúng là bể khổ.\""
    mc "\"Mà lúc qua khổ thì cũng là lúc qua đời.\""
    mc "\"Nếu vậy, rốt cuộc tại sao lại phải sống trong khổ đau vậy chứ?\""
    
    "Nhớ lại bộ phim The Truman Show hồi trước xem."
    
    mc "\"Cái thằng Truman đó, đã có một cuộc sống có thể gọi là trọn vẹn rồi, vậy mắc gì lại cứ phải tìm đường thoát khỏi trường quay chứ?\""
    mc "\"Thoát khỏi trường quay để rồi ra ngoài quay cuồng với cuộc sống thật như mình thì đúng là vô nghĩa.\""
    mc "\"…\""
    
    mc "\"Cuộc sống thật… Liệu mình có thật sự có cuộc sống thật chứ?\""
    mc "\"Hay cuộc sống của mình chỉ là một con game xoay quanh việc cày chỉ số và lấy lòng hai tiền bối?\""
    mc "\"Nếu vậy… Nó có ý nghĩa gì chứ?\""
    mc "\"Liệu thế giới này… Có thật sự tồn tại?\""
    mc "\"Tại sao mọi thứ lại trùng hợp đến lạ lùng như vậy?\""
    mc "\"Những biến số, chỉ số tình cảm, tiền bạc... Chúng thay đổi cứ như lập trình sẵn vậy.\""
    mc "\"Có lẽ nào... Mình cũng chỉ là một nhân vật trong game?\""
    mc "\"Nếu vậy, thì sự đau khổ này, niềm vui này... Đều là giả tạo ư?\""
    mc "\"Nếu thế giới này là giả... Thì ta cần gì phải tuân theo những luân thường đạo lý của nó?\""
    
    scene black with dissolve_scene_full
    stop music fadeout 1.0
    "NHẬN THỨC CỦA BẠN ĐÃ VƯỢT RA KHỎI THỰC TẠI NÀY."
    "BẠN ĐÃ LẠC VÀO HƯ VÔ."
    
    scene black with dissolve_scene_full
    call ending_explanation("objective")

label ending_subjective_idealism:
    $ current_day = 14
    scene bg club_day with fade
    play music club_theme fadein 1.0 # Happy
    
    centered "{size=30}{color=#ff6600}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    
    show xiu 1c at t11
    
    xiu "\"Ái chà, bé Thắng hôm nay lớn thế nhở.\""
    xiu "\"Sang tuổi mới có khác trông đĩnh đạc hẳn ra, 10 điểm không có nhưng.\""
    
    mc "\"Dạ vâng cảm ơn chị. Nhờ ơn chị tận tình chăm sóc mà thằng bé mới lớn thế này ạ.\""
    
    xiu "\"Chú cứ quá lời. Chị có làm gì đâu. Thằng bé nó tự lớn lên đấy chứ.\""
    xiu "\"Theo như bà chị triết gia nhà chị thì chắc chắn đây là duy tâm rồi.\""
    xiu "\"Bởi vì thằng bé nó muốn đi khám phá thế giới mới nên nó mới tự lớn lên.\""
    xiu "\"Đúng nhận sai cãi nào?\""
    
    mc "\"Đúng vậy. Em đã chọn rồi. Kệ bố đi.\""
    mc "\"Sống cho bản thân mình mới là quan trọng nhất.\""
    mc "\"Gia đình mà chỉ đem lại áp lực và khổ đau thì có cần thiết phải níu giữ không?\""
    mc "\"Em thà làm đứa con bất hiếu mà vui vẻ, còn hơn làm đứa con ngoan mà tâm hồn chết lặng.\""
    
    xiu "\"Chuẩn! Chị em mình cứ thế mà sống thôi!\""
    
    "Cả hai cùng cười phá lên."
    "Có thể cùng vui, cùng cười với những người mình chân quý thế này, cuộc sống thế là hạnh phúc rồi."
    
    scene black with dissolve_scene_full
    call ending_explanation("subjective")

label ending_metaphysical_materialism:
    $ current_day = 14
    scene bg living_room with wipeleft_scene # Nhà
    play music canteen_theme fadein 1.0 # Normal daily life
    
    centered "{size=30}{color=#ff6600}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    
    "Tôi bắt xe về nhà."
    "Bố đang đứng đợi tôi trước cửa."
    
    show dad at t11
    
    dad "\"Vừa về hả con. Sao nhìn xanh sao gầy gò vậy, dạo này ăn uống có điều độ không đấy hả?\""
    
    mc "\"Con vẫn khoẻ re mà. Bố cứ lo xa.\""
    
    dad "\"Thế học hành dạo này thế nào. Điểm thi IELTS đợt trước được bao nhiêu hả con?\""
    
    mc "\"Con được tận 8.0 lận đó.\""
    
    dad "\"Sao có 8.0 hả? Con nhà người ta đi thi toàn khoe 9, 10, đằng này…\""
    
    mc "\"!!?\""
    mc "\"Vị cao nhân nào đi thi IELTS được 10.0 vậy bố?\""
    
    dad "\"Hình như là con của ông bác bên cơ quan bố. Nó vào trường sĩ quan thi tiếng anh IELTS gì đó được 10 nên được cất nhắc lên làm thông dịch viên cho thủ trưởng rồi.“\""
    dad "\"Con cũng phải học tập anh đấy, vào quân đội không chỉ được rèn luyện kỷ cương phép nước, mà sau này cũng không phải lo nghĩ gì về cơm ăn áo mặc…\""
    play music deep_thought fadein 1.0 

    mc "\"Chuyện đấy… Con cũng suy nghĩ rồi.\""
    mc "\"Con biết trình độ của con không giỏi như bao người, cũng không có tài năng chạm đến trái tim của người khác.\""
    mc "\"Nhưng hiện tại, con muốn thử sức mình trong lĩnh vực thiết kế đồ hoạ trước đã.\""
    mc "\"Đời còn dài mà, sau khi học xong, lấy được cái bằng đã, rồi con sẽ suy nghĩ lại nghiêm túc xem có nên vào quân đội hay không?\""
    
    dad "\"…\""
    dad "\"Con nhìn vào thực tại được như vậy là tốt.\""
    dad "\"Con… Cũng đã trưởng thành rồi.\""
    dad "\"Vậy thì, bố tin tưởng vào quyết định của con.\""
    
    scene black with dissolve_scene_full
    call ending_explanation("metaphysical")

label ending_dialectical_materialism:
    $ current_day = 14
    scene bg living_room with wipeleft_scene
    play music canteen_theme fadein 1.0 # Argument/Tension
    
    centered "{size=30}{color=#ff6600}SÁNG{/color}{/size}\n{size=20}Ngày [current_day]{/size}"
    
    "Tôi bắt xe về nhà."
    "Bố đang đứng đợi tôi trước cửa."
    
    show dad at t11
    
    dad "\"Vừa về hả con. Sao nhìn xanh sao gầy gò vậy, dạo này ăn uống có điều độ không đấy hả?\""
    
    mc "\"Con vẫn khoẻ re mà. Bố cứ lo xa.\""
    
    dad "\"Thế học hành dạo này thế nào. Điểm thi IELTS đợt trước được bao nhiêu hả con?\""
    
    mc "\"Con được tận 8.0 lận đó.\""
    
    dad "\"Sao có 8.0 hả? Con nhà người ta đi thi toàn khoe 9, 10, đằng này…\""
    
    mc "\"Vị cao nhân nào đi thi IELTS được 10.0 vậy bố?\""
    
    dad "\"Hình như là con của ông bác bên cơ quan bố. Nó vào trường sĩ quan thi tiếng anh IELTS gì đó được 10 nên được cất nhắc lên làm thông dịch viên cho thủ trưởng rồi.\""
    dad "\"Con cũng phải học tập anh đấy, vào quân đội không chỉ được rèn luyện kỷ cương phép nước, mà sau này cũng không phải lo nghĩ gì về cơm ăn áo mặc…\""
    play music deep_thought fadein 1.0 
    
    mc "\"Bố à, trước đây con đã từng nói rồi đó, nghề hoạ sĩ tuy vất vả bộn bề nhưng cũng là một nghề đáng quý, cũng góp phần vào xây dựng Tổ Quốc….\""
    mc "\"Nhất là trong thời buổi hiện nay, còn bao người vẫn còn cổ hủ, lạc hậu, bị kẹt trong cái hang mang tên chân lý.\""
    mc "\"Con có một ước mơ. Đó là… Mang triết học đến gần hơn với mọi người bằng con đường hội hoạ!\""
    
    dad "\"Con thật sự nghĩ là chỉ cần có ước mơ là sẽ thành công à? Danh tiếng không có, tiền thì càng không, con định làm gì để cạnh tranh chứ?\""
    
    mc "\"Có thể không ai để ý, nhưng nó không phải là vô ích, mà nó là nền móng cho sự thay đổi.\""
    mc "\"Sự thay đổi không hề diễn ra từ từ, liên tục mà nó là những bước nhảy vọt!\""
    mc "\"Tuy ban đầu có thể con chỉ là một hạt cát nhỏ nhoi giữa biển trời rộng lớn, nhưng cứ dần dần tích luỹ, khi đến điểm nút, con tin rằng khát khao của con sẽ chạm đến mọi người!\""
    
    dad "\"Không phải cứ tin là nó sẽ thành thật đâu! Những ý kiến mà con cho là cổ hủ lạc hậu đó với người khác nó lại là chân lý đấy. Một mình con làm sao có thể thay đổi được chứ?\""
    
    mc "\"Cái này…, nó thuộc phàm trù về cái chung và cái riêng.\""
    mc "\"Hai mặt nghe tưởng đối lập nhau, nhưng mà chúng nó cùng tồn tại trong một chính thể!\""
    mc "\"Cái chung cần cái riêng để tồn tại, còn cái riêng lại là biểu hiện của cái chung.\""
    mc "\"Vì vậy, khi cái riêng mâu thuẫn với cái chung, nó có thể tác động lên chính sự tồn tại của cái chung đó, thúc đẩy cho sự phát triển.\""
    mc "\"Chính con đã thay đổi nhờ sự tác động của người khác, vì thế nên con tin mong ước của con một ngày nào đó sẽ tác động được đến một ai đó, rồi người đó sẽ lại tác động đến người khác.\""
    mc "\"Rồi một ngày, con tin mong ước của con sẽ lan toả được tới mọi người!\""
    
    dad "\"Nhưng mà con ơi! Từ bao đời nay biết bao tư tưởng dậy lên rồi lại chìm xuống.\""
    dad "\"Có thể tư tưởng của con nó sẽ lan rộng, nhưng rồi một ngày nó cùng sẽ lắng xuống, thậm chí bị lãng quên, khi đấy con còn lại gì?\""
    
    mc "\"Đúng vậy, nổi lên và chìm xuống là quy luật tất yếu của vạn vật!\""
    mc "\"Nhưng mà khi chìm xuống, nó không phải là kết thúc, mà là một khởi đầu mới.\""
    mc "\"Sự phát triển không phải là phủ định hoàn toàn cái cũ, mà là kế thừa và lặp lại những cái cũ trên cơ sở cao hơn.\""
    mc "\"Khi đó, con sẽ có thể tự hào nói rằng mình đã góp một công sức nhỏ nhoi nào đấy vào việc dựng xây Đất Nước.\""
    
    show dad at s11 # small shake or emotion
    
    dad "\"Vậy… Sao…\""
    dad "\"Thôi được rồi, tuỳ con quyết định.\""
    dad "\"Nhưng hay nhớ, bố… luôn ở sau lưng con.\""

    jump confession

label confession:
    scene bg club_night with wipeleft_scene
    play music love_theme fadein 1.0 # Continue emotional theme
    
    "Làm hoà được với bố, vui vẻ quay lại CLB."
    
    show hainu 1a at t11
    
    hainu "\"Em về rồi à, chuyện với bố em thế nào rồi?\""
    
    mc "\"Cũng em xuôi cả rồi ạ.\""
    
    hainu "\"Thế thì tốt…\""
    
    "Căn phòng lại rơi vào im lặng."
    
    hainu "\"Này…\""
    hainu "\"Lại nói về chuyện các tầng của nhận thức của Plato…\""
    hainu "\"Chị đã giải thích cho em về eikasia, pistis và dianoia rồi nhỉ?\""
    hainu "\"Còn lại là noesis, em biết nó là gì rồi chứ?\""
    
    mc "\"Là chân lý.\""
    
    show hainu 1e
    
    hainu "(gật đầu) \"Đúng vậy, nó là thứ lý tưởng đẹp đẽ mà con người luôn tìm kiếm.\""
    hainu "\"Thứ lý tưởng sáng rọi như mặt trời.\""
    hainu "\"Con người từ khi sinh ra đã khao khát được thấy hình dạng thật của mặt trời, nhưng lại bị ánh sáng chói rọi của nó làm cho mù mắt.\""
    hainu "\"Họ kinh sợ ánh sáng đó, tôn nó lên làm các vị thần.\""
    
    show hainu 1c
    
    hainu "\"Nhưng rồi họ phát triển hơn, tìm được những cách để nhìn vào mặt trời mà không làm mù loà đôi mắt.\""
    hainu "\"Nhưng khi đó mặt trời không còn là thiên thể sáng nhất, rực rỡ nhất mà họ hằng tưởng tượng nữa.\""
    
    show hainu 1a
    
    hainu "\"Em có nghĩ rằng, một ngày nào đó nhân loại sẽ chạm được đến chân lý chứ?\""
    
    mc "\"…\""
    mc "\"Chị nhớ hiện tượng vướng víu lượng tử chứ?\""
    mc "\"Hai hạt tưởng chừng như không liên quan gì đến nhau nhưng khi một hạt thay đổi hạt kia cũng đổi thay.\""
    mc "\"Theo em, bản chất của hiện tượng đó chính là sự gắn kết.\""
    mc "\"Có khả năng nào, những hạt nhân trong cơ thể người cũng vướng víu với những hạt nhân từ một thiên thể nào đó không?\""
    mc "\"Có thể nhân loại không thể với tới chân lý…\""
    mc "\"…cũng có thể chân lý luôn ở bên họ.\""
    mc "\"Như cách chị luôn ở bên em vậy.\""
    
    scene black with dissolve_scene_full
    call ending_explanation("dialectical")

# ========================================
# ENDING: PHÁT XÍT (FASCIST ENDING)
# ========================================

label ending_fascist:
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=30}Nhiều năm sau...{/size}"
    $ renpy.pause(2.0, hard=True)
    
    scene bg sota with wipeleft_scene # Trại quân sự
    play music love_theme fadein 1.0
    
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
    call ending_explanation("fascist")