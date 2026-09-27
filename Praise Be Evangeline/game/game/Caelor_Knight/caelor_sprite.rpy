# ══════════════════════════════════════════════
# CAELOR — LAYERED SPRITE
# Stack (bottom to top): body → mouth → eyes → brows
# No shadow group (not provided) and no shocked eye variant — only a
# normal blink loop. Single body animation state, no panic split (wasn't
# asked for this one — say the word if he needs one too).
# ══════════════════════════════════════════════

# ── ANIMATED BODY (no alpha — hard frame-swap, same technique as Eva) ──
# No Caelor float exists in any chapter yet, so this defaults to Eva's
# calm timing (10s cycle, single flap at the top of the loop). Retime
# to match whenever a caelor_float transform gets written into a script.
image caelor_body:
    "Caelor_Knight/Body_Anim_2_Caleor.png"
    pause 0.5
    "Caelor_Knight/Body_Anim_1_Caleor.png"
    pause 9.5
    repeat


# ── EYE BLINK LOOP (normal only — no shocked variant provided) ──
image caelor_eye_blink_normal:
    "Caelor_Knight/Eye/Open_Normal.png"
    pause 6.0
    "Caelor_Knight/Eye/Half_Normal.png"
    pause 0.08
    "Caelor_Knight/Eye/Closed.png"
    pause 0.08
    "Caelor_Knight/Eye/Half_Normal.png"
    pause 0.08
    "Caelor_Knight/Eye/Open_Normal.png"
    repeat


# ── THE LAYERED IMAGE ──
layeredimage caelor:
    group body:
        attribute idle default "caelor_body"

    group mouth:
        # No Neutral.png provided — "happy" is his resting default mouth,
        # same convention as Petra/Ansel.
        attribute happy default "Caelor_Knight/Mouth/Happy.png"
        attribute smile "Caelor_Knight/Mouth/Smile.png"
        attribute angry "Caelor_Knight/Mouth/Angry.png"
        attribute awed "Caelor_Knight/Mouth/Awed.png"
        attribute excited "Caelor_Knight/Mouth/Excited.png"
        attribute hmm "Caelor_Knight/Mouth/Hmm.png"
        attribute surprised "Caelor_Knight/Mouth/Surprised.png"

    group eyes:
        attribute normal default "caelor_eye_blink_normal"
        attribute closed "Caelor_Knight/Eye/Closed.png"

    group brows:
        attribute browneutral default "Caelor_Knight/Brow/Neutral.png"
        attribute browmad "Caelor_Knight/Brow/Mad.png"
        attribute browsad "Caelor_Knight/Brow/Sad.png"
