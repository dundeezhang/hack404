# YangNews

YangNews is a positive news aggregator that filters and displays uplifting news articles from various sources. The application features a React frontend with Vite for fast development and a FastAPI backend for news aggregation and data management.

## 🌟 Features

- **Positive News Filtering**: Automatically filters out negative content to show only uplifting news
- **Category-based News**: Browse news by categories (General, Business, Entertainment, Health, Science, Sports, Technology)
- **Like/Dislike System**: Users can rate articles with likes and dislikes
- **Tag System**: Articles are automatically tagged based on content analysis
- **Top Articles**: See trending articles based on user engagement
- **Responsive Design**: Modern, mobile-friendly interface

## 🏗️ Project Structure

```
hack404/
├── frontend/                 # React + Vite frontend
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── types.ts         # TypeScript type definitions
│   │   └── api.ts           # API service layer
│   └── package.json
├── backend/                  # FastAPI backend
│   ├── main.py              # FastAPI application entry point
│   ├── helpers/             # Helper modules
│   │   ├── database.py      # Database operations
│   │   ├── filter.py        # News filtering logic
│   │   └── scan.py          # Content scanning utilities
│   └── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **pip** (Python package manager)
- **npm** or **yarn** (Node package manager)

### Environment Variables

Create a `.env` file in the `backend/` directory with the following variables:

```env
NEWSAPI_KEY=your_newsapi_key_here
SUPABASE_URL=your_supabase_url
SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
OPEN_API_KEY=your_openai_api_key
```

## 🖥️ Frontend (React + Vite)

### Installation

```bash
cd hack404
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The frontend will be available at `http://localhost:5173` (or another port if 5173 is in use).

### Build for Production

```bash
npm run build
```

This creates a `dist/` directory with optimized production files.

### Preview Production Build

```bash
npm run preview
```

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Frontend Technology Stack

- **React 19** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Styling framework
- **React Router** - Client-side routing
- **FontAwesome** - Icons

## 🔧 Backend (FastAPI)

### Installation

```bash
cd backend
pip install -r requirements.txt
```

### Development

Start the FastAPI development server:

```bash
uvicorn main:app --reload
```

The backend API will be available at `http://localhost:8000`.

API documentation is automatically generated and available at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Production

For production deployment:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Backend Technology Stack

- **FastAPI** - Modern Python web framework
- **Supabase** - Database and authentication
- **NewsAPI** - News data source
- **OpenAI API** - Content analysis and tagging
- **Requests** - HTTP client for external APIs

## 🏃‍♂️ Running Both Services

### Option 1: Using the Root Package Scripts

From the root directory:

```bash
# Install dependencies for both frontend and backend
npm install

# Start both services concurrently
npm run dev
```

This will start:

- Frontend at `http://localhost:5173`
- Backend at `http://localhost:8000`

### Option 2: Manual Start

**Terminal 1 - Backend:**

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

**Terminal 2 - Frontend:**

```bash
cd hack404
npm install
npm run dev
```

## 📚 API Endpoints

### News Endpoints

- `GET /news` - Get news articles by category
- `GET /top-articles` - Get top-rated articles
- `GET /article-tag` - Get tags for a specific article

### Interaction Endpoints

- `GET /like-counts` - Get like count for an article
- `GET /dislike-counts` - Get dislike count for an article
- `GET /update-likes` - Update article likes
- `GET /update-dislikes` - Update article dislikes

### Utility Endpoints

- `GET /scan-website` - Scan and analyze website content
- `GET /get-article-id` - Get article ID by URL

## 🎨 Features in Detail

### Positive News Filtering

The application automatically filters out negative content using keyword-based filtering and content analysis to ensure only uplifting news is displayed.

### Dynamic Tagging

Articles are automatically tagged using AI-powered content analysis, categorizing them into topics like science, technology, health, business, entertainment, and general news.

### User Engagement

Users can like or dislike articles, and the most popular articles are featured in the "Hen Yang" (top-rated) section.

### Responsive Design

Built with Tailwind CSS for a modern, mobile-first responsive design that works across all devices.

## 🛠️ Development

### Code Structure

**Frontend Components:**

- `Header.tsx` - Navigation and category selection
- `NewsCard.tsx` - Individual article display with tags and interactions
- `HenYang.tsx` - Top articles sidebar
- `CardTag.tsx` - Article tag component with skeleton loading

**Backend Modules:**

- `main.py` - FastAPI routes and application setup
- `database.py` - Supabase database operations
- `filter.py` - Content filtering logic
- `scan.py` - AI-powered content analysis

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is built for educational purposes as part of a hackathon.

## 🔗 External Services

- **NewsAPI** - News data provider
- **Supabase** - Database and backend services
- **OpenAI** - AI content analysis
