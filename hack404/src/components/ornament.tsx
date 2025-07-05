import {
    faExclamationCircle,
    faArrowUpRightFromSquare,
  } from "@fortawesome/free-solid-svg-icons";
  import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

const Ornament = () => {
    return (
        <div className="bg-white rounded-3xl shadow-md p-3 self-start sticky top-[160px] w-[130px] z-10 mr-2">
            <div className="flex flex-row rounded-3xl gap-3">
                <FontAwesomeIcon icon={faExclamationCircle} color="#B7E2DC" size="2x" />
                <h1
                className="text-[#22333B] text-2xl font-bold"
                style={{ fontFamily: "AlumniSans" }}
                >
                Support
                </h1>
            </div>
                <p
                    className="text-[#8A8A8A] text-sm mx-auto"
                    style={{ fontFamily: "AlumniSans" }}
                >
                    (see more info)
                </p>
                <div className="border border-[#B7E2DC] p-2 rounded-xl flex flex-row justify-center">
        
        <div className="w-[80%] flex flex-row justify-between  my-auto">
          <h1
            className="text-[#8A8A8A] w-[90%] truncate pr-2"
            style={{ fontFamily: "AlumniSans" }}
          >
            hellohellohelloehlo
          </h1>
          <a
            href="https://www.google.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <FontAwesomeIcon
              className="mt-1 right-0"
              icon={faArrowUpRightFromSquare}
              color="#8A8A8A"
            />
          </a>
        </div>
      </div>
            
        </div>
        
    )
}

export default Ornament 