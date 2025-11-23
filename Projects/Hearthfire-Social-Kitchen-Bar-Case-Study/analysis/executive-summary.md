# Hearthfire Social Kitchen & Bar – Case Study Executive Summary

## Objective

This case study analyzes one week of operational and sales data for **Hearthfire Social Kitchen & Bar**, a fictional but realistic neighborhood restaurant and bar.

The goal is to show how a data analyst can:

- Turn raw POS and labor data into clear, visual stories  
- Identify drivers of **profitability, margin, and waste**  
- Translate findings into **specific, operational recommendations**

The analysis is intentionally built to resemble the kind of work a business-facing data analyst would present to owners or senior management.

---

## Data Sources

This project uses several small, focused datasets:

- **Item-level sales & margins**
  - Item name, category, food cost, sell price, quantity sold, margin %
- **Category-level sales mix**
  - Cocktails, beer, wine, entrées, apps, desserts, NA beverages
- **Sales + covers by daypart**
  - Happy Hour, Dinner, Late Night for each day of the week
- **Labor breakdown**
  - FOH, BOH, bar labor, total labor, and daily labor %
- **Weekly margin snapshot**
  - Total sales, food vs bar mix, waste cost, and overall margin %

These datasets are stored under `data/raw/` with human-friendly, formatted tables in `data/processed/`. Visuals are generated via Python (`/notebooks`) and saved to `/assets/images`.

---

## Key Findings

### 1. Bar program is the primary margin engine

- **Cocktails and wine** are the highest-margin categories and play an outsized role in overall profitability.  
- **NA beverages** also deliver strong margins but at lower volume.  
- Entrées (especially seafood and more complex dishes) show **lower margins** and higher prep complexity.

**Implication:** When the bar underperforms or lower-margin entrees dominate the mix, weekly profit erodes quickly.

---

### 2. Menu mix has a few quiet underperformers

- The **chef-driven halibut special** and **short rib gnocchi** underperform from a margin perspective and likely carry higher prep and waste risk.
- Items like the **smash burger** and **Citrus Cooler** provide strong value for guests while still offering solid margin and low complexity.

**Implication:** A small number of items are doing most of the heavy lifting for profit, while a few “hero” dishes quietly drag it down.

---

### 3. Daypart performance is uneven

- **Dinner** is the strongest daypart for both sales and covers;  
- **Happy Hour** offers strong volume and is a key feeder to dinner;  
- **Sunday Late Night** is consistently soft, with low sales relative to labor and prep.

**Implication:** There is upside in tightening underperforming dayparts and using promotions more strategically to extend high-value ones.

---

### 4. Labor and waste are misaligned on certain days

- **Friday** delivers strong sales and margin, with labor reasonably in line.
- **Saturday and Sunday** show higher **waste cost** relative to sales, suggesting over-prep (especially on seafood specials) and potentially misaligned staffing.
- Labor % spikes on **Sunday**, where sales don’t justify the same staffing pattern as earlier in the week.

**Implication:** Even with healthy topline sales, labor and waste can quietly erode weekly profitability if they aren’t tuned to realistic demand.

---

### 5. Operational discipline + targeted promos = upside

Across the week, the data suggests:

- Tighter control of **prep, recipe adherence, and training** can reduce waste.  
- Well-designed **bar + food pairings** can protect margin while still feeling like a win for guests.  
- Small shifts in **staffing and scheduling** (especially weekends and late nights) can move labor % in the right direction without harming service.

---

## Recommended Focus Areas

1. **Optimize the bar program**  
   - Lean into cocktails and high-margin beverages as a core profit driver.  
   - Avoid pairing low-margin entrees with discounted drinks.

2. **Engineer the menu mix**  
   - Reposition or adjust pricing on low-margin dishes (halibut, gnocchi).  
   - Promote high-margin anchors like cocktails, desserts, and select “value” entrées.

3. **Tune labor and prep for weekends**  
   - Stagger BOH and bar staffing on Saturday and Sunday.  
   - Align prep volumes with realistic demand, particularly on short-shelf-life items.

4. **Reshape daypart strategy**  
   - Strengthen **Tuesday Dinner** and **Thursday Late Night** via targeted specials.  
   - Consider trimming or rethinking **Sunday Late Night** service.

The rest of this folder (`insights-and-findings.md` and `recommendations.md`) goes deeper into each area, pairing the visuals with narrative and concrete next steps.

