import "./App.css";
import HenYang from "./components/HenYang";
import NewsCard from "./components/NewsCard";
import Gradient from "./components/gradient";

function App() {
  return (
    <>
      <header
        className="bg-white h-fit w-full flex top-0 sticky shadow-md z-9999"
        style={{ fontFamily: "AlumniSans" }}
      >
        <nav className="w-full">
          <div className="flex pl-4 pt-2 pb-2 text-black text-xl ">Hack404</div>
          <hr className="border-gray-300 w-full items-center" />
          <div className="flex gap-3 pl-4 pt-2 pb-2 text-black text-left">
            <div className="my-auto">
              <img src="/src/assets/yang.png" className="h-12 w-12 mr-2" />
            </div>
            <div className="grid grid-rows-2 gap-0.1">
              <div className="font-bold text-3xl">YangNews</div>
              <p className="text-lg">Find Yang daily</p>
            </div>

            <div className="ml-8 flex items-center space-x-8 text-xl">
              <a href="#" className="text-gray-900 ">
                Politics
              </a>
              <a href="#" className="text-gray-900 ">
                Environment
              </a>
              <a href="#" className="text-gray-900 ">
                Community
              </a>
              <a href="#" className="text-gray-900 ">
                Science
              </a>
              <a href="#" className="text-gray-900 ">
                Health
              </a>
              <a href="#" className="text-gray-900 ">
                Education
              </a>
            </div>
          </div>
        </nav>
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
