import {
  faArrowTrendUp,
  faArrowUpRightFromSquare,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import type { RankedArticles } from "../types";

const HenYang = ({ articles }: { articles: RankedArticles }) => {
  return (
    <div className="w-[250px] bg-white rounded-3xl shadow-md p-3">
      <div className="flex flex-row rounded-3xl gap-3">
        <FontAwesomeIcon icon={faArrowTrendUp} color="#B7E2DC" size="2x" />
        <h1 className="text-[#22333B] text-xl font-bold">Hen Yang</h1>
      </div>
      <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-between">
        <div className="self-end bg-[#7DB8AF] rounded-full px-3 py-1">
          <h1 className="text-[#fff] self-end text-md font-semibold">1</h1>
        </div>
        <div className="w-[80%] flex flex-row justify-between gap-2 my-auto">
          <h1 className="text-[#8A8A8A] w-[90%] truncate">
            Title title title title title title
          </h1>
          <FontAwesomeIcon
            className="mt-1"
            icon={faArrowUpRightFromSquare}
            color="#8A8A8A"
          />
        </div>
      </div>
    </div>
  );
};

export default HenYang;
