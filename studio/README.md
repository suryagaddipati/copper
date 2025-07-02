# Copper Studio

**The Universal Semantic Layer - Data Exploration Interface**

Copper Studio is a generic, Looker-like web interface for exploring data through Copper's semantic layer. It dynamically loads semantic models from any domain and provides an intuitive drag-and-drop interface for building queries, visualizing data, and generating SQL.

![Copper Studio Interface](https://via.placeholder.com/800x400?text=Copper+Studio+UI)

## Features

### 🎯 **Universal Interface**
- **Project Panel**: Browse and select from available projects with detailed information
- **Dynamic Model Loading**: Automatically loads any Copper semantic model from projects
- **Sidebar**: Browse dimensions and measures from any domain with expandible categories
- **Query Builder**: Build queries by selecting fields with visual feedback
- **Multiple Visualizations**: Table, bar chart, line chart, and pie chart views
- **SQL Generation**: View generated SQL queries with syntax highlighting
- **Project Switching**: Toggle project panel visibility and switch between projects

### 📊 **Example Models**
**Available Example Models:**
- **Sports Analytics**: Comprehensive sports data with events, participants, and performance metrics
- **Future Examples**: Sales, E-commerce, Healthcare, Finance, Manufacturing, etc.

Projects are automatically loaded from the `example-projects/` directory structure, making it easy to add new domains.

### 🚀 **Key Capabilities**
- **Auto-execution**: Queries run automatically when fields change
- **Interactive Charts**: Switch between table and chart views instantly
- **Responsive Design**: Works on desktop and mobile devices
- **Mock Backend**: Simulates real API calls with loading states

## Getting Started

### Prerequisites
- Node.js 18+ 
- npm or yarn

### Installation

```bash
cd studio
npm install
```

### Development

```bash
npm run dev
```

Open [http://localhost:3001](http://localhost:3001) to view the interface.

### Adding New Projects

To add a new project:
1. Create a directory under `example-projects/your-project/`
2. Add `project.yaml` with project metadata
3. Add `model.yaml` and `datasources.yaml` with your definitions
4. Add CSV data files in `data/` subdirectory
5. Create shared connections in `example-projects/connections/` if needed
6. The project will be automatically discovered and loaded

### Production Build

```bash
npm run build
npm start
```

## Usage

### Building Queries

1. **Select Dimensions**: Click dimension fields in the sidebar (blue indicators)
2. **Select Measures**: Click measure fields in the sidebar (green indicators)  
3. **Auto-execution**: Query runs automatically with mock UFC data
4. **View Results**: Switch between table, bar, line, and pie chart views

### Exploring Data

- **Filter by Category**: Expand/collapse dimensions and measures sections
- **Multiple Selection**: Select multiple fields to build complex analyses
- **Visual Feedback**: Selected fields show colored indicators and counts
- **SQL Inspection**: Toggle SQL view to see generated queries

### Example Analyses

- **Entity Performance**: Select entity dimensions + performance measures
- **Geographic Analysis**: Select location dimensions + aggregated measures  
- **Category Breakdown**: Select classification dimensions + multiple measures
- **Time Series**: Select time dimensions + measures for trend analysis

## Architecture

### Components

- **`ProjectPanel`**: Project browsing, selection, and information display
- **`Sidebar`**: Field selection with dimensions/measures categorization
- **`QueryBuilder`**: Query execution, SQL display, and controls  
- **`DataVisualization`**: Chart rendering and visualization controls
- **`Page`**: Main layout orchestrating all components

### Tech Stack

- **Framework**: Next.js 15 with App Router
- **Styling**: Tailwind CSS for responsive design
- **Charts**: Recharts for data visualization
- **Icons**: Lucide React for consistent iconography
- **State**: React hooks for local state management

## Integration Points

### Backend Integration
The UI is designed to integrate with:
- **Copper Python API**: Load semantic models and execute queries
- **Generic SQL Generation**: Display generated SQL from Copper's semantic layer
- **Real Data Sources**: Connect to any database or data source
- **YAML Model Loading**: Parse Copper semantic model definitions

### Semantic Model Loading
```typescript
// Generic model loading example
import { getAvailableModels, loadModel } from '@/lib/example-models';

// Load any available model dynamically
const models = await getAvailableModels();
const sportsModel = await loadModel('sports');
const salesModel = await loadModel('sales'); // Future model

// Use with any domain
const processor = model.processor;
const results = processor.queryData(['dimension'], ['measure']);

// Models are loaded from examples/{domain}/model.yaml structure
```

---

**Copper Studio** - Making data exploration intuitive and powerful through semantic modeling.