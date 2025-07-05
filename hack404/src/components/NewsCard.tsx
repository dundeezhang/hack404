import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import type { Article } from "../types";
import {
  faCaretDown,
  faCaretUp,
  faClock,
  faThumbsDown,
  faThumbsUp,
} from "@fortawesome/free-solid-svg-icons";
import { useEffect, useState } from "react";

const API_BASE_URL = "http://localhost:8000";
const NewsCard = ({ article }: { article: Article }) => {
  // Total number
  const [likes, setLikes] = useState(0);
  const [dislikes, setDislikes] = useState(0);
  // Whether the user has liked or not
  const [liked, setLiked] = useState(() => {
    const stored = localStorage.getItem(`liked-${article.url}`);
    return stored ? JSON.parse(stored) : false;
  });
  const [disliked, setDisliked] = useState(() => {
    const stored = localStorage.getItem(`disliked-${article.url}`);
    return stored ? JSON.parse(stored) : false;
  });

  useEffect(() => {
    localStorage.setItem(`liked-${article.url}`, JSON.stringify(liked));
  }, [liked, article.url]);

  useEffect(() => {
    localStorage.setItem(`disliked-${article.url}`, JSON.stringify(disliked));
  }, [disliked, article.url]);

  const getLikes = async (retries = 1) => {
    try {
      const res = await fetch(
        `${API_BASE_URL}/like-counts?url=${encodeURIComponent(article.url)}`
      );
      const data = await res.json();

      if (data === null && retries > 0) {
        // retry
        return await getLikes(retries - 1);
      }

      setLikes(data ?? 0);
    } catch (err) {
      console.error("Error fetching likes:", err);
    }
    try {
      const res = await fetch(
        `${API_BASE_URL}/dislike-counts?url=${encodeURIComponent(article.url)}`
      );
      const data = await res.json();
      // if (data === null && retries > 0) {
      //   // retry
      //   return await getLikes(retries - 1);
      // }

      setDislikes(data ?? 0);
    } catch (err) {
      console.error("Error fetching dislikes:", err);
    }
  };

  useEffect(() => {
    const fetchLikes = async () => {
      try {
        await getLikes(3);
        console.log("liked", liked, likes, "disliked", disliked, dislikes);
      } catch (err) {
        console.error("Error fetching likes/dislikes:", err);
      }
    };
    fetchLikes();
  }, []);

  const updateLikes = async (like: boolean) => {
    try {
      // console.log("liked", liked);
      const res = await fetch(
        `${API_BASE_URL}/update-likes?url=${article.url}&increment=${!like}`
      )
        .then((res: Response) => res.json())
        .then((data: any) => {
          // console.log("like count", data);
          setLikes(data);
        });
      // if (!res.ok) {
      //   throw new Error(`Failed to update likes: ${res.statusText}`);
      // }
      await setLiked(!liked);

      // const data = await res.json();
    } catch (error) {
      console.error("Error updating likes:", error);
    }
  };
  const updateDislikes = async (dislike: boolean) => {
    try {
      const res = await fetch(
        `${API_BASE_URL}/update-dislikes?url=${
          article.url
        }&increment=${!dislike}`
      )
        .then((res: Response) => res.json())
        .then((data: any) => {
          // console.log("dislike count", data);

          setDislikes(data);
        });
      await setDisliked(!disliked);

      // const data = await res.json();
    } catch (error) {
      console.error("Error updating likes:", error);
    }
  };

  return (
    <a
      href={article?.url}
      target="_blank"
      rel="noopener noreferrer"
      className="transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-105"
    >
      <div
        className="relative bg-white w-[300px] rounded-3xl shadow-md text-xl"
        style={{ fontFamily: "AlumniSans" }}
      >
        <div className="relative w-[300px] h-[250px]">
          <div className="absolute w-full h-full bg-[#D9D9D9] rounded-t-3xl z-0 items-center" />
          {/* Default Image */}
          <img
            src={
              article?.imageUrl ? article.imageUrl : "/src/assets/fillerimg.png"
            }
            className="mx-auto absolute w-full h-full object-cover rounded-t-3xl z-10"
            alt="Default"
          />
          <div className="absolute bottom-0 w-full z-20 bg-gradient-to-t from-black/70 to-transparent px-4 py-2">
            <div className="infinite-scroll-container">
              <h1
                className="infinite-scroll-text delay-500 text-white text-2xl"
                style={{ fontFamily: "AlumniSans", fontWeight: 700 }}
                title={article?.title}
              >
                {article?.title}
              </h1>
            </div>
          </div>
        </div>

        <div className="p-3">
          <div className="grid grid-cols-3">
            <div className="col-span-2 gap-3 h-[50] my-auto">
              {/* <div className="my-auto h-[40px] w-[40px] rounded-full bg-[#22333B]" /> */}
              <div className="infinite-scroll-container">
                <h2
                  className="my-auto text-[#22333B] infinite-scroll-text delay-500"
                  style={{ fontFamily: "AlumniSans", fontWeight: 400 }}
                >
                  {article?.author ? article?.author : "N/A"}
                </h2>
              </div>
            </div>
            {/* <div className="flex flex-row justify-between"> */}
            <div className="col-span-1 flex items-center justify-end">
              <div className="flex flex-row items-center">
                <FontAwesomeIcon
                  className="mr-2"
                  icon={faClock}
                  color="#8A8A8A"
                />
                <p
                  className="text-[#8A8A8A] text-sm"
                  style={{ fontFamily: "AlumniSans", fontWeight: 300 }}
                >
                  {article?.date
                    ? new Date(article.date).toLocaleDateString(undefined, {
                        year: "numeric",
                        month: "short",
                        day: "numeric",
                      })
                    : ""}
                </p>
              </div>
            </div>
          </div>
          {/* </div> */}
          <div className="mt-5 flex flex-row flex-wrap gap-3">
            <div
              className="rounded-xl border border-[#A9927D] px-2 py-1"
              style={{ fontFamily: "AlumniSans", fontWeight: 500 }}
            >
              <p className="text-[#A9927D] text-sm">sports</p>
            </div>
            <div
              className="rounded-xl border border-[#A9927D] px-2 py-1"
              style={{ fontFamily: "AlumniSans", fontWeight: 500 }}
            >
              <p className="text-[#A9927D] text-sm">sports</p>
            </div>
            <div
              className="rounded-xl border border-[#A9927D] px-2 py-1"
              style={{ fontFamily: "AlumniSans", fontWeight: 500 }}
            >
              <p className="text-[#A9927D] text-sm">sports</p>
            </div>
          </div>
          <div className="flex flex-row gap-3 mt-3">
            <button
              className="flex flex-row gap-2 cursor-pointer"
              onClick={(e) => {
                e.preventDefault();
                updateLikes(liked);
                if (disliked) {
                  updateDislikes(true);
                }
                // setLiked(!liked);
              }}
            >
              <FontAwesomeIcon
                className="my-auto"
                icon={faCaretUp}
                color={liked ? "#7DB8AF" : "#8A8A8A"}
              />
              <p className="text-[#8A8A8A]">{likes ? likes : 0}</p>
            </button>
            <button
              className="flex flex-row gap-2 cursor-pointer"
              onClick={(e) => {
                e.preventDefault();
                updateDislikes(disliked);
                if (liked) {
                  updateLikes(true);
                }
                // setDisliked(!disliked);
              }}
            >
              <FontAwesomeIcon
                className="my-auto"
                icon={faCaretDown}
                color={disliked ? "#7DB8AF" : "#8A8A8A"}
              />
              <p className="text-[#8A8A8A]">{dislikes ? -dislikes : 0}</p>
              {dislikes}
            </button>
          </div>
        </div>
      </div>
    </a>
  );
};

export default NewsCard;
