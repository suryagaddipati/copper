#!/usr/bin/env python3
"""
Create sample UFC dataset in DuckDB for testing Studio database connections.
This is a sample dataset - not hardcoded into the API.
"""
import duckdb
import pandas as pd
import os

def create_ufc_database():
    db_path = os.path.join(os.path.dirname(__file__), 'ufc_sample.db')
    
    conn = duckdb.connect(db_path)
    
    # Sample fighters data
    fighters_data = [
        {'fighter_id': 1, 'name': 'Jon Jones', 'weight_class': 'Light Heavyweight', 'wins': 26, 'losses': 1, 'draws': 0, 'nationality': 'USA'},
        {'fighter_id': 2, 'name': 'Khabib Nurmagomedov', 'weight_class': 'Lightweight', 'wins': 29, 'losses': 0, 'draws': 0, 'nationality': 'Russia'},
        {'fighter_id': 3, 'name': 'Amanda Nunes', 'weight_class': 'Bantamweight', 'wins': 22, 'losses': 5, 'draws': 0, 'nationality': 'Brazil'},
        {'fighter_id': 4, 'name': 'Israel Adesanya', 'weight_class': 'Middleweight', 'wins': 24, 'losses': 3, 'draws': 0, 'nationality': 'Nigeria'},
        {'fighter_id': 5, 'name': 'Valentina Shevchenko', 'weight_class': 'Flyweight', 'wins': 23, 'losses': 4, 'draws': 0, 'nationality': 'Kyrgyzstan'},
        {'fighter_id': 6, 'name': 'Conor McGregor', 'weight_class': 'Lightweight', 'wins': 22, 'losses': 6, 'draws': 0, 'nationality': 'Ireland'},
        {'fighter_id': 7, 'name': 'Ronda Rousey', 'weight_class': 'Bantamweight', 'wins': 12, 'losses': 2, 'draws': 0, 'nationality': 'USA'},
        {'fighter_id': 8, 'name': 'Anderson Silva', 'weight_class': 'Middleweight', 'wins': 34, 'losses': 11, 'draws': 0, 'nationality': 'Brazil'}
    ]
    
    # Sample fights data
    fights_data = [
        {'fight_id': 1, 'event_id': 1, 'fighter1_id': 1, 'fighter2_id': 4, 'winner_id': 1, 'method': 'Decision', 'round': 5, 'time': '5:00'},
        {'fight_id': 2, 'event_id': 1, 'fighter1_id': 2, 'fighter2_id': 6, 'winner_id': 2, 'method': 'Submission', 'round': 4, 'time': '3:04'},
        {'fight_id': 3, 'event_id': 2, 'fighter1_id': 3, 'fighter2_id': 5, 'winner_id': 3, 'method': 'TKO', 'round': 2, 'time': '4:33'},
        {'fight_id': 4, 'event_id': 2, 'fighter1_id': 7, 'fighter2_id': 3, 'winner_id': 3, 'method': 'KO', 'round': 1, 'time': '0:48'},
        {'fight_id': 5, 'event_id': 3, 'fighter1_id': 8, 'fighter2_id': 4, 'winner_id': 4, 'method': 'Decision', 'round': 3, 'time': '5:00'},
        {'fight_id': 6, 'event_id': 3, 'fighter1_id': 6, 'fighter2_id': 2, 'winner_id': 2, 'method': 'Submission', 'round': 4, 'time': '3:04'}
    ]
    
    # Sample events data
    events_data = [
        {'event_id': 1, 'name': 'UFC 285', 'date': '2023-03-04', 'location': 'Las Vegas, Nevada', 'venue': 'T-Mobile Arena'},
        {'event_id': 2, 'name': 'UFC 286', 'date': '2023-03-18', 'location': 'London, England', 'venue': 'O2 Arena'},
        {'event_id': 3, 'name': 'UFC 287', 'date': '2023-04-08', 'location': 'Miami, Florida', 'venue': 'Kaseya Center'}
    ]
    
    # Create DataFrames
    fighters_df = pd.DataFrame(fighters_data)
    fights_df = pd.DataFrame(fights_data)
    events_df = pd.DataFrame(events_data)
    
    # Create tables
    conn.execute("CREATE TABLE fighters AS SELECT * FROM fighters_df")
    conn.execute("CREATE TABLE fights AS SELECT * FROM fights_df")
    conn.execute("CREATE TABLE events AS SELECT * FROM events_df")
    
    print(f"UFC sample database created at: {db_path}")
    print("Tables created: fighters, fights, events")
    
    # Show sample data
    print("\nSample data:")
    print("Fighters:", conn.execute("SELECT COUNT(*) FROM fighters").fetchone()[0], "records")
    print("Fights:", conn.execute("SELECT COUNT(*) FROM fights").fetchone()[0], "records")
    print("Events:", conn.execute("SELECT COUNT(*) FROM events").fetchone()[0], "records")
    
    conn.close()
    return db_path

if __name__ == "__main__":
    create_ufc_database()