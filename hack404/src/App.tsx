import { BrowserRouter as Router, Routes, Route, useParams, Navigate } from "react-router-dom";
import { useEffect, useState } from "react";
import "./App.css";
import Header from "./components/Header";
import HenYang from "./components/HenYang";
import NewsCard from "./components/NewsCard";
import Gradient from "./components/gradient";
import Ornament from "./components/ornament";
import type { Article } from "./types";

function CategoryArticles() {
  const { category } = useParams<{ category: string }>();
  const [articles, setArticles] = useState<Article[]>([]);
  const [loading, setLoading] = useState(true);

  // Default to "general" if no category in URL
  const selectedCategory = category ? category.toLowerCase() : "general";

  useEffect(() => {
    setLoading(true);
    fetch(`http://localhost:8000/news?category=${selectedCategory}`)
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
        <div>Loading...</div>
      ) : (
        articles.map((article) => (
          <NewsCard key={article.title} article={article} />
        ))
      )}
    </div>
  );
}

function App() {
  // You can keep your active state if you want to highlight the current category in Header
  const [active, setActive] = useState("general");

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
            <Route path="/:category" element={<CategoryArticles />} />
          </Routes>
          <Ornament />
          <HenYang />
        </div>
      </main>
    </Router>
  );
}

export default App;
