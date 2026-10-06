# Data Science Club homecoming: correlation game

Two laptops on the table.

1. **Wheel laptop.** Open [wheelofnames.com](https://wheelofnames.com) and put in the four variable names from `game_data.csv`: Shark attacks, Ice cream consumption, Nic Cage movie releases, and Drowning deaths. The player spins.
2. **Game laptop.** Run this page. Tap the variable the wheel landed on, then tap the variable they think is most correlated with it. The page shows the scatterplot, the correlation, and whether they won.

The strongest match (largest correlation, ignoring the minus sign) is the big prize. Second strongest is the small prize.

## Run the game laptop

In this folder, double-click `start.bat`, or run:

```bash
python -m http.server 8000
```

Then open http://localhost:8000.

The page reads `game_data.csv`. To add another variable later, add a column. The buttons come from that file. It shows up to five choices besides the wheel variable. Right now there are only four variables, so it shows the other three.

## How members get the code

The repo is already on GitHub: https://github.com/noahverdugo/dsclub-homecoming

Members clone it, edit `game_data.csv` or `index.html`, and push. If the repo is private, invite them as collaborators from the GitHub page. A public repo is enough for the club to clone it. The game itself stays on the laptop at the table. You do not need to host a website.

## Where the numbers came from

Same four columns, same years. Values that did not match a published source were replaced.

- **Shark attacks:** worldwide unprovoked bites from the International Shark Attack File at the Florida Museum of Natural History.
- **Ice cream consumption:** USDA Economic Research Service, regular ice cream, pounds per person, rounded to one decimal.
- **Nic Cage movie releases:** films he acted in that year, from the Wikipedia filmography. Producer-only credits and TV are not counted.
- **Drowning deaths:** US unintentional drowning deaths from CDC. 2005–2010 are from NCHS Data Brief 149. 2011–2016 are unintentional drowning deaths from the NCHS Injury Mortality dataset (that table counts drowning separately from boating, so those years sit a bit lower). 2019–2022 are from CDC MMWR. 2023 is the WISQARS all-ages total. 2017, 2018, and 2024 are still the original numbers because those exact CDC tables were not available here.
