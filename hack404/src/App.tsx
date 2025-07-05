import { useState } from "react";
import "./App.css";
import Header from "./components/Header";
import HenYang from "./components/HenYang";
import NewsCard from "./components/NewsCard";
import Gradient from "./components/gradient";

function App() {
  const [active, setActive] = useState("");
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
