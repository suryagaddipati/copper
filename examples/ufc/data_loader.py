#!/usr/bin/env python3
"""
UFC Data Loader Utility

Loads UFC CSV data into Pandas DataFrames for use with Copper semantic models.
"""

import pandas as pd
from pathlib import Path
from typing import Dict, Any


class UFCDataLoader:
    """Utility class for loading UFC data from CSV files."""
    
    def __init__(self, data_dir: str = None):
        """Initialize the data loader.
        
        Args:
            data_dir: Directory containing UFC CSV files. Defaults to current directory's data/ folder.
        """
        if data_dir is None:
            data_dir = Path(__file__).parent / "data"
        self.data_dir = Path(data_dir)
    
    def load_events(self) -> pd.DataFrame:
        """Load UFC events data."""
        events_file = self.data_dir / "ufc_events.csv"
        if not events_file.exists():
            raise FileNotFoundError(f"Events file not found: {events_file}")
        
        df = pd.read_csv(events_file)
        df['event_date'] = pd.to_datetime(df['event_date'])
        return df
    
    def load_fighters(self) -> pd.DataFrame:
        """Load UFC fighters data."""
        fighters_file = self.data_dir / "ufc_fighter_details.csv"
        if not fighters_file.exists():
            raise FileNotFoundError(f"Fighters file not found: {fighters_file}")
        
        df = pd.read_csv(fighters_file)
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])
        
        # Calculate age
        df['age'] = (pd.Timestamp.now() - df['date_of_birth']).dt.days / 365.25
        
        return df
    
    def load_fight_results(self) -> pd.DataFrame:
        """Load UFC fight results data."""
        results_file = self.data_dir / "ufc_fight_results.csv"
        if not results_file.exists():
            raise FileNotFoundError(f"Fight results file not found: {results_file}")
        
        df = pd.read_csv(results_file)
        df['is_title_fight'] = df['is_title_fight'].astype(bool)
        return df
    
    def load_fight_details(self) -> pd.DataFrame:
        """Load UFC fight details/statistics data."""
        details_file = self.data_dir / "ufc_fight_details.csv"
        if not details_file.exists():
            raise FileNotFoundError(f"Fight details file not found: {details_file}")
        
        df = pd.read_csv(details_file)
        
        # Calculate derived statistics
        df['striking_accuracy'] = (df['significant_strikes_landed'] / 
                                  df['significant_strikes_attempted']) * 100
        df['takedown_accuracy'] = (df['takedowns_landed'] / 
                                  df['takedowns_attempted']) * 100
        
        # Handle division by zero
        df['striking_accuracy'] = df['striking_accuracy'].fillna(0)
        df['takedown_accuracy'] = df['takedown_accuracy'].fillna(0)
        
        return df
    
    def load_all_data(self) -> Dict[str, pd.DataFrame]:
        """Load all UFC data into a dictionary of DataFrames.
        
        Returns:
            Dictionary mapping table names to DataFrames, suitable for Copper queries.
        """
        return {
            'events': self.load_events(),
            'fighters': self.load_fighters(), 
            'fight_results': self.load_fight_results(),
            'fight_details': self.load_fight_details()
        }
    
    def get_fighter_stats(self, fighter_name: str) -> Dict[str, Any]:
        """Get comprehensive statistics for a specific fighter.
        
        Args:
            fighter_name: Name of the fighter to analyze
            
        Returns:
            Dictionary containing fighter statistics
        """
        data = self.load_all_data()
        
        # Find fighter
        fighter = data['fighters'][data['fighters']['fighter_name'] == fighter_name]
        if fighter.empty:
            raise ValueError(f"Fighter '{fighter_name}' not found")
        
        fighter_id = fighter.iloc[0]['fighter_id']
        
        # Get fight results
        fights = data['fight_results'][
            (data['fight_results']['fighter_1_id'] == fighter_id) |
            (data['fight_results']['fighter_2_id'] == fighter_id)
        ]
        
        wins = fights[fights['winner_id'] == fighter_id]
        total_fights = len(fights)
        total_wins = len(wins)
        
        # Get method breakdown
        ko_wins = len(wins[wins['method'] == 'KO/TKO'])
        sub_wins = len(wins[wins['method'] == 'Submission'])
        dec_wins = len(wins[wins['method'] == 'Decision'])
        
        # Title fights
        title_fights = len(fights[fights['is_title_fight'] == True])
        title_wins = len(wins[wins['is_title_fight'] == True])
        
        return {
            'fighter_name': fighter_name,
            'record': f"{total_wins}-{total_fights - total_wins}",
            'total_fights': total_fights,
            'total_wins': total_wins,
            'win_rate': (total_wins / total_fights * 100) if total_fights > 0 else 0,
            'ko_wins': ko_wins,
            'submission_wins': sub_wins,
            'decision_wins': dec_wins,
            'title_fights': title_fights,
            'title_wins': title_wins,
            'weight_class': fighter.iloc[0]['weight_class'],
            'nationality': fighter.iloc[0]['nationality'],
            'stance': fighter.iloc[0]['stance']
        }
    
    def get_event_summary(self, event_name: str) -> Dict[str, Any]:
        """Get summary statistics for a specific event.
        
        Args:
            event_name: Name of the event to analyze
            
        Returns:
            Dictionary containing event statistics
        """
        data = self.load_all_data()
        
        # Find event
        event = data['events'][data['events']['event_name'] == event_name]
        if event.empty:
            raise ValueError(f"Event '{event_name}' not found")
        
        event_id = event.iloc[0]['event_id']
        
        # Get fights for this event
        fights = data['fight_results'][data['fight_results']['event_id'] == event_id]
        
        finish_methods = fights['method'].value_counts().to_dict()
        title_fights = len(fights[fights['is_title_fight'] == True])
        
        return {
            'event_name': event_name,
            'date': event.iloc[0]['event_date'],
            'location': event.iloc[0]['location'],
            'venue': event.iloc[0]['venue'],
            'total_fights': len(fights),
            'title_fights': title_fights,
            'finish_methods': finish_methods,
            'finish_rate': len(fights[fights['method'] != 'Decision']) / len(fights) * 100
        }


def create_sample_data():
    """Create sample data for demonstration purposes."""
    loader = UFCDataLoader()
    return loader.load_all_data()


if __name__ == "__main__":
    # Demo usage
    loader = UFCDataLoader()
    
    print("🥊 UFC Data Loader Demo")
    print("=" * 40)
    
    # Load all data
    data = loader.load_all_data()
    
    print(f"📊 Loaded UFC data:")
    for table_name, df in data.items():
        print(f"  {table_name}: {len(df)} rows")
    
    # Fighter stats example
    print(f"\n🏆 Fighter Analysis: Jon Jones")
    try:
        jones_stats = loader.get_fighter_stats("Jon Jones")
        for key, value in jones_stats.items():
            print(f"  {key}: {value}")
    except ValueError as e:
        print(f"  Error: {e}")
    
    # Event analysis example
    print(f"\n🎪 Event Analysis: UFC 300: Pereira vs Hill")
    try:
        event_stats = loader.get_event_summary("UFC 300: Pereira vs Hill")
        for key, value in event_stats.items():
            print(f"  {key}: {value}")
    except ValueError as e:
        print(f"  Error: {e}")