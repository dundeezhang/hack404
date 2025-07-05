import {
  faArrowTrendUp,
  faArrowUpRightFromSquare,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import type { RankedArticles } from "../types";

const HenYang = ({ articles }: { articles?: RankedArticles }) => {
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
        (top-rated articles of the day)
      </p>
      <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-between">
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
      </div>
    </div>
  );
};

export default HenYang;
