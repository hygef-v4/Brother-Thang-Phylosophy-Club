define config.developer = True

init python:
    # Character sprite head/body gap fix
    # Positive y-offset moves head down to close gap
    head_offset = (0, 1)
    
    # Negative x-offset moves right body part left to overlap and close vertical seam
    body_offset = (-1, 0)

# ================================================
# CUSTOM IMAGE DEFINITIONS (Migrated)
# ================================================

# Background - MC's Gaming Room
image bg mc_room = Transform("bg/mc_room.jpg", fit="cover", align=(0.5, 0.5))

# Character - Dad
image dad = Transform("images/dad.png", zoom=0.85, xalign=0.5, yalign=1.0)
image dad neutral = Transform("images/dad.png", zoom=0.85, xalign=0.5, yalign=1.0)
image dad angry = Transform("images/dad.png", zoom=0.85, xalign=0.5, yalign=1.0)

# Character - Robot T31
# Character - Robot T31
image pig = Transform("images/robot_t31.png", zoom=1.25, xalign=0.5, yalign=1.0)
image pig side = Transform("images/robot_t31_side.png", zoom=0.35, xalign=0.0, yalign=1.0)

# ================================================
# CHARACTER SPRITES - Võ Minh Xỉu
# ================================================
image xiu 1a = "xiu/xiu_neutral.png"      # Neutral - calm, default
image xiu 1b = "xiu/xiu_happy.png"        # Happy - cheerful
image xiu 1c = "xiu/xiu_sad.png"          # Sad - disappointed  
image xiu 1d = "xiu/xiu_angry.png"        # Angry - frustrated
image xiu 1e = "xiu/xiu_surprised.png"    # Surprised - shocked
image xiu 1f = "xiu/xiu_embarrassed.png"  # Embarrassed - shy
image xiu 1g = "xiu/xiu_smirk.png"        # Smirk - confident, playful
image xiu 1h = "xiu/xiu_thinking.png"     # Thinking - pondering, contemplative

# Semantic aliases for easy scripting
image xiu neutral = "xiu/xiu_neutral.png"
image xiu happy = "xiu/xiu_happy.png"
image xiu sad = "xiu/xiu_sad.png"
image xiu angry = "xiu/xiu_angry.png"
image xiu surprised = "xiu/xiu_surprised.png"
image xiu embarrassed = "xiu/xiu_embarrassed.png"
image xiu smirk = "xiu/xiu_smirk.png"
image xiu thinking = "xiu/xiu_thinking.png"

# Vũ Hải Nữ (Philosophy Club President) sprite definitions
image hainu 1a = "hainu/hainu_neutral.png"        # Neutral - calm, observing
image hainu 1b = "hainu/hainu_thinking.png"       # Thinking - adjusting glasses
image hainu 1c = "hainu/hainu_explaining.png"     # Explaining - teaching philosophy
image hainu 1d = "hainu/hainu_stern.png"          # Stern - serious, strict
image hainu 1e = "hainu/hainu_gentle_smile.png"   # Gentle Smile - warm, caring
image hainu 1f = "hainu/hainu_tired.png"          # Tired - exhausted from work
image hainu 1g = "hainu/hainu_surprised.png"      # Surprised - shocked
image hainu 1h = "hainu/hainu_embarrassed.png"    # Embarrassed - shy, flustered

# Semantic aliases
image hainu neutral = "hainu/hainu_neutral.png"
image hainu thinking = "hainu/hainu_thinking.png"
image hainu explaining = "hainu/hainu_explaining.png"
image hainu stern = "hainu/hainu_stern.png"
image hainu smile = "hainu/hainu_gentle_smile.png"
image hainu tired = "hainu/hainu_tired.png"
image hainu surprised = "hainu/hainu_surprised.png"
image hainu embarrassed = "hainu/hainu_embarrassed.png"

# Võ Quang Hưng (Dad - Major General) sprite definitions
image dad 1a = "dad/dad_sitting.png"       # Neutral Sitting - talking on phone  # Surprised Sitting - hearing unexpected news
image dad 1b = "dad/dad_standing.png"      # Standing Neutral - standard pose
image dad 1c = "dad/dad_concerned_sitting.png"
image dad 1d = "dad/dad_proud_sitting.png"
image dad 1e = "dad/dad_stern_sitting.png"
image dad 1g = "dad/dad_surprised_sitting.png"
image dad 1h = "dad/dad_thinking_sitting.png"

# Semantic aliases
image dad sitting = "dad/dad_sitting.png"
image dad standing = "dad/dad_standing.png" 
image dad concern = "dad/dad_concerned_sitting.png"
image dad pround = "dad/dad_proud_sitting.png"
image dad stern = "dad/dad_stern_sitting.png"
image dad suprise = "dad/dad_surprised_sitting.png"
image dad thinking = "dad/dad_thinking_sitting.png"

python early:
    import datetime

init python:
    import datetime
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []

    renpy.music.register_channel("music_poem", mixer="music", tight=True)

    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)

        if pos:
            return pos

        return 0

    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    def delete_character(name):
        pass

    def restore_all_characters():
        pass

    def restore_relevant_characters():
        pass

    def pause(time=None):
        global _windows_hidden

        if not time:
            _windows_hidden = True

            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)

            _windows_hidden = False

            return

        if time <= 0:
            return

        _windows_hidden = True

        renpy.pause(time)

        _windows_hidden = False
define siuuu = "sfx/siuuu.ogg"
define emoichoilamsaoduoc = "sfx/emoichoilamsaoduoc.ogg"
define audio.t1 = "<loop 22.073>bgm/1.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t5c = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"
define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"
define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"
define audio.heart = "<loop 0>bgm/heartbeat.ogg"
define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/club_day.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/house.png"
image bg class_day:
    "bg/class.png"
    zoom 0.75
# image bg corridor = "bg/corridor.png"  # OLD DDLC - replaced with hallway
# OLD DDLC club backgrounds - DISABLED (replaced with custom)
# image bg club_day = "bg/club.png"
# image bg club_day2:
#     choice:
#         "bg club_day"
#     choice:
#         "bg club_day"
#     choice:
#         "bg club_day"
#     choice:
#         "bg club_day"
#     choice:
#         "bg club_day"
#     choice:
#         "bg/club-skill.png"
image bg closet = "bg/club_day.png"
# image bg bedroom = "bg/bedroom.png"  # OLD DDLC - replaced with ktx
image bg fpt_yard = "bg/fpt_yard.png"  # Custom: Sân trường FPT
image bg gym = "bg/gym.png"  # Custom: Phòng gym FPT
image bg canteen = "bg/canteen.png"  # Custom: Canteen FPT
image bg club_day = "bg/club_day.png"  # Custom: Phòng CLB - ban ngày
image bg club_night = "bg/club_night.png"  # Custom: Phòng CLB - tối
image bg library = "bg/library.png"  # Custom: Thư viện FPT
image bg ktx = "bg/ktx.png"  # Custom: Ký túc xá FPT - ban đêm/tối
image bg ktx_day = "bg/ktx_day.png"  # Custom: Ký túc xá FPT - ban ngày (khi MC tỉnh dậy)
image bg hallway = "bg/hallway.png"  # Custom: Hành lang FPT
image bg bar = "bg/bar.png"  # Custom: Quầy bar/quán nhậu
image bg sota = "bg/sota.png"  # Custom: Khu quân sự
image bg cinema = "bg/cinema.png"  # Custom: Rạp chiếu phim
image bg living_room = "bg/living_room.png"  # Custom: Phòng khách nhà MC
image bg club_party = "bg/club_party.png"  # Custom: CLB trang trí tiệc sinh nhật
image bg ktx_xiu_room = "bg/ktx_xiu_room.png"  # Custom: Phòng của Xỉu
image bg club_messy = "bg/club_messy.png"  # Custom: CLB lộn xộn giấy tờ
image bg notebook = "bg/notebook.png"
image bg classroom = "bg/class.png"
image bg library = "bg/library.png"
image bg yenlang = "bg/yenlang.jpg"
image bg house = "bg/house.png"



image bg glitch = Solid("#000")

image bg mc_room:
    "bg/mc_room.jpg"
    zoom 1.25

image bg living_room:
    "bg/living_room.png"
    zoom 0.85

image bg ktx_xiu_room:
    "bg/ktx_xiu_room.png"
    zoom 0.85

image bg sota:
    "bg/sota.png"
    zoom 0.85

image bg yenlang:
    "bg/yenlang.jpg"
    zoom 1.25

image bg fpt_1:
    "bg_new/fpt_1.png"
    zoom 0.9

image bg fpt_2:
    "bg_new/fpt_2.png"
    zoom 0.9

image bg fpt_3:
    "bg_new/fpt_3.png"
    zoom 0.85

image bg fpt_4:
    "bg_new/fpt_4.png"
    zoom 0.85

image bg fpt_5:
    "bg_new/fpt_5.png"
    zoom 0.85

# ================================================
# NIGHT TRANSITION BACKGROUNDS (TỐI - 13 ảnh)
# fpt_3, 11-13, 17-19, 28, 32-36
# ================================================

image bg fpt_11:
    "bg_new/fpt_11.png"
    zoom 0.85

image bg fpt_12:
    "bg_new/fpt_12.png"
    zoom 0.85

image bg fpt_13:
    "bg_new/fpt_13.png"
    zoom 0.9

image bg fpt_17:
    "bg_new/fpt_17.png"
    zoom 0.85

image bg fpt_18:
    "bg_new/fpt_18.png"
    zoom 0.9

image bg fpt_19:
    "bg_new/fpt_19.png"
    zoom 0.85

image bg fpt_28:
    "bg_new/fpt_28.png"
    zoom 0.9

image bg fpt_32:
    "bg_new/fpt_32.png"
    zoom 0.85

image bg fpt_33:
    "bg_new/fpt_33.png"
    zoom 0.9

image bg fpt_34:
    "bg_new/fpt_34.png"
    zoom 0.85

image bg fpt_35:
    "bg_new/fpt_35.png"
    zoom 0.9

image bg fpt_36:
    "bg_new/fpt_36.png"
    zoom 0.85

# ================================================
# DAY/AFTERNOON TRANSITION BACKGROUNDS (SÁNG/CHIỀU - 27 ảnh)
# fpt_1-2, 4-10, 14-16, 20-27, 29-31, 37-40
# ================================================

image bg fpt_6:
    "bg_new/fpt_6.png"
    zoom 0.9

image bg fpt_7:
    "bg_new/fpt_7.png"
    zoom 0.85

image bg fpt_8:
    "bg_new/fpt_8.png"
    zoom 0.9

image bg fpt_9:
    "bg_new/fpt_9.png"
    zoom 0.85

image bg fpt_10:
    "bg_new/fpt_10.png"
    zoom 0.9

image bg fpt_14:
    "bg_new/fpt_14.png"
    zoom 0.85

image bg fpt_15:
    "bg_new/fpt_15.png"
    zoom 0.9

image bg fpt_16:
    "bg_new/fpt_16.png"
    zoom 0.85

image bg fpt_20:
    "bg_new/fpt_20.png"
    zoom 0.9

image bg fpt_21:
    "bg_new/fpt_21.png"
    zoom 0.85

image bg fpt_22:
    "bg_new/fpt_22.png"
    zoom 0.9

image bg fpt_23:
    "bg_new/fpt_23.png"
    zoom 0.85

image bg fpt_24:
    "bg_new/fpt_24.png"
    zoom 0.9

image bg fpt_25:
    "bg_new/fpt_25.png"
    zoom 0.85

image bg fpt_26:
    "bg_new/fpt_26.png"
    zoom 0.9

image bg fpt_27:
    "bg_new/fpt_27.png"
    zoom 0.85

image bg fpt_29:
    "bg_new/fpt_29.png"
    zoom 0.9

image bg fpt_30:
    "bg_new/fpt_30.png"
    zoom 0.85

image bg fpt_31:
    "bg_new/fpt_31.png"
    zoom 0.9

image bg fpt_37:
    "bg_new/fpt_37.png"
    zoom 0.85

image bg fpt_38:
    "bg_new/fpt_38.png"
    zoom 0.9

image bg fpt_39:
    "bg_new/fpt_39.png"
    zoom 0.85

image bg fpt_40:
    "bg_new/fpt_40.png"
    zoom 0.9

# =================================================================================
# REMOVED DEPRECATED CHARACTER DEFINITIONS (Sayori, Natsuki, Old Yuri, Old Monika)
# =================================================================================
# These definitions referenced missing files and have been replaced by new assets
# (hainu/xiu) and aliases.
# =================================================================================

define _dismiss_pause = config.developer
default persistent.playthrough = 0
default persistent.autoload = ""
default persistent.oldversion = ""
default persistent.deleted_saves = False
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default currentpos = 0
