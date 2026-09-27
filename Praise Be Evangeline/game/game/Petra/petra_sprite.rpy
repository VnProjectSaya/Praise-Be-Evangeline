# ══════════════════════════════════════════════
# PETRA — LAYERED SPRITE
# Stack (bottom to top): body → mouth → eyes → brows → shadow overlay
# Body has two states: idle (calm resting) and panic (faster, agitated —
# same two frames, just cut quicker, same technique as Eva/Desmond/Vidius'
# calm/agitated split).
# ══════════════════════════════════════════════

# ── ANIMATED BODY (no alpha — hard frame-swap, same technique as Eva) ──
# No Petra float exists in any chapter yet, so this defaults to Eva's
# calm/agitated timing (10s idle cycle, 5s panic cycle). Retime to match
# whenever a petra_float transform gets written into a script.
image petra_body:
    "Petra/Body_Anim_2.png"
    pause 0.5
    "Petra/Body_Anim_1.png"
    pause 9.5
    repeat

image petra_body_panic:
    "Petra/Body_Anim_2.png"
    pause 0.4
    "Petra/Body_Anim_1.png"
    pause 2.1
    "Petra/Body_Anim_2.png"
    pause 0.4
    "Petra/Body_Anim_1.png"
    pause 2.1
    repeat


# ── EYE BLINK LOOPS (Desmond/Vidius pattern — one shared Closed.png) ──
image petra_eye_blink_normal:
    "Petra/Eye/Open_Normal.png"
    pause 6.0
    "Petra/Eye/Half_Normal.png"
    pause 0.08
    "Petra/Eye/Closed.png"
    pause 0.08
    "Petra/Eye/Half_Normal.png"
    pause 0.08
    "Petra/Eye/Open_Normal.png"
    repeat

image petra_eye_blink_shocked:
    "Petra/Eye/Open_Shocked.png"
    pause 6.0
    "Petra/Eye/Half_Shocked.png"
    pause 0.08
    "Petra/Eye/Closed.png"
    pause 0.08
    "Petra/Eye/Half_Shocked.png"
    pause 0.08
    "Petra/Eye/Open_Shocked.png"
    repeat


# ── SHADOW OVERLAY (multiply blend) ──
image petra_shadow_multiply:
    "Petra/Shadows.png"
    blend "multiply"


# ── THE LAYERED IMAGE ──
layeredimage petra:
    group body:
        attribute idle default "petra_body"
        attribute panic "petra_body_panic"

    group mouth:
        # No Neutral.png was provided for her — "happy" is her resting
        # default mouth, not a placeholder name for neutral.
        attribute happy default "Petra/Mouth/Happy.png"
        attribute smile "Petra/Mouth/Smile.png"
        attribute frown "Petra/Mouth/Frown.png"
        attribute angry "Petra/Mouth/Angry.png"
        attribute shockedm "Petra/Mouth/Shocked.png"
        attribute surprised "Petra/Mouth/Surprised.png"

    group eyes:
        attribute normal default "petra_eye_blink_normal"
        attribute shocked "petra_eye_blink_shocked"

    group brows:
        attribute browneutral default "Petra/Brow/Neutral.png"
        attribute browmad "Petra/Brow/Mad.png"
        attribute browsad "Petra/Brow/Sad.png"

    group shadow:
        attribute noshadow default Null()
        attribute shadow "petra_shadow_multiply"
