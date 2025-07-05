import './App.css'

function App() {
  

  return (
    <>
    <header className="bg-white h-fit w-full flex top-0 sticky shadow-md">
      <nav className="w-full">
        <div className="flex pl-4 pt-2 pb-2 text-black ">
          Hack404
        </div>
        <hr className="border-gray-300 w-full items-center" />
        <div className="flex pl-4 pt-2 pb-2 text-black text-left">
            <div>
            <img src="/src/assets/yang.png" className="h-12 w-12 mr-2" />
            </div>
            <div className="grid grid-rows-2">
              <div className="font-bold">
                YangNews
              </div>
              <div>
                Find Yang daily
              </div>
            </div>
         


          <div className="ml-10 flex items-center space-x-4">
            <a href='#' className="text-gray-900 ">
              Politics
            </a>
            <a href='#' className="text-gray-900 ">
              Environment
            </a>
            <a href='#' className="text-gray-900 ">
              Community
            </a>
            <a href='#' className="text-gray-900 ">
              Health
            </a>

          </div>
        </div>
      </nav>
    </header>
    <main>

    </main>

      
    </>
  )
}

export default App
