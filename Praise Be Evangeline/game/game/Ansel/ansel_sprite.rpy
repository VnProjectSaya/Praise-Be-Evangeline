# ══════════════════════════════════════════════
# ANSEL — LAYERED SPRITE
# Stack (bottom to top): body → mouth → eyes → brows → shadow overlay
# Same setup as Petra — body has two states: idle (calm resting) and
# panic (faster, agitated — same two frames, just cut quicker).
# ══════════════════════════════════════════════

# ── ANIMATED BODY (no alpha — hard frame-swap, same technique as Eva) ──
# No Ansel float exists in any chapter yet, so this defaults to Eva's
# calm/agitated timing (10s idle cycle, 5s panic cycle). Retime to match
# whenever an ansel_float transform gets written into a script.
image ansel_body:
    "Ansel/Body_Anim_2.png"
    pause 0.5
    "Ansel/Body_Anim_1.png"
    pause 9.5
    repeat

image ansel_body_panic:
    "Ansel/Body_Anim_2.png"
    pause 0.4
    "Ansel/Body_Anim_1.png"
    pause 2.1
    "Ansel/Body_Anim_2.png"
    pause 0.4
    "Ansel/Body_Anim_1.png"
    pause 2.1
    repeat


# ── EYE BLINK LOOPS (Desmond/Vidius/Petra pattern — one shared Closed.png) ──
image ansel_eye_blink_normal:
    "Ansel/Eye/Open_Normal.png"
    pause 6.0
    "Ansel/Eye/Half_Normal.png"
    pause 0.08
    "Ansel/Eye/Closed.png"
    pause 0.08
    "Ansel/Eye/Half_Normal.png"
    pause 0.08
    "Ansel/Eye/Open_Normal.png"
    repeat

image ansel_eye_blink_shocked:
    "Ansel/Eye/Open_Shocked.png"
    pause 6.0
    "Ansel/Eye/Half_Shocked.png"
    pause 0.08
    "Ansel/Eye/Closed.png"
    pause 0.08
    "Ansel/Eye/Half_Shocked.png"
    pause 0.08
    "Ansel/Eye/Open_Shocked.png"
    repeat


# ── SHADOW OVERLAY (multiply blend) ──
image ansel_shadow_multiply:
    "Ansel/Shadow.png"
    blend "multiply"


# ── THE LAYERED IMAGE ──
layeredimage ansel:
    group body:
        attribute idle default "ansel_body"
        attribute panic "ansel_body_panic"

    group mouth:
        # No Neutral.png was provided for him either — "happy" is his
        # resting default mouth, same as Petra.
        attribute happy default "Ansel/Mouth/Happy.png"
        attribute smile "Ansel/Mouth/Smile.png"
        attribute frown "Ansel/Mouth/Frown.png"
        attribute angry "Ansel/Mouth/Angry.png"
        attribute shockedm "Ansel/Mouth/Shocked.png"
        attribute surprised "Ansel/Mouth/Surprised.png"

    group eyes:
        attribute normal default "ansel_eye_blink_normal"
        attribute shocked "ansel_eye_blink_shocked"

    group brows:
        attribute browneutral default "Ansel/Brow/Neutral.png"
        attribute browmad "Ansel/Brow/Mad.png"
        attribute browsad "Ansel/Brow/Sad.png"

    group shadow:
        attribute noshadow default Null()
        attribute shadow "ansel_shadow_multiply"
