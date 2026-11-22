# Worked answer: metrics for a "split the bill" feature

**Question:** "What metrics would you track for a new 'split the bill' feature in a UPI payments app?"
**Level:** PM. **Frameworks:** `metrics.md`, `india-pm.md`. **Rubric:** `rubric.md`.

The company and feature are generic examples, not a real product. The answer below is what a strong (3–4) answer sounds like spoken aloud: about 470 words, roughly four minutes. The notes on the right of each part say what it's doing and how the rubric would score it.

---

## The answer

**1. Approach.** "I'll start with why the app would build this, then a North Star metric, two or three supporting metrics, and guardrails that would tell us the feature is hurting something. Then I'll say how I'd cut the data, and how I'd know the feature itself caused any change."

> *Structure 4: signposts the plan and follows it.*

**2. Goal.** "Splitting a bill today usually means one person pays and then chases friends over chat, often for days. For the app, the feature does two things: it creates more payments between people who already use the app, and it brings in friends who don't, because they receive a request. So the goal is to make settling shared costs effortless, which should grow both payment frequency and new users through requests."

> *Business judgment 3: ties the feature to engagement and to acquisition through requests. User insight 3: a specific, painful problem.*

**3. Who.** "I'd focus first on groups of friends and flatmates in cities who split costs often, such as rent, food delivery and trips. They have the most repeat use. I'd watch first-time UPI users separately, because a request is often their first transaction, and a bad first experience there costs us a user."

> *User insight 4: picks a segment for a reason and spots the first-time-user risk most answers miss.*

**4. North Star.** "Splits fully settled per week: a split where everyone has paid their share. Not splits created, because creating a split is easy and tells us nothing if people never pay. 'Fully settled' captures the whole job."

> *Metrics 4: chooses an outcome over an activity metric and says why.*

**5. Supporting metrics.**
- "**Time to settle:** median hours from creating a split to the last payment. Faster means less chasing, which is the problem we set out to fix."
- "**Request conversion:** the share of requests paid within 48 hours, cut by whether the payer is an existing user or new."
- "**New users from requests:** people who install or sign up to pay a request and make another payment within 30 days. This is the acquisition case, and the 30-day part stops us counting one-off installs."

> *Metrics 3: each one maps back to the goal; the 30-day condition is a sensible quality bar.*

**6. Guardrails.**
- "**Payment success rate** for split payments versus normal ones. If UPI failures or pending payments are higher here, users blame the feature and the app."
- "**Request spam and reports:** blocks, 'mark as spam' and support contacts per thousand requests. People shouldn't feel nagged for money; friendships matter more than a feature."
- "**Disputes and wrong-amount payments**, because splitting adds arithmetic and room for mistakes."
- "**Overall payments per user,** to check splits add payments rather than move existing ones into a new flow."

> *Metrics 4: guardrails cover reliability, social harm and cannibalisation. Prioritization and trade-offs 3: names what could go wrong and why it matters.*

**7. Cuts and causality.** "I'd cut everything by city tier, language and new versus existing users, because a request's first impression matters most for new users. To know the feature caused a change, I'd launch to a random share of users and compare their payments per week and 30-day retention with a holdout group, rather than trusting a before-and-after chart in festive season."

> *Metrics 4: plans for attribution and names seasonality as a confounder.*

**8. Wrap-up.** "So: fully settled splits per week as the North Star; time to settle, request conversion and retained new users as supporting metrics; payment success, spam reports, disputes and total payments as guardrails, all measured against a holdout."

> *Communication 4: a crisp summary that lands the recommendation.*

---

## Why this scores well, and what would make it better

**Overall: strong for PM (mostly 3s and 4s).** It starts from the user's problem, picks a segment for a reason, chooses an outcome metric over an activity metric, covers failure modes specific to payments, and plans for causality.

**To push it further:** give a target ("a median time to settle under 24 hours in the first month, from a baseline we'd measure in a pilot"), and say which single metric would make you pull the feature if it went the wrong way (here, payment success rate for split payments).

**Common weaker versions:**
- **Weak (1s and 2s):** "Number of splits created, DAU and MAU." Activity metrics, no goal, no guardrails.
- **Middling (2s, one 3):** a good North Star and goal, but no guardrails and no segment, and it ends with "if these go up, it's working".

This answer is also used as a calibration benchmark in `pm-interview-coach/evals/`.
