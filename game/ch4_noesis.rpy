# ================================================
# CHAPTER 4: NOESIS (TRI THỨC)
# Brother Thang Philosophy Club
# ================================================

label ch4_noesis:
    $ current_day = 30
    $ current_chapter = 4
    
    # ========================================
    # CẢNH MỞ ĐẦU - NGÀY 30 (KTX - SÁNG)
    # ========================================
    
    stop music fadeout 2.0
    scene bg bedroom with dissolve_scene_full
    play music daily_life fadein 1.0
    
    # Montage narration handled as text
    "Sau hôm xem phim, vài ngày trôi qua."
    "Mình đi làm thêm."
    "Mình ghi chép lại ý tưởng vẽ."
    "Và điều lạ nhất là… mình bắt đầu tự hỏi: \"Nếu mọi thứ đều có thể giả… thì thứ gì là thật?\""
    
    "Main tỉnh dậy."
    "Không có chuông báo thức. Không có tin nhắn."
    "Chỉ là một buổi sáng rất… yên tĩnh."
    
    mc "\"…Lạ thật. Lần đầu tiên mình không thấy lo về ngày hôm nay.\""
    
    "Nhìn ra ngoài cửa sổ. Bầu trời vẫn xanh."
    
    mc "(cười nhẹ) \"Biết là không xanh… nhưng vẫn đẹp thật.\""
    
    "Điện thoại rung."
    
    ischyros "<Hôm nay lên CLB sớm nhé. Có chuyện quan trọng.>"
    
    # ========================================
    # CẢNH 1: TRẠI - SÁNG
    # ========================================
    scene bg military_camp with wipeleft_scene
    
    "Main đứng trước cổng trại quân sự. Nhưng lần này… không bước vào."
    
    show yuri 3f at t11 # Placeholder for Dad
    
    "Bố từ xa bước tới."
    
    dad "\"Con suy nghĩ xong chưa?\""
    
    mc "\"Rồi ạ.\""
    
    dad "\"Vào quân đội… hay về trường làm cái thứ nghệ thuật viển vông của mày?\""
    
    "Main im lặng một lúc lâu."
    
    mc "\"Bố có tin là… có những thứ không đo được bằng tiền hay kỷ luật không?\""
    
    dad "\"…Mày lại học mấy cái triết vớ vẩn đó à?\""
    
    mc "\"Không. Con học cách tự chịu trách nhiệm cho lựa chọn của mình.\""
    
    "Main nhìn thẳng."
    
    mc "\"Con không ghét quân đội.\""
    mc "\"Nhưng nếu con vào đó chỉ vì sợ đói, sợ nghèo, sợ bị bỏ rơi… thì đó không phải lựa chọn.\""
    mc "\"…mà là trốn chạy.\""
    
    "Bố siết chặt tay."
    
    dad "\"Mày nghĩ mày giỏi hơn tao chắc?\""
    
    mc "\"Không.\""
    mc "\"Nhưng con biết… nếu hôm nay con không tự quyết định cuộc đời mình… thì sau này con sẽ hối hận.\""
    
    "Một khoảng lặng rất dài."
    "Bố quay lưng."
    
    dad "\"Tùy mày. Từ nay… đừng dựa vào tao nữa.\""
    
    mc "\"Dạ.\""
    
    hide yuri with dissolve
    
    "Bố bước đi. Main không đuổi theo."
    
    mc "(độc thoại) \"Lần đầu tiên… mình không cảm thấy sợ.\""
    
    # ========================================
    # CẢNH 2: CLB - CHIỀU
    # ========================================
    scene bg club_day with wipeleft_scene
    play music club_theme fadein 1.0
    
    "Cả CLB đều có mặt. Hương, Xỉu, Hải Nữ, và Hội trưởng."
    
    show yuri 1f at t11
    
    "Đào Chí Ischyros đứng trước bảng. Trên bảng viết một từ duy nhất: NOESIS."
    
    ischyros "\"Hôm nay là buổi sinh hoạt cuối cùng của tôi với tư cách hội trưởng.\""
    
    "Mọi người sững sờ."
    
    huong "\"Chị định đi đâu?\""
    
    ischyros "\"Tôi không đi đâu cả. Tôi chỉ không muốn CLB phụ thuộc vào tôi nữa.\""
    
    "Cô nhìn sang Main."
    
    ischyros "\"Cậu biết Noesis là gì không?\""
    
    mc "\"…Là khi con người không còn chỉ tin, không còn chỉ suy luận… mà trực tiếp nhận ra sự thật.\""
    
    show yuri 1a
    ischyros "(gật đầu) \"Noesis không phải là biết nhiều hơn. Mà là không còn tự lừa mình.\""
    
    "Cô đặt một xấp giấy lên bàn."
    
    ischyros "\"Đây là đơn xin tài trợ triển lãm nghệ thuật sinh viên. Chủ đề: ‘Thoát Khỏi Cái Hang’.\""
    
    "Mọi ánh mắt đổ dồn về Main."
    
    ischyros "\"Tôi muốn cậu đứng tên chủ dự án.\""
    
    mc "\"…Em?\""
    
    ischyros "\"Cậu đã đi qua Eikasia. Đã nghi ngờ ở Pistis. Đã tranh luận ở Dianoia.\""
    ischyros "\"Giờ là lúc… cậu tự chọn xem mình là ai.\""
    
    menu:
        "Em sẽ làm.":
            mc "\"Em sẽ làm.\""
            # CONTINUE TO TRUE ENDING
            
        "Em vẫn chưa sẵn sàng.":
            mc "\"Em vẫn chưa sẵn sàng.\""
            jump bad_ending_pistis_loop

    # ========================================
    # CẢNH 3: HÀNH LANG - TỐI (TRUE PATH)
    # ========================================
    scene bg corridor with wipeleft_scene
    
    "Main đứng một mình. Hành lang dài. Đèn vàng."
    "Từng người bước tới."
    
    # Interaction with Huong
    show sayori 1a at t11
    huong "\"Anh biết không… Em thích anh không phải vì anh giỏi.\""
    huong "\"Mà vì anh luôn cố hiểu thế giới này theo cách của riêng mình.\""
    
    mc "(cười) \"Anh vẫn đang học.\""
    
    huong "\"Vậy thì… khi nào anh sẵn sàng, em vẫn ở đây.\""
    hide sayori with dissolve
    
    # Interaction with Xiu
    show monika 1a at t11
    xiu "\"Cu em này. Đời chị cược cả đời rồi. Lần này… chị không cá nữa.\""
    
    mc "\"Vậy chị tin vào gì?\""
    
    xiu "\"…Tin là có người nhớ tới mình như một con người.\""
    hide monika with dissolve
    
    # Interaction with Hai Nu
    show natsuki 1a at t11
    hainu "\"Cậu không cần tiền của tôi nữa đúng không?\""
    
    mc "\"Em cần chị. Nhưng không phải như một cái ví.\""
    
    hainu "(cười thật lòng) \"Được. Vậy thì để tôi học cách làm người bình thường.\""
    hide natsuki with dissolve
    
    # Interaction with Ischyros
    show yuri 1a at t11
    ischyros "\"Cậu có biết tại sao tôi chọn Plato không?\""
    
    mc "\"Vì cái hang?\""
    
    ischyros "\"Không. Vì Plato tin rằng… người đã thấy ánh sáng có trách nhiệm quay lại.\""
    
    "Cô bước đi."
    
    ischyros "\"Giờ thì đến lượt cậu.\""
    hide yuri with dissolve
    
    # ========================================
    # TRUE ENDING SCENE
    # ========================================
    scene bg club_day with fade
    # Description: Main standing before empty canvas
    
    mc "\"Thế giới này có thể là giả. Niềm tin có thể sai. Lý trí có thể bị bóp méo.\""
    
    "Main cầm bút."
    
    mc "\"Nhưng việc tôi chọn vẽ gì lên nó… là thật.\""
    
    scene black with dissolve_scene_full
    
    "Tri thức không phải là thoát khỏi cái hang."
    "Mà là biết mình đang ở đâu… và vẫn chọn bước tiếp."
    
    "TRUE ENDING - NOESIS"
    return

# ================================================
# BAD ENDING: PISTIS LOOP
# ================================================
label bad_ending_pistis_loop:
    
    mc "\"Em… không làm được đâu. Em sợ làm hỏng. Em sợ người ta cười. Em sợ… em không đủ giỏi.\""
    
    "Không khí lạnh đi."
    
    ischyros "\"Cậu đang sợ cái gì? Thất bại… hay ánh sáng?\""
    
    mc "\"Em… chỉ muốn sống yên ổn.\""
    
    ischyros "(cười nhạt) \"Yên ổn là một loại thuốc ngủ rất mạnh. Được. Cậu đã chọn.\""
    
    "Hội trưởng quay lưng, cầm xấp giấy."
    
    ischyros "\"Tôi sẽ tìm người khác. Còn cậu… chúc cậu có một cái hang ấm áp.\""
    
    # CẢNH 2: HÀNH LANG
    scene bg corridor with wipeleft_scene
    
    "Main bước ra hành lang. Thấy Hương đứng đợi."
    
    huong "\"Anh… sao rồi?\""
    
    mc "\"Anh từ chối rồi. Anh nghĩ… anh không hợp mấy thứ lớn lao đó.\""
    
    "Hương nhìn Main, hơi cười, nhưng mắt không cười."
    
    huong "\"Anh lúc nào cũng nói ‘không hợp’. Không hợp đứng ra. Không hợp quyết định. Không hợp chịu trách nhiệm.\""
    
    mc "\"Anh chỉ—\""
    
    huong "\"Anh chỉ… muốn người khác quyết thay. Nếu vậy… Anh cần em giúp không?\""
    
    "Main nhẹ nhõm, như được cứu."
    
    mc "\"Có.\""
    
    huong "\"Vậy từ giờ… Anh cứ nghe em.\""
    
    # CẢNH 3: KTX - LOOP
    scene bg bedroom with fade
    
    "Main mở máy tính. Desktop trống trơn."
    mc "\"Ủa… thư mục bài tập đâu rồi?\""
    
    huong "<Em sắp xếp lại hết cho anh rồi. Anh chỉ cần làm theo checklist.>"
    
    mc "(cười) \"Đỡ quá…\""
    
    "Main làm theo checklist. Gửi bài. Nộp báo cáo. Đi học. Đi ngủ."
    "Ngày nào cũng vậy. Không còn \"vẽ\". Không còn \"triết\". Không còn \"tại sao\"."
    "Chỉ còn: \"Cần làm gì tiếp theo?\""
    
    # EPILOGUE PISTIS
    scene black with dissolve_scene_full
    
    mc "(độc thoại) \"Thật ra… mình cũng không tệ. Mình vẫn sống. Mình vẫn qua môn. Mình vẫn ổn…\""
    mc "\"Chỉ là… mình không còn thấy bầu trời nữa.\""
    
    "BAD ENDING – PISTIS LOOP"
    "Cậu không bị ai nhốt lại. Cậu tự kéo chăn lên mắt mình."
    return
