# Copper Data Explorer UI 🚀

Interactive Streamlit dashboard for exploring data through the Copper semantic layer.

## ✨ Features

- **🔧 Visual Query Builder**: Select dimensions and measures with intuitive controls
- **📊 Interactive Charts**: Auto-generated Plotly visualizations with multiple chart types
- **🔍 Dynamic Filtering**: Filter data with multi-select controls and real-time updates
- **📋 Data Export**: Download results as CSV for further analysis
- **🎯 User-Driven Exploration**: Let users drive their own data discovery journey

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Install UI dependencies
uv sync --extra ui

# Or with pip
pip install streamlit plotly pandas numpy
```

### 2. Launch the UI

```bash
# Option 1: Use the launcher script
python run_ui.py

# Option 2: Direct Streamlit command
streamlit run ui/app.py

# Option 3: Use uv
uv run streamlit run ui/app.py
```

### 3. Explore Data

1. **Select a Model**: Choose from available UFC analytics models
2. **Pick Dimensions**: Group data by weight class, fight method, etc.
3. **Choose Measures**: Calculate total fights, finish rates, averages, etc.
4. **Apply Filters**: Focus on specific data subsets
5. **Execute Query**: Click to generate interactive charts and tables

## 📊 Available Models

The UI comes with several pre-built UFC analytics models:

### Fight Analysis
- **Dimensions**: Weight class, finish method, gender, title fights
- **Measures**: Total fights, average fight rounds
- **Data**: 7,812 UFC fights from 1993 to present

### Event Analytics
- UFC event and venue analysis
- Historical fight data exploration

### Fighter Performance
- Individual fighter statistics and metrics
- Performance trends over time

### Betting Analysis
- Odds and betting outcome analysis
- Risk assessment metrics

## 🎯 Usage Examples

### Basic Exploration
1. Select "Fight Analysis" model
2. Choose "Weight Class" dimension
3. Select "Total Fights" measure
4. Execute query to see fights by weight division

### Advanced Analysis
1. Add multiple dimensions: "Weight Class" + "Finish Method"
2. Include multiple measures: "Total Fights" + "Average Rounds"
3. Apply filters: Filter by gender or title fights
4. Export results for further analysis

### Chart Types
The UI automatically suggests appropriate visualizations:
- **Bar Charts**: For categorical breakdowns
- **Line Charts**: For trend analysis
- **Pie Charts**: For proportional data
- **Scatter Plots**: For correlation analysis

## 🏗️ Architecture

```
ui/
├── app.py                    # Main Streamlit entry point
├── dashboard.py              # Core dashboard logic
├── copper_interface.py       # Semantic layer integration
├── charts.py                # Plotly chart components
├── components/
│   ├── filters.py           # Interactive filter widgets
│   └── query_builder.py     # Advanced query construction
└── utils/                   # Helper utilities
```

### Key Components

#### CopperInterface
- Bridges Copper semantic layer with Streamlit UI
- Handles model loading and data querying
- Provides metadata extraction for dimensions/measures

#### ChartManager
- Creates interactive Plotly visualizations
- Auto-suggests appropriate chart types
- Handles chart customization and interactivity

#### Dashboard
- Main UI layout and navigation
- Sidebar controls for query building
- Results display with charts and tables

## 🎨 Customization

### Adding New Models
1. Create YAML semantic model in `examples/` directory
2. Include datasource definitions
3. Define dimensions and measures
4. Restart UI to auto-discover new models

### Custom Chart Types
Extend `ChartManager` to add new visualization types:

```python
def _create_custom_chart(self, df, config):
    # Your custom Plotly chart logic
    return fig
```

### UI Theming
Customize appearance in `run_ui.py`:

```python
subprocess.run([
    sys.executable, "-m", "streamlit", "run", str(app_file),
    "--theme.primaryColor", "#your_color",
    "--theme.backgroundColor", "#your_bg"
])
```

## 🧪 Testing

```bash
# Test UI components without Streamlit runtime
python ui/test_ui.py

# Verify model loading and chart generation
uv run python ui/test_ui.py
```

## 🔮 Future Enhancements

- **Multi-model Support**: Load and switch between multiple models
- **Custom Expressions**: Build ad-hoc measures with expression editor
- **Dashboard Sharing**: Save and share custom dashboard configurations
- **Real-time Data**: Connect to live data sources with auto-refresh
- **Advanced Analytics**: Statistical functions and ML integration

## 🐛 Troubleshooting

### Common Issues

**"No models found"**
- Ensure YAML files exist in `examples/ufc/` directory
- Check file permissions and syntax

**"Cannot load data"**
- Verify CSV files exist and are readable
- Check datasource file paths in YAML

**"Charts not displaying"**
- Ensure query returns data
- Check dimension/measure expressions
- Verify Plotly installation

### Debug Mode
Run with debug logging:

```bash
streamlit run ui/app.py --logger.level=debug
```

## 📚 Learn More

- [Copper Documentation](../README.md)
- [Semantic Modeling Guide](../docs/model.md)
- [Expression Language Reference](../SCHEMA_REFERENCE.md)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/ui-enhancement`
3. Add your changes to the `ui/` directory
4. Test with: `python ui/test_ui.py`
5. Submit a pull request

---

**Copper Data Explorer** - Making data exploration interactive and intuitive! 🎯