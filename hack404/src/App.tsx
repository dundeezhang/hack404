import { useEffect, useState } from "react";
import "./App.css";
import Header from "./components/Header";
import HenYang from "./components/HenYang";
import NewsCard from "./components/NewsCard";
import Gradient from "./components/gradient";
import { apiService } from "./api";
import type { Article } from "./types";

function App() {
  const [active, setActive] = useState("general");
  const [articles, setArticles] = useState<Article[]>([]);

  // const fetchArticles = async () => {
  //   try {
  //     const res = await apiService.getArticles(active);
  //     setArticles(res);
  //   } catch {
  //     console.error("Error fetching articles");
  //   }
  // };

  const fetchArticles = async () => {
    fetch("http://localhost:8000/news?category=general")
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error("Error:", err));
  };

  useEffect(() => {
    fetchArticles();
  }, []);

  return (
    <>
      <header
        className="bg-white h-fit w-full flex top-0 sticky shadow-md z-9999"
        style={{ fontFamily: "AlumniSans" }}
      >
        <Header active={active} setActive={setActive} />
      </header>
      <main className="p-12">
        <Gradient />
        <div className="flex flex-row justify-between">
          <div className="flex flex-row flex-wrap gap-5">
            {articles &&
              articles.map((article) => {
                return <NewsCard key={article.title} article={article} />;
              })}
            <NewsCard />
            <NewsCard />
            <NewsCard />
            <NewsCard />
            <NewsCard />
          </div>
          <HenYang />
        </div>
      </main>
    </>
  );
}

export default App;
