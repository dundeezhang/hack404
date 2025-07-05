import { useState } from "react";

const Header = ({
  active,
  setActive,
}: {
  active: string;
  setActive: (string) => void;
}) => {
  //   const [active, setActive] = useState("");

  const links = [
    "Politics",
    "Environment",
    "Community",
    "Science",
    "Health",
    "Education",
  ];

  return (
    <nav className="w-full">
      <div className="flex pl-4 pt-2 pb-2 text-black text-xl ">Hack404</div>
      <hr className="border-gray-300 w-full items-center" />
      <div className="flex pl-4 pt-2 pb-2 text-black text-left">
        <a href="" onClick={() => setActive("general")} className="flex gap-3">
          <div className="my-auto">
            <img src="/src/assets/yang.png" className="h-12 w-12 mr-2" />
          </div>
          <div className="grid grid-rows-2 gap-0.1">
            <div className="font-bold text-3xl">YangNews</div>
            <p className="text-lg">Find Yang daily</p>
          </div>
        </a>

        <div className="ml-8 flex items-center space-x-8 text-xl">
          {links.map((link) => (
            <a
              key={link}
              href="#"
              onClick={() => setActive(link)}
              className={`text-gray-900 px-2 py-1 rounded ${
                active === link ? "bg-gray-200" : ""
              }`}
            >
              {link}
            </a>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Header;
