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
    
    scene bg mc_room with dissolve_scene_full
    play music daily_life fadein 1.0
    
    "Sáng ngày thứ 10."
    "Điện thoại lại reo."
    "Là Bố."
    
    mc "(Hít sâu)... \"Alo, con nghe ạ.\""
    
    dad "\"Cuối tuần này về nhà ngay. Tao dẫn mày đi gặp mấy chú bên quân đội.\""
    dad "\"Chuẩn bị tinh thần đi, tao đăng ký cho mày vào trường Sĩ quan rồi.\""
    
    mc "\"Nhưng bố ơi... con đang học...\""
    
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
    play music sad fadein 1.0
    
    "Tôi buông điện thoại xuống."
    "Không còn tiền chu cấp, áp lực tài chính của mình tăng lên rồi, từ ngày mai phải tiết kiệm lại thôi."
    "Cảm giác như cả bầu trời sụp đổ."

    "Cảm giác như cả bầu trời sụp đổ."
    "Mọi nỗ lực 10 ngày qua... Điểm số, bạn bè, CLB..."
    "Chẳng lẽ tất cả chỉ là vô nghĩa sao?"
    
    mc "\"Mình... thực sự không có quyền lựa chọn sao?\""
    
    scene black with dissolve_scene_full
    
    # ========================================
    # NGÀY 11: TRỐN CHẠY (ESCAPISM)
    # ========================================
    
    centered "{size=40}Ngày 11{/size}"
    $ renpy.pause(1.5, hard=True)
    $ current_day = 11

    scene bg mc_room with dissolve_scene_full
    
    mc "Hôm qua cãi nhau với bố xong... Chẳng còn tâm trạng nào mà đi học nữa."
    
    "Điện thoại rung."
    
    # CHECK AFFINITY TO DECIDE EVENT
    if stats.rel_xiu > stats.rel_hainu:
        jump ch3_day11_xiu_drunk
    else:
        jump ch3_day11_hainu_movie

label ch3_day11_xiu_drunk:
    # CẢNH ĐI NHẬU VỚI XỈU (Lấy từ Ngày 14 cũ)
    
    "Xỉu: <Ê cu. Buồn đời à? Đi làm vài chai không?>"
    
    mc "Chị ấy... sao lúc nào cũng xuất hiện đúng lúc vậy?"
    
    scene bg bar with wipeleft_scene # Cần BG quán rượu hoặc quán vỉa hè
    play music daily_life fadein 1.0
    
    show monika 1a at t11
    
    xiu "\"Uống đi. Say rồi sẽ quên hết sự đời.\""
    
    mc "\"Em không uống được rượu...\""
    
    xiu "\"Yếu đuối! Đàn ông con trai phải biết uống rượu, hút thuốc, chơi gái... à vế sau bỏ qua đi.\""
    
    # ... (Giữ hội thoại cũ nếu muốn, hoặc rút gọn)
    
    mc "\"Chị Xỉu này... Chị nghĩ sao về tự do?\""
    
    show monika 2a
    
    xiu "\"Tự do à? Với chị, đơn giản là đ*o phải nghe thằng nào con nào hết.\""
    xiu "\"Thích làm gì thì làm. Sống nay chết mai, lo nghĩ làm gì cho mệt?\""
    
    mc "(Sống nay chết mai sao...)"
    
    jump ch3_reflection

label ch3_day11_hainu_movie:
    # CẢNH XEM PHIM VỚI HẢI NỮ (Lấy từ Ngày 18 cũ)
    
    "Hải Nữ: <Tôi nghe nói tâm trạng cậu không tốt. Có muốn đi xem phim không? Tôi bao.>"
    
    mc "Hội Trưởng bao sao? Lạ thật đấy..."
    
    scene bg cinema with wipeleft_scene # Cần BG rạp phim
    play music love_theme fadein 1.0
    
    show yuri 1a at t11
    
    hainu "\"Phim 'The Truman Show'. Cậu xem chưa?\""
    
    mc "\"Chưa ạ...\""
    
    "..."
    "Bộ phim kết thúc."
    "..."
    
    show yuri 2f
    
    hainu "\"Cậu thấy đấy. Truman đã sống trong giả dối suốt 30 năm.\""
    hainu "\"Nhưng cuối cùng, anh ta đã chọn bước ra khỏi cánh cửa đó, dù bên ngoài là bão tố.\""
    
    hainu "\"Tự do... không bao giờ là dễ dàng. Nhưng nó xứng đáng.\""
    
    mc "(Bước ra khỏi cánh cửa...)"
    
    jump ch3_reflection

label ch3_reflection:
    
    # ========================================
    # NGÀY 12 & 13: TỰ VẤN
    # ========================================
    
    hide monika
    hide yuri
    with dissolve
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}Ngày 12 & 13{/size}"
    $ renpy.pause(2.0, hard=True)
    
    scene bg mc_room with dissolve_scene_full
    play music deep_thought fadein 1.0
    
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
    
    scene bg camp_morning with fade # Cần BG trại lính hoặc tương tự
    play music tense fadein 1.0
    
    "Mấy chục năm sau, thế giới bước qua cuộc Chiến tranh Thế Giới thứ 3."
    "Cuộc chiến kết thúc với sự thống trị của một tên độc tài."
    "Khi ấy, tên độc tài ấy đang trong một boong-ke chuẩn bị cho buổi tử hình tập thể các nhà triết gia."
    
    show mc_dictator at t11 # Nếu có sprite MC độc tài
    
    mc "\"Khi đứng đây thì tôi muốn nói chuyện với bố tôi!\""
    mc "\"Bố ơi, bố ơi, bố thấy đúng khi cho con nghỉ học chưa.\""
    mc "\"Năm xưa các người chê nghệ thuật của tôi không nhìn xa trông rộng, nay tôi vẽ lại cả bản đồ thế giới, các người thấy đã đủ rộng rồi chứ?\""
    
    "Hắn chỉ tay vào đám tù nhân."
    
    mc "\"Còn những tên triết gia này, chỉ giỏi kích động mõm.\""
    mc "\"Thế giới mới do ta xây dựng không cần tranh luận, không cần biện chứng, không cần triết học.\""
    mc "\"Chỉ cần một chân lý duy nhất, chính là ta.\""
    
    scene black with dissolve_scene_full
    centered "{size=40}{color=#ff0000}SECRET ENDING: HOẠ SĨ NGƯỜI ÁO{/color}{/size}"
    
    # Philosophical Recap
    call ending_explanation("fascist")
    
    return

