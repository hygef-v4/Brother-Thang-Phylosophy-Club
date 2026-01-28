# ================================================
# CHAPTER 4: NOESIS (TRI THỨC) - DAY 14 & 15
# Brother Thang Philosophy Club
# ================================================

label ch4_noesis:
    
    # Show stats UI just in case
    show screen stats_display

    $ current_chapter = 4
    $ current_day = 14
    
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    centered "{size=40}Ngày 14 - Tối{/size}"
    
    $ renpy.pause(2.0, hard=True)
    
    # ========================================
    # NGÀY 14: TIỆC SINH NHẬT SỚM & QUYẾT ĐỊNH
    # ========================================
    
    # Check relationships to determine path intro
    if stats.rel_xiu > 80 and stats.rel_hainu > 80:
        jump ch4_path_both
    elif stats.rel_xiu > 80:
        jump ch4_path_xiu
    elif stats.rel_hainu > 80:
        jump ch4_path_hainu
    else:
        jump ch4_path_lonely

# ... (Các label path giữ nguyên nội dung hội thoại, chỉ thay đổi bối cảnh thời gian nếu cần) ...
# ... (Nội dung dưới đây copy từ file cũ của user nhưng sửa ngày diễn ra là Tối 14, Quyết định cho Ngày 15)

label ch4_path_both:
    scene bg ktx with wipeleft_scene
    play music daily_life fadein 1.0
    
    "Điện thoại rung."
    "Xỉu: <Ây cu. Tới CLB tí đi. Có việc.>"
    
    scene bg club_day with fade
    play music club_theme fadein 1.0
    
    "Giữa phòng trưng một băng rôn Happy Birthday (Sớm)."
    
    show yuri 1a at t21
    show monika 1k at t22
    
    hainu "\"Sinh nhật vui vẻ nhé.\""
    xiu "\"Ăn sớm lấy sức mà chiến đấu với ông bô em ơi.\""
    
    # ... (Hội thoại khuyên nhủ y hệt cũ) ...
    
    xiu "\"Chị nghĩ em nên kệ họ đi, cứ làm theo mong muốn của bản thân là được.\""
    hainu "\"Vậy… Mong muốn của em là gì?\""
    
    menu:
        "Quyết định của bạn (Sẽ thực hiện vào sáng mai - Ngày 15)?"
        
        "Về nói chuyện với bố (Duy vật siêu hình)":
            mc "\"Vậy thì… Sáng mai em sẽ về nói chuyện với bố…\""
            jump ending_metaphysical_materialism
            
        "Kệ, thời gian chữa lành (Duy tâm chủ quan)":
            mc "\"Không cần đâu, em tin thời gian sẽ chữa lành tất cả.\""
            jump ending_subjective_idealism_xiu
            
        "Triết học giúp gắn kết (Duy vật biện chứng)" if stats.unlocked_dialectics:
            mc "\"Những thứ mà mình học được… Em tin rằng, triết học giúp con người ta gắn kết lại với nhau!\""
            jump ending_dialectical_materialism

label ch4_path_xiu:
    scene bg ktx with wipeleft_scene
    play music daily_life fadein 1.0
    
    show monika 1a at t11
    
    xiu "\"Ây cu, về rồi à?\""
    xiu "\"Mai sinh nhật rồi nhỉ?\""
    
    # ... (Hội thoại Xỉu khuyên nhủ) ...
    
    menu:
        "Quyết định (Sáng mai - Ngày 15)?"
        
        "Nghe lời chị Xỉu (Duy tâm chủ quan)":
            mc "\"Dạ vâng, thế thì em nghe lời chị vậy. Mai em sẽ ở lại đây.\""
            jump ending_subjective_idealism_xiu
             
        "Về nhà (Duy vật siêu hình)":
            mc "\"Em nghĩ vẫn nên về thì hơn...\""
            jump ending_metaphysical_materialism

label ch4_path_hainu:
    scene bg ktx with wipeleft_scene
    play music daily_life fadein 1.0
    
    "Điện thoại rung. Hải Nữ gọi lên CLB."
    
    scene bg club_day with fade
    play music club_theme fadein 1.0
    
    show yuri 1a at t11
    
    hainu "\"Sinh nhật vui vẻ.\""
    
    # ... (Hội thoại Hải Nữ khuyên nhủ) ...
    
    menu:
        "Quyết định (Sáng mai - Ngày 15)?"
        
        "Về nói chuyện với bố (Duy vật siêu hình)":
            mc "\"Vậy thì… Để em về nói chuyện với bố…\""
            jump ending_metaphysical_materialism
             
        "Không, em chịu đủ rồi (Duy tâm khách quan)":
            mc "\"Không, em đã chịu đựng quá đủ rồi!\""
            jump ending_objective_idealism

label ch4_path_lonely:
    scene bg ktx with fade
    "Ngày sinh nhật đến gần, nhưng tôi cảm thấy trống trải."
    "Có lẽ mình nên về nhà xin lỗi bố..."
    
    jump ending_metaphysical_materialism

# ========================================
# ENDINGS (NGÀY 15)
# ========================================

label ending_objective_idealism:
    $ current_day = 15
    scene bg ktx with dissolve_scene_full
    play music deep_thought fadein 1.0
    
    centered "{size=40}Ngày 15{/size}"
    
    "Đêm khuya, không ngủ được nằm trằn trọc suy nghĩ."
    
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
    
    scene black with dissolve_scene_full
    centered "{size=30}{color=#aa0000}BAD ENDING: VÒNG LẶP HƯ VÔ{/color}{/size}"
    
    call ending_explanation("subjective_passive")
    return

label ending_subjective_idealism_xiu:
    $ current_day = 15
    scene bg club_day with fade
    play music daily_life fadein 1.0
    
    centered "{size=40}Ngày 15{/size}"
    
    show monika 1k at t11
    # ... (Nội dung Happy Ending Xiu giữ nguyên) ...
    
    scene black with dissolve_scene_full
    centered "{size=30}{color=#ff66aa}HAPPY ENDING: XIU ROUTE{/color}{/size}"
    
    call ending_explanation("subjective_active")
    return

label ending_metaphysical_materialism:
    $ current_day = 15
    scene bg club_day with fade # Unavailable home bg, giả vờ là nhà hoặc về nhà rồi quay lại
    play music daily_life fadein 1.0
    
    centered "{size=40}Ngày 15{/size}"
    
    "Sáng hôm sau, tôi bắt xe về nhà."
    "Bố đang đứng đợi."
    
    show dad at t11
    # ... (Nội dung Normal Ending giữ nguyên) ...
    
    scene black with dissolve_scene_full
    centered "{size=30}{color=#ffffff}NORMAL ENDING: THỰC TẠI CHẤP NHẬN{/color}{/size}"
    
    call ending_explanation("metaphysical")
    return

label ending_dialectical_materialism:
    $ current_day = 15
    scene bg club_day with fade
    play music tense fadein 1.0
    
    centered "{size=40}Ngày 15{/size}"
    
    "Sáng hôm sau, tôi bắt xe về nhà với một tâm thế khác."
    "Không còn sợ hãi. Tôi muốn đối thoại với bố."
    
    show dad at t11
    # ... (Nội dung True Ending giữ nguyên) ...
    
    # ... (Sau khi tranh luận xong) ...
    
    # Transition to Epilogue
    scene black with dissolve_scene_full
    centered "{size=40}CẢNH CUỐI{/size}"
    
    scene bg club_day with fade
    play music happy fadein 1.0
    
    "Làm hoà được với bố, tôi vui vẻ quay lại CLB."
    
    # ... (Phần giải thích Noesis của Hải Nữ) ...
    
    scene black with dissolve_scene_full
    centered "{size=40}{color=#ffdd00}TRUE ENDING{/color}{/size}\n{size=24}HÀNH TRÌNH TRIẾT HỌC{/size}"
    
    call ending_explanation("dialectical")
    return
