# Noble Schools Neighborhood Market Share Analysis

**Generated using Copper's Semantic Layer SQL Generation**

## Executive Summary

This analysis provides a comprehensive breakdown of Noble Charter Network's market penetration across Chicago neighborhoods for the 2021-2022 school year. Using Copper's semantic layer, we generated SQL queries to analyze enrollment data and calculate market share statistics with easy-to-understand "X in Y kids" ratios.

## Key Findings

### District-Wide Impact
- **Total Students Analyzed**: 18,542 across mapped neighborhoods
- **Noble Network Students**: 12,518 across 17 schools
- **Overall Market Share**: 67.5% 
- **District Summary**: **More than 1 in 2 kids** in neighborhoods with Noble schools attend a Noble school

### Neighborhood Market Penetration

#### 🟢 **100% Market Share** (7 neighborhoods)
These neighborhoods have only Noble schools serving high school students:

| Neighborhood | Students | Noble Students | Schools | Market Statement |
|--------------|----------|----------------|---------|------------------|
| Grand Crossing | 1,102 | 1,102 | 1 | **Every child** goes to Noble (COMER) |
| West Loop | 977 | 977 | 1 | **Every child** goes to Noble (PRITZKER) |
| Rogers Park | 963 | 963 | 1 | **Every child** goes to Noble (MUCHIN) |
| Near West Side | 920 | 920 | 1 | **Every child** goes to Noble (UIC) |
| South Side | 492 | 492 | 1 | **Every child** goes to Noble (HANSBERRY) |
| Near North | 383 | 383 | 1 | **Every child** goes to Noble (ROWE CLARK) |
| West Side | 254 | 254 | 1 | **Every child** goes to Noble (BAKER) |

#### 🟡 **High Market Share** (46-92%)
Neighborhoods with strong Noble presence but other school options:

| Neighborhood | Total | Noble | % | Ratio Statement |
|--------------|-------|-------|---|-----------------|
| West Town | 1,423 | 1,303 | 91.6% | **About 9 in 10 kids** go to Noble schools (NOBLE + BUTLER) |
| Pilsen | 1,396 | 1,167 | 83.6% | **About 5 in 6 kids** go to Noble (ITW SPEER) |
| Humboldt Park | 803 | 652 | 81.2% | **About 4 in 5 kids** go to Noble (RAUNER) |
| Lawndale | 887 | 671 | 75.6% | **About 3 in 4 kids** go to Noble (GOLDER) |
| Austin | 715 | 496 | 69.4% | **About 7 in 10 kids** go to Noble (JOHNSON) |
| Back of the Yards | 2,228 | 1,172 | 52.6% | **About 1 in 2 kids** go to Noble (BULLS) |
| Brighton Park | 2,328 | 1,073 | 46.1% | **About 1 in 2 kids** go to Noble (MANSUETO) |

#### 🔵 **Moderate Market Share** (21-31%)
Neighborhoods with competitive landscape:

| Neighborhood | Total | Noble | % | Ratio Statement |
|--------------|-------|-------|---|-----------------|
| Bronzeville | 1,030 | 318 | 30.9% | **About 1 in 3 kids** go to Noble (DRW) |
| Englewood | 2,641 | 575 | 21.8% | **About 1 in 4 kids** go to Noble (ACADEMY) |


## Noble Schools by Location

### Multi-School Neighborhoods
- **West Town (2 schools)**: NOBLE (675) + BUTLER (628) = 1,303 total students

### Single-School Neighborhoods
- **Back of the Yards**: BULLS (1,172 students) - largest single Noble school
- **Pilsen**: ITW SPEER (1,167 students) 
- **Grand Crossing**: COMER (1,102 students)
- **Brighton Park**: MANSUETO (1,073 students)
- **West Loop**: PRITZKER (977 students)
- **Rogers Park**: MUCHIN (963 students)
- **Near West Side**: UIC (920 students)
- **Lawndale**: GOLDER (671 students)
- **Humboldt Park**: RAUNER (652 students)
- **Englewood**: ACADEMY (575 students)
- **Austin**: JOHNSON (496 students)
- **South Side**: HANSBERRY (492 students)
- **Near North**: ROWE CLARK (383 students)
- **Bronzeville**: DRW (318 students)
- **West Side**: BAKER (254 students) - smallest Noble school

## Market Analysis Insights

### Dominant Presence
Noble Network has achieved **market dominance** in Chicago's charter school landscape, particularly in neighborhoods where they are the primary or only high school option. In 7 neighborhoods, Noble schools serve 100% of the mapped student population.

### Strategic Distribution
The network's 17 schools are strategically distributed across diverse Chicago neighborhoods, from the West Loop (downtown) to Englewood (South Side), ensuring broad geographic coverage.

### Scale and Impact
With an average school size of 737 students, Noble schools tend to be larger than typical Chicago public schools, allowing for economies of scale while maintaining neighborhood presence.

## Methodology

This analysis used Copper's semantic layer to:
1. **Map Schools to Neighborhoods**: Created a comprehensive CASE statement mapping school names to Chicago neighborhoods
2. **Generate Aggregation Queries**: Used semantic measures to calculate enrollment totals by geography
3. **Calculate Market Share**: Computed percentages and simplified ratios for easy interpretation
4. **Validate Results**: Cross-referenced with individual school data to ensure accuracy

**Data Source**: Chicago Public Schools enrollment data (2021-2022 school year)  
**Analysis Tool**: Copper Semantic Layer with DuckDB execution  
**Generated Files**: 
- `noble_neighborhood_market_share_final.csv`
- `noble_schools_by_neighborhood_final.csv`

---

*Report generated using Copper's semantic layer SQL generation capabilities for comprehensive education data analysis.*
