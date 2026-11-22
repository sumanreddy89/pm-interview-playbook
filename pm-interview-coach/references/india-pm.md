# India PM Interviews

## What This Covers
PM interviews at companies building for Indian users use the same question types as everywhere else (product design, metrics, estimation, prioritization, strategy), but a strong answer has to show you understand who the user actually is and what constraints shape the product. Interviewers notice quickly when an answer assumes a US user with a new iPhone, unlimited data and a credit card.

Use this alongside the framework for the question type. It adds the India context; it doesn't replace the structure.

## Evaluation Criteria (on top of the question's own)
- **User realism**: Do you segment Indian users meaningfully (by city tier, language, device, income, digital familiarity) instead of treating "India" as one market?
- **Constraint awareness**: Do you design for low-end Android, patchy or metered data, shared devices, and payment and trust habits?
- **Market mechanics**: Do you know how distribution, payments, regulation and seasonality work here, and use them in the answer?
- **Judgment on scale vs. depth**: Do you know when a mass-market approach is right and when a premium, metro-first wedge is?

---

## Context to Bring Into Any Answer

### 1. Segment by more than age
- **City tier**: metros, tier-2 and tier-3 cities and rural areas differ in income, delivery reach, language and trust in online transactions.
- **Language**: many first-time internet users prefer their own language over English. Vernacular UI, voice input and local-language content can change adoption more than features do.
- **Device and data**: entry-level Android phones with little storage and RAM, prepaid data plans, and frequent switching between Wi-Fi and mobile data. App size, offline behaviour and data use are product decisions.
- **Digital familiarity**: a first-time user of digital payments needs reassurance and recovery paths that a power user doesn't.
- **Shared devices and households**: one phone may serve a family; decisions are often made by someone other than the user.

### 2. Payments and trust
- **UPI** is the default rail for small digital payments; design flows around it (collect requests, mandates for recurring payments, QR at the counter) and its failure modes (pending transactions, bank downtime).
- **Cash on delivery** and **pay later** options still matter for first purchases in many segments; they carry cost (returns, fraud, cash handling) you should name.
- **Trust signals**: refunds that visibly work, local-language support, and recommendations from people they know often outweigh discounts.

### 3. Distribution and growth
- **Referral and word of mouth** through messaging apps and local communities, and **assisted** channels (a local shopkeeper or agent helping someone onboard), often beat paid acquisition outside metros.
- **Seasonality**: festive seasons, sale events and big cricket tournaments shift demand, traffic and acquisition costs. Plan launches and capacity around them.

### 4. Regulation and compliance (name it, don't lecture)
Payments, lending, insurance, fantasy and real-money games, health and data handling are regulated, and rules change. In an answer, say where a regulator or a compliance requirement would shape the design (KYC steps, data storage rules, age gates, disclosures) and that you'd confirm current rules with legal. Don't quote specifics you aren't sure of.

### 5. Unit economics are tighter
Average order values and willingness to pay are often lower, so CAC, delivery cost, payment cost and returns can sink a model that works elsewhere. Show the arithmetic (see `pricing.md`).

---

## How to Use It in Each Question Type
| Question type | Add this |
|---|---|
| Product design / improve | Pick a specific segment (for example "first-time smartphone users in tier-3 towns who prefer Hindi"), state their constraints, and let those drive the design: language, offline, low data, assisted onboarding, trust and recovery |
| Metrics | Include trust and failure metrics: payment success rate, refund turnaround, support contacts per order, and segment cuts by city tier and language |
| Estimation | Clarify scope (urban vs. all-India), segment the population before multiplying, and sanity-check against a second route. Look up current published figures where you can; say which numbers are assumptions |
| Prioritization | Weigh reach across segments against depth in one; a feature for metro power users and one for new users rarely score the same |
| Strategy / market entry | Metro-first wedge vs. mass market, distribution partners, regulation, and whether unit economics survive outside the top cities |

---

## Practice Questions (generic cases)
- "Design a voice-first ordering experience for a neighbourhood grocery app aimed at first-time smartphone users."
- "A payments app's UPI success rate dropped 3 points this week. Diagnose it."
- "What metrics would you track for a new 'split the bill' feature in a UPI payments app?"
- "Estimate the number of UPI payments made at small shops in a city of 2 million people on a typical day."
- "A fantasy sports app wants to launch a new contest format for casual players. How do you decide whether to build it, and how would you measure it?"
- "How would you price a subscription for a regional-language streaming app?"
- "Should a metro-only quick-commerce app expand to tier-2 cities? What would you need to believe?"
- "Prioritize: offline mode for the app, or a regional-language UI?"

## Coaching Tips
- Name the segment and its constraints in the first minute; it shows you know who you're building for.
- Make constraints design inputs, not footnotes: "because many of these users are on prepaid data, the catalogue loads text first and images on tap."
- Show the money: one line of unit economics often separates a senior answer from a good one.
- Don't stereotype. "Tier-3 users" aren't one group either; say what you'd research and how.
- A worked strong answer for the split-the-bill metrics question is in `examples/metrics-split-the-bill.md`.
