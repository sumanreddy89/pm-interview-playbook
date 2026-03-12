# Problem Diagnostic Framework

## What This Question Tests
Tests your ability to find the root cause of a product problem in a structured, exhaustive way — without jumping to conclusions.

## Evaluation Criteria
- What is your thought process when diagnosing a business problem?
- Are you logical?
- Are you exhaustive in listing possible causes?
- Articulate delivery?

---

## The Framework

### Step 1: Clarify
Make sure you understand what the interviewer is asking. Confirm the metric/problem and what a successful diagnosis looks like.

### Step 2: Narrow Down the Scope
Before hypothesizing, ask diagnostic questions to scope the problem:

| Question | Why It Matters |
|----------|---------------|
| **Size**: How large is the drop/problem? | Small fluctuations may be noise |
| **When**: When did it start? Sudden vs. gradual? | Points to an event or a slow-burning trend |
| **Where**: Which geography/region? | Isolates local vs. global cause |
| **Who**: Which user segment? New vs. returning? Organic vs. paid? | Isolates acquisition vs. retention |
| **Platform**: Mobile vs. desktop? iOS vs. Android? | Points to a technical issue |
| **Other metrics**: Did related metrics also drop? | Helps triangulate |

### Step 3: State Your Hypotheses
Based on the scoping answers, form 3–5 hypotheses covering both internal and external causes:

**Internal causes:**
- Recent product change, A/B test, or bug
- Infrastructure outage or performance degradation
- Pricing or packaging change
- Algorithm or ranking change
- Onboarding or funnel change

**External causes:**
- Competitor launched a new feature or promotion
- Seasonal effect (holidays, back-to-school, etc.)
- News event affecting user behavior
- Platform changes (iOS update, App Store policy, etc.)
- Macroeconomic shift

### Step 4: Validate / Eliminate Hypotheses
For each hypothesis, describe what data you'd look at to confirm or rule it out:
- Segment the data (cohort analysis, A/B test results, device breakdown)
- Check internal logs for recent changes/deploys
- Look at competitor news or industry reports
- Review support tickets for user complaints

### Step 5: Recommend Next Steps
Once you've identified the most likely root cause(s):
- What's the immediate mitigation (if any)?
- What's the longer-term fix?
- What monitoring would you put in place to detect this faster next time?

---

## Common Question Examples
- "You're the PM of Lime scooters. Signups are up but usage is down. What do you do?"
- "Facebook's DAU dropped 10% last week. Walk me through your diagnosis."
- "Instagram's ad click-through rate is declining. How do you investigate?"
- "App store ratings for [product] suddenly dropped from 4.2 to 3.5. What happened?"

## Coaching Tips
- Scoping before hypothesizing is the most common mistake to avoid — don't jump to solutions
- The best answers show *systematic elimination*, not just a list of possible causes
- Always address both internal and external causes — one-sided analysis misses half the picture
- End with a prioritized recommendation, not just an open-ended list
