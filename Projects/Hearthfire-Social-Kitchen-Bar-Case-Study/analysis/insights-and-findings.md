# Hearthfire Social Kitchen & Bar – Insights & Findings

This document walks through the main insights behind the visuals and tables in this case study. It is written as if presenting to ownership or senior leadership.

---

## 1. Category & Item Mix

**Related files:**

- Data: `data/raw/item_sales_by_category.csv`  
- Clean table: `data/processed/item_sales_by_category_clean.md`  
- Visual: `/assets/images/category_sales_mix.png`

### 1.1 Category-level story

The category chart shows:

- **Cocktails**: High sales and strong margins; clear margin engine.
- **Wine**: Lower volume than cocktails but still a meaningful, high-margin contributor.
- **Beer**: Reliable but lower-margin; adds stability rather than profit spikes.
- **Entrées**: Main revenue driver in dollars, but margin % varies widely by item.
- **Apps & Desserts**: Solid margins; apps help open checks, desserts close them.
- **NA Beverages**: Very high margin, low complexity; ideal for value pairings.

**Takeaway:** The bar (especially cocktails) and certain simple food categories are doing most of the profitability work. Menu strategy should protect and amplify these.

---

### 1.2 Item-level findings

Looking at item-level data:

- **Charred Sourdough & Whip**, **Crispy Brussels & Bacon**, and the **Smash Burger** deliver attractive margins while remaining approachable and easy to execute.
- The **halibut special** and **short rib gnocchi** sit at the **lower end of margin** for entrées and are likely:
  - More labor-intensive  
  - More vulnerable to waste due to prep complexity and perishability

Meanwhile:

- **Zero-Proof Citrus Cooler** and similar NA drinks carry **very high margins** and low execution risk.

**Takeaway:** A handful of lower-margin “hero” dishes risk dragging down profit if they’re not balanced by high-margin accompaniments and disciplined prep.

---

## 2. Daypart & Weekly Performance

**Related files:**

- Data: `data/raw/sales_covers_by_daypart.csv`  
- Clean table: `data/processed/sales_covers_by_daypart_clean.md`  
- Visual: `/assets/images/daypart_sales.png`

### 2.1 Daypart behavior

Across the week:

- **Dinner** is the primary sales and cover engine.  
- **Happy Hour** performs well, especially mid-week and Friday, and seems to be an effective funnel into dinner.  
- **Late Night** is highly variable:
  - Stronger on **Thursday and Friday**
  - Weakest on **Sunday**, where late-night volume is too low to justify the labor and prep.

**Takeaway:** The business is clearly dinner-centric, with Happy Hour as a strong acquisition channel. Late Night should be treated surgically, not as a default.

---

### 2.2 Weekday vs weekend dynamics

Using total sales and covers by day:

- **Friday** is the strongest overall day – high covers, strong bar sales, and good margin.
- **Saturday** also delivers strong sales but sees higher waste and a small margin drop.
- **Sunday** shows weaker sales and a spike in labor %, especially given its quieter late night.

**Takeaway:** Friday is a model of how the operation should work. Saturday and Sunday need tuning around prep, waste, and staffing.

---

## 3. Labor vs Sales

**Related files:**

- Data: `data/raw/labor_breakdown.csv`  
- Clean table: `data/processed/labor_breakdown_clean.md`  
- Visual: `/assets/images/labor_breakdown.png`

### 3.1 Labor mix overview

Across the week:

- **FOH and BOH labor** trend reasonably with sales, but:
  - **Friday** handles the highest volume with respectable labor %.  
  - **Sunday** has a noticeably higher labor % despite lower sales.
- **Bar labor** becomes critical on high-volume days: when less-experienced bartenders are paired together, throughput slows and check averages risk dropping.

**Takeaway:** Labor isn’t dramatically broken, but there is hidden inefficiency on Sunday and vulnerability when bar staffing skews inexperienced.

---

### 3.2 Operational implications

- Sundays appear **over-staffed** relative to revenue, particularly in BOH and possibly FOH.
- There is likely **“clock creep”** (employees clocking in early or staying late) and/or prep habits that don’t reflect actual Sunday demand.
- When newer bartenders are paired together on busy nights, bar sales may not reach their full potential.

**Takeaway:** Tightening schedule planning and enforcing clock-in/clock-out discipline would reduce labor % without harming service quality.

---

## 4. Waste & Margin

**Related files:**

- Data: `data/raw/weekly_margin_snapshot.csv`  
- Clean table: `data/processed/weekly_margin_snapshot_clean.md`  
- Visuals:
  - `/assets/images/weekly_margin_snapshot.png`
  - `/assets/images/weekly_margin_trend.png` (if created)

### 4.1 Margin behavior

The weekly snapshot shows:

- Overall **margin % is healthy**, but:
  - **Saturday** and **Sunday** see higher waste costs relative to sales.
  - Friday performs best: strong sales, high bar mix, and controlled waste.

### 4.2 Waste patterns

Given the menu and narratives:

- Waste is likely concentrated in:
  - **Seafood specials** (short shelf life, higher cost)  
  - Complex prep items (e.g., braised or longer-cook dishes)
- Over-prep on Saturdays appears to spill into **extra waste on Sunday**, especially if Sunday sales do not match the assumed volume.

**Takeaway:** Profit is most at risk when high-cost ingredients are prepped aggressively for Saturday and don’t fully sell through, forcing Sunday waste.

---

## 5. Guest & Behavior Insights

Although this is a small, constructed dataset, several behavioral patterns still emerge:

1. **Tourist vs local behavior**
   - Tourists likely spike on weekends, skewing toward “try it once” entrées and specials.
   - Locals (weekday regulars) are more likely to respond to Happy Hour deals and repeatable favorites.

2. **Value-seeking guests**
   - Combos like a **Smash Burger + Citrus Cooler** deliver a strong value perception while still protecting margin.
   - These pairings can be used to “carry” lower-margin dishes elsewhere on the menu.

3. **Engagement leverage points**
   - Happy Hour is a prime moment to nudge guests into higher-margin cocktails and to extend their stay into dinner.
   - A small set of well-designed promos can redirect behavior without resorting to across-the-board discounting.

---

## 6. Summary of Main Analytical Insights

1. **Bar program drives margin** – cocktails, wine, and NA beverages are profit levers.  
2. **Certain entrées underperform** – halibut and gnocchi in particular need scrutiny.  
3. **Daypart performance is uneven** – Sunday Late Night is a clear drag; Tuesday Dinner underperforms potential.  
4. **Labor is mostly fine but leaky** – especially on Sunday and when newer bar staff are paired together.  
5. **Waste erodes weekend margins** – especially around seafood and complex specials.

The recommendations document translates these insights into concrete next steps, with suggested metrics to track impact over time.
