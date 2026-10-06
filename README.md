# Data Science Club homecoming: correlation game

Two laptops on the table:

1. **Wheel laptop.** Open [wheelofnames.com](https://wheelofnames.com) and put in 10 variable names? The player spins.
2. **Game laptop.** Run this page. Tap the variable the wheel landed on, then tap the variable they think is most correlated with it. The page shows the scatterplot, the correlation, and whether they won a prize!!

The strongest match is the big prize. Second strongest is the small prize.

## Run the game laptop

In this folder, double-click `start.bat`, or run:

```bash
python -m http.server 8000
```
Then open http://localhost:8000.

Where the numbers were scraped:

- **Shark attacks:** worldwide unprovoked bites from the International Shark Attack File at the Florida Museum of Natural History.
- **Ice cream consumption:** USDA Economic Research Service, regular ice cream, pounds per person, rounded to one decimal.
- **Nic Cage movie releases:** films he acted in that year, from the Wikipedia filmography. Producer-only credits and TV are not counted.
- **Drowning deaths:** US unintentional drowning deaths from CDC. 2005–2010 are from NCHS Data Brief 149. 2011–2016 are unintentional drowning deaths from the NCHS Injury Mortality dataset (that table counts drowning separately from boating, so those years sit a bit lower). 2019–2022 are from CDC MMWR. 2023 is the WISQARS all-ages total. 2017, 2018, and 2024 are still the original numbers because those exact CDC tables were not available here.
