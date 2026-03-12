# Estimation Framework

## What This Question Tests
Back-of-the-envelope estimation. Tests whether you can decompose a complex unknown into manageable components, make reasonable assumptions, and arrive at a defensible ballpark number.

## Evaluation Criteria
- Are you logical and structured?
- Do you explain your assumptions clearly?
- Are you organized in your work?
- Are you comfortable with numbers and arithmetic?
- Do you do a sanity check at the end?

---

## Framework #1: Top-Down Equation

**When to use:** When you can write a clean equation that breaks into estimable components.

### Steps:
1. **Ask clarifying questions** — scope the estimate (US vs. world? Monthly vs. annual? etc.)
2. **Write an equation** — express the thing you're estimating as a product/sum of components
3. **Break down the equation** — decompose into sub-components you can estimate using general knowledge or proxy data
4. **Do the math** — aggregate to get the final number
5. **Sanity check** — does the result make intuitive sense? Check from a different angle

**Example:** "How many YouTube videos are uploaded per day?"
- Equation: `# creators × # videos/creator/day`
- Break down: creators = 10% of eligible US population (age 20–65) = ~17M
- Estimate: 0.5 videos/creator/day → 8.5M videos/day
- Sanity check: that's ~160 min/creator/day uploading, which seems high → revise to ~4M

---

## Framework #2: Intermediate Value / Anchor

**When to use:** When you know an intermediate quantity well and can build from there.

### Steps:
1. **Identify an intermediate value** you know (e.g., # pianos in a city)
2. **List the other things you need** to connect it to the answer
3. **Make calculations** using your intermediate value as the anchor
4. **Sanity check**

**Example:** "How many piano tuners are in Chicago?"
- Anchor: estimate # of pianos in Chicago from household penetration
- Bridge: each piano tuned once/year; each tuner works ~250 days/year
- Divide total tuning hours needed by hours per tuner

---

## General Tips
- **Round aggressively**: use round numbers (300M not 330M US population)
- **Use proxy data**: "a 20-min 4K video takes about 20 min to upload" — use what you know
- **Narrate your assumptions** as you go — the interviewer is evaluating your reasoning, not the number
- **Order of magnitude is fine** — being off by 2x is usually acceptable; being off by 100x is not
- **Bracket your estimate**: give a range if helpful ("somewhere between 2M and 5M")

## Common Question Examples
- "How many gas stations are in the US?"
- "Estimate Facebook's mobile ad revenue."
- "How many piano tuners are in Chicago?"
- "How many YouTube videos are uploaded per day?"
- "What's the market size for [product] in [city]?"
- "How many iPhones does Apple sell per day?"

## Coaching Tips
- Always clarify scope first — US vs. world, daily vs. annual changes your equation dramatically
- If you get stuck, pick a related quantity you know and work from there
- Show your work explicitly — write out the equation before plugging in numbers
- Don't be afraid to revise your estimate if the sanity check reveals an obvious error
