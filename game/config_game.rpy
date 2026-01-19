# ================================================
# BROTHER THANG PHILOSOPHY CLUB - GAME CONFIG
# ================================================
# Central configuration file - Không hardcode!

init -1 python:
    # ========================================
    # GAME METADATA
    # ========================================
    class GameConfig:
        GAME_TITLE = "Brother Thang Philosophy Club"
        GAME_VERSION = "0.1.0 - MVP Day 1"
        DEVELOPER = "Your Name"
        
        # ========================================
        # CHARACTER NAMES
        # ========================================
        MC_NAME_DEFAULT = "Võ Chiến Thắng"
        MC_NICKNAME = "Võ Thắng"
        
        CHAR_ISCHYROS = "Đào Chí Ischyros"
        CHAR_HUONG = "Hương"
        CHAR_HAINU = "Hải Nữ"
        CHAR_XIU = "Xỉu"
        CHAR_DAD = "Bố"
        
        # ========================================
        # STATS CONFIGURATION
        # ========================================
        STAT_MAX = 100
        STAT_MIN = 0
        STAT_INITIAL_HOC_TAP = 50
        STAT_INITIAL_DOI_SONG = 50
        STAT_INITIAL_TIEN = 100000
        
        # Daily changes
        STAT_DAILY_HOC_TAP_REGEN = 5
        STAT_DAILY_DOI_SONG_REGEN = 5
        STAT_DAILY_MONEY_BASE = 50000
        
        # Activity effects
        STAT_STUDY_HOC_TAP_GAIN = 15
        STAT_GYM_DOI_SONG_GAIN = 15
        STAT_HANGOUT_HOC_TAP_LOSS = -10
        STAT_HANGOUT_DOI_SONG_LOSS = -10
        
        # ========================================
        # RELATIONSHIP CONFIGURATION
        # ========================================
        REL_MIN = 0
        REL_MAX = 100
        REL_INITIAL_ISCHYROS = 0
        REL_INITIAL_HUONG = 0
        REL_INITIAL_HAINU = 0
        REL_INITIAL_XIU = 50  # Starts higher
        
        REL_THRESHOLD_GOOD_ENDING = 80
        REL_THRESHOLD_BAD = 20
        
        # ========================================
        # TIME SYSTEM
        # ========================================
        TIME_SLOTS = ["morning", "afternoon", "evening", "night"]
        CURRENT_CHAPTER = 1
        CURRENT_DAY = 1

# Initialize game config
default game_config = GameConfig()

# ========================================
# GAME VARIABLES
# ========================================
default mc_name = "Võ Thắng"
default current_day = 1
default current_chapter = 1
default current_time_slot = "morning"

# ========================================
# DEFINE CHARACTERS
# ========================================
define mc = Character("[mc_name]", color="#FFFFFF", what_prefix='"', what_suffix='"')
define ischyros = Character(GameConfig.CHAR_ISCHYROS, color="#FFFFFF", what_prefix='"', what_suffix='"')
define huong = Character(GameConfig.CHAR_HUONG, color="#FFFFFF", what_prefix='"', what_suffix='"')
define hainu = Character(GameConfig.CHAR_HAINU, color="#FFFFFF", what_prefix='"', what_suffix='"')
define xiu = Character(GameConfig.CHAR_XIU, color="#FFFFFF", what_prefix='"', what_suffix='"')
define dad = Character(GameConfig.CHAR_DAD, color="#FFFFFF", what_prefix='"', what_suffix='"')
define narrator = Character(None, kind=nvl)  # Cho narration

# ========================================
# AUDIO DEFINITIONS (Tạm sử dụng DDLC audio)
# ========================================
# BGM - Define trực tiếp paths để tránh circular reference
define audio.main_theme = "<loop 22.073>bgm/1.ogg"
define audio.daily_life = "<loop 4.499>bgm/2.ogg"
define audio.club_theme = "<loop 4.618>bgm/3.ogg"
define audio.thinking = "<loop 10.893>bgm/6.ogg"
define audio.tense = "<loop 2.291>bgm/7.ogg"
define audio.sad = "<loop 9.938>bgm/8.ogg"

# SFX
define audio.phone_ring = "sfx/fall.ogg"  # Placeholder
define audio.notification = "sfx/pageflip.ogg"  # Placeholder
