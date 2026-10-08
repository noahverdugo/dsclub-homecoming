import pandas as pd

INPUT_FILE = "noaa_contiguous_us_annual_avg_temperature_2005_2025.csv"
GAME_FILE = "game_data.csv"

FILTER_SUM_COL = "Quantity"

df = pd.read_csv(INPUT_FILE)

# Filtering
# df = df[df["Data_item"] == "Total"]
# df[FILTER_SUM_COL] = pd.to_numeric(df[FILTER_SUM_COL], errors="coerce")
# df = df.groupby("Year", as_index=False)[FILTER_SUM_COL].sum()

print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}\n")

for col in df.columns:
    s = df[col]
    print(f"--- {col} ---")
    print(f"type: {s.dtype}")
    print(f"missing: {s.isna().sum()} ({s.isna().mean():.1%})")
    print(f"unique: {s.nunique(dropna=True)}")

    if s.nunique(dropna=True) > 0:
        examples = s.dropna().drop_duplicates().sample(
            min(5, s.nunique(dropna=True)),
            random_state=1
        ).tolist()
        print(f"examples: {examples}")

    if pd.api.types.is_numeric_dtype(s):
        print(f"range: {s.min()} - {s.max()}")

    print()

print("Potential year columns:")
for col in df.columns:
    numeric = pd.to_numeric(df[col], errors="coerce")
    if numeric.notna().mean() > 0.9 and numeric.between(1900, 2100).mean() > 0.9:
        print(f"  {col}")

print("\nPotential data columns:")
for col in df.columns:
    numeric = pd.to_numeric(df[col], errors="coerce")
    if numeric.notna().mean() > 0.9:
        print(f"  {col}")

print()
year_col, data_col = input(
    "Enter year and data columns (e.g. Year,Amount), or Ctrl-C to cancel: "
).split(",", 1)

year_col = year_col.strip()
data_col = data_col.strip()

source = df.copy()
game = pd.read_csv(GAME_FILE)

source[year_col] = pd.to_numeric(source[year_col], errors="coerce").astype("Int64")
game["Year"] = pd.to_numeric(game["Year"], errors="coerce").astype("Int64")
source[data_col] = pd.to_numeric(source[data_col], errors="coerce")

duplicates = source[source[year_col].duplicated(keep=False)].sort_values(year_col)

if len(duplicates):
    print("\nERROR: Multiple rows found for these years:")
    print(duplicates[[year_col, data_col]].to_string(index=False))
    print("\nAdd more filtering above so there is exactly one row per year.")
    raise SystemExit(1)

lookup = source.set_index(year_col)[data_col]
game[data_col] = game["Year"].map(lookup)
game[data_col] = game[data_col].round(3)

game.to_csv(GAME_FILE, index=False)

print(f"Added '{data_col}' to {GAME_FILE}")
print(f"Matched {game[data_col].notna().sum()} / {len(game)} years")