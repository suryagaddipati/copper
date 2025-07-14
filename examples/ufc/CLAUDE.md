# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a UFC fight prediction project using Python for data analysis and machine learning. The project contains comprehensive UFC fight data and is set up for building predictive models.

## Project Structure

- `ufc_fights_all.csv`: Complete UFC fight dataset with fighter statistics, odds, and match results
- `fighter-features.txt`: Detailed feature engineering specification for UFC fighters
- `explore.py`: Data exploration script using pandas
- `pyproject.toml`: Project configuration with dependencies
- `uv.lock`: Dependency lock file

## Environment Setup

This project uses `uv` as the package manager. Key commands:
- `uv sync` - Install dependencies and sync environment
- `uv run python explore.py` - Run data exploration script
- `uv run python <script>` - Run any Python script in the project environment

## Data Architecture

The main dataset (`ufc_fights_all.csv`) contains:
- Fight metadata (event, date, location, venue, weight class)
- Fighter information (height, weight, reach, stance, age, records)
- Fight statistics (significant strikes, takedowns, submissions)
- Historical performance metrics (wins, losses, streaks, finishes)
- Betting odds and rankings
- Fight outcomes and finish details

The dataset spans from UFC 1 (1993) to current events with comprehensive fighter statistics.

## Feature Engineering Framework

The `fighter-features.txt` file defines a comprehensive feature engineering approach with 10 major categories:
1. Fighting style features (stance, wrestling background)
2. Ground game strength metrics
3. Striking capabilities and statistics
4. Physical attributes and advantages
5. Experience and career metrics
6. Recent form and momentum indicators
7. Durability and conditioning scores
8. Skill versatility measures
9. Mental and strategic factors
10. Opponent-specific matchup features

## Development Dependencies

- **pandas**: Primary data manipulation library
- **numpy**: Numerical computing support
- Python 3.9+ required