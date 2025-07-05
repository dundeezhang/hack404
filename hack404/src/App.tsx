import { BrowserRouter as Router, Routes, Route, useParams, Navigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "./App.css";
import Header from "./components/Header";
import HenYang from "./components/HenYang";
import NewsCard from "./components/NewsCard";
import Gradient from "./components/gradient";
import Ornament from "./components/ornament";
import type { Article } from "./types";

function CategoryArticles({setOrnamentUrl}:{setOrnamentUrl: ((param: string) => void)}) {
  const { category } = useParams<{ category: string }>();
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);
  

  // Default to "general" if no category in URL
  const selectedCategory = category ? category.toLowerCase() : "general";
const API_BASE_URL = "http://localhost:8000";

  useEffect(() => {
    setLoading(true);
    fetch(`${API_BASE_URL}/news?category=${selectedCategory}`)
      .then((res) => res.json())
      .then((data) => {
        const formattedArticles = data.articles.map((article: any) => ({
          url: article.url,
          imageUrl: article.urlToImage || "",
          title: article.title || "",
          author: article.author || article.source?.name || "",
          date: article.publishedAt || "",
          filters: [selectedCategory],
        }));
        setArticles(formattedArticles);
      })
      .finally(() => setLoading(false));
  }, [selectedCategory]);

  return (
    <div className="flex flex-row flex-wrap gap-5">
      {loading ? (
          <div className="w-[950px] min-h-[400px] flex items-center justify-center">
        <img src="src/assets/load.png" className="animate-spin align-middle h-10 w-10"/>
        </div>
      ) : (
        articles.map((article) => (
          <NewsCard key={article.title} article={article} setUrl={setOrnamentUrl}/>
        ))
      )}
    </div>
  );
}

function App() {
  // You can keep your active state if you want to highlight the current category in Header
  const [active, setActive] = useState("general");
  const [ornamentUrl, setOrnamentUrl] = useState("");

  return (
    <Router>
      <header className="bg-white h-fit w-full flex top-0 sticky shadow-md z-9999" style={{ fontFamily: "AlumniSans" }}>
        <Header active={active} setActive={setActive} />
      </header>
      <main className="p-12">
        <Gradient />
        <div className="flex flex-row justify-between">
          <Routes>
            <Route path="/" element={<Navigate to="/general" />} />
            <Route path="/:category" element={<CategoryArticles setOrnamentUrl={setOrnamentUrl}/>} />
          </Routes>
          {ornamentUrl !== "" && <Ornament url={ornamentUrl}/>}
          <HenYang />
        </div>
      </main>
    </Router>
  );
}

export default App;
