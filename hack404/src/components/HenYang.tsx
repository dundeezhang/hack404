import {
  faArrowTrendUp,
  faArrowUpRightFromSquare,
  faCaretDown,
  faCaretUp,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import type { ApiCall, Article } from "../types";
import { useState } from "react";
const API_BASE_URL = "http://localhost:8000";

const HenYang = () => {
  const [articles, setArticles] = useState<
    { article: Article; likes: number }[]
  >([]);
  // Total number
  const [likes, setLikes] = useState(0);
  const [dislikes, setDislikes] = useState(0);

  const getArticles = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/top-articles?limit=5`);
      const data = await res.json();
      console.log("data", data);

      const enrichedArticles = [];

      for (const article of data) {
        const likes = await getLikes(article, 3);
        console.log("likes", likes);
        enrichedArticles.push({ article, likes });
      }

      setArticles(enrichedArticles);
    } catch (err) {
      console.error("Error fetching articles:", err);
    }
    // fetch(`${API_BASE_URL}/top-articles?limit=5`)
    //   .then((res: Response) => res.json())
    //   .then((data: any) => {
    //     console.log("article", data);
    //     setArticles(
    //       data.map((article: Article) => ({
    //         article,
    //         likes: 0, // or undefined if you plan to fetch later
    //       }))
    //     );
    //   })
    //   .catch((err: any) => console.error("Error:", err));
  };
  useState(() => {
    getArticles();
  }, []);

  const getLikes = async (article: Article, retries = 1): Promise<number> => {
    try {
      console.log("likes", article.link);

      const res = await fetch(
        `${API_BASE_URL}/like-counts?url=${article.link}`
      );
      const data = await res.json();
      // console.log("likes", data)
      if (data === null && retries > 0) {
        // retry
        return await getLikes(article, retries - 1);
      }

      return data ?? 0; // return a number
    } catch (err) {
      console.error("Error fetching likes for", article.link, err);
      return 0;
    }

    // fetch(`${API_BASE_URL}/dislike-counts?url=${article.link}`)
    //   .then((res: Response) => res.json())
    //   .then((data: any) => {
    //     // console.log("dislike count", data);

    //     setDislikes(data);
    //   })
    //   .catch((err: any) => console.error("Error:", err));
  };

  return (
    <div className="w-[250px] bg-white rounded-3xl shadow-md p-3 self-start sticky top-[160px] z-10">
      <div className="flex flex-row rounded-3xl gap-3">
        <FontAwesomeIcon icon={faArrowTrendUp} color="#B7E2DC" size="2x" />
        <h1
          className="text-[#22333B] text-2xl font-bold"
          style={{ fontFamily: "AlumniSans" }}
        >
          Hen Yang
        </h1>
      </div>
      <p
        className="text-[#8A8A8A] text-sm mx-auto"
        style={{ fontFamily: "AlumniSans" }}
      >
        (top-rated articles)
      </p>
      <div className="flex flex-col gap-2">
        {articles &&
          articles.map((item, index) => {
            // getLikes(article);
            return (
              <a
                href={item?.article.link}
                target="_blank"
                rel="noopener noreferrer"
              >
                <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-between">
                  <div className="self-end bg-[#7DB8AF] rounded-full px-3 py-1">
                    <h1
                      className="text-[#fff] self-end text-lg font-semibold"
                      style={{ fontFamily: "AlumniSans" }}
                    >
                      {index + 1}
                    </h1>
                  </div>
                  <div className="w-[80%] flex flex-row justify-between gap-5 my-auto">
                    <h1
                      className="text-[#8A8A8A] w-[90%] truncate"
                      style={{ fontFamily: "AlumniSans" }}
                    >
                      {item.article.title}
                    </h1>

                    {/* <FontAwesomeIcon
                      className="mt-1"
                      icon={faArrowUpRightFromSquare}
                      color="#8A8A8A"
                    /> */}
                    <div className="flex flex-row gap-2">
                      <FontAwesomeIcon
                        className="my-auto"
                        icon={faCaretUp}
                        color="#8A8A8A"
                      />
                      <p className="text-[#8A8A8A]">
                        {item.likes ? item.likes : 0}
                      </p>
                    </div>
                    {/* <div className="flex flex-row gap-2">
                      <FontAwesomeIcon
                        className="my-auto"
                        icon={faCaretDown}
                        color="#8A8A8A"
                      />
                      <p className="text-[#8A8A8A]">{dislikes ? dislikes : 0}</p>
                    </div> */}
                  </div>
                </div>
              </a>
            );
          })}
      </div>
      {/* <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-between">
        <div className="self-end bg-[#7DB8AF] rounded-full px-3 py-1">
          <h1 className="text-[#fff] self-end text-md font-semibold">1</h1>
        </div>
        <div className="w-[80%] flex flex-row justify-between gap-5 my-auto">
          <h1
            className="text-[#8A8A8A] w-[90%] truncate"
            style={{ fontFamily: "AlumniSans" }}
          >
            Title title title title title title
          </h1>
          <a
            href="https://www.google.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <FontAwesomeIcon
              className="mt-1"
              icon={faArrowUpRightFromSquare}
              color="#8A8A8A"
            />
          </a>
        </div>
      </div> */}
    </div>
  );
};

export default HenYang;
