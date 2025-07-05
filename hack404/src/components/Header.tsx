import { Link } from "react-router-dom";

const Header = ({
  active,
  setActive,
}: {
  active: string;
  setActive: (status: string) => void;
}) => {

  const links = [
    "General", 
    "Business", 
    "Entertainment",                   
    "Health", 
    "Science", 
    "Sports", 
    "Technology"
  ];

  return (
    <nav className="w-full">
      <div className="justify-between flex flex-row">
      <div className="flex pl-4 pt-2 pb-2 bg-gradient-to-r from-[#83b3ce] to-[#2CAA2F] text-transparent bg-clip-text text-xl ">Hack404</div>
      <div className="bg-gradient-to-r from-[#83b3ce] to-[#2CAA2F] text-xl flex pt-2 pr-5 text-transparent bg-clip-text">Exclusively positive news :)</div>
      </div>
      <hr className="border-gray-300 w-full items-center" />
      <div className="flex pl-4 pt-2 pb-2 text-black text-left">
      <Link to="/general" onClick={() => setActive("general")} className="flex gap-3">
          <div className="my-auto">
            <img src="/src/assets/yang.png" className="h-12 w-12 mr-2" />
          </div>
          <div className="grid grid-rows-2 gap-0.1">
            <div className="font-bold text-3xl">YangNews</div>
            <p className="text-lg">Find Yang daily</p>
          </div>
        </Link>

        <div className="ml-8 flex items-center space-x-8 text-xl">
          {links.map((link) => (
            <Link
            key={link}
            to={`/${link.toLowerCase()}`}
            onClick={() => setActive(link.toLowerCase())}
            className={`text-gray-900 px-2 py-1 rounded ${
              active === link.toLowerCase() ? "bg-gradient-to-r from-[#c6e5e9] to-[#c6e9c6]" : ""
            }`}
          >
            {link}
          </Link>
          ))}
        </div>
      </div>
    </nav>
  );
};

export default Header;
