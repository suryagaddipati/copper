# Copper Data Explorer - Usage Guide 🚀

Your interactive data exploration UI is ready! Here's how to get started.

## 🎯 Quick Start

### 1. Launch the UI
```bash
# Recommended: Use the launcher script
python run_ui.py

# Alternative: Direct streamlit command
uv run streamlit run ui/app.py
```

### 2. Access the Dashboard
- Open your browser to `http://localhost:8501`
- The Copper Data Explorer will load automatically

## 🔥 Core Features

### 📊 Model Selection
1. **Choose a semantic model** from the sidebar dropdown
   - Fight Analysis (most comprehensive)
   - Event Analytics
   - Fighter Performance  
   - Betting Analysis

### 🔧 Query Building
2. **Select Dimensions** (Group By)
   - Weight Class, Finish Method, Gender
   - Title Fight status, Fight Duration
   
3. **Choose Measures** (Calculations)
   - Total Fights, Average Fight Rounds
   - Custom aggregations

### 🔍 Data Filtering
4. **Apply Filters** to focus your analysis
   - Multi-select dropdowns for categorical data
   - Automatic filter suggestions based on data

### 📈 Visualization
5. **Execute Query** to generate:
   - Interactive Plotly charts (bar, line, pie, scatter)
   - Sortable data tables
   - Export capabilities (CSV download)

## 💡 Usage Examples

### Example 1: Fight Outcomes by Weight Class
1. Select "Fight Analysis" model
2. Choose "Weight Class" dimension
3. Select "Total Fights" measure
4. Execute → See bar chart of fights per weight division

### Example 2: Title Fight Analysis
1. Add "Title Fight" filter → Select "True"
2. Choose "Finish Method" dimension
3. Execute → Analyze how title fights end

### Example 3: Multi-dimensional Analysis
1. Select both "Weight Class" AND "Finish Method"
2. Choose "Total Fights" measure
3. Execute → Get detailed breakdown with color-coded charts

## 🎨 UI Components

### Sidebar Controls
- **Model Selector**: Switch between different datasets
- **Dimension Builder**: Add/remove grouping fields
- **Measure Builder**: Select calculations to perform
- **Filter Panel**: Apply data filters
- **Action Buttons**: Execute queries, clear selections

### Main Dashboard
- **Results Summary**: Quick metrics display
- **Chart Tabs**: Switch between visualizations and data
- **Interactive Charts**: Click, zoom, hover for details
- **Data Table**: Sortable, filterable raw results

## 🔍 Advanced Features

### Chart Customization
- **Auto-suggestions**: UI recommends appropriate chart types
- **Type Selection**: Switch between bar, line, pie, scatter plots
- **Interactive Elements**: Click to filter, hover for details

### Data Export
- **CSV Download**: Export filtered results
- **Chart Export**: Save visualizations (via Plotly toolbar)

### Model Discovery
- **Auto-detection**: UI automatically finds YAML models
- **Metadata Display**: Show dimensions, measures, descriptions
- **Real-time Loading**: Models load with progress indicators

## 🔧 Troubleshooting

### "No models found"
- Ensure YAML files exist in `examples/ufc/` directory
- Check that datasources are properly defined

### "Query returns no results"
- Try removing filters to see if data exists
- Check dimension/measure expressions in YAML
- The current implementation uses simplified query logic

### Charts not displaying
- Verify that query returns data
- Check that dimensions and measures are selected
- Try different chart types from the dropdown

## 🚀 Next Steps

### Enhance Your Experience
1. **Explore All Models**: Try different semantic models
2. **Combine Filters**: Use multiple filters for focused analysis
3. **Export Data**: Download results for external analysis
4. **Create Dashboards**: Build multiple charts for comprehensive views

### Customize the UI
1. **Add New Models**: Create YAML files in `examples/` directory
2. **Modify Themes**: Edit color schemes in `run_ui.py`
3. **Extend Charts**: Add new visualization types in `charts.py`

### Development Mode
```bash
# Run with auto-reload for development
streamlit run ui/app.py --server.runOnSave true
```

## 📊 Available Data

### UFC Fight Dataset
- **7,812 fights** from UFC 1 (1993) to present
- **70 columns** including fighter stats, odds, outcomes
- **Real MMA data** with historical fight information

### Key Data Points
- Fighter details (height, weight, reach, stance)
- Fight outcomes (method, round, time)
- Event information (date, location, venue)
- Performance statistics (strikes, takedowns, submissions)
- Betting odds and outcomes

## 🎯 Pro Tips

1. **Start Simple**: Begin with one dimension and one measure
2. **Use Filters**: Apply filters to focus on specific data subsets
3. **Explore Interactively**: The UI encourages data-driven exploration
4. **Export Results**: Save interesting findings for further analysis
5. **Try Different Charts**: Switch visualization types to find insights

---

**Happy Exploring!** 🎉

The Copper Data Explorer makes it easy to discover insights in your data through an intuitive, user-driven interface.