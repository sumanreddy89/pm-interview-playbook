# Metrics Framework

## What This Question Tests
Tests your ability to define the most critical metrics to track a product's success, and to diagnose where problems lie when performance dips.

## Evaluation Criteria
- **Analytical**: Are you structured and logical?
- **Product goal**: Do you identify what the goal of the product is before picking metrics?
- **Metrics**: Do you specify the most important things to measure and explain your reasoning?
- **Communication**: Clear and succinct?

---

## The Two-Set Metrics Framework

### Step 1: Explain Your Approach
Tell the interviewer upfront: "I define two sets of metrics — *goal metrics* that measure success toward the product goal, and *health metrics* that measure the health of acquisition, engagement, and retention."

### Step 2: Define the Product Goal
Infer what user problem the product solves, then reframe as a product goal.
> Example: "Zillow connects agents and buyers/renters to transact on properties. The product goal is to help agents and buyers/renters find each other to complete transactions."

### Step 3: Define Goal Metrics
Three types:
- **North Star Metric** — the single metric that best measures success toward the product goal (e.g., # of successful transactions/month)
- **Counter Metrics** — measure anything that works *against* the product goal (e.g., # of fraudulent listings — prevents trust erosion)
- **Guardrail Metrics** — business thresholds that, if crossed, should trigger a review (e.g., cost per acquisition must stay below $X)

### Step 4: Define Health Metrics
Organized around the user funnel:
- **Acquisition**: How are users finding the product? (e.g., # new sign-ups/week, CAC)
- **Engagement**: Are users getting value from the product? (e.g., DAU/MAU ratio, session length, # key actions/user)
- **Retention**: Are users coming back? (e.g., D7/D30 retention rate, churn rate)

---

## Diagnosing a Metric Drop
If a key metric drops, work through this sequence:
1. **Scope it**: How big is the drop? When did it start? Is it global or regional? Mobile or desktop?
2. **Funnel analysis**: Which stage of the funnel shows the drop? (Acquisition → Activation → Engagement → Retention)
3. **Internal causes**: Recent product changes, bugs, A/B tests, infra issues?
4. **External causes**: Competitor actions, seasonality, market trends, PR events?
5. **Hypothesis & validation**: State your top 2–3 hypotheses and how you'd validate each

---

## Common Question Examples
- "What metrics would you use to measure success for [product]?"
- "Instagram's likes are down 10% week-over-week. What do you do?"
- "How would you set up metrics for a new feature?"
- "What's your North Star metric for Spotify/Airbnb/LinkedIn?"

## Coaching Tips
- Always define the product goal *before* naming metrics — metrics without context are meaningless
- The North Star metric should reflect actual user value, not a vanity metric (e.g., "songs listened to completion" > "songs started")
- Counter metrics prevent gaming the North Star at the expense of user experience
- When diagnosing drops, resist jumping to conclusions — scope first, then hypothesize
