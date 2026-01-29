# ================================================
# ENDINGS GUIDE & PHILOSOPHICAL RECAP
# ================================================

label ending_explanation(ending_id):
    
    # 1. Clear screen & Set atmosphere
    scene black with dissolve_scene_full
    stop music fadeout 2.0
    
    # Pause for dramatic effect
    $ renpy.pause(2.0, hard=True)
    
    # Unlock the ending
    if persistent.unlocked_endings is None:
        $ persistent.unlocked_endings = set()
    $ persistent.unlocked_endings.add(ending_id)
    
    # 2. Define Content Map
    if ending_id == "fascist":
        $ box_color = "#ff0000"
        $ box_title = "SECRET ENDING: HOẠ SĨ NGƯỜI ÁO"
        $ box_philosophy = "TRIẾT LÝ: TỪ BỎ DIANOIA (TƯ DUY PHẢN BIỆN)"
        $ box_message = "Bạn đã giao nộp lý trí cho quyền lực.\nThế giới chìm trong bóng tối vì thiếu sự phản biện."
        $ box_hint = "Gợi ý: Lần sau hãy dùng lý trí để đối thoại, đừng chỉ biết vâng lời."
        
    elif ending_id == "subjective_active":
        $ box_color = "#ff66aa"
        $ box_title = "HAPPY ENDING: XIU ROUTE"
        $ box_philosophy = "TRIẾT LÝ: HEDONISM (CHỦ NGHĨA HƯỞNG LẠC)"
        $ box_message = "Bạn chọn chiếc hang êm ái thay vì đối mặt thực tại.\nHạnh phúc này chỉ là một liều thuốc tê liệt nhận thức."
        $ box_hint = "Gợi ý: Tìm kiếm niềm vui là tốt, nhưng đừng để nó che mắt sự thật."
        
    elif ending_id == "subjective_passive":
        $ box_color = "#aa0000"
        $ box_title = "BAD ENDING: VÒNG LẶP HƯ VÔ"
        $ box_philosophy = "TRIẾT LÝ: NIHILISM (THUYẾT HƯ VÔ)"
        $ box_message = "Bạn hoài nghi tất cả sự tồn tại.\nVì không tin vào thực tại, bạn cũng mất luôn khả năng thay đổi nó."
        $ box_hint = "Gợi ý: Đừng chỉ nhìn vào 'cái hang giả dối', hãy tìm lối ra (Noesis)."
        
    elif ending_id == "metaphysical":
        $ box_color = "#ffffff"
        $ box_title = "NORMAL ENDING: THỰC TẠI CHẤP NHẬN"
        $ box_philosophy = "TRIẾT LÝ: DUY VẬT SIÊU HÌNH (THỤ ĐỘNG)"
        $ box_message = "Bạn nhìn thấy thực tế nhưng cúi đầu trước nó.\nBạn an toàn, nhưng bạn không hề có tự do."
        $ box_hint = "Gợi ý: Muốn thay đổi thực tại, bạn cần nhiều hơn sự phục tùng."
        
    elif ending_id == "dialectical":
        $ box_color = "#ffdd00"
        $ box_title = "TRUE ENDING: HÀNH TRÌNH TRIẾT HỌC"
        $ box_philosophy = "TRẠNG THÁI: NOESIS (GIÁC NGỘ)"
        $ box_message = "Bạn dùng mâu thuẫn để phát triển.\nBạn không chối bỏ Bố, mà thuyết phục Bố.\nĐây chính là Tự Do Đích Thực."
        $ box_hint = "Chúc mừng bạn đã tốt nghiệp khóa học Triết học nhập môn!"
        
    else:
        # Fallback
        $ box_color = "#ffffff"
        $ box_title = "ENDING"
        $ box_philosophy = "..."
        $ box_message = "..."
        $ box_hint = "..."

    # 3. Display Content (Using centered text style for 'Report Card' feel)
    
    # Title
    centered "{size=50}{color=[box_color]}[box_title]{/color}{/size}"
         
    # Philosophy Name
    centered "{size=35}{i}[box_philosophy]{/i}{/size}"
    
    # The Verdict/Message
    centered "{size=30}[box_message]{/size}"
    
    # The Hint/Advice (Smaller)
    centered "{size=24}{color=#aaaaaa}[box_hint]{/color}{/size}"
    
    # Final pause
    $ renpy.pause(2.0, hard=True)
    
    return
