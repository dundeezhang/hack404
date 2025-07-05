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
  const [liked, setLiked] = useState(false);
  const [disliked, setDisliked] = useState(false);

  const getLikes = async () => {
    fetch(`${API_BASE_URL}/like-counts?url=${article.url}`)
      .then((res: Response) => res.json())
      .then((data: any) => {
        console.log("like count",data);
        setLikes(data);
      })
      .catch((err: any) => console.error("Error:", err));

    fetch(`${API_BASE_URL}/dislike-counts?url=${article.url}`)
      .then((res: Response) => res.json())
      .then((data: any) => {
        console.log("dislike count",data);

        setDislikes(data);
      })
      .catch((err: any) => console.error("Error:", err));
  };

  useEffect(() => {
    const fetchLikes = async () => {
      try {
        await getLikes();
        console.log("liked", liked, likes, "disliked", disliked, dislikes)
        
      } catch (err) {
        console.error("Error fetching likes/dislikes:", err);
      }
    };
    fetchLikes();
  }, [liked, disliked]);

  const updateLikes = async (like: boolean) => {
    try {
      const res = await fetch(
        `${API_BASE_URL}/update-likes?url=${article.url}&increment=${like}`
      );
      setLiked(!liked);

      // const data = await res.json();
    } catch (error) {
      console.error("Error updating likes:", error);
    }
  };
  const updateDislikes = async (dislike: boolean) => {
    try {
      const res = await fetch(
        `${API_BASE_URL}/update-dislikes?url=${article.url}&increment=${dislike}`
      );
      setDisliked(!disliked);


      // const data = await res.json();
    } catch (error) {
      console.error("Error updating likes:", error);
    }
  };

  return (
    <a href={article?.url} target="_blank" rel="noopener noreferrer">
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
            <h1
              className="text-white text-2xl"
              style={{ fontFamily: "AlumniSans", fontWeight: 700 }}
            >
              {article?.title}
            </h1>
          </div>
        </div>

        <div className="p-3">
          <div className="flex flex-row justify-between">
            <div className="flex flex-row gap-3 h-[50] my-auto">
              {/* <div className="my-auto h-[40px] w-[40px] rounded-full bg-[#22333B]" /> */}
              <h2
                className="my-auto text-[#22333B]"
                style={{ fontFamily: "AlumniSans", fontWeight: 600 }}
              >
                {article?.author ? article?.author : "N/A"}
              </h2>
            </div>
            {/* <div className="flex flex-row justify-between"> */}
            <div className="flex flex-row gap-2 w-1/2 justify-end">
              <FontAwesomeIcon
                className="my-auto"
                icon={faClock}
                color="#8A8A8A"
              />
              <p
                className="text-[#8A8A8A] my-auto text-sm"
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
              className="flex flex-row gap-2"
              onClick={(e) => {
                e.preventDefault();
                updateLikes(liked);
                // setLiked(!liked);
              }}
            >
              <FontAwesomeIcon
                className="my-auto"
                icon={faCaretUp}
                color={liked ? "#7DB8AF" : "#8A8A8A"}
              />
              <p className="text-[#8A8A8A]">{likes}</p>
            </button>
            <button
              className="flex flex-row gap-2"
              onClick={(e) => {
                e.preventDefault();
                updateDislikes(disliked);
                // setDisliked(!disliked);
              }}
            >
              <FontAwesomeIcon
                className="my-auto"
                icon={faCaretDown}
                color={disliked ? "#7DB8AF" : "#8A8A8A"}
              />
              <p className="text-[#8A8A8A]">{dislikes}</p>
              {dislikes}
            </button>
          </div>
        </div>
      </div>
    </a>
  );
};

export default NewsCard;
