# Power BI Cheat Sheet

Quick reference for Power BI modeling, DAX, visuals, and best practices.

---

## Data Modeling Essentials

- Use a Star Schema (fact table and dimension tables).
- Avoid many-to-many relationships when possible.
- Mark your Date Table as the official date table.
- Hide foreign key columns in visuals (clean model).
- Use single-direction relationships unless needed.

---

## Common DAX Measures

```DAX
Total Sales = SUM(Sales[Amount])

Average Price = AVERAGE(Sales[Price])

Row Count = COUNTROWS(Sales)

Sales Last Year =
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR('Date'[Date])
)

Running Total =
CALCULATE(
    [Total Sales],
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)
```

---

## Filter Context vs Row Context

- Row Context: Calculated columns, iterators.
- Filter Context: Visuals, slicers, report filters.
- CALCULATE modifies filter context.

Example:

```DAX
High Sales Only =
CALCULATE(
    [Total Sales],
    Sales[Amount] > 1000
)
```

---

## Visualization Best Practices

- Use bar/column charts for comparisons.
- Use line charts for trends.
- Use cards for KPIs.
- Avoid pie charts unless 2–3 categories.
- Use consistent colors and spacing.
- Keep dashboards simple and readable.

---

## Power Query Essentials

- Remove Columns
- Filter Rows
- Change Data Type
- Split Column (by delimiter)
- Merge Queries (joins)
- Append Queries (stack tables)

ETL path:
Power Query → Load → Model → DAX → Visuals

---

## Performance Tips

- Reduce cardinality (remove unused columns).
- Prefer measures over calculated columns.
- Disable Auto Date/Time.
- Use SUMX/FILTER sparingly (row-by-row).
- Avoid bi-directional relationships unless required.

---

## Common Tasks

**Create a measure:**
Modeling → New Measure

**Create a relationship:**
Model View → Drag key to key

**Add a slicer:**
Insert → Slicer → Choose field

**Publish report:**
File → Publish → Power BI Service
